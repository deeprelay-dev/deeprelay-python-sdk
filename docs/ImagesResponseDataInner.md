# ImagesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b64_json** | **str** | Base64-encoded image bytes. | 

## Example

```python
from deeprelay_sdk.models.images_response_data_inner import ImagesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesResponseDataInner from a JSON string
images_response_data_inner_instance = ImagesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ImagesResponseDataInner.to_json())

# convert the object into a dict
images_response_data_inner_dict = images_response_data_inner_instance.to_dict()
# create an instance of ImagesResponseDataInner from a dict
images_response_data_inner_from_dict = ImagesResponseDataInner.from_dict(images_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


