# RequestLogEntry

One inference call as the request log records it. Never carries prompt or completion content. Optional numeric fields are omitted when they do not apply (for example token counts on a rejected call).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The &#x60;X-Request-Id&#x60; the call was answered with. | 
**client_request_id** | **str** | The caller&#39;s &#x60;X-Client-Request-Id&#x60;, when one was sent. | [optional] 
**occurred_at** | **datetime** |  | 
**surface** | **str** |  | 
**model** | **str** |  | 
**key_id** | **str** | The &#x60;api_key_id&#x60; of the key that sent the call. Absent for dashboard playground calls. | [optional] 
**key_name** | **str** |  | [optional] 
**key_prefix** | **str** | The key&#39;s public prefix. The secret is never stored or returned. | [optional] 
**status** | **str** |  | 
**http_status** | **int** |  | [optional] 
**error_code** | **str** | The &#x60;X-Deeprelay-Error-Code&#x60; the caller received, on a failed or rejected call. | [optional] 
**finish_reason** | **str** |  | [optional] 
**prompt_tokens** | **int** |  | [optional] 
**completion_tokens** | **int** |  | [optional] 
**cached_tokens** | **int** |  | [optional] 
**reasoning_tokens** | **int** |  | [optional] 
**search_count** | **int** | Server-side web searches billed on this call (failed searches are not counted). Omitted when the call ran none. | [optional] 
**search_overflow_count** | **int** | The subset of &#x60;search_count&#x60; that ran past the plan&#39;s monthly search allowance and was billed to the wallet (the organization opted in on &#x60;/search/settings&#x60;). Never greater than &#x60;search_count&#x60;. Omitted when none did. | [optional] 
**search_result_tokens** | **int** | The subset of &#x60;prompt_tokens&#x60; that were web-search results fed back to the model. Already counted in &#x60;prompt_tokens&#x60;; do not add them again. Omitted when the call ran no search. | [optional] 
**search_overflow_fee_micro_cents** | **int** | The wallet charge, in micro-cents, for this call&#39;s &#x60;search_overflow_count&#x60; searches at the overflow price. It is a field of this request, not a separate request: the log never lists the fee as its own row. Omitted when there was no overflow fee. | [optional] 
**quota_units** | **int** | Weighted tokens drawn from the subscription quota. | [optional] 
**cost** | **float** | The call&#39;s cost in USD: an exact decimal with up to 8 places, emitted as a JSON number. On a pay-as-you-go row (&#x60;plan_covered: false&#x60;) it is the amount billed to the wallet, the same figure as &#x60;usage.cost&#x60;. On a plan-covered row it is the list-price equivalent, not a charge: tokens plus every web search the allowance covered, at the per-search list price; the subscription paid for it. A paid web-search overflow fee is not included; it is in &#x60;search_overflow_fee_micro_cents&#x60;. &#x60;0&#x60; for a rejected or failed call. | 
**cost_micro_cents** | **int** | The same amount as an integer number of micro-cents. | 
**plan_covered** | **bool** | Whether the subscription plan paid for the call. | 
**ttft_ms** | **int** | Time to first token, for a streamed call. | [optional] 
**duration_ms** | **int** |  | [optional] 
**ignored_params** | **List[str]** | Request parameters that were accepted and ignored. | [optional] 
**had_tool_calls** | **bool** |  | [optional] 
**image_count** | **int** |  | [optional] 
**video_seconds** | **int** |  | [optional] 
**suppressed_count** | **int** | For a rejected row: how many further identical rejections in the same minute were folded into this one. | [optional] 
**requested_model** | **str** | The model the request asked for. Always present; equal to &#x60;model&#x60; unless a backup model was tried. | [optional] 
**served_model** | **str** | The model that produced the response. Omitted when no model served (a failed or rejected call). When a backup served, &#x60;model&#x60; is this model and the row is billed at its price. | [optional] 
**fallback_reason** | **str** | Set when backup models were tried: the requested model&#39;s public error code (for example &#x60;upstream_timeout&#x60;). Rows with it set are the ones &#x60;fallback&#x3D;true&#x60; returns. | [optional] 
**attempts** | [**List[RequestAttempt]**](RequestAttempt.md) | Present when backup models were tried: every model the request went through, in order, including skipped backups. Upstream providers are never named. | [optional] 

## Example

```python
from deeprelay_sdk.models.request_log_entry import RequestLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLogEntry from a JSON string
request_log_entry_instance = RequestLogEntry.from_json(json)
# print the JSON string representation of the object
print(RequestLogEntry.to_json())

# convert the object into a dict
request_log_entry_dict = request_log_entry_instance.to_dict()
# create an instance of RequestLogEntry from a dict
request_log_entry_from_dict = RequestLogEntry.from_dict(request_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


