# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created** | **int** |  | [optional] 
**owned_by** | **str** |  | 
**author** | **str** | Model creator/organization (e.g. \&quot;Meta\&quot;, \&quot;Qwen\&quot;, \&quot;Black Forest Labs\&quot;). | [optional] 
**modality** | **str** |  | 
**category** | **str** | Browse-facing category; mirrors modality (chat/image/video/embedding). | [optional] 
**context_length** | **int** |  | [optional] 
**supported_parameters** | **List[str]** |  | [optional] 
**parameters** | [**List[ModelParametersInner]**](ModelParametersInner.md) | Typed parameter descriptors for media (image/video) models — name, type, enum/bounds/default. Playgrounds render input forms from these. | [optional] 
**pricing** | [**ModelPricing**](ModelPricing.md) |  | 
**aliases** | **List[str]** |  | [optional] 
**fine_tunable** | **bool** | Whether this model can be used as the base of a managed fine-tuning job. The tunable allowlist is operator-curated and much narrower than the serving catalog, so this is false for almost every model. Absent means false. | [optional] 
**fine_tune_base_model** | **str** | The exact id to send as &#x60;model&#x60; when creating a fine-tuning job for this entry. Present only when &#x60;fine_tunable&#x60; is true, and deliberately distinct from &#x60;id&#x60;: the allowlist matches the customer-facing base id (e.g. &#x60;qwen2.5-7b-instruct&#x60;), which a served model normally carries as an alias rather than as its namespaced catalog id. | [optional] 
**plan_covered** | **bool** | Whether the flat subscription tier covers this model. A covered model rides the plan&#39;s quota while the subscription is entitled and has quota left; everything else bills pay-as-you-go at list rates, as does a covered model once the quota is spent. Absent means false.  Coverage is a property of the platform, not of the caller: the flag reads the same for every organization, subscribed or not. Use &#x60;/billing/subscription&#x60; for what the caller&#39;s own plan has left. | [optional] 
**status** | **str** |  | 

## Example

```python
from deeprelay_sdk.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


