# ImagesResponseUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_count** | **int** | Number of images generated (the billable unit). | 

## Example

```python
from deeprelay_sdk.models.images_response_usage import ImagesResponseUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesResponseUsage from a JSON string
images_response_usage_instance = ImagesResponseUsage.from_json(json)
# print the JSON string representation of the object
print(ImagesResponseUsage.to_json())

# convert the object into a dict
images_response_usage_dict = images_response_usage_instance.to_dict()
# create an instance of ImagesResponseUsage from a dict
images_response_usage_from_dict = ImagesResponseUsage.from_dict(images_response_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


