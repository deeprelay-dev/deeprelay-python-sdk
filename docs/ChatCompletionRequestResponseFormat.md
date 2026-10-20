# ChatCompletionRequestResponseFormat

Constrain the reply format. Gated per model: `json_object` needs \"response_format\" in the model's supported_parameters, and a strict `json_schema` needs \"structured_outputs\". A model without the capability returns 400 unsupported_parameter naming the models that have it. A non-strict json_schema on a model with only \"response_format\" is served as json_object and reported as `response_format:downgraded` in x-deeprelay-ignored-params. The relay never emulates JSON mode by prompting. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**json_schema** | [**JSONSchemaFormat**](JSONSchemaFormat.md) |  | 

## Example

```python
from deeprelay_sdk.models.chat_completion_request_response_format import ChatCompletionRequestResponseFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequestResponseFormat from a JSON string
chat_completion_request_response_format_instance = ChatCompletionRequestResponseFormat.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequestResponseFormat.to_json())

# convert the object into a dict
chat_completion_request_response_format_dict = chat_completion_request_response_format_instance.to_dict()
# create an instance of ChatCompletionRequestResponseFormat from a dict
chat_completion_request_response_format_from_dict = ChatCompletionRequestResponseFormat.from_dict(chat_completion_request_response_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


