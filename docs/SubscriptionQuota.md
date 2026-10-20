# SubscriptionQuota

A plan's configured allowances — the denominators of the usage meter. On `/billing/subscription` it is the quota of the plan the organization is on; always present, including for an organization that has not subscribed, where it describes what the Base plan would provide. Each entry of `plans` carries its own.  Token figures are WEIGHTED tokens: every model carries a usage factor, so a model at factor 2 spends two of these per token it serves. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens_monthly** | **int** | Weighted input tokens included per billing period. | 
**output_tokens_monthly** | **int** | Weighted output tokens included per billing period. Reasoning tokens are output tokens. | 
**weekly_input_tokens** | **int** | Weighted input tokens allowed over a ROLLING 7-day window. This cap slides with the clock; it does not reset with the billing period. 0 means no weekly input cap is configured on this deployment. | 
**weekly_output_tokens** | **int** | Weighted output tokens allowed over a ROLLING 7-day window, independent of the weekly input cap. Slides with the clock; it does not reset with the billing period. Reasoning tokens are output tokens. 0 means no weekly output cap is configured. | 
**max_usage_micro_cents** | **int** | Per-period backstop on list-price metered cost, in micro-cents (1e-6 cent). 0 means no backstop is configured on this deployment. | 
**payg_discount_bp** | **int** | Deprecated and always 0. There is no subscriber discount on pay-as-you-go spend: a request that exhausts the plan quota bills at list rates, the same rates an org without a subscription pays. The field is retained so existing deserializers keep working and will be removed in the next breaking revision. Do not display it. | 

## Example

```python
from deeprelay_sdk.models.subscription_quota import SubscriptionQuota

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionQuota from a JSON string
subscription_quota_instance = SubscriptionQuota.from_json(json)
# print the JSON string representation of the object
print(SubscriptionQuota.to_json())

# convert the object into a dict
subscription_quota_dict = subscription_quota_instance.to_dict()
# create an instance of SubscriptionQuota from a dict
subscription_quota_from_dict = SubscriptionQuota.from_dict(subscription_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


