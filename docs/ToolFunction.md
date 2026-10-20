# ToolFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The function name the model will emit when it calls this tool. | 
**description** | **str** | What the function does. The model reads this to decide when to call it. | [optional] 
**parameters** | **Dict[str, object]** | JSON Schema for the function&#39;s arguments. Forwarded to the model untouched; deeprelay does not interpret it.  | [optional] 

## Example

```python
from deeprelay_sdk.models.tool_function import ToolFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ToolFunction from a JSON string
tool_function_instance = ToolFunction.from_json(json)
# print the JSON string representation of the object
print(ToolFunction.to_json())

# convert the object into a dict
tool_function_dict = tool_function_instance.to_dict()
# create an instance of ToolFunction from a dict
tool_function_from_dict = ToolFunction.from_dict(tool_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


