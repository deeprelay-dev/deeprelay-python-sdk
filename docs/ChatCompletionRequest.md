# ChatCompletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Canonical model id, e.g. \&quot;deeprelay/llama-3.3-70b-instruct\&quot;. | 
**messages** | [**List[ChatMessage]**](ChatMessage.md) |  | 
**temperature** | **float** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**max_completion_tokens** | **int** | OpenAI&#39;s newer name for max_tokens, accepted for client compatibility. When both are sent, max_tokens wins.  | [optional] 
**stream** | **bool** |  | [optional] [default to False]
**stream_options** | [**StreamOptions**](StreamOptions.md) |  | [optional] 
**tools** | [**List[Tool]**](Tool.md) | Functions the model may call. Support is per-model — check for \&quot;tools\&quot; in the model&#39;s supported_parameters before sending it. Omit the field entirely rather than sending an empty array.  | [optional] 
**tool_choice** | [**ChatCompletionRequestToolChoice**](ChatCompletionRequestToolChoice.md) |  | [optional] 
**response_format** | [**ChatCompletionRequestResponseFormat**](ChatCompletionRequestResponseFormat.md) |  | [optional] 
**reasoning_effort** | **str** | Hint: how much a reasoning model should think. Values in use are none, minimal, low, medium, high and xhigh; which ones a model accepts varies. Forwarded to an upstream that accepts the value, otherwise dropped and reported in x-deeprelay-ignored-params. Never rejected.  | [optional] 
**presence_penalty** | **float** | Hint. Forwarded when the serving upstream accepts it, otherwise dropped and reported in x-deeprelay-ignored-params. | [optional] 
**frequency_penalty** | **float** | Hint. Forwarded when the serving upstream accepts it, otherwise dropped and reported in x-deeprelay-ignored-params. | [optional] 
**seed** | **int** | Hint for best-effort determinism. Forwarded when the serving upstream accepts it, otherwise dropped and reported. Identical seeds are not guaranteed to give identical output across upstreams.  | [optional] 
**parallel_tool_calls** | **bool** | Whether the model may emit several tool calls in one turn. When false and the serving upstream cannot honour it, the relay returns only the first tool call and reports &#x60;parallel_tool_calls:enforced&#x60; in x-deeprelay-ignored-params.  | [optional] 
**logprobs** | **bool** | Return per-token log probabilities in choices[].logprobs. Gated per model (\&quot;logprobs\&quot; in supported_parameters). Values come from the serving upstream and are not comparable across upstreams or numeric precisions.  | [optional] 
**top_logprobs** | **int** | Number of alternatives per token (requires logprobs). Gated per model; each model has its own maximum, and a larger value returns 400 unsupported_parameter.  | [optional] 

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


