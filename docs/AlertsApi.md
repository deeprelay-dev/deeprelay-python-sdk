# deeprelay_sdk.AlertsApi

All URIs are relative to *https://api.deeprelay.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_settings**](AlertsApi.md#get_alert_settings) | **GET** /alerts/settings | Get the organization&#39;s alert settings
[**put_alert_settings**](AlertsApi.md#put_alert_settings) | **PUT** /alerts/settings | Replace the organization&#39;s alert settings


# **get_alert_settings**
> AlertSettings get_alert_settings()

Get the organization's alert settings

Returns the low-balance threshold and the four org-level alert email toggles. An organization that has never saved settings gets the defaults with `updated_at: null`. Requires the `billing:read` scope.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.alert_settings import AlertSettings
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
    api_instance = deeprelay_sdk.AlertsApi(api_client)

    try:
        # Get the organization's alert settings
        api_response = api_instance.get_alert_settings()
        print("The response of AlertsApi->get_alert_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertSettings**](AlertSettings.md)

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

# **put_alert_settings**
> AlertSettings put_alert_settings(alert_settings_update)

Replace the organization's alert settings

Replaces every setting at once: send `balance_threshold_cents` and all four `email` toggles (a missing field is 422 `validation_failed` naming the `field`). Requires the `billing:write` scope AND an org admin's key or a `full_access` key (403 `forbidden` otherwise). The toggles only control the org-level emails; a member always receives their own spend-limit emails. Webhook delivery of the same events is configured on the webhook endpoint, not here.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.alert_settings import AlertSettings
from deeprelay_sdk.models.alert_settings_update import AlertSettingsUpdate
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
    api_instance = deeprelay_sdk.AlertsApi(api_client)
    alert_settings_update = deeprelay_sdk.AlertSettingsUpdate() # AlertSettingsUpdate | 

    try:
        # Replace the organization's alert settings
        api_response = api_instance.put_alert_settings(alert_settings_update)
        print("The response of AlertsApi->put_alert_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->put_alert_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_settings_update** | [**AlertSettingsUpdate**](AlertSettingsUpdate.md)|  | 

### Return type

[**AlertSettings**](AlertSettings.md)

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
**422** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

