# NOT GENERATED — hand-written. It is absent from
# sdk/python/.openapi-generator/FILES by design, so never sweep it up as
# "stale generated output" when reconciling this tree against that manifest.
# coding: utf-8

"""Regression tests for RFC3339 datetime query-param serialisation (Phase 103,
SDK-04, D-04).

The generator emits `<var>.strftime(self.api_client.configuration.datetime_format)`
inline in every per-operation `*_api.py`, which produces a colon-less UTC
offset (`+0000`). Go's `time.Parse(time.RFC3339, …)` — what every deeprelay
handler uses — rejects that, so `UsageApi.list_usage(bucket="day", start=…,
end=…)` returned 422 from the shipped 0.1.1 wheel with no caller-side
workaround.

`sdk/release/patch-generated-python-datetime.py`, run by `make sdk-generate`,
rewrites those calls to `.isoformat()`. THIS FILE is the proof that the patch
actually ran: test 3 fails the moment a regenerated tree lands without it.
It anchors on the datetime_format form specifically — the date_format
sibling the generator emits for `format: date` params is correct as-is.

Run via `make sdk-python-test` (also wired into ci.yml's `sdk` job and
sdk-release.yml's `prepare` job). No network: only the private
`_list_usage_serialize` is exercised, which builds the request URL and stops.
"""

import re
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import deeprelay_sdk
from deeprelay_sdk.api.usage_api import UsageApi
from deeprelay_sdk.api_client import ApiClient
from deeprelay_sdk.configuration import Configuration

# RFC3339 with a colon-separated offset, which is what Go's time.RFC3339 layout
# ("Z07:00") accepts. `+0000` — the pre-patch output — does not match.
RFC3339_COLON_OFFSET = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?(\+00:00|Z)$"
)

# The defect, precisely. The generator emits a SECOND strftime form for
# `format: date` query params — strftime(self.api_client.configuration.date_format)
# — which yields a valid `%Y-%m-%d` and is deliberately left alone by
# sdk/release/patch-generated-python-datetime.py. Matching bare "strftime("
# would fail this suite the first time the spec grows a date query param, with
# a misleading message; anchor on datetime_format instead.
DATETIME_STRFTIME = re.compile(
    r"strftime\(\s*self\.api_client\.configuration\.datetime_format"
)


class TestDatetimeQueryParams(unittest.TestCase):
    """Datetime query params must serialise as RFC3339 with a colon offset."""

    def setUp(self) -> None:
        self.api = UsageApi(api_client=ApiClient(configuration=Configuration()))

    def _serialize_usage_query(self, start, end):
        """Return the decoded query dict from GET /usage's serialised request."""
        serialized = self.api._list_usage_serialize(
            bucket="day",
            group_by=None,
            start=start,
            end=end,
            cursor=None,
            limit=None,
            modality=None,
            model=None,
            _request_auth=None,
            _content_type=None,
            _headers=None,
            _host_index=0,
        )
        url = serialized[1]
        return parse_qs(urlsplit(url).query)

    def test_list_usage_start_and_end_are_rfc3339_with_colon_offset(self) -> None:
        now = datetime.now(timezone.utc)
        qs = self._serialize_usage_query(now - timedelta(days=7), now)
        for name in ("start", "end"):
            self.assertIn(name, qs, f"{name} missing from the serialised query")
            value = qs[name][0]
            self.assertRegex(
                value,
                RFC3339_COLON_OFFSET,
                f"{name}={value!r} is not RFC3339 with a colon-separated"
                " offset — Go's time.Parse(time.RFC3339, …) will 422 this."
                " Did sdk/release/patch-generated-python-datetime.py stop"
                " running inside `make sdk-generate`?",
            )

    def test_non_utc_offset_keeps_colon(self) -> None:
        ist = timezone(timedelta(hours=5, minutes=30))
        start = datetime(2026, 9, 23, 7, 13, 47, tzinfo=ist)
        qs = self._serialize_usage_query(start, None)
        self.assertEqual(qs["start"][0], "2026-09-23T07:13:47+05:30")

    def test_no_generated_api_file_uses_strftime(self) -> None:
        api_dir = Path(deeprelay_sdk.__file__).resolve().parent / "api"
        api_files = sorted(api_dir.glob("*_api.py"))
        self.assertTrue(api_files, f"no generated *_api.py found under {api_dir}")
        for path in api_files:
            # assertFalse on a precomputed bool, not assertNotIn/assertNotRegex:
            # those dump the entire generated module into the failure output.
            has_defect = bool(
                DATETIME_STRFTIME.search(path.read_text(encoding="utf-8"))
            )
            self.assertFalse(
                has_defect,
                f"{path.name} still pre-stringifies a datetime with"
                " strftime(datetime_format) — the generator's colon-less %z"
                " offset is back. Re-run `make sdk-generate` (which applies"
                " sdk/release/patch-generated-python-datetime.py).",
            )


if __name__ == '__main__':
    unittest.main()
