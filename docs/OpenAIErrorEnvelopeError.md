# OpenAIErrorEnvelopeError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**type** | **str** | OpenAI error class (e.g. invalid_request_error, authentication_error, billing_error). | 
**param** | **str** |  | [optional] 
**code** | **str** | Stable machine-readable error code. | 

## Example

```python
from deeprelay_sdk.models.open_ai_error_envelope_error import OpenAIErrorEnvelopeError

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIErrorEnvelopeError from a JSON string
open_ai_error_envelope_error_instance = OpenAIErrorEnvelopeError.from_json(json)
# print the JSON string representation of the object
print(OpenAIErrorEnvelopeError.to_json())

# convert the object into a dict
open_ai_error_envelope_error_dict = open_ai_error_envelope_error_instance.to_dict()
# create an instance of OpenAIErrorEnvelopeError from a dict
open_ai_error_envelope_error_from_dict = OpenAIErrorEnvelopeError.from_dict(open_ai_error_envelope_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


