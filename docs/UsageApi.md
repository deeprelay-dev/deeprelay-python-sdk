# deeprelay_sdk.UsageApi

All URIs are relative to *https://api.deeprelay.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_usage**](UsageApi.md#list_usage) | **GET** /usage | Time-bucketed usage


# **list_usage**
> UsagePage list_usage(bucket=bucket, group_by=group_by, start=start, end=end, cursor=cursor, limit=limit, modality=modality, model=model)

Time-bucketed usage

Returns spend aggregated into time buckets over `[start, end)` (default: the last 30 days, `bucket=day`), newest bucket first.

The response has one of two row shapes, selected by the query:

- **Inference usage** — set `modality` and/or `model`. Rows aggregate serverless inference calls, one row per (bucket, modality, model), and carry `modality`, `model`, `prompt_tokens`, `completion_tokens` and `image_count`. This is the usage a serverless-inference customer is billed for.
- **Instance usage** — neither `modality` nor `model` set. Rows aggregate GPU instance billing sessions, optionally split by `group_by`. With no instance usage this returns an empty `data` array, so to read inference spend always pass `modality` or `model`.

Requires the `billing:read` scope.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.usage_page import UsagePage
from deeprelay_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deeprelay.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deeprelay_sdk.Configuration(
    host = "https://api.deeprelay.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (deeprelay_live_<24-base62>): bearerAuth
configuration = deeprelay_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with deeprelay_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deeprelay_sdk.UsageApi(api_client)
    bucket = 'bucket_example' # str | Bucket width. Defaults to `day`. (optional)
    group_by = 'group_by_example' # str | Split instance-usage rows by instance or GPU type. Applies only to the instance-usage shape (neither `modality` nor `model` set); ignored when either is set, since inference rows are always split by modality and model.  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | Inclusive RFC 3339 range start. Defaults to 30 days ago. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | Exclusive RFC 3339 range end. Defaults to now; must be after `start`. (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    modality = 'modality_example' # str | Return inference-usage rows for this modality only. Setting `modality` or `model` selects the inference-usage shape; omit both for the instance-usage shape.  (optional)
    model = 'model_example' # str | Return inference-usage rows for this model only: an exact match on the model `id` as listed by `GET /models`. May be combined with `modality`. Setting `modality` or `model` selects the inference-usage shape.  (optional)

    try:
        # Time-bucketed usage
        api_response = api_instance.list_usage(bucket=bucket, group_by=group_by, start=start, end=end, cursor=cursor, limit=limit, modality=modality, model=model)
        print("The response of UsageApi->list_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->list_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Bucket width. Defaults to &#x60;day&#x60;. | [optional] 
 **group_by** | **str**| Split instance-usage rows by instance or GPU type. Applies only to the instance-usage shape (neither &#x60;modality&#x60; nor &#x60;model&#x60; set); ignored when either is set, since inference rows are always split by modality and model.  | [optional] 
 **start** | **datetime**| Inclusive RFC 3339 range start. Defaults to 30 days ago. | [optional] 
 **end** | **datetime**| Exclusive RFC 3339 range end. Defaults to now; must be after &#x60;start&#x60;. | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **modality** | **str**| Return inference-usage rows for this modality only. Setting &#x60;modality&#x60; or &#x60;model&#x60; selects the inference-usage shape; omit both for the instance-usage shape.  | [optional] 
 **model** | **str**| Return inference-usage rows for this model only: an exact match on the model &#x60;id&#x60; as listed by &#x60;GET /models&#x60;. May be combined with &#x60;modality&#x60;. Setting &#x60;modality&#x60; or &#x60;model&#x60; selects the inference-usage shape.  | [optional] 

### Return type

[**UsagePage**](UsagePage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

