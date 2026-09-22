# VideoCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Customer-facing video model id (e.g. deeprelay/wan-2.2-t2v) or alias. | 
**prompt** | **str** | Text description of the video to generate. | 
**size** | **str** | Output video dimensions as WxH (e.g. 1280x720). | [optional] 
**seconds** | **int** | Output video duration in seconds (the billable unit). | [optional] 

## Example

```python
from deeprelay_sdk.models.video_create_request import VideoCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VideoCreateRequest from a JSON string
video_create_request_instance = VideoCreateRequest.from_json(json)
# print the JSON string representation of the object
print(VideoCreateRequest.to_json())

# convert the object into a dict
video_create_request_dict = video_create_request_instance.to_dict()
# create an instance of VideoCreateRequest from a dict
video_create_request_from_dict = VideoCreateRequest.from_dict(video_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


