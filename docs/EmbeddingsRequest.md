# EmbeddingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Canonical embedding model id, e.g. \&quot;deeprelay/qwen3-embedding-8b\&quot;. | 
**input** | [**EmbeddingsRequestInput**](EmbeddingsRequestInput.md) |  | 
**encoding_format** | **str** | Only \&quot;float\&quot; is supported. A value of \&quot;base64\&quot; is rejected with invalid_request_error / unsupported_parameter. | [optional] [default to 'float']
**dimensions** | **int** | Requested output dimensionality, for models that support truncated (Matryoshka) embeddings. Passed through to the model when set. | [optional] 
**user** | **str** | Opaque end-user identifier for abuse tracing. Optional. | [optional] 

## Example

```python
from deeprelay_sdk.models.embeddings_request import EmbeddingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingsRequest from a JSON string
embeddings_request_instance = EmbeddingsRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddingsRequest.to_json())

# convert the object into a dict
embeddings_request_dict = embeddings_request_instance.to_dict()
# create an instance of EmbeddingsRequest from a dict
embeddings_request_from_dict = EmbeddingsRequest.from_dict(embeddings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


