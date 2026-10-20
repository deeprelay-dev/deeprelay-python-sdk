# ChatMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | \&quot;developer\&quot; is OpenAI&#39;s newer spelling of \&quot;system\&quot; and is treated as system.  | 
**content** | **str** | The message text. Null on an assistant turn that is purely a tool call — branch on that to tell a tool call from a reply. Responses always carry a string (or null).  Requests may instead send an array of content parts, as OpenAI clients do (typed here as a string so SDK callers can keep passing plain text). Text parts ({\&quot;type\&quot;:\&quot;text\&quot;,\&quot;text\&quot;:\&quot;...\&quot;}) are joined with newlines. Image parts ({\&quot;type\&quot;:\&quot;image_url\&quot;,\&quot;image_url\&quot;:{\&quot;url\&quot;:\&quot;...\&quot;}}) are accepted on models whose supported_parameters list \&quot;vision\&quot;; any other model returns 400 unsupported_parameter (param messages) naming the models that accept images. &#x60;url&#x60; must be an https URL or a data:image/{png,jpeg,webp,gif};base64 URI, and the relay never fetches it itself. Limits: 16 images per request, 20 MiB per image, 8 KiB per URL, inside the 32 MiB body cap (413 request_too_large). Each image counts as 1,600 tokens in the spend preflight. &#x60;image_url.detail&#x60; is accepted but not forwarded, and is reported in x-deeprelay-ignored-params. Audio and file parts are rejected with 400 unsupported_content_part.  | [optional] 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) | Calls the model wants made. Assistant messages only. | [optional] 
**tool_call_id** | **str** | Which call this message answers. REQUIRED on a role \&quot;tool\&quot; message — without it the upstream cannot match the result to its call.  | [optional] 

## Example

```python
from deeprelay_sdk.models.chat_message import ChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessage from a JSON string
chat_message_instance = ChatMessage.from_json(json)
# print the JSON string representation of the object
print(ChatMessage.to_json())

# convert the object into a dict
chat_message_dict = chat_message_instance.to_dict()
# create an instance of ChatMessage from a dict
chat_message_from_dict = ChatMessage.from_dict(chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


