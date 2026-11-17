# BatchMoney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microcents** | **int** |  | 

## Example

```python
from deeprelay_sdk.models.batch_money import BatchMoney

# TODO update the JSON string below
json = "{}"
# create an instance of BatchMoney from a JSON string
batch_money_instance = BatchMoney.from_json(json)
# print the JSON string representation of the object
print(BatchMoney.to_json())

# convert the object into a dict
batch_money_dict = batch_money_instance.to_dict()
# create an instance of BatchMoney from a dict
batch_money_from_dict = BatchMoney.from_dict(batch_money_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


