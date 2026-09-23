# VideoJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**model** | **str** |  | 
**status** | **str** |  | 
**progress** | **int** | Generation progress 0-100. | 
**size** | **str** |  | [optional] 
**seconds** | **int** |  | [optional] 
**created_at** | **int** | Unix timestamp (seconds) when the job was created. | 
**completed_at** | **int** | Unix timestamp (seconds) when the job completed. | [optional] 
**expires_at** | **int** | Unix timestamp (seconds) when the artifact expires (24h after completion). | [optional] 
**error** | **str** | Canonical failure code when status is failed. | [optional] 
**error_message** | **str** | Human-readable reason behind &#x60;error&#x60;, when the upstream supplied one. &#x60;error&#x60; classifies the failure, &#x60;error_message&#x60; explains it (for example a requested duration outside the model&#39;s supported range). Sanitized before storage; only ever present alongside &#x60;error&#x60;. | [optional] 
**cost_cents** | **int** | Final billed cost in cents; present once the job completes (failed/cancelled jobs are never billed). | [optional] 

## Example

```python
from deeprelay_sdk.models.video_job import VideoJob

# TODO update the JSON string below
json = "{}"
# create an instance of VideoJob from a JSON string
video_job_instance = VideoJob.from_json(json)
# print the JSON string representation of the object
print(VideoJob.to_json())

# convert the object into a dict
video_job_dict = video_job_instance.to_dict()
# create an instance of VideoJob from a dict
video_job_from_dict = VideoJob.from_dict(video_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


