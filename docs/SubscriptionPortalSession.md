# SubscriptionPortalSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portal_url** | **str** | The hosted billing portal — cancel, resume, change payment method, download invoices. | 

## Example

```python
from deeprelay_sdk.models.subscription_portal_session import SubscriptionPortalSession

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPortalSession from a JSON string
subscription_portal_session_instance = SubscriptionPortalSession.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPortalSession.to_json())

# convert the object into a dict
subscription_portal_session_dict = subscription_portal_session_instance.to_dict()
# create an instance of SubscriptionPortalSession from a dict
subscription_portal_session_from_dict = SubscriptionPortalSession.from_dict(subscription_portal_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


