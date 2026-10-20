# SubscriptionUsage

Consumption against the quota, from the same factor-weighted read the request-time gate evaluates — so this meter and enforcement cannot disagree.  Present only for an entitled subscription whose meter could be read. Its absence is never a statement that nothing was used. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | Start of the window the period figures were summed over: the subscription&#39;s current period, or the UTC calendar month when the billing provider has not reported one yet. | 
**period_end** | **datetime** | End of that window. | 
**weighted_input_tokens** | **int** | Weighted input tokens spent this period, against &#x60;quota.input_tokens_monthly&#x60;. | 
**weighted_output_tokens** | **int** | Weighted output tokens spent this period, against &#x60;quota.output_tokens_monthly&#x60;. | 
**weekly_weighted_input_tokens** | **int** | Weighted input tokens over the trailing 7 days, against &#x60;quota.weekly_input_tokens&#x60;. A rolling figure, not a period one — it can be non-zero moments after a period rolls over. | 
**weekly_weighted_output_tokens** | **int** | Weighted output tokens over the trailing 7 days, against &#x60;quota.weekly_output_tokens&#x60;. A rolling figure, like &#x60;weekly_weighted_input_tokens&#x60;. | 
**cost_micro_cents** | **int** | List-price metered cost of this period&#39;s plan traffic in micro-cents (1e-6 cent), against &#x60;quota.max_usage_micro_cents&#x60;. | 
**recent_payg_calls_24h** | **int** | Wallet-billed calls while subscribed, e.g. input-overshoot or quota-gate pay-as-you-go fallbacks and models the plan does not cover. Recent means the last 24 hours, clamped to the current period. Omitted when the count could not be read; its absence means unknown, not zero. | [optional] 
**by_model** | [**List[SubscriptionModelUsage]**](SubscriptionModelUsage.md) | This period&#39;s plan-covered usage split by model: the raw tokens each model served, its usage factor, and the weighted tokens they drew from the allowance. Heaviest weighted input first. Each model&#39;s weighted figures round down on their own, so they can sum to slightly less than &#x60;weighted_input_tokens&#x60; / &#x60;weighted_output_tokens&#x60;, which stay authoritative. Omitted when the breakdown could not be read or there is no covered usage. | [optional] 
**weekly_by_model** | [**List[SubscriptionModelUsage]**](SubscriptionModelUsage.md) | The same breakdown over the trailing 7 days, against the weekly caps. Omitted under the same conditions as &#x60;by_model&#x60;. | [optional] 

## Example

```python
from deeprelay_sdk.models.subscription_usage import SubscriptionUsage

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUsage from a JSON string
subscription_usage_instance = SubscriptionUsage.from_json(json)
# print the JSON string representation of the object
print(SubscriptionUsage.to_json())

# convert the object into a dict
subscription_usage_dict = subscription_usage_instance.to_dict()
# create an instance of SubscriptionUsage from a dict
subscription_usage_from_dict = SubscriptionUsage.from_dict(subscription_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


