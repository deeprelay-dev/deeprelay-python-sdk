# SubscriptionUpgradeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_key** | **str** | The plan to move to (&#x60;plus&#x60;). Must be bigger than the plan the organization is on. | 

## Example

```python
from deeprelay_sdk.models.subscription_upgrade_request import SubscriptionUpgradeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUpgradeRequest from a JSON string
subscription_upgrade_request_instance = SubscriptionUpgradeRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionUpgradeRequest.to_json())

# convert the object into a dict
subscription_upgrade_request_dict = subscription_upgrade_request_instance.to_dict()
# create an instance of SubscriptionUpgradeRequest from a dict
subscription_upgrade_request_from_dict = SubscriptionUpgradeRequest.from_dict(subscription_upgrade_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


