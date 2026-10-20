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
**quota_units** | **int** | Weighted tokens drawn from the subscription quota. | [optional] 
**cost** | **float** | The exact USD amount billed to the wallet, in the same format as &#x60;usage.cost&#x60;: an exact decimal with up to 8 places, emitted as a JSON number. &#x60;0&#x60; for a plan-covered, rejected or failed call. | 
**cost_micro_cents** | **int** | The same amount as an integer number of micro-cents. | 
**plan_covered** | **bool** | Whether the subscription plan paid for the call. | 
**ttft_ms** | **int** | Time to first token, for a streamed call. | [optional] 
**duration_ms** | **int** |  | [optional] 
**ignored_params** | **List[str]** | Request parameters that were accepted and ignored. | [optional] 
**had_tool_calls** | **bool** |  | [optional] 
**image_count** | **int** |  | [optional] 
**video_seconds** | **int** |  | [optional] 
**suppressed_count** | **int** | For a rejected row: how many further identical rejections in the same minute were folded into this one. | [optional] 

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


