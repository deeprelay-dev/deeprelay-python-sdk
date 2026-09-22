# EmbeddingsRequestInput

Text to embed: either a single string or an array of up to 2048 strings. Token-id arrays are not supported. The per-request ceiling is bounded so the response stays under 64 MiB — about 680 inputs at 4096 dimensions, fewer at a larger `dimensions` value; an over-limit batch is rejected with 400 invalid_request_error whose message states the limit, before any processing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deeprelay_sdk.models.embeddings_request_input import EmbeddingsRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingsRequestInput from a JSON string
embeddings_request_input_instance = EmbeddingsRequestInput.from_json(json)
# print the JSON string representation of the object
print(EmbeddingsRequestInput.to_json())

# convert the object into a dict
embeddings_request_input_dict = embeddings_request_input_instance.to_dict()
# create an instance of EmbeddingsRequestInput from a dict
embeddings_request_input_from_dict = EmbeddingsRequestInput.from_dict(embeddings_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


