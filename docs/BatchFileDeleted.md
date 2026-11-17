# BatchFileDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**deleted** | **bool** |  | 

## Example

```python
from deeprelay_sdk.models.batch_file_deleted import BatchFileDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of BatchFileDeleted from a JSON string
batch_file_deleted_instance = BatchFileDeleted.from_json(json)
# print the JSON string representation of the object
print(BatchFileDeleted.to_json())

# convert the object into a dict
batch_file_deleted_dict = batch_file_deleted_instance.to_dict()
# create an instance of BatchFileDeleted from a dict
batch_file_deleted_from_dict = BatchFileDeleted.from_dict(batch_file_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


