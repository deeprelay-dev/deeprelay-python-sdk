# Batch

The OpenAI batch object plus a `deeprelay` sub-object with the schedule, rate and cost. Timestamps are Unix seconds, null when unset. A paused batch stays `in_progress` with `deeprelay.pause_reason` set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | \&quot;batch_\&quot; followed by 24 hex characters. | 
**object** | **str** |  | 
**endpoint** | **str** |  | 
**model** | **str** | The one model every line of the batch uses. | 
**errors** | **object** | Always null. A file with an invalid line is rejected whole at submit, so an accepted batch has no validation errors. | 
**input_file_id** | **str** |  | 
**completion_window** | **str** |  | 
**status** | **str** | &#x60;expired&#x60; means at least one line did not run before the batch&#39;s deadline; the output file still holds every completed line. | 
**output_file_id** | **str** | Set once the batch has finished. | 
**error_file_id** | **str** | Set once the batch has finished, when any line failed, expired or was cancelled. | 
**created_at** | **int** |  | 
**in_progress_at** | **int** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**finalizing_at** | **int** |  | [optional] 
**completed_at** | **int** |  | [optional] 
**failed_at** | **int** |  | [optional] 
**expired_at** | **int** |  | [optional] 
**cancelling_at** | **int** |  | [optional] 
**cancelled_at** | **int** |  | [optional] 
**request_counts** | [**BatchRequestCounts**](BatchRequestCounts.md) |  | 
**usage** | [**BatchUsage**](BatchUsage.md) |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**deeprelay** | [**BatchDeeprelay**](BatchDeeprelay.md) |  | 

## Example

```python
from deeprelay_sdk.models.batch import Batch

# TODO update the JSON string below
json = "{}"
# create an instance of Batch from a JSON string
batch_instance = Batch.from_json(json)
# print the JSON string representation of the object
print(Batch.to_json())

# convert the object into a dict
batch_dict = batch_instance.to_dict()
# create an instance of Batch from a dict
batch_from_dict = Batch.from_dict(batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


