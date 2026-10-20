# SubscriptionTier

One plan as the plan catalogue lists it: identity, price and the allowance it buys. Every offered plan covers the same models at the same usage factors — Plus is Base with a larger allowance. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Stable plan identifier — &#x60;flat&#x60; (Base) or &#x60;plus&#x60;. | 
**name** | **str** | Human-facing plan name. | 
**price** | [**SubscriptionPrice**](SubscriptionPrice.md) |  | [optional] 
**quota** | [**SubscriptionQuota**](SubscriptionQuota.md) |  | 

## Example

```python
from deeprelay_sdk.models.subscription_tier import SubscriptionTier

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionTier from a JSON string
subscription_tier_instance = SubscriptionTier.from_json(json)
# print the JSON string representation of the object
print(SubscriptionTier.to_json())

# convert the object into a dict
subscription_tier_dict = subscription_tier_instance.to_dict()
# create an instance of SubscriptionTier from a dict
subscription_tier_from_dict = SubscriptionTier.from_dict(subscription_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


