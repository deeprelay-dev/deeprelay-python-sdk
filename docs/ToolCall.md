# ToolCall

A function call the model emitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Position among parallel calls. Present on streaming deltas, which key their fragments by it; absent on assembled messages.  | [optional] 
**id** | **str** | Identifier for this call. Echo it back as tool_call_id on the message carrying the result.  | [optional] 
**type** | **str** |  | [optional] 
**function** | [**ToolCallFunction**](ToolCallFunction.md) |  | 

## Example

```python
from deeprelay_sdk.models.tool_call import ToolCall

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCall from a JSON string
tool_call_instance = ToolCall.from_json(json)
# print the JSON string representation of the object
print(ToolCall.to_json())

# convert the object into a dict
tool_call_dict = tool_call_instance.to_dict()
# create an instance of ToolCall from a dict
tool_call_from_dict = ToolCall.from_dict(tool_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


