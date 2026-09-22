# ModelRate

One per-1M-token rate triple, in rounded cents and exact micro-cents (1e-6 cent). Prefer the micro-cent fields for arithmetic; cached rates are routinely sub-cent and their cents field is then omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_per_1m_tokens_cents** | **int** |  | [optional] 
**input_per_1m_tokens_microcents** | **int** |  | [optional] 
**cached_input_per_1m_tokens_cents** | **int** |  | [optional] 
**cached_input_per_1m_tokens_microcents** | **int** |  | [optional] 
**output_per_1m_tokens_cents** | **int** |  | [optional] 
**output_per_1m_tokens_microcents** | **int** |  | [optional] 

## Example

```python
from deeprelay_sdk.models.model_rate import ModelRate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelRate from a JSON string
model_rate_instance = ModelRate.from_json(json)
# print the JSON string representation of the object
print(ModelRate.to_json())

# convert the object into a dict
model_rate_dict = model_rate_instance.to_dict()
# create an instance of ModelRate from a dict
model_rate_from_dict = ModelRate.from_dict(model_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


