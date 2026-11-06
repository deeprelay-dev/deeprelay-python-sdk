# PayFromBalanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_key** | **str** | The plan to pay for (&#x60;base&#x60; or &#x60;plus&#x60;). With an active subscription it must be bigger than the current plan. | 

## Example

```python
from deeprelay_sdk.models.pay_from_balance_request import PayFromBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayFromBalanceRequest from a JSON string
pay_from_balance_request_instance = PayFromBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(PayFromBalanceRequest.to_json())

# convert the object into a dict
pay_from_balance_request_dict = pay_from_balance_request_instance.to_dict()
# create an instance of PayFromBalanceRequest from a dict
pay_from_balance_request_from_dict = PayFromBalanceRequest.from_dict(pay_from_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


