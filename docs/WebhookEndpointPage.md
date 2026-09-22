# WebhookEndpointPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhookEndpoint]**](WebhookEndpoint.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from deeprelay_sdk.models.webhook_endpoint_page import WebhookEndpointPage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEndpointPage from a JSON string
webhook_endpoint_page_instance = WebhookEndpointPage.from_json(json)
# print the JSON string representation of the object
print(WebhookEndpointPage.to_json())

# convert the object into a dict
webhook_endpoint_page_dict = webhook_endpoint_page_instance.to_dict()
# create an instance of WebhookEndpointPage from a dict
webhook_endpoint_page_from_dict = WebhookEndpointPage.from_dict(webhook_endpoint_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


