# AlertSettingsUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_threshold_cents** | **int** |  | 
**email** | [**AlertEmailToggles**](AlertEmailToggles.md) |  | 

## Example

```python
from deeprelay_sdk.models.alert_settings_update import AlertSettingsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AlertSettingsUpdate from a JSON string
alert_settings_update_instance = AlertSettingsUpdate.from_json(json)
# print the JSON string representation of the object
print(AlertSettingsUpdate.to_json())

# convert the object into a dict
alert_settings_update_dict = alert_settings_update_instance.to_dict()
# create an instance of AlertSettingsUpdate from a dict
alert_settings_update_from_dict = AlertSettingsUpdate.from_dict(alert_settings_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


