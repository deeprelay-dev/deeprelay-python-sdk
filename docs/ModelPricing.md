# ModelPricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**input_per_1m_tokens_cents** | **int** |  | [optional] 
**output_per_1m_tokens_cents** | **int** |  | [optional] 
**cached_input_per_1m_tokens_microcents** | **int** | Exact per-1M-token rate in micro-cents (1e-6 cent) for the cache-HIT part of a chat prompt (usage.prompt_tokens_details.cached_tokens). Present only on models with a published cached-input rate; absent means no discount — every prompt token bills at input_per_1m_tokens_cents. Treat this field as the presence signal: cached rates are routinely sub-cent, so the rounded cents field below is often omitted. | [optional] 
**cached_input_per_1m_tokens_cents** | **int** | cached_input_per_1m_tokens_microcents rounded to whole cents; omitted when the exact rate rounds below half a cent. | [optional] 
**per_image_cents** | **int** |  | [optional] 
**per_image_microcents** | **int** | Exact per-image rate in micro-cents (1e-6 cent). Prefer this for image models — per_image_cents rounds sub-cent prices to 0. | [optional] 
**per_mpxl_microcents** | **int** | Price per output megapixel in micro-cents (1e-6 cent) for image models metered per megapixel. Mutually exclusive with the per-image fields. | [optional] 
**per_video_microcents** | **int** | Representative per-clip price in micro-cents (1e-6 cent) for video models — a \&quot;from\&quot; price taken from the provider&#39;s published example rate. | [optional] 
**per_video_second_cents** | **int** |  | [optional] 
**per_video_second_microcents** | **int** | Exact per-second-of-output-video rate in micro-cents (1e-6 cent). Prefer this for video models. | [optional] 
**period** | **str** | Present only on a model priced by time of day. Which side of the peak schedule the instant this response was rendered falls on; the flat rate fields above are the rates in effect at that instant. A request is billed at the rate in effect when it ARRIVES (UTC), so a caller planning a call for later should price it from &#x60;peak&#x60; / &#x60;off_peak&#x60; and &#x60;peak_windows_utc&#x60;. | [optional] 
**peak_windows_utc** | [**List[PeakWindow]**](PeakWindow.md) | The daily UTC ranges during which the &#x60;peak&#x60; rates apply, start inclusive and end exclusive (\&quot;24:00\&quot; is a valid end; a range whose end sorts before its start wraps midnight). Present only on a model priced by time of day. | [optional] 
**peak** | [**ModelRate**](ModelRate.md) |  | [optional] 
**off_peak** | [**ModelRate**](ModelRate.md) |  | [optional] 

## Example

```python
from deeprelay_sdk.models.model_pricing import ModelPricing

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPricing from a JSON string
model_pricing_instance = ModelPricing.from_json(json)
# print the JSON string representation of the object
print(ModelPricing.to_json())

# convert the object into a dict
model_pricing_dict = model_pricing_instance.to_dict()
# create an instance of ModelPricing from a dict
model_pricing_from_dict = ModelPricing.from_dict(model_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


