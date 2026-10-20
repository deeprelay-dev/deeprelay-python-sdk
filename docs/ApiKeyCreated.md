# ApiKeyCreated

The new key's metadata plus its secret (`key`), returned exactly once. The same fields as `ApiKey`, plus `key`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **UUID** |  | 
**name** | **str** |  | 
**key_prefix** | **str** |  | 
**last4** | **str** |  | 
**scopes** | [**ApiKeyScopes**](ApiKeyScopes.md) |  | 
**budget_cents** | **int** | Monthly spend budget in cents, reset at the start of each UTC month. Null means no budget. A call that would take the key past it is refused with 402 &#x60;api_key_budget_exceeded&#x60;. | 
**budget_used_micro_cents** | **int** | Spend so far this month, in micro-cents. Present when the key has a budget. | [optional] 
**budget_resets_at** | **datetime** | When the budget resets. Present when the key has a budget. | [optional] 
**allowed_models** | **List[str]** | The models this key may call. Null means every model. A call for any other model is refused with 403 &#x60;model_not_allowed_for_key&#x60;, and &#x60;GET /models&#x60; lists only these. | 
**stale_models** | **List[str]** | Entries of &#x60;allowed_models&#x60; that are no longer in the catalog. | [optional] 
**rate_limit_rps** | **int** |  | 
**rate_limit_burst** | **int** |  | 
**expires_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**last_used_at** | **datetime** |  | 
**revoked_at** | **datetime** |  | [optional] 
**key** | **str** | The secret. Shown once; it cannot be read again. | 

## Example

```python
from deeprelay_sdk.models.api_key_created import ApiKeyCreated

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyCreated from a JSON string
api_key_created_instance = ApiKeyCreated.from_json(json)
# print the JSON string representation of the object
print(ApiKeyCreated.to_json())

# convert the object into a dict
api_key_created_dict = api_key_created_instance.to_dict()
# create an instance of ApiKeyCreated from a dict
api_key_created_from_dict = ApiKeyCreated.from_dict(api_key_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


