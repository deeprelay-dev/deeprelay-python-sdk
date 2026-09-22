# EmbeddingsUsage

Embeddings are billed on input tokens only, so this block carries no completion_tokens field — an embeddings call emits none, and total_tokens always equals prompt_tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **int** |  | 
**total_tokens** | **int** |  | 

## Example

```python
from deeprelay_sdk.models.embeddings_usage import EmbeddingsUsage

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingsUsage from a JSON string
embeddings_usage_instance = EmbeddingsUsage.from_json(json)
# print the JSON string representation of the object
print(EmbeddingsUsage.to_json())

# convert the object into a dict
embeddings_usage_dict = embeddings_usage_instance.to_dict()
# create an instance of EmbeddingsUsage from a dict
embeddings_usage_from_dict = EmbeddingsUsage.from_dict(embeddings_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


