# ApiKeyUpdate

Send only the fields to change. `null` clears `budget_cents`, `allowed_models`, `fallback_models` or `expires_at`. `scopes` cannot be changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**budget_cents** | **int** |  | [optional] 
**allowed_models** | **List[str]** |  | [optional] 
**fallback_models** | **List[str]** | Replace the backup list (priority order), or &#x60;null&#x60; to turn model fallback off. Same rules as on create, judged against the key&#39;s allowlist after this update. An empty array is a 422 &#x60;validation_failed&#x60;; send &#x60;null&#x60; instead. | [optional] 
**rate_limit_rps** | **int** |  | [optional] 
**rate_limit_burst** | **int** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from deeprelay_sdk.models.api_key_update import ApiKeyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyUpdate from a JSON string
api_key_update_instance = ApiKeyUpdate.from_json(json)
# print the JSON string representation of the object
print(ApiKeyUpdate.to_json())

# convert the object into a dict
api_key_update_dict = api_key_update_instance.to_dict()
# create an instance of ApiKeyUpdate from a dict
api_key_update_from_dict = ApiKeyUpdate.from_dict(api_key_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


