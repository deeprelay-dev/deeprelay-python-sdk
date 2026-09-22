# SubscriptionPlan

What the organization is — or would be — subscribing to. Always present, including for an organization that never subscribed: it is what a point of purchase renders before sending anyone to pay. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Stable identifier for the tier. Send it as &#x60;plan_key&#x60; on /billing/subscription/checkout to pin the plan you displayed. | 
**name** | **str** | Human-facing plan name. | 
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


