# SubscriptionModelUsage

One model's plan-covered usage in a window. Cached input is part of `input_tokens` and counts toward the allowance in full; it is broken out only so you can see how much of your input was cache reads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Catalog model id, e.g. &#x60;deeprelay/kimi-k3&#x60;. | 
**input_tokens** | **int** | Raw input tokens served, cached input included. | 
**cached_input_tokens** | **int** | The part of &#x60;input_tokens&#x60; served from a prompt cache. A subset, never an addition. | 
**output_tokens** | **int** | Raw output tokens served, reasoning included. | 
**usage_factor_milli** | **int** | The model&#39;s usage factor in thousandths (1000 &#x3D; ×1, 24000 &#x3D; ×24). | 
**weighted_input_tokens** | **int** | &#x60;input_tokens&#x60; × the usage factor: what this model drew from the input allowance. | 
**weighted_output_tokens** | **int** | &#x60;output_tokens&#x60; × the usage factor: what this model drew from the output allowance. | 

## Example

```python
from deeprelay_sdk.models.subscription_model_usage import SubscriptionModelUsage

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionModelUsage from a JSON string
subscription_model_usage_instance = SubscriptionModelUsage.from_json(json)
# print the JSON string representation of the object
print(SubscriptionModelUsage.to_json())

# convert the object into a dict
subscription_model_usage_dict = subscription_model_usage_instance.to_dict()
# create an instance of SubscriptionModelUsage from a dict
subscription_model_usage_from_dict = SubscriptionModelUsage.from_dict(subscription_model_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


