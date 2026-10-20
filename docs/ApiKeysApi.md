# deeprelay_sdk.ApiKeysApi

All URIs are relative to *https://api.deeprelay.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeysApi.md#create_api_key) | **POST** /api-keys | Create an API key
[**get_api_key**](ApiKeysApi.md#get_api_key) | **GET** /api-keys/{id} | Get an API key
[**list_api_keys**](ApiKeysApi.md#list_api_keys) | **GET** /api-keys | List API keys
[**revoke_api_key**](ApiKeysApi.md#revoke_api_key) | **DELETE** /api-keys/{id} | Revoke an API key
[**update_api_key**](ApiKeysApi.md#update_api_key) | **PATCH** /api-keys/{id} | Update an API key&#39;s name or limits


# **create_api_key**
> ApiKeyCreated create_api_key(api_key_create)

Create an API key

Mints a key. The response is the only place the secret (`key`) appears; store it then, because it cannot be read again.

Requires the `keys:manage` capability: a `full_access` key, or a key whose scopes grant `{"keys": "write"}`. Any other key gets 403 `keys_manage_required`. A key can never mint a key stronger than itself: scopes it does not hold answer 403 `scope_exceeds_caller`, and a minting key that has a budget, a model allowlist, a rate limit or an expiry passes each down as an upper bound (422 `validation_failed` naming the `field`). Only an org admin can mint a `full_access` key.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.api_key_create import ApiKeyCreate
from deeprelay_sdk.models.api_key_created import ApiKeyCreated
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
    api_instance = deeprelay_sdk.ApiKeysApi(api_client)
    api_key_create = deeprelay_sdk.ApiKeyCreate() # ApiKeyCreate | 

    try:
        # Create an API key
        api_response = api_instance.create_api_key(api_key_create)
        print("The response of ApiKeysApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_create** | [**ApiKeyCreate**](ApiKeyCreate.md)|  | 

### Return type

[**ApiKeyCreated**](ApiKeyCreated.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created. The response is sent with &#x60;Cache-Control: no-store&#x60;. |  -  |
**400** | Error response (RFC 7807) |  -  |
**403** | &#x60;keys_manage_required&#x60; (the calling key cannot manage keys), &#x60;scope_exceeds_caller&#x60; (the requested scopes exceed the calling key&#39;s own) or &#x60;forbidden&#x60; (only an org admin can mint a &#x60;full_access&#x60; key). |  -  |
**422** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> ApiKey get_api_key(id)

Get an API key

Returns one key. A key the caller cannot see answers 404. Requires the `keys:read` scope.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.api_key import ApiKey
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
    api_instance = deeprelay_sdk.ApiKeysApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an API key
        api_response = api_instance.get_api_key(id)
        print("The response of ApiKeysApi->get_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->get_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**ApiKey**](ApiKey.md)

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

# **list_api_keys**
> ApiKeyList list_api_keys()

List API keys

Lists the organization's API keys with their limits and current budget use. An org admin's key and a `full_access` key see every key in the organization; any other key sees only the keys its owner created. The secret is never returned here. Requires the `keys:read` scope.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.api_key_list import ApiKeyList
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
    api_instance = deeprelay_sdk.ApiKeysApi(api_client)

    try:
        # List API keys
        api_response = api_instance.list_api_keys()
        print("The response of ApiKeysApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->list_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiKeyList**](ApiKeyList.md)

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

# **revoke_api_key**
> revoke_api_key(id, idempotency_key=idempotency_key)

Revoke an API key

Revokes the key immediately; it cannot be restored. Requires the `keys:manage` capability (403 `keys_manage_required` otherwise); a member can only revoke keys they created.


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
    api_instance = deeprelay_sdk.ApiKeysApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Revoke an API key
        api_instance.revoke_api_key(id, idempotency_key=idempotency_key)
    except Exception as e:
        print("Exception when calling ApiKeysApi->revoke_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Revoked |  -  |
**403** | Error response (RFC 7807) |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ApiKey update_api_key(id, api_key_update, idempotency_key=idempotency_key)

Update an API key's name or limits

Changes a key's name, budget, model allowlist, rate limit or expiry. An absent field is left unchanged; an explicit `null` clears `budget_cents`, `allowed_models` or `expires_at`. `scopes` cannot be changed after minting, and unknown fields are refused (422), so a typo never looks like a successful change. Requires the `keys:manage` capability (403 `keys_manage_required` otherwise); a member can only change keys they created.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.api_key import ApiKey
from deeprelay_sdk.models.api_key_update import ApiKeyUpdate
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
    api_instance = deeprelay_sdk.ApiKeysApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    api_key_update = deeprelay_sdk.ApiKeyUpdate() # ApiKeyUpdate | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Update an API key's name or limits
        api_response = api_instance.update_api_key(id, api_key_update, idempotency_key=idempotency_key)
        print("The response of ApiKeysApi->update_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->update_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **api_key_update** | [**ApiKeyUpdate**](ApiKeyUpdate.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error response (RFC 7807) |  -  |
**403** | Error response (RFC 7807) |  -  |
**404** | Error response (RFC 7807) |  -  |
**422** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

