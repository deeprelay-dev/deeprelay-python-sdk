# SubscriptionPortalRequest

Optional overrides for a billing-portal mint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | Where the provider returns when the customer leaves the portal. Defaults to the deployment&#39;s configured URL. | [optional] 

## Example

```python
from deeprelay_sdk.models.subscription_portal_request import SubscriptionPortalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPortalRequest from a JSON string
subscription_portal_request_instance = SubscriptionPortalRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPortalRequest.to_json())

# convert the object into a dict
subscription_portal_request_dict = subscription_portal_request_instance.to_dict()
# create an instance of SubscriptionPortalRequest from a dict
subscription_portal_request_from_dict = SubscriptionPortalRequest.from_dict(subscription_portal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


