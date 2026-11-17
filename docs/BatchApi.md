# deeprelay_sdk.BatchApi

All URIs are relative to *https://api.deeprelay.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_batch**](BatchApi.md#cancel_batch) | **POST** /batches/{id}/cancel | Cancel a batch (OpenAI-compatible)
[**create_batch**](BatchApi.md#create_batch) | **POST** /batches | Create an off-peak batch (OpenAI-compatible)
[**create_file**](BatchApi.md#create_file) | **POST** /files | Upload a batch input file (OpenAI-compatible)
[**delete_file**](BatchApi.md#delete_file) | **DELETE** /files/{id} | Delete a batch file (OpenAI-compatible)
[**get_batch_limits**](BatchApi.md#get_batch_limits) | **GET** /batches/limits | Per-organization batch limits with current values
[**list_batches**](BatchApi.md#list_batches) | **GET** /batches | List batches, newest first (OpenAI-compatible)
[**list_files**](BatchApi.md#list_files) | **GET** /files | List batch files (OpenAI-compatible)
[**retrieve_batch**](BatchApi.md#retrieve_batch) | **GET** /batches/{id} | Retrieve a batch (OpenAI-compatible)
[**retrieve_file**](BatchApi.md#retrieve_file) | **GET** /files/{id} | Retrieve a batch file (OpenAI-compatible)
[**retrieve_file_content**](BatchApi.md#retrieve_file_content) | **GET** /files/{id}/content | Download a batch file&#39;s content (JSONL)


# **cancel_batch**
> Batch cancel_batch(id)

Cancel a batch (OpenAI-compatible)

Stops the batch's queued lines at once. Lines already running finish and are billed; the output file holds every completed line and the error file lists the rest as `batch_cancelled`. The batch moves to `cancelling`, then `cancelled`.

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch import Batch
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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel a batch (OpenAI-compatible)
        api_response = api_instance.cancel_batch(id)
        print("The response of BatchApi->cancel_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->cancel_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Batch**](Batch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The batch object (cancelling, or unchanged when finalizing or finished). |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch**
> Batch create_batch(create_batch_request)

Create an off-peak batch (OpenAI-compatible)

Submits an uploaded input file as a batch. deeprelay runs it in the model's next off-peak window (at once when the model is off-peak now, or has no peak schedule) and bills each line at the rate in effect when it runs. Every line is checked first through the same validation a synchronous request gets; a batch with any invalid line is rejected whole with 400 `batch_validation_failed` naming the lines. One model and one endpoint per batch. The submit is gated on the batch's estimated cost (input tokens plus `max_tokens` at the batch rate) with the same balance and spend checks as a synchronous request; the estimate is not a hold. Pay-as-you-go only: batch lines are never covered by a subscription plan.

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch import Batch
from deeprelay_sdk.models.create_batch_request import CreateBatchRequest
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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    create_batch_request = deeprelay_sdk.CreateBatchRequest() # CreateBatchRequest | 

    try:
        # Create an off-peak batch (OpenAI-compatible)
        api_response = api_instance.create_batch(create_batch_request)
        print("The response of BatchApi->create_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->create_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_batch_request** | [**CreateBatchRequest**](CreateBatchRequest.md)|  | 

### Return type

[**Batch**](Batch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The batch object. |  -  |
**400** | &#x60;batch_validation_failed&#x60; (invalid lines, more than one model, a line &#x60;url&#x60; that differs from &#x60;endpoint&#x60;, &#x60;stream: true&#x60;, a server tool, a model with no off-peak time, or an input file that expires before the batch could finish), &#x60;batch_limit_exceeded&#x60; (active batches or the queued-token cap), &#x60;server_tool_unsupported&#x60;, &#x60;invalid_completion_window&#x60; (anything but &#x60;\&quot;24h\&quot;&#x60;) or &#x60;invalid_request&#x60;. OpenAI error envelope. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**402** | Insufficient balance or a spend limit reached (OpenAI error envelope, SERV-06): &#x60;insufficient_balance&#x60;, &#x60;daily_limit_reached&#x60;, &#x60;spending_limit_reached&#x60;, &#x60;api_key_budget_exceeded&#x60; (this API key&#39;s monthly budget) or &#x60;member_spend_limit_reached&#x60; (the member&#39;s monthly spend limit). Carries &#x60;x-should-retry: false&#x60;: the same request will not succeed until the wallet or the limit changes. |  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**413** | Request body too large (OpenAI error envelope, code request_too_large). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> BatchFile create_file(purpose, file, expires_after=expires_after)

Upload a batch input file (OpenAI-compatible)

Uploads a JSONL batch input file (`purpose=batch`), one request per line in the OpenAI batch shape (`custom_id`, `method: POST`, `url`, `body`). The whole file is checked before anything is stored: a bad line is 400 `batch_validation_failed` naming the line numbers, a file over a size, line-count, line-size or stored-file limit is 400 `batch_limit_exceeded`, and any purpose other than `batch` is 400 `invalid_purpose`. A body over the file-size limit is 413 `request_too_large`. The stored file is encrypted at rest and deleted at `expires_at` (30 days by default) or on `DELETE /files/{id}`.

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch_file import BatchFile
from deeprelay_sdk.models.create_file_request_expires_after import CreateFileRequestExpiresAfter
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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    purpose = 'purpose_example' # str | 
    file = None # bytes | A JSONL file, one request per line.
    expires_after = deeprelay_sdk.CreateFileRequestExpiresAfter() # CreateFileRequestExpiresAfter |  (optional)

    try:
        # Upload a batch input file (OpenAI-compatible)
        api_response = api_instance.create_file(purpose, file, expires_after=expires_after)
        print("The response of BatchApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purpose** | **str**|  | 
 **file** | **bytes**| A JSONL file, one request per line. | 
 **expires_after** | [**CreateFileRequestExpiresAfter**](CreateFileRequestExpiresAfter.md)|  | [optional] 

### Return type

[**BatchFile**](BatchFile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The uploaded file object. |  -  |
**400** | &#x60;batch_validation_failed&#x60; (one or more lines are invalid; the message lists the line numbers), &#x60;batch_limit_exceeded&#x60; (a file, line or stored-file limit), &#x60;invalid_purpose&#x60;, &#x60;invalid_multipart&#x60;, &#x60;missing_file&#x60; or &#x60;invalid_request&#x60; (a bad &#x60;expires_after&#x60;). OpenAI error envelope. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**413** | Request body too large (OpenAI error envelope, code request_too_large). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> BatchFileDeleted delete_file(id)

Delete a batch file (OpenAI-compatible)

Deletes the file and its stored content immediately. There are no versioned or replicated copies of batch file content, so nothing is left to purge. The input file of a batch that is still queued or running cannot be deleted (409 `file_in_use`); cancel the batch first.

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch_file_deleted import BatchFileDeleted
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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a batch file (OpenAI-compatible)
        api_response = api_instance.delete_file(id)
        print("The response of BatchApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BatchFileDeleted**](BatchFileDeleted.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deletion result. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**409** | &#x60;file_in_use&#x60;: the file is the input of a batch that is still queued or running; cancel the batch first. OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_limits**
> BatchLimits get_batch_limits()

Per-organization batch limits with current values

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch_limits import BatchLimits
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
    api_instance = deeprelay_sdk.BatchApi(api_client)

    try:
        # Per-organization batch limits with current values
        api_response = api_instance.get_batch_limits()
        print("The response of BatchApi->get_batch_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->get_batch_limits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BatchLimits**](BatchLimits.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every batch limit and its current value. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_batches**
> BatchList list_batches(after=after, limit=limit)

List batches, newest first (OpenAI-compatible)

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch_list import BatchList
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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List batches, newest first (OpenAI-compatible)
        api_response = api_instance.list_batches(after=after, limit=limit)
        print("The response of BatchApi->list_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->list_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**BatchList**](BatchList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of batch objects. |  -  |
**400** | Invalid request (OpenAI error envelope). |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> BatchFileList list_files(purpose=purpose, after=after, limit=limit, order=order)

List batch files (OpenAI-compatible)

Lists the organization's batch files: inputs you uploaded and the output and error files written for finished batches. Deleted and expired files are not listed.

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch_file_list import BatchFileList
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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    purpose = 'purpose_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)

    try:
        # List batch files (OpenAI-compatible)
        api_response = api_instance.list_files(purpose=purpose, after=after, limit=limit, order=order)
        print("The response of BatchApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->list_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purpose** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 

### Return type

[**BatchFileList**](BatchFileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of file objects. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_batch**
> Batch retrieve_batch(id)

Retrieve a batch (OpenAI-compatible)

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch import Batch
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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    id = 'id_example' # str | 

    try:
        # Retrieve a batch (OpenAI-compatible)
        api_response = api_instance.retrieve_batch(id)
        print("The response of BatchApi->retrieve_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->retrieve_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Batch**](Batch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The batch object. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_file**
> BatchFile retrieve_file(id)

Retrieve a batch file (OpenAI-compatible)

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.batch_file import BatchFile
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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    id = 'id_example' # str | 

    try:
        # Retrieve a batch file (OpenAI-compatible)
        api_response = api_instance.retrieve_file(id)
        print("The response of BatchApi->retrieve_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->retrieve_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BatchFile**](BatchFile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file object. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_file_content**
> bytes retrieve_file_content(id)

Download a batch file's content (JSONL)

Streams the file's JSONL content. For an output or error file each line is a `BatchResultLine`. A file past its `expires_at` is 410 `expired`.

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
    api_instance = deeprelay_sdk.BatchApi(api_client)
    id = 'id_example' # str | 

    try:
        # Download a batch file's content (JSONL)
        api_response = api_instance.retrieve_file_content(id)
        print("The response of BatchApi->retrieve_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->retrieve_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytes**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jsonl, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file content, one JSON object per line. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**410** | The requested artifact has expired and is no longer available (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

