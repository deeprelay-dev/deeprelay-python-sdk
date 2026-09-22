# deeprelay_sdk.InferenceApi

All URIs are relative to *https://api.deeprelay.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_video**](InferenceApi.md#cancel_video) | **POST** /videos/{id}/cancel | Cancel a video generation job
[**create_chat_completion**](InferenceApi.md#create_chat_completion) | **POST** /chat/completions | Create a chat completion (OpenAI-compatible)
[**create_embeddings**](InferenceApi.md#create_embeddings) | **POST** /embeddings | Create embeddings (OpenAI-compatible)
[**create_image**](InferenceApi.md#create_image) | **POST** /images/generations | Create image (OpenAI-compatible)
[**create_video**](InferenceApi.md#create_video) | **POST** /videos | Create a video generation job (async)
[**get_model**](InferenceApi.md#get_model) | **GET** /models/{id} | Get a specific model (OpenAI-compatible)
[**get_video**](InferenceApi.md#get_video) | **GET** /videos/{id} | Get a video generation job
[**get_video_content**](InferenceApi.md#get_video_content) | **GET** /videos/{id}/content | Download a completed video artifact
[**list_models**](InferenceApi.md#list_models) | **GET** /models | List available models (OpenAI-compatible)
[**list_videos**](InferenceApi.md#list_videos) | **GET** /videos | List video generation jobs


# **cancel_video**
> VideoJob cancel_video(id)

Cancel a video generation job

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.video_job import VideoJob
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel a video generation job
        api_response = api_instance.cancel_video(id)
        print("The response of InferenceApi->cancel_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->cancel_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VideoJob**](VideoJob.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A video generation job object. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**409** | Invalid request (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chat_completion**
> ChatCompletionResponse create_chat_completion(chat_completion_request)

Create a chat completion (OpenAI-compatible)

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.chat_completion_request import ChatCompletionRequest
from deeprelay_sdk.models.chat_completion_response import ChatCompletionResponse
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    chat_completion_request = deeprelay_sdk.ChatCompletionRequest() # ChatCompletionRequest | 

    try:
        # Create a chat completion (OpenAI-compatible)
        api_response = api_instance.create_chat_completion(chat_completion_request)
        print("The response of InferenceApi->create_chat_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->create_chat_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_completion_request** | [**ChatCompletionRequest**](ChatCompletionRequest.md)|  | 

### Return type

[**ChatCompletionResponse**](ChatCompletionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. application/json for non-streaming requests; text/event-stream for streaming requests (stream&#x3D;true).  |  -  |
**400** | Invalid request (OpenAI error envelope). |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**402** | Insufficient balance (OpenAI error envelope, SERV-06). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**422** | Request validation failed (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**500** | Internal server error (OpenAI error envelope). |  -  |
**503** | Upstream provider unavailable (OpenAI error envelope). Retry-After header may indicate seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embeddings**
> EmbeddingsResponse create_embeddings(embeddings_request)

Create embeddings (OpenAI-compatible)

Synchronous text embeddings. Accepts a single string or an array of up to 2048 strings, bounded so the response stays under 64 MiB (about 680 inputs at 4096 dimensions; fewer at a larger `dimensions` value) — over-limit requests are rejected with 400 before any processing. Returns one float vector per input, in request order. Billed on the upstream's reported prompt tokens at the model's listed input rate, rounded up to the next whole cent per request; an embeddings call emits no completion tokens, so `usage` carries `prompt_tokens` and `total_tokens` only. `encoding_format` accepts only `float` — a value of `base64` is rejected with `unsupported_parameter`. A chat model id on this route returns 404 `model_not_found`: the id is valid, but not on this surface.

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.embeddings_request import EmbeddingsRequest
from deeprelay_sdk.models.embeddings_response import EmbeddingsResponse
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    embeddings_request = deeprelay_sdk.EmbeddingsRequest() # EmbeddingsRequest | 

    try:
        # Create embeddings (OpenAI-compatible)
        api_response = api_instance.create_embeddings(embeddings_request)
        print("The response of InferenceApi->create_embeddings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->create_embeddings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embeddings_request** | [**EmbeddingsRequest**](EmbeddingsRequest.md)|  | 

### Return type

[**EmbeddingsResponse**](EmbeddingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One embedding vector per input, in request order. |  -  |
**400** | Invalid request (OpenAI error envelope). |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**402** | Insufficient balance (OpenAI error envelope, SERV-06). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**413** | Request body too large (OpenAI error envelope, code request_too_large). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**500** | Internal server error (OpenAI error envelope). |  -  |
**502** | The upstream answered but its response could not be used (OpenAI error envelope): code upstream_response_too_large when the vector payload exceeded the per-request size limit, or upstream_error for a malformed / misaligned response. Not retryable as-is for upstream_response_too_large — send fewer inputs. |  -  |
**503** | Upstream provider unavailable (OpenAI error envelope). Retry-After header may indicate seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**504** | Upstream provider exceeded the synchronous per-attempt deadline (OpenAI error envelope). 504 semantic — distinct from 503 OpenAIUpstreamUnavailable which signals a connection or routing failure rather than a timeout.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image**
> ImagesResponse create_image(images_generations_request, idempotency_key=idempotency_key)

Create image (OpenAI-compatible)

Synchronous text-to-image generation. Returns base64-encoded images only (`response_format` is restricted to `b64_json`); a value of `url` is rejected with `invalid_request_error` until S3-backed URL delivery lands. Pass an `Idempotency-Key` header to make a retried request replay the original response without a second charge.

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.images_generations_request import ImagesGenerationsRequest
from deeprelay_sdk.models.images_response import ImagesResponse
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    images_generations_request = deeprelay_sdk.ImagesGenerationsRequest() # ImagesGenerationsRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Create image (OpenAI-compatible)
        api_response = api_instance.create_image(images_generations_request, idempotency_key=idempotency_key)
        print("The response of InferenceApi->create_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->create_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **images_generations_request** | [**ImagesGenerationsRequest**](ImagesGenerationsRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**ImagesResponse**](ImagesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAI-shaped image generation response (b64_json only). |  -  |
**400** | Invalid request (OpenAI error envelope). |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**402** | Insufficient balance (OpenAI error envelope, SERV-06). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**422** | Request validation failed (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**500** | Internal server error (OpenAI error envelope). |  -  |
**503** | Upstream provider unavailable (OpenAI error envelope). Retry-After header may indicate seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**504** | Upstream provider exceeded the synchronous per-attempt deadline (OpenAI error envelope). 504 semantic — distinct from 503 OpenAIUpstreamUnavailable which signals a connection or routing failure rather than a timeout.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_video**
> VideoJob create_video(video_create_request, idempotency_key=idempotency_key)

Create a video generation job (async)

Submit an asynchronous text-to-video generation job. Returns a job object with status `queued`; poll GET /videos/{id} until `completed`, then stream the result from GET /videos/{id}/content. Pass an `Idempotency-Key` header to make a retried request replay the original response without a second charge.

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.video_create_request import VideoCreateRequest
from deeprelay_sdk.models.video_job import VideoJob
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    video_create_request = deeprelay_sdk.VideoCreateRequest() # VideoCreateRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Create a video generation job (async)
        api_response = api_instance.create_video(video_create_request, idempotency_key=idempotency_key)
        print("The response of InferenceApi->create_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->create_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_create_request** | [**VideoCreateRequest**](VideoCreateRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**VideoJob**](VideoJob.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A video generation job object. |  -  |
**400** | Invalid request (OpenAI error envelope). |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**402** | Insufficient balance (OpenAI error envelope, SERV-06). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**500** | Internal server error (OpenAI error envelope). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(id)

Get a specific model (OpenAI-compatible)

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.model import Model
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a specific model (OpenAI-compatible)
        api_response = api_instance.get_model(id)
        print("The response of InferenceApi->get_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->get_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Model**](Model.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAI-shaped single model. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video**
> VideoJob get_video(id)

Get a video generation job

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.video_job import VideoJob
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a video generation job
        api_response = api_instance.get_video(id)
        print("The response of InferenceApi->get_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->get_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VideoJob**](VideoJob.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A video generation job object. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_content**
> bytes get_video_content(id)

Download a completed video artifact

Streams the generated MP4 for a completed job. Returns 410 Gone once the artifact has expired (24h retention).

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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # Download a completed video artifact
        api_response = api_instance.get_video_content(id)
        print("The response of InferenceApi->get_video_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->get_video_content: %s\n" % e)
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
 - **Accept**: video/mp4, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The generated video stream. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**410** | The requested artifact has expired and is no longer available (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_models**
> ModelList list_models(modality=modality)

List available models (OpenAI-compatible)

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.model_list import ModelList
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    modality = 'modality_example' # str |  (optional)

    try:
        # List available models (OpenAI-compatible)
        api_response = api_instance.list_models(modality=modality)
        print("The response of InferenceApi->list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->list_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modality** | **str**|  | [optional] 

### Return type

[**ModelList**](ModelList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAI-shaped model list. |  -  |
**400** | Invalid request (OpenAI error envelope). |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_videos**
> VideoList list_videos(after=after, limit=limit)

List video generation jobs

### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.video_list import VideoList
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
    api_instance = deeprelay_sdk.InferenceApi(api_client)
    after = 'after_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List video generation jobs
        api_response = api_instance.list_videos(after=after, limit=limit)
        print("The response of InferenceApi->list_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->list_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**VideoList**](VideoList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of video generation jobs. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

