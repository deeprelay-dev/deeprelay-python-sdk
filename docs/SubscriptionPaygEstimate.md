# SubscriptionPaygEstimate

What this period's plan-covered traffic would have cost on pay-as-you-go, read off the request ledger. `list_micro_cents` is exact: every covered request records its list price with the model's cached-input rate honored. `uncached_micro_cents` is the same traffic with every cache read billed at the full input rate (today's off-peak rates, so approximate); the gap is the cached-input discount, which the plan allowance does not give (cached input counts in full). The token counts are the raw input and its cached subset over the period. Omitted from `usage` until the period has covered usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**list_micro_cents** | **int** | The period&#39;s covered traffic at pay-as-you-go list rates, in micro-cents. | 
**uncached_micro_cents** | **int** | The same traffic with cache reads at the full input rate, in micro-cents. | 
**input_tokens** | **int** |  | 
**cached_input_tokens** | **int** | The cache-read subset of &#x60;input_tokens&#x60;. | 

## Example

```python
from deeprelay_sdk.models.subscription_payg_estimate import SubscriptionPaygEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPaygEstimate from a JSON string
subscription_payg_estimate_instance = SubscriptionPaygEstimate.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPaygEstimate.to_json())

# convert the object into a dict
subscription_payg_estimate_dict = subscription_payg_estimate_instance.to_dict()
# create an instance of SubscriptionPaygEstimate from a dict
subscription_payg_estimate_from_dict = SubscriptionPaygEstimate.from_dict(subscription_payg_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


