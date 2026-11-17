# BatchLimits

Every per-organization batch limit with its current value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_lines** | **int** | Lines per input file (default 50,000). | 
**max_file_bytes** | **int** | Input file size in bytes (default 200 MiB). | 
**max_line_bytes** | **int** | One line&#39;s size in bytes (default 8 MiB). | 
**max_active_batches** | **int** | Batches that are not finished yet (default 10). | 
**active_batches** | **int** |  | 
**max_files** | **int** | Stored batch input files (default 500). | 
**files** | **int** |  | 
**queued_token_cap** | **int** | Estimated tokens across all unfinished batches. | 
**queued_tokens** | **int** |  | 
**max_age_hours** | **int** | Hours from submit until a batch expires (default 72). | 
**retention_days** | **int** | Days batch files are kept after the batch finishes (default 30). | 

## Example

```python
from deeprelay_sdk.models.batch_limits import BatchLimits

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLimits from a JSON string
batch_limits_instance = BatchLimits.from_json(json)
# print the JSON string representation of the object
print(BatchLimits.to_json())

# convert the object into a dict
batch_limits_dict = batch_limits_instance.to_dict()
# create an instance of BatchLimits from a dict
batch_limits_from_dict = BatchLimits.from_dict(batch_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


