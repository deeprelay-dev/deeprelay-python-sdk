# BatchUsage

Token usage summed over the batch's billed lines.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** |  | 
**input_tokens_details** | [**BatchUsageInputTokensDetails**](BatchUsageInputTokensDetails.md) |  | 
**output_tokens** | **int** |  | 
**output_tokens_details** | [**BatchUsageOutputTokensDetails**](BatchUsageOutputTokensDetails.md) |  | 
**total_tokens** | **int** |  | 

## Example

```python
from deeprelay_sdk.models.batch_usage import BatchUsage

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUsage from a JSON string
batch_usage_instance = BatchUsage.from_json(json)
# print the JSON string representation of the object
print(BatchUsage.to_json())

# convert the object into a dict
batch_usage_dict = batch_usage_instance.to_dict()
# create an instance of BatchUsage from a dict
batch_usage_from_dict = BatchUsage.from_dict(batch_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


