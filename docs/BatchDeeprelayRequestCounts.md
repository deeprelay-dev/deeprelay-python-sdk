# BatchDeeprelayRequestCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **int** |  | 
**expired** | **int** |  | 
**remaining** | **int** |  | 

## Example

```python
from deeprelay_sdk.models.batch_deeprelay_request_counts import BatchDeeprelayRequestCounts

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeeprelayRequestCounts from a JSON string
batch_deeprelay_request_counts_instance = BatchDeeprelayRequestCounts.from_json(json)
# print the JSON string representation of the object
print(BatchDeeprelayRequestCounts.to_json())

# convert the object into a dict
batch_deeprelay_request_counts_dict = batch_deeprelay_request_counts_instance.to_dict()
# create an instance of BatchDeeprelayRequestCounts from a dict
batch_deeprelay_request_counts_from_dict = BatchDeeprelayRequestCounts.from_dict(batch_deeprelay_request_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


