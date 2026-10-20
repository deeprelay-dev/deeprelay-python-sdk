# OpenAIErrorEnvelopeError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**type** | **str** | OpenAI error class (e.g. invalid_request_error, authentication_error, billing_error). | 
**param** | **str** | On a 429 subscription_quota_exhausted this is the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound, max_tokens or the model&#39;s declared maximum). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. | [optional] 
**code** | **str** | Stable machine-readable error code. | 
**quota_frees_at** | **datetime** | Only on a 429 &#x60;subscription_quota_exhausted&#x60; whose &#x60;param&#x60; is &#x60;weekly_input_tokens&#x60; or &#x60;weekly_output_tokens&#x60; (the rolling 7-day caps): the RFC 3339 time at which enough plan-covered usage ages out of the rolling window for requests to ride the plan again — the earlier of the two windows&#39; free times, each computed from its own dimension. The message names the same time. Omitted on every other error, and omitted when it cannot be computed. There is no Retry-After on this 429 and &#x60;x-should-retry&#x60; is &#x60;false&#x60;: wait until this time or add credits, rather than auto-retrying. | [optional] 

## Example

```python
from deeprelay_sdk.models.open_ai_error_envelope_error import OpenAIErrorEnvelopeError

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIErrorEnvelopeError from a JSON string
open_ai_error_envelope_error_instance = OpenAIErrorEnvelopeError.from_json(json)
# print the JSON string representation of the object
print(OpenAIErrorEnvelopeError.to_json())

# convert the object into a dict
open_ai_error_envelope_error_dict = open_ai_error_envelope_error_instance.to_dict()
# create an instance of OpenAIErrorEnvelopeError from a dict
open_ai_error_envelope_error_from_dict = OpenAIErrorEnvelopeError.from_dict(open_ai_error_envelope_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


