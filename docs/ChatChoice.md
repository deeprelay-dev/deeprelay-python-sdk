# ChatChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**message** | [**ChatMessage**](ChatMessage.md) |  | [optional] 
**finish_reason** | **str** | tool_calls appears only when the request carried tools and the model made a call, which requires a model that lists \&quot;tools\&quot; in its supported_parameters.  | [optional] 
**logprobs** | **Dict[str, object]** | Per-token log probabilities (OpenAI shape, &#x60;content&#x60; array) when the request set logprobs: true, passed through from the serving upstream. Not comparable across upstreams or numeric precisions.  | [optional] 

## Example

```python
from deeprelay_sdk.models.chat_choice import ChatChoice

# TODO update the JSON string below
json = "{}"
# create an instance of ChatChoice from a JSON string
chat_choice_instance = ChatChoice.from_json(json)
# print the JSON string representation of the object
print(ChatChoice.to_json())

# convert the object into a dict
chat_choice_dict = chat_choice_instance.to_dict()
# create an instance of ChatChoice from a dict
chat_choice_from_dict = ChatChoice.from_dict(chat_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


