# SubscriptionCheckoutRequest

Optional overrides for a checkout mint. Every field has a deployment default, so an empty body is the normal call. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_url** | **str** | Where the provider returns after a completed payment. Defaults to the deployment&#39;s configured URL. | [optional] 
**cancel_url** | **str** | Where the provider returns if checkout is abandoned. Defaults to the deployment&#39;s configured URL. | [optional] 
**plan_key** | **str** | Pins the plan the client displayed. An unknown key is a 400 rather than a silent purchase of a different tier. | [optional] 

## Example

```python
from deeprelay_sdk.models.subscription_checkout_request import SubscriptionCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCheckoutRequest from a JSON string
subscription_checkout_request_instance = SubscriptionCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCheckoutRequest.to_json())

# convert the object into a dict
subscription_checkout_request_dict = subscription_checkout_request_instance.to_dict()
# create an instance of SubscriptionCheckoutRequest from a dict
subscription_checkout_request_from_dict = SubscriptionCheckoutRequest.from_dict(subscription_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


