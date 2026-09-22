# ListDeposits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposits** | [**List[CryptoDeposit]**](CryptoDeposit.md) |  | 
**min_deposit_cents** | **int** | The effective minimum deposit in USD cents (admin override, else the deployment&#39;s configured floor). Validate amounts against this live value rather than hardcoding the default. | 

## Example

```python
from deeprelay_sdk.models.list_deposits200_response import ListDeposits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeposits200Response from a JSON string
list_deposits200_response_instance = ListDeposits200Response.from_json(json)
# print the JSON string representation of the object
print(ListDeposits200Response.to_json())

# convert the object into a dict
list_deposits200_response_dict = list_deposits200_response_instance.to_dict()
# create an instance of ListDeposits200Response from a dict
list_deposits200_response_from_dict = ListDeposits200Response.from_dict(list_deposits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


