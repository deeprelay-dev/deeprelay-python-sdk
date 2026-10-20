# AlertEmailToggles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_low** | **bool** |  | 
**subscription_quota** | **bool** |  | 
**api_key_budget** | **bool** |  | 
**member_spend** | **bool** |  | 

## Example

```python
from deeprelay_sdk.models.alert_email_toggles import AlertEmailToggles

# TODO update the JSON string below
json = "{}"
# create an instance of AlertEmailToggles from a JSON string
alert_email_toggles_instance = AlertEmailToggles.from_json(json)
# print the JSON string representation of the object
print(AlertEmailToggles.to_json())

# convert the object into a dict
alert_email_toggles_dict = alert_email_toggles_instance.to_dict()
# create an instance of AlertEmailToggles from a dict
alert_email_toggles_from_dict = AlertEmailToggles.from_dict(alert_email_toggles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


