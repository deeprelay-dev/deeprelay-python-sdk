# ModelParametersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**enum** | **List[str]** |  | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**default** | **object** |  | [optional] 

## Example

```python
from deeprelay_sdk.models.model_parameters_inner import ModelParametersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModelParametersInner from a JSON string
model_parameters_inner_instance = ModelParametersInner.from_json(json)
# print the JSON string representation of the object
print(ModelParametersInner.to_json())

# convert the object into a dict
model_parameters_inner_dict = model_parameters_inner_instance.to_dict()
# create an instance of ModelParametersInner from a dict
model_parameters_inner_from_dict = ModelParametersInner.from_dict(model_parameters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


