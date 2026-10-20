# SubscriptionCheckoutRequest

Optional overrides for a checkout mint. Every field has a deployment default, so an empty body is the normal call. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_url** | **str** | Where the provider returns after a completed payment. Defaults to the deployment&#39;s configured URL. Must be on the deployment&#39;s dashboard origin, else 422 &#x60;validation_failed&#x60;. | [optional] 
**cancel_url** | **str** | Where the provider returns if checkout is abandoned. Defaults to the deployment&#39;s configured URL. Must be on the deployment&#39;s dashboard origin, else 422 &#x60;validation_failed&#x60;. | [optional] 
**plan_key** | **str** | The plan to buy — &#x60;flat&#x60; (Base, the default) or &#x60;plus&#x60;. Pins the plan the client displayed: an unknown or un-offered key is a 400 rather than a silent purchase of a different tier. | [optional] 
**method** | **str** | &#x60;card&#x60; (dollars, card or Link; the default) or &#x60;upi&#x60; (rupees, UPI AutoPay). On a subscribed organization, the other currency&#39;s method switches the existing plan&#39;s billing. | [optional] 

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


