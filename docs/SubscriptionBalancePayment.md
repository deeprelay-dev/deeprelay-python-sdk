# SubscriptionBalancePayment

How the organization's balance splits for paying a plan. free_credit_cents + pending_deposit_cents + spendable_cents equals the balance (zero when the balance is negative). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_cents** | **int** |  | 
**spendable_cents** | **int** | Deposited cash that can pay for a plan now. | 
**free_credit_cents** | **int** | Unspent free credit. Pays for usage, never for a plan. | 
**pending_deposit_cents** | **int** | Card or UPI deposits still inside their 24-hour wait. | 
**pending_until** | **datetime** | When the oldest pending deposit can pay for a plan. | [optional] 

## Example

```python
from deeprelay_sdk.models.subscription_balance_payment import SubscriptionBalancePayment

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionBalancePayment from a JSON string
subscription_balance_payment_instance = SubscriptionBalancePayment.from_json(json)
# print the JSON string representation of the object
print(SubscriptionBalancePayment.to_json())

# convert the object into a dict
subscription_balance_payment_dict = subscription_balance_payment_instance.to_dict()
# create an instance of SubscriptionBalancePayment from a dict
subscription_balance_payment_from_dict = SubscriptionBalancePayment.from_dict(subscription_balance_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


