# RequestAttempt

One model in a request's backup-model trail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**outcome** | **str** | &#x60;ok&#x60;: this model served. &#x60;failed&#x60;: it was dialled and every provider failed before the first token. &#x60;skipped&#x60;: it was passed over without being dialled. | 
**reason** | **str** | Why the attempt failed (a public error code such as &#x60;upstream_timeout&#x60;) or was skipped: &#x60;model_not_allowed_for_key&#x60;, &#x60;subscription_quota_exhausted&#x60;, &#x60;api_key_budget_exceeded&#x60;, &#x60;member_spend_limit_reached&#x60;, &#x60;insufficient_balance&#x60;, &#x60;daily_limit_reached&#x60;, &#x60;spending_limit_reached&#x60;, &#x60;wallet_only&#x60; (not on the plan roster, for a plan-covered request), &#x60;unavailable&#x60;, &#x60;capability_mismatch&#x60;, &#x60;context_window_too_small&#x60;, &#x60;breaker_open&#x60; or &#x60;deadline_exhausted&#x60; (too little time was left to start another model). | [optional] 
**duration_ms** | **int** | How long this model&#39;s attempt took, in milliseconds. | 
**ttft_ms** | **int** | Time to first token, for the model that served a streamed call. | [optional] 
**tries** | **int** | How many upstream attempts were made for this model. 0 for a skipped model. | 

## Example

```python
from deeprelay_sdk.models.request_attempt import RequestAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAttempt from a JSON string
request_attempt_instance = RequestAttempt.from_json(json)
# print the JSON string representation of the object
print(RequestAttempt.to_json())

# convert the object into a dict
request_attempt_dict = request_attempt_instance.to_dict()
# create an instance of RequestAttempt from a dict
request_attempt_from_dict = RequestAttempt.from_dict(request_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


