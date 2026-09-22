# InferencePreflight

The verdict for one (organization, model) pair: what would happen if the model were invoked right now. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The canonical catalog id the request resolved to. | 
**verdict** | **str** | &#x60;ok&#x60; — the request will be served (covered by the plan, or payable). &#x60;warn&#x60; — it will be served AND charged in a way the caller may not expect. &#x60;block&#x60; — it will be refused (402 or 429). | 
**reason** | **str** | Stable code explaining the verdict, for clients that need their own wording. Absent on a plain &#x60;ok&#x60; that needs no explanation. | [optional] 
**message** | **str** | A ready-to-print sentence, phrased for this exact plan/credit combination. Prefer it over composing one from verdict and reason: it improves without a client release. | 
**plan_covered** | **bool** | Whether the subscription tier covers this model. A property of the PLATFORM, not of the caller — it stays true for an organization that has no subscription, which is what makes the \&quot;this is included in the plan\&quot; upsell honest. | 
**subscribed** | **bool** | Whether the organization is entitled to the plan right now. | 
**funded** | **bool** | Whether a pay-as-you-go request could be paid for right now: a positive credit balance AND no self-set spending cap already at its limit. A boolean and never a figure — this route is on the inference read scope and must not disclose the balance. | 

## Example

```python
from deeprelay_sdk.models.inference_preflight import InferencePreflight

# TODO update the JSON string below
json = "{}"
# create an instance of InferencePreflight from a JSON string
inference_preflight_instance = InferencePreflight.from_json(json)
# print the JSON string representation of the object
print(InferencePreflight.to_json())

# convert the object into a dict
inference_preflight_dict = inference_preflight_instance.to_dict()
# create an instance of InferencePreflight from a dict
inference_preflight_from_dict = InferencePreflight.from_dict(inference_preflight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


