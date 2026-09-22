# Balance

The organization's credit balance with its auto-pay configuration and live burn rate. Mirrors the dashboard's balance contract field for field. No payment-instrument detail appears here — saved cards live behind separate admin-only routes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_cents** | **int** | Remaining credit in USD cents. May be negative when usage has outrun the balance. | 
**balance_dollars** | **float** | The same figure in dollars, for display. | 
**auto_pay_enabled** | **bool** |  | 
**auto_pay_threshold_cents** | **int** | Auto-pay triggers when the balance falls below this. Meaningful only when auto_pay_enabled. | 
**auto_pay_amount_cents** | **int** | Amount auto-pay charges when it triggers. Meaningful only when auto_pay_enabled. | 
**burn_cents_per_hour** | **int** | Live burn rate in USD cents per hour: the committed hourly price of every instance that is live, counted from launch — so instances still creating, provisioning or booting are included, not only those that have reached running. 0 when nothing is live.  &#x60;null&#x60; means the burn rate could not be determined. Treat that as unknown, never as 0: reading an unavailable burn rate as \&quot;nothing running\&quot; reports unbounded runway to an organization that may be minutes from empty. | 

## Example

```python
from deeprelay_sdk.models.balance import Balance

# TODO update the JSON string below
json = "{}"
# create an instance of Balance from a JSON string
balance_instance = Balance.from_json(json)
# print the JSON string representation of the object
print(Balance.to_json())

# convert the object into a dict
balance_dict = balance_instance.to_dict()
# create an instance of Balance from a dict
balance_from_dict = Balance.from_dict(balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


