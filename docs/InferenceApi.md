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
[**inference_preflight**](InferenceApi.md#inference_preflight) | **GET** /inference/preflight | Check whether a model request would be served, and at whose expense
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
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**409** | Invalid request (OpenAI error envelope). |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chat_completion**
> ChatCompletionResponse create_chat_completion(chat_completion_request, x_client_request_id=x_client_request_id, x_deeprelay_fallback_models=x_deeprelay_fallback_models)

Create a chat completion (OpenAI-compatible)

OpenAI-compatible chat completion. Parameters fall into three groups:

- **Semantic parameters are gated per model.** `response_format`,
  `tools`/`tool_choice`, `logprobs`/`top_logprobs` and `image_url`
  content parts are sent only to a model whose `/v1/models` entry
  lists the capability in `supported_parameters` (`vision` for
  images). A model without it returns 400 `unsupported_parameter`
  whose message names the models that do support it. When the model
  supports the parameter but none of its currently routable upstreams
  does, the request fails with 503 `upstream_unavailable` rather than
  being silently degraded.
- **Hints are forwarded or dropped, never rejected.**
  `reasoning_effort`, `presence_penalty`, `frequency_penalty`, `seed`
  and `parallel_tool_calls` are forwarded to an upstream that accepts
  them and otherwise dropped. Every drop is reported in the
  `x-deeprelay-ignored-params` response header.
- **Rejected everywhere.** `logit_bias` and `function_call` return
  400 `unsupported_parameter`; `input_audio` and `file` content parts
  return 400 `unsupported_content_part`.

A non-strict `json_schema` sent to a model that can only guarantee
JSON is served as `json_object` and reported as
`response_format:downgraded`; a strict one is rejected. A
`json_schema` over 64 KiB or nested deeper than 32 levels returns 400
`unsupported_parameter` (param `response_format`). An upstream
rejection of a request the relay accepted returns 400
`upstream_rejected_request`. A non-chat model id returns 404
`model_not_found`. The request body is capped at 32 MiB (413
`request_too_large`).

Every successful response carries `usage.cost` and
`usage.cost_details` (on a stream, only in the final usage chunk).
See https://deeprelay.ai/docs/api/inference#openai-compatibility.

**Backup models.** When the API key has `fallback_models`, or the
request sends `models` or X-Deeprelay-Fallback-Models, and every
provider for the requested model fails before the first token with a
temporary error (unavailable, timed out, rate limited upstream, or
stalled), deeprelay tries the next backup model. It never switches
after the first byte, and never on a client error, a quota or budget
refusal, or a content-filter result. A backup is billed at its own
price under the same billing mode as the requested model. The body
`model` and X-Deeprelay-Served-Model name the model that served;
X-Deeprelay-Requested-Model names the one asked for, and
X-Deeprelay-Fallback-Reason says why it was passed over. If no model
serves, the response is the requested model's own error, with
X-Deeprelay-Fallback-Attempted.


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
    x_client_request_id = 'x_client_request_id_example' # str | Your own correlation id for this call, up to 128 characters. It is stored on the request-log row as `client_request_id` and can be filtered on with `GET /requests?client_request_id=`. When it is absent, an inbound `X-Request-Id` is kept in its place; the response's own `X-Request-Id` is always minted by deeprelay. Surrounding whitespace and control characters are removed; a longer value is dropped, never truncated. It is never used as a lookup key, so it does not need to be unique. (optional)
    x_deeprelay_fallback_models = 'deeprelay/glm-5.3,deeprelay/kimi-k3' # str | Backup models for this request only, in priority order: a comma-separated list of up to 3 model ids, for example `deeprelay/glm-5.3,deeprelay/kimi-k3`. It replaces the API key's `fallback_models` for this request; the two lists are never merged. `none` (or an empty value) turns model fallback off for this request. If every provider for the requested model fails before the first token with a temporary error, deeprelay tries the next listed model. Each backup must still pass the key's model allowlist, the request's billing mode and the request's capability needs; one that does not is skipped, so this header can never widen what the key may call. More than 3 models, a malformed id, `none` mixed with ids, or this header together with a `models` body field is a 400 `invalid_request`. Not accepted by Liquid, which always serves exactly the requested model. (optional)

    try:
        # Create a chat completion (OpenAI-compatible)
        api_response = api_instance.create_chat_completion(chat_completion_request, x_client_request_id=x_client_request_id, x_deeprelay_fallback_models=x_deeprelay_fallback_models)
        print("The response of InferenceApi->create_chat_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->create_chat_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_completion_request** | [**ChatCompletionRequest**](ChatCompletionRequest.md)|  | 
 **x_client_request_id** | **str**| Your own correlation id for this call, up to 128 characters. It is stored on the request-log row as &#x60;client_request_id&#x60; and can be filtered on with &#x60;GET /requests?client_request_id&#x3D;&#x60;. When it is absent, an inbound &#x60;X-Request-Id&#x60; is kept in its place; the response&#39;s own &#x60;X-Request-Id&#x60; is always minted by deeprelay. Surrounding whitespace and control characters are removed; a longer value is dropped, never truncated. It is never used as a lookup key, so it does not need to be unique. | [optional] 
 **x_deeprelay_fallback_models** | **str**| Backup models for this request only, in priority order: a comma-separated list of up to 3 model ids, for example &#x60;deeprelay/glm-5.3,deeprelay/kimi-k3&#x60;. It replaces the API key&#39;s &#x60;fallback_models&#x60; for this request; the two lists are never merged. &#x60;none&#x60; (or an empty value) turns model fallback off for this request. If every provider for the requested model fails before the first token with a temporary error, deeprelay tries the next listed model. Each backup must still pass the key&#39;s model allowlist, the request&#39;s billing mode and the request&#39;s capability needs; one that does not is skipped, so this header can never widen what the key may call. More than 3 models, a malformed id, &#x60;none&#x60; mixed with ids, or this header together with a &#x60;models&#x60; body field is a 400 &#x60;invalid_request&#x60;. Not accepted by Liquid, which always serves exactly the requested model. | [optional] 

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
**200** | Successful response. application/json for non-streaming requests; text/event-stream for streaming requests (stream&#x3D;true).  |  * X-Deeprelay-Served-Model -  <br>  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Reason -  <br>  * x-deeprelay-ignored-params -  <br>  * x-deeprelay-cost -  <br>  * x-deeprelay-quota-input-remaining -  <br>  * x-deeprelay-quota-output-remaining -  <br>  * x-deeprelay-quota-reset -  <br>  * x-deeprelay-quota-weekly-input-remaining -  <br>  * x-deeprelay-quota-weekly-input-limit -  <br>  * x-deeprelay-quota-weekly-output-remaining -  <br>  * x-deeprelay-quota-weekly-output-limit -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  |
**400** | Invalid request (OpenAI error envelope). |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**402** | Insufficient balance or a spend limit reached (OpenAI error envelope, SERV-06): &#x60;insufficient_balance&#x60;, &#x60;daily_limit_reached&#x60;, &#x60;spending_limit_reached&#x60;, &#x60;api_key_budget_exceeded&#x60; (this API key&#39;s monthly budget) or &#x60;member_spend_limit_reached&#x60; (the member&#39;s monthly spend limit). Carries &#x60;x-should-retry: false&#x60;: the same request will not succeed until the wallet or the limit changes. |  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**413** | Request body too large (OpenAI error envelope, code request_too_large). |  * X-Deeprelay-Error-Code -  <br>  |
**422** | Request validation failed (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**503** | No upstream could serve the request (OpenAI error envelope, &#x60;upstream_unavailable&#x60;): every capable upstream is down, shedding load, or none of the model&#39;s routable upstreams supports a capability the request needs. Always carries Retry-After (whole seconds, rounded up) and retry-after-ms; on an overload the wait is jittered between 2 and 2.5 seconds. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embeddings**
> EmbeddingsResponse create_embeddings(embeddings_request, x_client_request_id=x_client_request_id)

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
    x_client_request_id = 'x_client_request_id_example' # str | Your own correlation id for this call, up to 128 characters. It is stored on the request-log row as `client_request_id` and can be filtered on with `GET /requests?client_request_id=`. When it is absent, an inbound `X-Request-Id` is kept in its place; the response's own `X-Request-Id` is always minted by deeprelay. Surrounding whitespace and control characters are removed; a longer value is dropped, never truncated. It is never used as a lookup key, so it does not need to be unique. (optional)

    try:
        # Create embeddings (OpenAI-compatible)
        api_response = api_instance.create_embeddings(embeddings_request, x_client_request_id=x_client_request_id)
        print("The response of InferenceApi->create_embeddings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->create_embeddings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embeddings_request** | [**EmbeddingsRequest**](EmbeddingsRequest.md)|  | 
 **x_client_request_id** | **str**| Your own correlation id for this call, up to 128 characters. It is stored on the request-log row as &#x60;client_request_id&#x60; and can be filtered on with &#x60;GET /requests?client_request_id&#x3D;&#x60;. When it is absent, an inbound &#x60;X-Request-Id&#x60; is kept in its place; the response&#39;s own &#x60;X-Request-Id&#x60; is always minted by deeprelay. Surrounding whitespace and control characters are removed; a longer value is dropped, never truncated. It is never used as a lookup key, so it does not need to be unique. | [optional] 

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
**400** | Invalid request (OpenAI error envelope). |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**402** | Insufficient balance or a spend limit reached (OpenAI error envelope, SERV-06): &#x60;insufficient_balance&#x60;, &#x60;daily_limit_reached&#x60;, &#x60;spending_limit_reached&#x60;, &#x60;api_key_budget_exceeded&#x60; (this API key&#39;s monthly budget) or &#x60;member_spend_limit_reached&#x60; (the member&#39;s monthly spend limit). Carries &#x60;x-should-retry: false&#x60;: the same request will not succeed until the wallet or the limit changes. |  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**413** | Request body too large (OpenAI error envelope, code request_too_large). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**502** | The upstream answered but its response could not be used (OpenAI error envelope): code upstream_response_too_large when the vector payload exceeded the per-request size limit, or upstream_error for a malformed / misaligned response. Not retryable as-is for upstream_response_too_large — send fewer inputs. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**503** | No upstream could serve the request (OpenAI error envelope, &#x60;upstream_unavailable&#x60;): every capable upstream is down, shedding load, or none of the model&#39;s routable upstreams supports a capability the request needs. Always carries Retry-After (whole seconds, rounded up) and retry-after-ms; on an overload the wait is jittered between 2 and 2.5 seconds. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**504** | Upstream provider exceeded the synchronous per-attempt deadline (OpenAI error envelope). 504 semantic — distinct from 503 OpenAIUpstreamUnavailable which signals a connection or routing failure rather than a timeout.  |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image**
> ImagesResponse create_image(images_generations_request, idempotency_key=idempotency_key, x_client_request_id=x_client_request_id)

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
    x_client_request_id = 'x_client_request_id_example' # str | Your own correlation id for this call, up to 128 characters. It is stored on the request-log row as `client_request_id` and can be filtered on with `GET /requests?client_request_id=`. When it is absent, an inbound `X-Request-Id` is kept in its place; the response's own `X-Request-Id` is always minted by deeprelay. Surrounding whitespace and control characters are removed; a longer value is dropped, never truncated. It is never used as a lookup key, so it does not need to be unique. (optional)

    try:
        # Create image (OpenAI-compatible)
        api_response = api_instance.create_image(images_generations_request, idempotency_key=idempotency_key, x_client_request_id=x_client_request_id)
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
 **x_client_request_id** | **str**| Your own correlation id for this call, up to 128 characters. It is stored on the request-log row as &#x60;client_request_id&#x60; and can be filtered on with &#x60;GET /requests?client_request_id&#x3D;&#x60;. When it is absent, an inbound &#x60;X-Request-Id&#x60; is kept in its place; the response&#39;s own &#x60;X-Request-Id&#x60; is always minted by deeprelay. Surrounding whitespace and control characters are removed; a longer value is dropped, never truncated. It is never used as a lookup key, so it does not need to be unique. | [optional] 

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
**400** | Invalid request (OpenAI error envelope). |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**402** | Insufficient balance or a spend limit reached (OpenAI error envelope, SERV-06): &#x60;insufficient_balance&#x60;, &#x60;daily_limit_reached&#x60;, &#x60;spending_limit_reached&#x60;, &#x60;api_key_budget_exceeded&#x60; (this API key&#39;s monthly budget) or &#x60;member_spend_limit_reached&#x60; (the member&#39;s monthly spend limit). Carries &#x60;x-should-retry: false&#x60;: the same request will not succeed until the wallet or the limit changes. |  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**422** | Request validation failed (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**503** | No upstream could serve the request (OpenAI error envelope, &#x60;upstream_unavailable&#x60;): every capable upstream is down, shedding load, or none of the model&#39;s routable upstreams supports a capability the request needs. Always carries Retry-After (whole seconds, rounded up) and retry-after-ms; on an overload the wait is jittered between 2 and 2.5 seconds. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**504** | Upstream provider exceeded the synchronous per-attempt deadline (OpenAI error envelope). 504 semantic — distinct from 503 OpenAIUpstreamUnavailable which signals a connection or routing failure rather than a timeout.  |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_video**
> VideoJob create_video(video_create_request, idempotency_key=idempotency_key, x_client_request_id=x_client_request_id)

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
    x_client_request_id = 'x_client_request_id_example' # str | Your own correlation id for this call, up to 128 characters. It is stored on the request-log row as `client_request_id` and can be filtered on with `GET /requests?client_request_id=`. When it is absent, an inbound `X-Request-Id` is kept in its place; the response's own `X-Request-Id` is always minted by deeprelay. Surrounding whitespace and control characters are removed; a longer value is dropped, never truncated. It is never used as a lookup key, so it does not need to be unique. (optional)

    try:
        # Create a video generation job (async)
        api_response = api_instance.create_video(video_create_request, idempotency_key=idempotency_key, x_client_request_id=x_client_request_id)
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
 **x_client_request_id** | **str**| Your own correlation id for this call, up to 128 characters. It is stored on the request-log row as &#x60;client_request_id&#x60; and can be filtered on with &#x60;GET /requests?client_request_id&#x3D;&#x60;. When it is absent, an inbound &#x60;X-Request-Id&#x60; is kept in its place; the response&#39;s own &#x60;X-Request-Id&#x60; is always minted by deeprelay. Surrounding whitespace and control characters are removed; a longer value is dropped, never truncated. It is never used as a lookup key, so it does not need to be unique. | [optional] 

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
**400** | Invalid request (OpenAI error envelope). |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**402** | Insufficient balance or a spend limit reached (OpenAI error envelope, SERV-06): &#x60;insufficient_balance&#x60;, &#x60;daily_limit_reached&#x60;, &#x60;spending_limit_reached&#x60;, &#x60;api_key_budget_exceeded&#x60; (this API key&#39;s monthly budget) or &#x60;member_spend_limit_reached&#x60; (the member&#39;s monthly spend limit). Carries &#x60;x-should-retry: false&#x60;: the same request will not succeed until the wallet or the limit changes. |  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**500** | Internal server error (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(id)

Get a specific model (OpenAI-compatible)

A key with a model allowlist gets 403 `model_not_allowed_for_key` for a model off its list, and the same 403 for an id that does not exist.

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
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |

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
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |

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
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**410** | The requested artifact has expired and is no longer available (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_preflight**
> InferencePreflight inference_preflight(model)

Check whether a model request would be served, and at whose expense

Answers "what happens if I call this model right now?" before the call is made: whether the plan covers the model, whether the organization is subscribed, and whether there is credit to pay if it is not covered. Requires the `serverless:read` scope.

Nothing is sent, counted, charged, or reserved. The verdict is computed from the state of the SAME gates that judge the real request — plan coverage, subscription entitlement, remaining plan quota, credit balance and self-set spending caps — so the advice cannot drift from enforcement. It is deliberately NOT a dry run: no per-request cost estimate is quoted, because that figure changes with every prompt and quoting it would invite clients to cache it.

The gates consulted depend on the model's MODALITY, because the endpoints do not all meet the same ones. Chat, embeddings and image requests meet the full gate (balance, then the organization's opt-in daily cap, then its monthly cap). Video creation meets only the balance check, so an organization past its own spending cap but holding credit is reported as fundable for video — which is what the video endpoint will in fact do. Predicting the strictest gate rather than the applicable one would make this endpoint refuse requests the API accepts.

The same is true of the plan: video creation does not run the subscription gate, so `plan_covered` is false for a video model even if an operator has placed it on the plan's covered list. That is a deliberate divergence from the same-named field on `/v1/models`, which reports the platform's configuration. Here it means "the plan covers this REQUEST" — describing what will happen is the entire job of a preflight.

One caveat on "read-only": resolving the balance creates the organization's balance row if it has never had one (idempotent, org-scoped, and the same row the first real request would create). Nothing else is written.

The case this exists for is `warn` / `not_plan_covered`. A subscriber calling a model outside the plan IS served and IS charged pay-as-you-go, and nothing in the response to that request says so — the first signal used to be the invoice.

`funded` is a boolean and never a figure. This route is on the inference read scope, so it must not disclose the organization's balance; use `/billing/balance` for the number.

Failure posture is the opposite of the request gate's: any gate that cannot be read degrades the verdict toward `ok`, never toward `block`. A false `block` would stop a customer whose request would have succeeded, while a false `ok` costs them one honest error from the real call.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.inference_preflight import InferencePreflight
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
    model = 'model_example' # str | Model id or alias, optionally with a `:economy` tier suffix. It is resolved through the catalog exactly as the inference endpoints resolve it, so an alias and a tier view answer for the model that would actually serve.

    try:
        # Check whether a model request would be served, and at whose expense
        api_response = api_instance.inference_preflight(model)
        print("The response of InferenceApi->inference_preflight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->inference_preflight: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model id or alias, optionally with a &#x60;:economy&#x60; tier suffix. It is resolved through the catalog exactly as the inference endpoints resolve it, so an alias and a tier view answer for the model that would actually serve. | 

### Return type

[**InferencePreflight**](InferencePreflight.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_models**
> ModelList list_models(modality=modality, if_none_match=if_none_match)

List available models (OpenAI-compatible)

Works with or without an API key, and returns the same body either
way. Without a key the response is publicly cacheable
(`Cache-Control: public, max-age=60`), carries a strong `ETag`
(send `If-None-Match` to get a 304), and is rate-limited per client
IP (429 `rate_limit_exceeded` with Retry-After). With a key it is
`Cache-Control: private` and counts against the key's rate limit;
an invalid key returns 401, it does not fall back to anonymous
access. Error responses are `no-store`.

Each entry's `supported_parameters` is backed by live capability
probes of the model's upstreams: it is the list to check before
sending a gated parameter (`response_format`,
`structured_outputs`, `logprobs`, `tools`, `vision`, ...).

One exception to "the same body": a key with a model allowlist
(`allowed_models`) sees only the models on its list.

Each entry may carry a `metrics` object (always the last key):
measured time to first token, decode rate and success rate over a
rolling window of deeprelay customer traffic. Below the sample minimum
`insufficient_data` is true and the figure is omitted, never zero.


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
    if_none_match = 'if_none_match_example' # str | An ETag from an earlier anonymous response; a match returns 304. (optional)

    try:
        # List available models (OpenAI-compatible)
        api_response = api_instance.list_models(modality=modality, if_none_match=if_none_match)
        print("The response of InferenceApi->list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->list_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modality** | **str**|  | [optional] 
 **if_none_match** | **str**| An ETag from an earlier anonymous response; a match returns 304. | [optional] 

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
**200** | OpenAI-shaped model list. |  * Cache-Control - &#x60;public, max-age&#x3D;60&#x60; without a key; &#x60;private&#x60; with one. <br>  * ETag - Strong validator for the anonymous listing. <br>  |
**304** | Not modified; the If-None-Match ETag still matches. |  -  |
**400** | Invalid request (OpenAI error envelope). |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * X-Deeprelay-Error-Code -  <br>  |
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |

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
**401** | Missing or invalid API key (OpenAI error envelope). |  * X-Deeprelay-Error-Code -  <br>  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or the key has a model allowlist that does not include the requested model (&#x60;model_not_allowed_for_key&#x60;; also the answer for a model that does not exist, so a restricted key cannot probe the catalog). OpenAI error envelope. |  * X-Deeprelay-Error-Code -  <br>  |
**429** | Rate limit or subscription quota exceeded (OpenAI error envelope). A per-key or per-IP rate limit (&#x60;rate_limit_exceeded&#x60;) carries Retry-After, the whole seconds to wait, rounded up (minimum 1), and retry-after-ms, the exact wait; both are the time until one request is allowed, not a full refill. A per-key denial also carries the x-ratelimit-*-requests headers. A subscription quota denial (&#x60;subscription_quota_exhausted&#x60;, raised only when the wallet cannot cover the pay-as-you-go fallback) carries &#x60;x-should-retry: false&#x60; and no Retry-After. When the tripped gate is a rolling 7-day cap (&#x60;param: weekly_input_tokens&#x60; or &#x60;param: weekly_output_tokens&#x60;), the error object also carries &#x60;quota_frees_at&#x60;, the RFC 3339 time the window frees enough capacity — the earlier of the two windows. &#x60;param&#x60; names the tripped gate: monthly_input_tokens, monthly_output_tokens, weekly_input_tokens, weekly_output_tokens, max_usage, input_overshoot (this request&#39;s estimated input alone exceeds what is left in the tighter of the monthly and rolling 7-day input allowances), or output_overshoot (the same for the estimated output — the completion bound). On an overshoot the quota is not exhausted — send a smaller request (or a smaller max_tokens) or add credits. |  * X-Deeprelay-Requested-Model -  <br>  * X-Deeprelay-Fallback-Attempted -  <br>  * Retry-After - Seconds the client should wait before retrying. <br>  * retry-after-ms -  <br>  * x-ratelimit-limit-requests -  <br>  * x-ratelimit-remaining-requests -  <br>  * x-ratelimit-reset-requests -  <br>  * x-should-retry -  <br>  * X-Deeprelay-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

