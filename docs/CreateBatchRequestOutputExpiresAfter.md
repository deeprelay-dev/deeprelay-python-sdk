# CreateBatchRequestOutputExpiresAfter

Lifetime of the output and error files. Absent means 30 days after the batch finishes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** |  | 
**seconds** | **int** |  | 

## Example

```python
from deeprelay_sdk.models.create_batch_request_output_expires_after import CreateBatchRequestOutputExpiresAfter

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchRequestOutputExpiresAfter from a JSON string
create_batch_request_output_expires_after_instance = CreateBatchRequestOutputExpiresAfter.from_json(json)
# print the JSON string representation of the object
print(CreateBatchRequestOutputExpiresAfter.to_json())

# convert the object into a dict
create_batch_request_output_expires_after_dict = create_batch_request_output_expires_after_instance.to_dict()
# create an instance of CreateBatchRequestOutputExpiresAfter from a dict
create_batch_request_output_expires_after_from_dict = CreateBatchRequestOutputExpiresAfter.from_dict(create_batch_request_output_expires_after_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


