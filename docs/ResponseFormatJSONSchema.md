# ResponseFormatJSONSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**json_schema** | [**JSONSchemaFormat**](JSONSchemaFormat.md) |  | 

## Example

```python
from deeprelay_sdk.models.response_format_json_schema import ResponseFormatJSONSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseFormatJSONSchema from a JSON string
response_format_json_schema_instance = ResponseFormatJSONSchema.from_json(json)
# print the JSON string representation of the object
print(ResponseFormatJSONSchema.to_json())

# convert the object into a dict
response_format_json_schema_dict = response_format_json_schema_instance.to_dict()
# create an instance of ResponseFormatJSONSchema from a dict
response_format_json_schema_from_dict = ResponseFormatJSONSchema.from_dict(response_format_json_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


