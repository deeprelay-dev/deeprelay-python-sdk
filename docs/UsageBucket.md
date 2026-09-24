# UsageBucket

One `/usage` row. Every row carries `bucket_start`, `gpu_seconds` and `cost_cents`. When the request set `modality` or `model` the row is an inference-usage row: it also carries `modality`, `model`, `prompt_tokens`, `completion_tokens` and `image_count` (aggregating every serverless inference call in the bucket for that modality and model), and `gpu_seconds` is always 0. Otherwise it is an instance-usage row, carrying `instance_id` / `gpu_type` when `group_by` asked for them. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_start** | **datetime** | Start of the time bucket (truncated to &#x60;bucket&#x60;). | 
**instance_id** | **str** | Instance-usage rows with &#x60;group_by&#x3D;instance_id&#x60; only. | [optional] 
**gpu_type** | **str** | Instance-usage rows with &#x60;group_by&#x3D;gpu_type&#x60; only. | [optional] 
**gpu_seconds** | **int** | GPU instance seconds billed in the bucket. Always 0 on inference-usage rows. | 
**cost_cents** | **int** | Total cost of the row, in US cents. | 
**modality** | **str** | Inference-usage rows only: the modality of the calls in this row (chat, image, video or embedding).  | [optional] 
**model** | **str** | Inference-usage rows only: the model &#x60;id&#x60; the calls in this row were made against.  | [optional] 
**prompt_tokens** | **int** | Inference-usage rows only. Sum of input tokens; 0 for modalities not billed per token. | [optional] 
**completion_tokens** | **int** | Inference-usage rows only. Sum of output tokens; 0 for modalities not billed per token. | [optional] 
**image_count** | **int** | Inference-usage rows only. Sum of generated images; 0 for non-image modalities. | [optional] 

## Example

```python
from deeprelay_sdk.models.usage_bucket import UsageBucket

# TODO update the JSON string below
json = "{}"
# create an instance of UsageBucket from a JSON string
usage_bucket_instance = UsageBucket.from_json(json)
# print the JSON string representation of the object
print(UsageBucket.to_json())

# convert the object into a dict
usage_bucket_dict = usage_bucket_instance.to_dict()
# create an instance of UsageBucket from a dict
usage_bucket_from_dict = UsageBucket.from_dict(usage_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


