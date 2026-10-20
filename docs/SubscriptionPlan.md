# SubscriptionPlan

The plan the organization is on — or, for an organization that never subscribed, the Base plan it would get. Always present: it is what a point of purchase renders before sending anyone to pay. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Stable identifier for the plan: &#x60;flat&#x60; (Base) or &#x60;plus&#x60;. Send it as &#x60;plan_key&#x60; on /billing/subscription/checkout to pin the plan you displayed, or on /billing/subscription/upgrade to name the target. | 
**name** | **str** | Human-facing plan name (\&quot;Base\&quot;, \&quot;Plus\&quot;). | 
**price** | [**SubscriptionPrice**](SubscriptionPrice.md) |  | [optional] 

## Example

```python
from deeprelay_sdk.models.subscription_plan import SubscriptionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPlan from a JSON string
subscription_plan_instance = SubscriptionPlan.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPlan.to_json())

# convert the object into a dict
subscription_plan_dict = subscription_plan_instance.to_dict()
# create an instance of SubscriptionPlan from a dict
subscription_plan_from_dict = SubscriptionPlan.from_dict(subscription_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


