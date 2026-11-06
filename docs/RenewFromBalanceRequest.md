# RenewFromBalanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Pay each renewal from deposited balance when it covers the full price. | 

## Example

```python
from deeprelay_sdk.models.renew_from_balance_request import RenewFromBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenewFromBalanceRequest from a JSON string
renew_from_balance_request_instance = RenewFromBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(RenewFromBalanceRequest.to_json())

# convert the object into a dict
renew_from_balance_request_dict = renew_from_balance_request_instance.to_dict()
# create an instance of RenewFromBalanceRequest from a dict
renew_from_balance_request_from_dict = RenewFromBalanceRequest.from_dict(renew_from_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


