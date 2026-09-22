# Subscription

The organization's flat subscription tier: entitlement, billing period, the configured quota, and consumption against it. The console and this endpoint assemble it from the same source, so the two surfaces cannot report different numbers. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribed** | **bool** | Whether the organization is entitled to the plan right now. Only an &#x60;active&#x60; or &#x60;trialing&#x60; subscription entitles, including a short grace window past the period end that absorbs renewal webhook lag; a failed payment (&#x60;past_due&#x60;) cuts access immediately. Render from this; do not re-derive entitlement from &#x60;status&#x60; and the period bounds. | 
**status** | **str** | Raw subscription status — \&quot;active\&quot;, \&quot;trialing\&quot;, \&quot;past_due\&quot;, \&quot;canceled\&quot; and so on — or \&quot;none\&quot; when the organization never subscribed. | 
**cancel_at_period_end** | **bool** | Whether the subscription stops at the end of the current period instead of renewing. | 
**current_period_start** | **datetime** | Start of the current billing period. Absent until the billing provider has reported a period for this subscription. | [optional] 
**current_period_end** | **datetime** | End of the current billing period. Absent under the same condition as current_period_start. | [optional] 
**plan** | [**SubscriptionPlan**](SubscriptionPlan.md) |  | 
**quota** | [**SubscriptionQuota**](SubscriptionQuota.md) |  | 
**usage** | [**SubscriptionUsage**](SubscriptionUsage.md) |  | [optional] 

## Example

```python
from deeprelay_sdk.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


