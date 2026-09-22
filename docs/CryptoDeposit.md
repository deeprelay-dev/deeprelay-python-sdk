# CryptoDeposit

A stablecoin deposit. Mirrors the Go DTO field for field. Like that struct, this schema deliberately has NO payment-processor property — the processor is an implementation detail and is structurally absent from the customer contract, not merely filtered out. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_id** | **str** |  | 
**status** | **str** | Lifecycle state: created, detected, confirming, settled, screening, held_screening, credited, credited_underpaid, credited_overpaid, expired, expired_received, failed, failed_screening.  | 
**chain** | **str** |  | 
**asset** | **str** |  | 
**pay_address** | **str** | The address to send funds to. Unique to this deposit. | [optional] 
**pay_amount** | **str** | The exact token amount to send, as a decimal string (never a number — the value must not round-trip through a float).  | [optional] 
**amount_usd_cents** | **int** | The amount requested, in USD cents. Never the settled or credited value. | 
**credited_cents** | **int** | USD cents actually credited to the balance. Absent until credited. | [optional] 
**tx_hash** | **str** |  | [optional] 
**expires_at** | **datetime** | RFC3339 UTC. After this, send nothing to pay_address. | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from deeprelay_sdk.models.crypto_deposit import CryptoDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoDeposit from a JSON string
crypto_deposit_instance = CryptoDeposit.from_json(json)
# print the JSON string representation of the object
print(CryptoDeposit.to_json())

# convert the object into a dict
crypto_deposit_dict = crypto_deposit_instance.to_dict()
# create an instance of CryptoDeposit from a dict
crypto_deposit_from_dict = CryptoDeposit.from_dict(crypto_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


