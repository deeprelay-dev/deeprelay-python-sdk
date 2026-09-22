# ChatCompletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Canonical model id, e.g. \&quot;deeprelay/qwen2.5-7b-instruct\&quot;. | 
**messages** | [**List[ChatMessage]**](ChatMessage.md) |  | 
**temperature** | **float** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**stream** | **bool** |  | [optional] [default to False]
**stream_options** | [**StreamOptions**](StreamOptions.md) |  | [optional] 

## Example

```python
from deeprelay_sdk.models.chat_completion_request import ChatCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequest from a JSON string
chat_completion_request_instance = ChatCompletionRequest.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequest.to_json())

# convert the object into a dict
chat_completion_request_dict = chat_completion_request_instance.to_dict()
# create an instance of ChatCompletionRequest from a dict
chat_completion_request_from_dict = ChatCompletionRequest.from_dict(chat_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


