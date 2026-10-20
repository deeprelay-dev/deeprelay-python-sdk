# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created** | **int** | Always present for OpenAI-client compatibility. Currently 0 for every model (the catalog carries no creation date); do not sort on it. | 
**owned_by** | **str** | The model&#39;s author (the same value as &#x60;author&#x60;), or \&quot;deeprelay\&quot; when the author is unknown. | 
**author** | **str** | Model creator/organization (e.g. \&quot;Meta\&quot;, \&quot;Qwen\&quot;, \&quot;Black Forest Labs\&quot;). | [optional] 
**modality** | **str** |  | 
**category** | **str** | Browse-facing category; mirrors modality (chat/image/video/embedding). | [optional] 
**tier** | **str** | The serving tier this entry prices: &#x60;serverless&#x60; or &#x60;economy&#x60; today, and more values may be added. A model served on both tiers appears twice: under its bare id for &#x60;serverless&#x60;, and under the &#x60;:economy&#x60;-suffixed id for &#x60;economy&#x60;. Send the id of the tier you want. Omitted on &#x60;coming_soon&#x60; placeholder entries. | [optional] 
**context_length** | **int** |  | [optional] 
**max_completion_tokens** | **int** | The model&#39;s maximum output, in tokens, from the catalog. Omitted when the catalog lists none. | [optional] 
**supported_parameters** | **List[str]** |  | [optional] 
**reasoning_efforts** | **List[str]** | The &#x60;reasoning_effort&#x60; values this model accepts (for example &#x60;none&#x60;, &#x60;low&#x60;, &#x60;medium&#x60;, &#x60;high&#x60;), as the catalog lists them. Omitted when the catalog lists none. | [optional] 
**parameters** | [**List[ModelParametersInner]**](ModelParametersInner.md) | Typed parameter descriptors for media (image/video) models — name, type, enum/bounds/default. Playgrounds render input forms from these. | [optional] 
**pricing** | [**ModelPricing**](ModelPricing.md) |  | 
**aliases** | **List[str]** |  | [optional] 
**fine_tunable** | **bool** | Whether this model can be used as the base of a managed fine-tuning job. The tunable allowlist is operator-curated and much narrower than the serving catalog, so this is false for almost every model. Absent means false. | [optional] 
**fine_tune_base_model** | **str** | The exact id to send as &#x60;model&#x60; when creating a fine-tuning job for this entry. Present only when &#x60;fine_tunable&#x60; is true, and deliberately distinct from &#x60;id&#x60;: the allowlist matches the customer-facing base id (e.g. &#x60;qwen2.5-7b-instruct&#x60;), which a served model normally carries as an alias rather than as its namespaced catalog id. | [optional] 
**hf_repo** | **str** | The Hugging Face repo that publishes this model&#39;s open weights, e.g. &#x60;meta-llama/Llama-3.3-70B-Instruct&#x60;. Send it as &#x60;base_model&#x60; to run the same model on a dedicated deployment. Absent when the weights are not public. | [optional] 
**usage_factor_milli** | **int** | How heavily this model draws on the subscription quota, ×1000: each token counts as usage_factor_milli / 1000 weighted tokens toward the quota (and in cost_details.quota_units_used). Omitted at the default 1000 (1.0×). | [optional] 
**plan_covered** | **bool** | \&quot;Included in the flat subscription\&quot;: whether the subscription tier covers this model. A model-level fact, the same for every caller. A covered model rides the plan&#39;s quota while the subscription is entitled and has quota left; everything else bills pay-as-you-go at list rates, as does a covered model once the quota is spent. Absent means false.  Coverage is a property of the platform, not of the caller: the flag reads the same for every organization, subscribed or not. Use &#x60;/billing/subscription&#x60; for what the caller&#39;s own plan has left. | [optional] 
**recommended_for** | **List[str]** | The audiences deeprelay recommends this model for. The only value today is &#x60;coding-agents&#x60;: models tested with coding agents, which &#x60;deeprelay setup &lt;agent&gt;&#x60; configures. More values may be added. Omitted on every model that is not recommended. | [optional] 
**coding_agent_rank** | **int** | The model&#39;s position in the coding-agent list, 1 first. Present exactly when &#x60;recommended_for&#x60; contains &#x60;coding-agents&#x60;; a setup command makes the rank-1 model the default. | [optional] 
**status** | **str** |  | 
**metrics** | [**ModelMetrics**](ModelMetrics.md) |  | [optional] 

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


