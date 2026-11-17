# BatchDeeprelayCurrentWindow

The off-peak run the batch is in now; null outside off-peak time or once the batch has finished.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | 
**end** | **int** | Null when no peak time falls within the next 8 days (a model with no peak schedule). | 

## Example

```python
from deeprelay_sdk.models.batch_deeprelay_current_window import BatchDeeprelayCurrentWindow

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeeprelayCurrentWindow from a JSON string
batch_deeprelay_current_window_instance = BatchDeeprelayCurrentWindow.from_json(json)
# print the JSON string representation of the object
print(BatchDeeprelayCurrentWindow.to_json())

# convert the object into a dict
batch_deeprelay_current_window_dict = batch_deeprelay_current_window_instance.to_dict()
# create an instance of BatchDeeprelayCurrentWindow from a dict
batch_deeprelay_current_window_from_dict = BatchDeeprelayCurrentWindow.from_dict(batch_deeprelay_current_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


