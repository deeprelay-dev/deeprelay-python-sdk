# OpenAIErrorEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**OpenAIErrorEnvelopeError**](OpenAIErrorEnvelopeError.md) |  | 

## Example

```python
from deeprelay_sdk.models.open_ai_error_envelope import OpenAIErrorEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIErrorEnvelope from a JSON string
open_ai_error_envelope_instance = OpenAIErrorEnvelope.from_json(json)
# print the JSON string representation of the object
print(OpenAIErrorEnvelope.to_json())

# convert the object into a dict
open_ai_error_envelope_dict = open_ai_error_envelope_instance.to_dict()
# create an instance of OpenAIErrorEnvelope from a dict
open_ai_error_envelope_from_dict = OpenAIErrorEnvelope.from_dict(open_ai_error_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


