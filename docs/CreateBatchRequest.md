# CreateBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file_id** | **str** | An uploaded file with &#x60;purpose: batch&#x60;. It must not expire before the batch could finish (the submit is refused otherwise). | 
**endpoint** | **str** | Every line&#39;s &#x60;url&#x60; must equal this value. One endpoint and one model per batch. | 
**completion_window** | **str** | Only &#x60;\&quot;24h\&quot;&#x60; is accepted. It is a target, not a promise: a batch runs only in off-peak time and expires 72 hours after submit. | 
**metadata** | **Dict[str, str]** | Up to 16 pairs; keys up to 64 characters, values up to 512. | [optional] 
**output_expires_after** | [**CreateBatchRequestOutputExpiresAfter**](CreateBatchRequestOutputExpiresAfter.md) |  | [optional] 

## Example

```python
from deeprelay_sdk.models.create_batch_request import CreateBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchRequest from a JSON string
create_batch_request_instance = CreateBatchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBatchRequest.to_json())

# convert the object into a dict
create_batch_request_dict = create_batch_request_instance.to_dict()
# create an instance of CreateBatchRequest from a dict
create_batch_request_from_dict = CreateBatchRequest.from_dict(create_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


