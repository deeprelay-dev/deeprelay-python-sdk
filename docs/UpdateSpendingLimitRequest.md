# UpdateSpendingLimitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_limit_dollars** | **float** | Monthly limit in USD (minimum 1.00). | 
**enforcement** | **str** |  | [optional] 
**auto_terminate_hours** | **int** | Hours after the limit is reached before auto-terminate; null &#x3D; never. | [optional] 
**daily_limit_dollars** | **float** | Opt-in daily cap in USD. Omit &#x3D; unchanged, 0 &#x3D; clear, &gt; 0 &#x3D; set. | [optional] 

## Example

```python
from deeprelay_sdk.models.update_spending_limit_request import UpdateSpendingLimitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSpendingLimitRequest from a JSON string
update_spending_limit_request_instance = UpdateSpendingLimitRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSpendingLimitRequest.to_json())

# convert the object into a dict
update_spending_limit_request_dict = update_spending_limit_request_instance.to_dict()
# create an instance of UpdateSpendingLimitRequest from a dict
update_spending_limit_request_from_dict = UpdateSpendingLimitRequest.from_dict(update_spending_limit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


