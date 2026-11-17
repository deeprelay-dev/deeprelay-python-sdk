# BatchFile

A batch file object: an input you uploaded (`batch`) or a result file written for a finished batch (`batch_output`, `batch_error`). The storage location is an internal detail and is intentionally absent from this schema (privacy-by-omission, D6).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | \&quot;file-\&quot; followed by 24 hex characters. | 
**object** | **str** |  | 
**bytes** | **int** |  | 
**created_at** | **int** | Unix timestamp (seconds). | 
**expires_at** | **int** | Unix timestamp (seconds) at which the file and its content are deleted. Input files default to 30 days after upload; result files to 30 days after the batch finishes. | 
**filename** | **str** |  | 
**purpose** | **str** |  | 

## Example

```python
from deeprelay_sdk.models.batch_file import BatchFile

# TODO update the JSON string below
json = "{}"
# create an instance of BatchFile from a JSON string
batch_file_instance = BatchFile.from_json(json)
# print the JSON string representation of the object
print(BatchFile.to_json())

# convert the object into a dict
batch_file_dict = batch_file_instance.to_dict()
# create an instance of BatchFile from a dict
batch_file_from_dict = BatchFile.from_dict(batch_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


