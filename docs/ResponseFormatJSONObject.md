# ResponseFormatJSONObject

The reply is a single valid JSON object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from deeprelay_sdk.models.response_format_json_object import ResponseFormatJSONObject

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseFormatJSONObject from a JSON string
response_format_json_object_instance = ResponseFormatJSONObject.from_json(json)
# print the JSON string representation of the object
print(ResponseFormatJSONObject.to_json())

# convert the object into a dict
response_format_json_object_dict = response_format_json_object_instance.to_dict()
# create an instance of ResponseFormatJSONObject from a dict
response_format_json_object_from_dict = ResponseFormatJSONObject.from_dict(response_format_json_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


