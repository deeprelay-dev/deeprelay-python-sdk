# UsageBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_start** | **datetime** |  | 
**instance_id** | **str** |  | [optional] 
**gpu_type** | **str** |  | [optional] 
**gpu_seconds** | **int** |  | 
**cost_cents** | **int** |  | 

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


