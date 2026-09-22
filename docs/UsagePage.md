# UsagePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UsageBucket]**](UsageBucket.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from deeprelay_sdk.models.usage_page import UsagePage

# TODO update the JSON string below
json = "{}"
# create an instance of UsagePage from a JSON string
usage_page_instance = UsagePage.from_json(json)
# print the JSON string representation of the object
print(UsagePage.to_json())

# convert the object into a dict
usage_page_dict = usage_page_instance.to_dict()
# create an instance of UsagePage from a dict
usage_page_from_dict = UsagePage.from_dict(usage_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


