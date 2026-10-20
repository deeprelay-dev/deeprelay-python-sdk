# UsageCompletionTokensDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasoning_tokens** | **int** |  | [optional] 

## Example

```python
from deeprelay_sdk.models.usage_completion_tokens_details import UsageCompletionTokensDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UsageCompletionTokensDetails from a JSON string
usage_completion_tokens_details_instance = UsageCompletionTokensDetails.from_json(json)
# print the JSON string representation of the object
print(UsageCompletionTokensDetails.to_json())

# convert the object into a dict
usage_completion_tokens_details_dict = usage_completion_tokens_details_instance.to_dict()
# create an instance of UsageCompletionTokensDetails from a dict
usage_completion_tokens_details_from_dict = UsageCompletionTokensDetails.from_dict(usage_completion_tokens_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


