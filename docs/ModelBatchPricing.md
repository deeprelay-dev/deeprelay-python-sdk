# ModelBatchPricing

`pricing.batch`: what a Batch API line for this model bills at. Present on chat models while the Batch API is enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** | Whether the model can be used in a batch. | 
**rate_tier** | **str** | &#x60;off_peak&#x60; (the model&#39;s off-peak rate), &#x60;batch&#x60; (a batch price set for the model) or &#x60;normal&#x60; (the standard rate; a model with no peak schedule). Present when eligible. | [optional] 
**input_per_1m_tokens_microcents** | **int** |  | [optional] 
**cached_input_per_1m_tokens_microcents** | **int** |  | [optional] 
**output_per_1m_tokens_microcents** | **int** |  | [optional] 
**schedule_url** | **str** | Where the model&#39;s peak and off-peak schedule is documented. | [optional] 

## Example

```python
from deeprelay_sdk.models.model_batch_pricing import ModelBatchPricing

# TODO update the JSON string below
json = "{}"
# create an instance of ModelBatchPricing from a JSON string
model_batch_pricing_instance = ModelBatchPricing.from_json(json)
# print the JSON string representation of the object
print(ModelBatchPricing.to_json())

# convert the object into a dict
model_batch_pricing_dict = model_batch_pricing_instance.to_dict()
# create an instance of ModelBatchPricing from a dict
model_batch_pricing_from_dict = ModelBatchPricing.from_dict(model_batch_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


