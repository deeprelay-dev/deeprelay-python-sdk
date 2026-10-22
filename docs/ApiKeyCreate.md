# ApiKeyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**scopes** | **Dict[str, object]** | One of &#x60;{\&quot;full_access\&quot;: true}&#x60;, &#x60;{\&quot;standard\&quot;: true}&#x60;, &#x60;{\&quot;read_only\&quot;: true}&#x60;, or a per-resource map such as &#x60;{\&quot;serverless\&quot;: \&quot;read\&quot;, \&quot;keys\&quot;: \&quot;write\&quot;}&#x60;. A shortcut cannot be combined with per-resource entries. | 
**budget_cents** | **int** |  | [optional] 
**allowed_models** | **List[str]** |  | [optional] 
**fallback_models** | **List[str]** | Backup models in priority order. Omit it to leave model fallback off. Each entry must be a chat model in the catalog and, when the key has &#x60;allowed_models&#x60;, on that list. Duplicates are removed. An empty array, more than 3 models or an invalid entry is a 422 &#x60;validation_failed&#x60; naming the &#x60;fallback_models&#x60; field. | [optional] 
**rate_limit_rps** | **int** |  | [optional] 
**rate_limit_burst** | **int** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from deeprelay_sdk.models.api_key_create import ApiKeyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyCreate from a JSON string
api_key_create_instance = ApiKeyCreate.from_json(json)
# print the JSON string representation of the object
print(ApiKeyCreate.to_json())

# convert the object into a dict
api_key_create_dict = api_key_create_instance.to_dict()
# create an instance of ApiKeyCreate from a dict
api_key_create_from_dict = ApiKeyCreate.from_dict(api_key_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


