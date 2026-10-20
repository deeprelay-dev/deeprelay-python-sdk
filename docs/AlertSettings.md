# AlertSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_threshold_cents** | **int** | The wallet balance, in cents, below which a low-balance alert fires. | 
**email** | [**AlertEmailToggles**](AlertEmailToggles.md) |  | 
**updated_at** | **datetime** | Null until the organization saves its settings once. | 
**note** | **str** | A fixed note that the member always receives their own limit emails. | 

## Example

```python
from deeprelay_sdk.models.alert_settings import AlertSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AlertSettings from a JSON string
alert_settings_instance = AlertSettings.from_json(json)
# print the JSON string representation of the object
print(AlertSettings.to_json())

# convert the object into a dict
alert_settings_dict = alert_settings_instance.to_dict()
# create an instance of AlertSettings from a dict
alert_settings_from_dict = AlertSettings.from_dict(alert_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


