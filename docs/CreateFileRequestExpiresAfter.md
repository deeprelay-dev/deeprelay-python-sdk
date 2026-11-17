# CreateFileRequestExpiresAfter

Optional file lifetime, sent as the form fields `expires_after[anchor]` and `expires_after[seconds]`. Absent means 30 days after upload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** |  | 
**seconds** | **int** |  | 

## Example

```python
from deeprelay_sdk.models.create_file_request_expires_after import CreateFileRequestExpiresAfter

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileRequestExpiresAfter from a JSON string
create_file_request_expires_after_instance = CreateFileRequestExpiresAfter.from_json(json)
# print the JSON string representation of the object
print(CreateFileRequestExpiresAfter.to_json())

# convert the object into a dict
create_file_request_expires_after_dict = create_file_request_expires_after_instance.to_dict()
# create an instance of CreateFileRequestExpiresAfter from a dict
create_file_request_expires_after_from_dict = CreateFileRequestExpiresAfter.from_dict(create_file_request_expires_after_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


