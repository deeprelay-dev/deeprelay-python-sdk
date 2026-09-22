# SpendingLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_limit_cents** | **int** |  | 
**monthly_limit_dollars** | **float** |  | 
**current_month_spend_cents** | **int** |  | 
**current_month_spend_dollars** | **float** |  | 
**percent_used** | **float** |  | 
**billing_cycle_start** | **datetime** |  | 
**enforcement** | **str** |  | 
**auto_terminate_hours** | **int** |  | [optional] 
**daily_limit_cents** | **int** |  | [optional] 
**daily_limit_dollars** | **float** |  | [optional] 
**current_day_spend_cents** | **int** |  | 

## Example

```python
from deeprelay_sdk.models.spending_limit import SpendingLimit

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingLimit from a JSON string
spending_limit_instance = SpendingLimit.from_json(json)
# print the JSON string representation of the object
print(SpendingLimit.to_json())

# convert the object into a dict
spending_limit_dict = spending_limit_instance.to_dict()
# create an instance of SpendingLimit from a dict
spending_limit_from_dict = SpendingLimit.from_dict(spending_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


