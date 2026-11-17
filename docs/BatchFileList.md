# BatchFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**data** | [**List[BatchFile]**](BatchFile.md) |  | 
**first_id** | **str** |  | 
**last_id** | **str** |  | 
**has_more** | **bool** |  | 

## Example

```python
from deeprelay_sdk.models.batch_file_list import BatchFileList

# TODO update the JSON string below
json = "{}"
# create an instance of BatchFileList from a JSON string
batch_file_list_instance = BatchFileList.from_json(json)
# print the JSON string representation of the object
print(BatchFileList.to_json())

# convert the object into a dict
batch_file_list_dict = batch_file_list_instance.to_dict()
# create an instance of BatchFileList from a dict
batch_file_list_from_dict = BatchFileList.from_dict(batch_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


