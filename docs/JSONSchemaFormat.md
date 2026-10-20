# JSONSchemaFormat

The schema is forwarded byte-for-byte. It may be at most 64 KiB and nested at most 32 levels deep; larger or deeper schemas return 400 unsupported_parameter (param response_format). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**var_schema** | **Dict[str, object]** | A JSON Schema object describing the reply. | [optional] 
**strict** | **bool** | When true, the reply is guaranteed to match the schema; only models listing \&quot;structured_outputs\&quot; accept it.  | [optional] 

## Example

```python
from deeprelay_sdk.models.json_schema_format import JSONSchemaFormat

# TODO update the JSON string below
json = "{}"
# create an instance of JSONSchemaFormat from a JSON string
json_schema_format_instance = JSONSchemaFormat.from_json(json)
# print the JSON string representation of the object
print(JSONSchemaFormat.to_json())

# convert the object into a dict
json_schema_format_dict = json_schema_format_instance.to_dict()
# create an instance of JSONSchemaFormat from a dict
json_schema_format_from_dict = JSONSchemaFormat.from_dict(json_schema_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


