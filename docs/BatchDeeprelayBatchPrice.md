# BatchDeeprelayBatchPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_per_1m_microcents** | **int** |  | 
**cached_input_per_1m_microcents** | **int** |  | 
**output_per_1m_microcents** | **int** |  | 

## Example

```python
from deeprelay_sdk.models.batch_deeprelay_batch_price import BatchDeeprelayBatchPrice

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeeprelayBatchPrice from a JSON string
batch_deeprelay_batch_price_instance = BatchDeeprelayBatchPrice.from_json(json)
# print the JSON string representation of the object
print(BatchDeeprelayBatchPrice.to_json())

# convert the object into a dict
batch_deeprelay_batch_price_dict = batch_deeprelay_batch_price_instance.to_dict()
# create an instance of BatchDeeprelayBatchPrice from a dict
batch_deeprelay_batch_price_from_dict = BatchDeeprelayBatchPrice.from_dict(batch_deeprelay_batch_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


