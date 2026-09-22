# SubscriptionUsage

Consumption against the quota, from the same factor-weighted read the request-time gate evaluates — so this meter and enforcement cannot disagree.  Present only for an entitled subscription whose meter could be read. Its absence is never a statement that nothing was used. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | Start of the window the period figures were summed over: the subscription&#39;s current period, or the UTC calendar month when the billing provider has not reported one yet. | 
**period_end** | **datetime** | End of that window. | 
**weighted_input_tokens** | **int** | Weighted input tokens spent this period, against &#x60;quota.input_tokens_monthly&#x60;. | 
**weighted_output_tokens** | **int** | Weighted output tokens spent this period, against &#x60;quota.output_tokens_monthly&#x60;. | 
**weekly_weighted_tokens** | **int** | Weighted input+output tokens over the trailing 7 days, against &#x60;quota.weekly_tokens&#x60;. A rolling figure, not a period one — it can be non-zero moments after a period rolls over. | 
**cost_micro_cents** | **int** | List-price metered cost of this period&#39;s plan traffic in micro-cents (1e-6 cent), against &#x60;quota.max_usage_micro_cents&#x60;. | 

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


