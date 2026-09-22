# ImagesGenerationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Customer-facing image model id (e.g. deeprelay/flux.1-schnell) or alias. | 
**prompt** | **str** | Text description of the image(s) to generate. | 
**n** | **int** | Number of images to generate. Defaults to 1. | [optional] [default to 1]
**size** | **str** | Output image dimensions as WxH (e.g. 1024x1024). | [optional] 
**response_format** | **str** | Only b64_json is supported. A value of \&quot;url\&quot; is rejected with invalid_request_error until S3-backed URL delivery lands. | [optional] [default to 'b64_json']

## Example

```python
from deeprelay_sdk.models.images_generations_request import ImagesGenerationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesGenerationsRequest from a JSON string
images_generations_request_instance = ImagesGenerationsRequest.from_json(json)
# print the JSON string representation of the object
print(ImagesGenerationsRequest.to_json())

# convert the object into a dict
images_generations_request_dict = images_generations_request_instance.to_dict()
# create an instance of ImagesGenerationsRequest from a dict
images_generations_request_from_dict = ImagesGenerationsRequest.from_dict(images_generations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


