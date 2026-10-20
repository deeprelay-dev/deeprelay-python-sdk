# ApiKeyScopes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shape** | **str** |  | 
**keys_manage** | **bool** | Whether the key can create, update and revoke keys: true for a &#x60;full_access&#x60; key and for a granular key granted &#x60;{\&quot;keys\&quot;: \&quot;write\&quot;}&#x60;. | 
**resources** | **Dict[str, str]** | Per-resource levels, present for a granular key. | [optional] 

## Example

```python
from deeprelay_sdk.models.api_key_scopes import ApiKeyScopes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyScopes from a JSON string
api_key_scopes_instance = ApiKeyScopes.from_json(json)
# print the JSON string representation of the object
print(ApiKeyScopes.to_json())

# convert the object into a dict
api_key_scopes_dict = api_key_scopes_instance.to_dict()
# create an instance of ApiKeyScopes from a dict
api_key_scopes_from_dict = ApiKeyScopes.from_dict(api_key_scopes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


