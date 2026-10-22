# deeprelay_sdk.RequestsApi

All URIs are relative to *https://api.deeprelay.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_requests**](RequestsApi.md#export_requests) | **GET** /requests/export | Export the request log as CSV
[**get_request**](RequestsApi.md#get_request) | **GET** /requests/{id} | Get one request
[**list_requests**](RequestsApi.md#list_requests) | **GET** /requests | List requests (the request log)


# **export_requests**
> str export_requests(key=key, model=model, surface=surface, status=status, error_code=error_code, client_request_id=client_request_id, var_from=var_from, to=to, fallback=fallback)

Export the request log as CSV

Streams every request-log row matching the filters as a CSV attachment, oldest columns first: `request_id, client_request_id, occurred_at, surface, model, key_id, key_name, key_prefix, status, http_status, error_code, finish_reason, prompt_tokens, completion_tokens, cached_tokens, reasoning_tokens, quota_units, cost, plan_covered, ttft_ms, duration_ms, ignored_params, requested_model, served_model, fallback_reason`. Takes the same filters and visibility rules as `GET /requests`, without the cursor and limit.

The export is counted before anything is written. When the filters match more rows than the export cap, the answer is 422 `export_too_large` and the problem body carries `max_rows`; narrow the time range or add a filter, then export again.

Requires the `serverless:read` scope. Exports have their own, tighter per-key rate limit.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
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
    api_instance = deeprelay_sdk.RequestsApi(api_client)
    key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only rows sent with this API key (its `api_key_id`). (optional)
    model = 'model_example' # str | Only rows for this model id. (optional)
    surface = 'surface_example' # str | Only rows from this endpoint family. (optional)
    status = 'status_example' # str | Only rows with this outcome. `rejected` is a call refused before it reached a model (a budget, limit, allowlist or quota gate). (optional)
    error_code = 'error_code_example' # str | Only rows that ended with this `X-Deeprelay-Error-Code`. (optional)
    client_request_id = 'client_request_id_example' # str | Only rows whose `X-Client-Request-Id` equals this value. (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Inclusive RFC 3339 range start. Defaults to the start of the 90-day window; an older value is clamped to it. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Exclusive RFC 3339 range end. Defaults to now; must be after `from`. (optional)
    fallback = True # bool | `true` returns only rows a backup model served or where backups were tried (`fallback_reason` is set); `false` or absent applies no filter. Any other value is a 400. (optional)

    try:
        # Export the request log as CSV
        api_response = api_instance.export_requests(key=key, model=model, surface=surface, status=status, error_code=error_code, client_request_id=client_request_id, var_from=var_from, to=to, fallback=fallback)
        print("The response of RequestsApi->export_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->export_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **UUID**| Only rows sent with this API key (its &#x60;api_key_id&#x60;). | [optional] 
 **model** | **str**| Only rows for this model id. | [optional] 
 **surface** | **str**| Only rows from this endpoint family. | [optional] 
 **status** | **str**| Only rows with this outcome. &#x60;rejected&#x60; is a call refused before it reached a model (a budget, limit, allowlist or quota gate). | [optional] 
 **error_code** | **str**| Only rows that ended with this &#x60;X-Deeprelay-Error-Code&#x60;. | [optional] 
 **client_request_id** | **str**| Only rows whose &#x60;X-Client-Request-Id&#x60; equals this value. | [optional] 
 **var_from** | **datetime**| Inclusive RFC 3339 range start. Defaults to the start of the 90-day window; an older value is clamped to it. | [optional] 
 **to** | **datetime**| Exclusive RFC 3339 range end. Defaults to now; must be after &#x60;from&#x60;. | [optional] 
 **fallback** | **bool**| &#x60;true&#x60; returns only rows a backup model served or where backups were tried (&#x60;fallback_reason&#x60; is set); &#x60;false&#x60; or absent applies no filter. Any other value is a 400. | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV attachment (&#x60;Content-Disposition&#x60; names the file). |  -  |
**400** | Error response (RFC 7807) |  -  |
**422** | &#x60;export_too_large&#x60;: the filters match more rows than the export cap. &#x60;max_rows&#x60; in the problem body is the cap. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request**
> RequestLogEntry get_request(id)

Get one request

Returns one request-log row. An unknown id, an id older than 90 days and an id the caller cannot see all answer the same 404. Requires the `serverless:read` scope.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.request_log_entry import RequestLogEntry
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
    api_instance = deeprelay_sdk.RequestsApi(api_client)
    id = 'id_example' # str | Any id the caller holds for the request: the `X-Request-Id` response header, a chat completion id (`chatcmpl-…`), a message id (`msg_…`), a response id (`resp_…`) or a video id.

    try:
        # Get one request
        api_response = api_instance.get_request(id)
        print("The response of RequestsApi->get_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Any id the caller holds for the request: the &#x60;X-Request-Id&#x60; response header, a chat completion id (&#x60;chatcmpl-…&#x60;), a message id (&#x60;msg_…&#x60;), a response id (&#x60;resp_…&#x60;) or a video id. | 

### Return type

[**RequestLogEntry**](RequestLogEntry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_requests**
> RequestLogPage list_requests(key=key, model=model, surface=surface, status=status, error_code=error_code, client_request_id=client_request_id, var_from=var_from, to=to, fallback=fallback, cursor=cursor, limit=limit)

List requests (the request log)

Returns one newest-first page of the organization's inference request log: one row per call to chat completions, messages, responses, embeddings, image generation or video creation, including calls that were refused before they reached a model (`status: rejected`). Rows are kept for 90 days; `window_days` says how far back the log reaches, and a `from` older than that is clamped rather than rejected.

Visibility follows the caller. An org admin's key and a `full_access` key see the whole organization; any other key sees only its own rows. A `key` filter naming a key the caller cannot see returns an empty page.

A row never carries prompt or completion content. `client_request_id` is the value the caller sent in `X-Client-Request-Id` (or `metadata.client_request_id` on `/responses`), kept for correlation.

Requires the `serverless:read` scope. Reads are rate-limited per key (429 `rate_limited` with Retry-After).


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.request_log_page import RequestLogPage
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
    api_instance = deeprelay_sdk.RequestsApi(api_client)
    key = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only rows sent with this API key (its `api_key_id`). (optional)
    model = 'model_example' # str | Only rows for this model id. (optional)
    surface = 'surface_example' # str | Only rows from this endpoint family. (optional)
    status = 'status_example' # str | Only rows with this outcome. `rejected` is a call refused before it reached a model (a budget, limit, allowlist or quota gate). (optional)
    error_code = 'error_code_example' # str | Only rows that ended with this `X-Deeprelay-Error-Code`. (optional)
    client_request_id = 'client_request_id_example' # str | Only rows whose `X-Client-Request-Id` equals this value. (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Inclusive RFC 3339 range start. Defaults to the start of the 90-day window; an older value is clamped to it. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Exclusive RFC 3339 range end. Defaults to now; must be after `from`. (optional)
    fallback = True # bool | `true` returns only rows a backup model served or where backups were tried (`fallback_reason` is set); `false` or absent applies no filter. Any other value is a 400. (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int | Page size. Defaults to 50; values above 100 are clamped to 100. (optional) (default to 50)

    try:
        # List requests (the request log)
        api_response = api_instance.list_requests(key=key, model=model, surface=surface, status=status, error_code=error_code, client_request_id=client_request_id, var_from=var_from, to=to, fallback=fallback, cursor=cursor, limit=limit)
        print("The response of RequestsApi->list_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->list_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **UUID**| Only rows sent with this API key (its &#x60;api_key_id&#x60;). | [optional] 
 **model** | **str**| Only rows for this model id. | [optional] 
 **surface** | **str**| Only rows from this endpoint family. | [optional] 
 **status** | **str**| Only rows with this outcome. &#x60;rejected&#x60; is a call refused before it reached a model (a budget, limit, allowlist or quota gate). | [optional] 
 **error_code** | **str**| Only rows that ended with this &#x60;X-Deeprelay-Error-Code&#x60;. | [optional] 
 **client_request_id** | **str**| Only rows whose &#x60;X-Client-Request-Id&#x60; equals this value. | [optional] 
 **var_from** | **datetime**| Inclusive RFC 3339 range start. Defaults to the start of the 90-day window; an older value is clamped to it. | [optional] 
 **to** | **datetime**| Exclusive RFC 3339 range end. Defaults to now; must be after &#x60;from&#x60;. | [optional] 
 **fallback** | **bool**| &#x60;true&#x60; returns only rows a backup model served or where backups were tried (&#x60;fallback_reason&#x60; is set); &#x60;false&#x60; or absent applies no filter. Any other value is a 400. | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**| Page size. Defaults to 50; values above 100 are clamped to 100. | [optional] [default to 50]

### Return type

[**RequestLogPage**](RequestLogPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

