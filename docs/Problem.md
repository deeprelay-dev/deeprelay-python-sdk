# Problem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | 
**detail** | **str** |  | 
**code** | **str** |  | 
**request_id** | **str** |  | 
**var_field** | **str** | On a 422 &#x60;validation_failed&#x60;, the request field that failed. | [optional] 
**max_rows** | **int** | On a 422 &#x60;export_too_large&#x60;, the export row cap. | [optional] 

## Example

```python
from deeprelay_sdk.models.problem import Problem

# TODO update the JSON string below
json = "{}"
# create an instance of Problem from a JSON string
problem_instance = Problem.from_json(json)
# print the JSON string representation of the object
print(Problem.to_json())

# convert the object into a dict
problem_dict = problem_instance.to_dict()
# create an instance of Problem from a dict
problem_from_dict = Problem.from_dict(problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


