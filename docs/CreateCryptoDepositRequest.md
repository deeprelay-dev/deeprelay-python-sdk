# CreateCryptoDepositRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** | Amount to deposit in USD cents. Must be at least the configured minimum (500 &#x3D; $5.00 by default).  | 
**chain** | **str** |  | 
**asset** | **str** |  | 

## Example

```python
from deeprelay_sdk.models.create_crypto_deposit_request import CreateCryptoDepositRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCryptoDepositRequest from a JSON string
create_crypto_deposit_request_instance = CreateCryptoDepositRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCryptoDepositRequest.to_json())

# convert the object into a dict
create_crypto_deposit_request_dict = create_crypto_deposit_request_instance.to_dict()
# create an instance of CreateCryptoDepositRequest from a dict
create_crypto_deposit_request_from_dict = CreateCryptoDepositRequest.from_dict(create_crypto_deposit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


