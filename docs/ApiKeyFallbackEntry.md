# ApiKeyFallbackEntry

One backup model on a key, as it stands now.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**state** | **str** | &#x60;ok&#x60;: usable as a backup. &#x60;wallet_only&#x60;: the model is not on the subscription plan roster, so it backs up only requests billed to the wallet; a plan-covered request skips it. &#x60;unavailable&#x60;: the model is no longer in the catalog and is always skipped. | 
**input_per_1m_tokens_microcents** | **int** | Current input price per 1M tokens, in micro-cents. 0 when unknown or unavailable. | 
**output_per_1m_tokens_microcents** | **int** | Current output price per 1M tokens, in micro-cents. 0 when unknown or unavailable. | 
**above_primary** | **bool** | True when this backup&#39;s input plus output price is above &#x60;primary_model&#x60;&#39;s. Pricier backups are allowed; a request served by one is billed at its own price, and the key budget is checked at that price. | 

## Example

```python
from deeprelay_sdk.models.api_key_fallback_entry import ApiKeyFallbackEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyFallbackEntry from a JSON string
api_key_fallback_entry_instance = ApiKeyFallbackEntry.from_json(json)
# print the JSON string representation of the object
print(ApiKeyFallbackEntry.to_json())

# convert the object into a dict
api_key_fallback_entry_dict = api_key_fallback_entry_instance.to_dict()
# create an instance of ApiKeyFallbackEntry from a dict
api_key_fallback_entry_from_dict = ApiKeyFallbackEntry.from_dict(api_key_fallback_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


