# PeakWindow

One daily UTC time range during which a model's peak rates apply.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | \&quot;HH:MM\&quot; UTC, inclusive. | 
**end** | **str** | \&quot;HH:MM\&quot; UTC, exclusive (\&quot;24:00\&quot; means until midnight). | 

## Example

```python
from deeprelay_sdk.models.peak_window import PeakWindow

# TODO update the JSON string below
json = "{}"
# create an instance of PeakWindow from a JSON string
peak_window_instance = PeakWindow.from_json(json)
# print the JSON string representation of the object
print(PeakWindow.to_json())

# convert the object into a dict
peak_window_dict = peak_window_instance.to_dict()
# create an instance of PeakWindow from a dict
peak_window_from_dict = PeakWindow.from_dict(peak_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


