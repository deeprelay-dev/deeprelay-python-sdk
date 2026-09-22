# SubscriptionCheckoutSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_url** | **str** | The hosted page the customer must open to pay. | 
**session_id** | **str** | Checkout session id, for support correlation. | 
**plan** | [**SubscriptionPlan**](SubscriptionPlan.md) |  | 

## Example

```python
from deeprelay_sdk.models.subscription_checkout_session import SubscriptionCheckoutSession

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCheckoutSession from a JSON string
subscription_checkout_session_instance = SubscriptionCheckoutSession.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCheckoutSession.to_json())

# convert the object into a dict
subscription_checkout_session_dict = subscription_checkout_session_instance.to_dict()
# create an instance of SubscriptionCheckoutSession from a dict
subscription_checkout_session_from_dict = SubscriptionCheckoutSession.from_dict(subscription_checkout_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


