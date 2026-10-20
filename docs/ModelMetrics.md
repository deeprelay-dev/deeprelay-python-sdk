# ModelMetrics

Measured performance over a rolling window, from deeprelay's own customer traffic only. A figure is omitted (never zero) when it has too few samples behind it; the counts and minimums are always present so a reader can tell why.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window_days** | **int** |  | 
**as_of** | **datetime** | The hour the figures were computed for. | 
**sample_count** | **int** |  | 
**stream_sample_count** | **int** |  | 
**min_samples** | **int** | Samples needed before &#x60;success_rate&#x60; is published. | 
**min_stream_samples** | **int** | Streamed samples needed before the TTFT and tokens/s figures are published. | 
**ttft_p50_ms** | **float** | Median time to first token, in milliseconds. | [optional] 
**tokens_per_second_p50** | **float** | Median decode rate after the first token, in tokens per second. | [optional] 
**success_rate** | **float** |  | [optional] 
**insufficient_data** | **bool** | True when &#x60;sample_count&#x60; is below &#x60;min_samples&#x60;. | 
**precision** | **str** | What deeprelay can state about the numeric precision this model is served at: &#x60;full&#x60; (always full precision), &#x60;mixed&#x60; (some serving capacity is quantized) or &#x60;unverified&#x60; (not verified; the default). | 

## Example

```python
from deeprelay_sdk.models.model_metrics import ModelMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ModelMetrics from a JSON string
model_metrics_instance = ModelMetrics.from_json(json)
# print the JSON string representation of the object
print(ModelMetrics.to_json())

# convert the object into a dict
model_metrics_dict = model_metrics_instance.to_dict()
# create an instance of ModelMetrics from a dict
model_metrics_from_dict = ModelMetrics.from_dict(model_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


