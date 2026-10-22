# ApiKey

An API key's metadata and limits. Never carries the secret.

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
**fallback_models** | **List[str]** | Backup models in priority order, applied to every model this key calls. Null means model fallback is off (the default). If every provider for the requested model fails before the first token with a temporary error, the next entry is tried. Entries are kept when a model leaves the plan roster or the catalog and are skipped at request time; see &#x60;fallback_entries&#x60;. Not applied to Liquid. | 
**fallback_entries** | [**List[ApiKeyFallbackEntry]**](ApiKeyFallbackEntry.md) | Present when &#x60;fallback_models&#x60; is set: one entry per backup, in order, explaining it as of now. | [optional] 
**primary_model** | **str** | The model this key requested most over the last 30 days, which &#x60;above_primary&#x60; is measured against. Present only for a key with &#x60;fallback_models&#x60; and recent usage. | [optional] 
**rate_limit_rps** | **int** |  | 
**rate_limit_burst** | **int** |  | 
**expires_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**last_used_at** | **datetime** |  | 
**revoked_at** | **datetime** |  | [optional] 

## Example

```python
from deeprelay_sdk.models.api_key import ApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKey from a JSON string
api_key_instance = ApiKey.from_json(json)
# print the JSON string representation of the object
print(ApiKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of ApiKey from a dict
api_key_from_dict = ApiKey.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


