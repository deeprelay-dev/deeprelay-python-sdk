# CostDetails

How this call was priced, in USD (exact decimals, up to 8 places). list_price_equivalent = plan_covered_amount + charged_amount. A call is either fully covered by the subscription or fully charged: there is no partial coverage. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_price_equivalent** | **float** | What the call costs at the model&#39;s pay-as-you-go list rates (peak rates inside a peak window). | 
**plan_covered_amount** | **float** | The part the flat subscription covered (the full list price, or 0). | 
**charged_amount** | **float** | The part charged to the wallet; equal to usage.cost. | 
**quota_units_used** | **int** | Weighted subscription-quota units this call consumed: (prompt + completion tokens) × the model&#39;s usage factor. 0 for a subscriber call billed pay-as-you-go (a model the plan does not cover, or a quota fallback); null for a pay-as-you-go organization.  | 
**cache_savings** | **float** | What the prompt cache saved: the list price without the cache discount minus list_price_equivalent. Null when the upstream did not report cache usage. Can be negative when a model&#39;s cached rate is not a discount.  | 

## Example

```python
from deeprelay_sdk.models.cost_details import CostDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CostDetails from a JSON string
cost_details_instance = CostDetails.from_json(json)
# print the JSON string representation of the object
print(CostDetails.to_json())

# convert the object into a dict
cost_details_dict = cost_details_instance.to_dict()
# create an instance of CostDetails from a dict
cost_details_from_dict = CostDetails.from_dict(cost_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


