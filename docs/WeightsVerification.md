# WeightsVerification

Present only for an open-weight chat model whose latest public fingerprint run passed: the run compared the relay's output distributions against independent deployments of the same weights and found them the same model. Derived from the newest run the public harness published (see `method_url`), through a short cache, and dropped once that run is older than 14 days. There is no negative value: a model the run did not verify, for any reason, simply has no `weights_verification` key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Always &#x60;verified&#x60;; the object is absent otherwise. | 
**weights** | **str** | The Hugging Face repo the served weights were verified against. | 
**verified_at** | **datetime** | When the run that made the finding finished. | 
**run_id** | **str** | The public GitHub Actions run id. | 
**run_url** | **str** | The public run, where the report and job log live. | 
**harness_version** | **str** | The version of the measuring code that run used. | 
**references** | **int** | How many independent deployments of the same weights the relay was compared against. | 
**method_url** | **str** | The public harness repository that defines the method. | 

## Example

```python
from deeprelay_sdk.models.weights_verification import WeightsVerification

# TODO update the JSON string below
json = "{}"
# create an instance of WeightsVerification from a JSON string
weights_verification_instance = WeightsVerification.from_json(json)
# print the JSON string representation of the object
print(WeightsVerification.to_json())

# convert the object into a dict
weights_verification_dict = weights_verification_instance.to_dict()
# create an instance of WeightsVerification from a dict
weights_verification_from_dict = WeightsVerification.from_dict(weights_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


