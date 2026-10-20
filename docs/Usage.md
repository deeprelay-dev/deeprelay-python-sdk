# Usage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **int** |  | 
**completion_tokens** | **int** |  | 
**total_tokens** | **int** |  | 
**prompt_tokens_details** | [**UsagePromptTokensDetails**](UsagePromptTokensDetails.md) |  | [optional] 
**completion_tokens_details** | [**UsageCompletionTokensDetails**](UsageCompletionTokensDetails.md) |  | [optional] 
**cost** | **float** | The amount charged for this call in USD: equal to cost_details.charged_amount, so 0 for a call covered by the flat subscription. An exact decimal with up to 8 places, emitted as a JSON number. On a stream it appears only in the final usage chunk. Your invoice is computed from the billing ledger, which prices the call from the same breakdown.  | [optional] 
**cost_details** | [**CostDetails**](CostDetails.md) |  | [optional] 

## Example

```python
from deeprelay_sdk.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print(Usage.to_json())

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_from_dict = Usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


