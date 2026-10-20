# UsagePromptTokensDetails

Present whenever the upstream reported prompt-cache usage, including a reported 0. Absent means the upstream did not report it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached_tokens** | **int** | Prompt tokens served from the upstream&#39;s prompt cache. | [optional] 

## Example

```python
from deeprelay_sdk.models.usage_prompt_tokens_details import UsagePromptTokensDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UsagePromptTokensDetails from a JSON string
usage_prompt_tokens_details_instance = UsagePromptTokensDetails.from_json(json)
# print the JSON string representation of the object
print(UsagePromptTokensDetails.to_json())

# convert the object into a dict
usage_prompt_tokens_details_dict = usage_prompt_tokens_details_instance.to_dict()
# create an instance of UsagePromptTokensDetails from a dict
usage_prompt_tokens_details_from_dict = UsagePromptTokensDetails.from_dict(usage_prompt_tokens_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


