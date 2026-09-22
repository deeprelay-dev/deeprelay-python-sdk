# deeprelay_sdk.BillingApi

All URIs are relative to *https://api.deeprelay.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_crypto_deposit**](BillingApi.md#create_crypto_deposit) | **POST** /billing/deposits/crypto | Create a stablecoin deposit
[**create_subscription_checkout**](BillingApi.md#create_subscription_checkout) | **POST** /billing/subscription/checkout | Start a subscription checkout session
[**create_subscription_portal**](BillingApi.md#create_subscription_portal) | **POST** /billing/subscription/portal | Open the billing portal to cancel or manage the subscription
[**get_balance**](BillingApi.md#get_balance) | **GET** /billing/balance | Get the org credit balance
[**get_deposit**](BillingApi.md#get_deposit) | **GET** /billing/deposits/{id} | Get one stablecoin deposit
[**get_spending_limit**](BillingApi.md#get_spending_limit) | **GET** /billing/spending-limit | Get the org spending limit
[**get_subscription**](BillingApi.md#get_subscription) | **GET** /billing/subscription | Get the org subscription status and quota usage
[**list_deposits**](BillingApi.md#list_deposits) | **GET** /billing/deposits | List stablecoin deposits
[**update_spending_limit**](BillingApi.md#update_spending_limit) | **PUT** /billing/spending-limit | Set the org spending limit


# **create_crypto_deposit**
> CryptoDeposit create_crypto_deposit(create_crypto_deposit_request)

Create a stablecoin deposit

Creates a deposit intent and returns the payment address and the exact token amount to send. Requires the `billing:write` scope; any member of the organization may add funds. Send the exact `pay_amount` of `asset` on `chain` and no other network — funds sent on a different network are not detected automatically. Returns 404 when stablecoin deposits are not enabled for this deployment.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.create_crypto_deposit_request import CreateCryptoDepositRequest
from deeprelay_sdk.models.crypto_deposit import CryptoDeposit
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
    api_instance = deeprelay_sdk.BillingApi(api_client)
    create_crypto_deposit_request = deeprelay_sdk.CreateCryptoDepositRequest() # CreateCryptoDepositRequest | 

    try:
        # Create a stablecoin deposit
        api_response = api_instance.create_crypto_deposit(create_crypto_deposit_request)
        print("The response of BillingApi->create_crypto_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_crypto_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_crypto_deposit_request** | [**CreateCryptoDepositRequest**](CreateCryptoDepositRequest.md)|  | 

### Return type

[**CryptoDeposit**](CryptoDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | &#x60;validation-error&#x60; — &#x60;amount_cents&#x60; is below the configured minimum. &#x60;unsupported-chain-asset&#x60; — the chain/asset pair is not available. &#x60;invalid-request&#x60; — malformed JSON body.  |  -  |
**403** | &#x60;org-frozen&#x60; — the organization cannot add funds; contact support. |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**503** | &#x60;payment-source-unavailable&#x60; — deposits are temporarily unavailable; retry shortly. |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_checkout**
> SubscriptionCheckoutSession create_subscription_checkout(subscription_checkout_request=subscription_checkout_request)

Start a subscription checkout session

Opens a hosted checkout session for the flat tier and returns its URL. Requires the `billing:write` scope AND organization-admin privileges — subscribing spends organization money.

This endpoint does NOT subscribe anyone. Checkout is a hosted page that needs a browser and a card, so the caller's job is to put the returned URL in front of a human. The subscription becomes active when payment completes, which is not synchronous with this call: poll `/billing/subscription` to confirm.

`success_url` and `cancel_url` are optional and fall back to the deployment's configured redirects, which is what lets a command-line client start a purchase without having any URLs of its own. An empty request body is valid and means "use every default".

`plan_key`, when sent, pins the plan the client DISPLAYED: an unknown key is a 400 rather than a silent purchase of a different tier. Today there is one tier, so the only accepted value is its key — but sending it is the forward-compatible choice.

One flat tier means at most one subscription per organization: a second checkout while an entitling subscription exists is a 409.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.subscription_checkout_request import SubscriptionCheckoutRequest
from deeprelay_sdk.models.subscription_checkout_session import SubscriptionCheckoutSession
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
    api_instance = deeprelay_sdk.BillingApi(api_client)
    subscription_checkout_request = deeprelay_sdk.SubscriptionCheckoutRequest() # SubscriptionCheckoutRequest |  (optional)

    try:
        # Start a subscription checkout session
        api_response = api_instance.create_subscription_checkout(subscription_checkout_request=subscription_checkout_request)
        print("The response of BillingApi->create_subscription_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_subscription_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_checkout_request** | [**SubscriptionCheckoutRequest**](SubscriptionCheckoutRequest.md)|  | [optional] 

### Return type

[**SubscriptionCheckoutSession**](SubscriptionCheckoutSession.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Not an organization admin |  -  |
**409** | The organization already has an active subscription |  -  |
**503** | Subscription billing is not configured on this deployment |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_portal**
> SubscriptionPortalSession create_subscription_portal(subscription_portal_request=subscription_portal_request)

Open the billing portal to cancel or manage the subscription

Returns a URL for the hosted billing portal: where a customer cancels the subscription, resumes one they cancelled, changes payment method, or downloads invoices. Requires the `billing:write` scope AND organization-admin privileges.

Cancellation lives here rather than on its own endpoint because it is one surface with the rest of the billing lifecycle. The common reason a subscription is about to lapse is a declined card, and the fix for that is a new card, not a cancellation — sending a customer somewhere that can only cancel would lose renewals.

Cancelling in the portal ends the subscription at the close of the current period; coverage continues until then and `/billing/subscription` reports `cancel_at_period_end: true`.

An organization that has never paid for anything gets 404: there is no billing account to manage, and this endpoint deliberately does not create one as a side effect of looking.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.subscription_portal_request import SubscriptionPortalRequest
from deeprelay_sdk.models.subscription_portal_session import SubscriptionPortalSession
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
    api_instance = deeprelay_sdk.BillingApi(api_client)
    subscription_portal_request = deeprelay_sdk.SubscriptionPortalRequest() # SubscriptionPortalRequest |  (optional)

    try:
        # Open the billing portal to cancel or manage the subscription
        api_response = api_instance.create_subscription_portal(subscription_portal_request=subscription_portal_request)
        print("The response of BillingApi->create_subscription_portal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_subscription_portal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_portal_request** | [**SubscriptionPortalRequest**](SubscriptionPortalRequest.md)|  | [optional] 

### Return type

[**SubscriptionPortalSession**](SubscriptionPortalSession.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Not an organization admin |  -  |
**404** | The organization has no billing account yet |  -  |
**503** | Subscription billing is not configured on this deployment |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance**
> Balance get_balance()

Get the org credit balance

Returns the organization's credit balance, its auto-pay configuration, and the live burn rate. Requires the `billing:read` scope. The organization is taken from the authenticated API key, never from a parameter.

Divide `balance_cents` by `burn_cents_per_hour` for the remaining runway in hours. The quotient is undefined in three cases a caller must keep apart: `burn_cents_per_hour` is 0 (nothing running, so the balance funds unbounded idle time), it is `null` (the burn rate could not be determined — NOT the same as idle), or the balance is already at or below zero.

This is the balance itself — for spend against a configured cap see `/billing/spending-limit`, and for past consumption see `/usage`.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.balance import Balance
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
    api_instance = deeprelay_sdk.BillingApi(api_client)

    try:
        # Get the org credit balance
        api_response = api_instance.get_balance()
        print("The response of BillingApi->get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Balance**](Balance.md)

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

# **get_deposit**
> CryptoDeposit get_deposit(id)

Get one stablecoin deposit

Returns a single deposit belonging to the caller's organization. Requires the `billing:read` scope. A deposit belonging to another organization returns the same `404 deposit-not-found` as one that does not exist — deliberately, so this endpoint cannot be used to test whether a deposit id is real. Also 404 when stablecoin deposits are not enabled for this deployment.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.crypto_deposit import CryptoDeposit
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
    api_instance = deeprelay_sdk.BillingApi(api_client)
    id = 'id_example' # str | The deposit id.

    try:
        # Get one stablecoin deposit
        api_response = api_instance.get_deposit(id)
        print("The response of BillingApi->get_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The deposit id. | 

### Return type

[**CryptoDeposit**](CryptoDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | &#x60;deposit-not-found&#x60; — no such deposit, or it belongs to another organization. &#x60;not-found&#x60; — the feature is not enabled.  |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spending_limit**
> SpendingLimit get_spending_limit()

Get the org spending limit

Returns the organization's monthly spending limit and opt-in daily spend cap, with the current month and day spend. Requires the `billing:read` scope. Returns 404 when no limit is configured.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.spending_limit import SpendingLimit
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
    api_instance = deeprelay_sdk.BillingApi(api_client)

    try:
        # Get the org spending limit
        api_response = api_instance.get_spending_limit()
        print("The response of BillingApi->get_spending_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_spending_limit: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SpendingLimit**](SpendingLimit.md)

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

# **get_subscription**
> Subscription get_subscription()

Get the org subscription status and quota usage

Returns the organization's flat-tier subscription: whether it is entitled, the current billing period, the plan's configured quota, and — for an entitled subscription — consumption against the four limits the server enforces on every request. Requires the `billing:read` scope. The organization is taken from the authenticated API key, never from a parameter.

An organization that never subscribed is NOT an error. It gets 200 with `subscribed: false`, `status: "none"` and the quota the plan would provide, so a client can answer "what does the plan include" without a second endpoint and without an error path.

Read `subscribed`, not `status`, to decide whether the plan applies: `status` carries the billing provider's vocabulary, and the two can disagree — an `active` subscription just past its period end still entitles for a short grace window (renewal-webhook lag), while `past_due` and `canceled` never entitle.

`usage` is present only for an entitled subscription whose meter could be read. An absent `usage` NEVER means "nothing used" — reading it as zero would report a full quota to an organization that has none left.

This is the plan's meter. For pay-as-you-go credit see `/billing/balance`, for spend against a self-set cap see `/billing/spending-limit`, and for past consumption see `/usage`.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.subscription import Subscription
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
    api_instance = deeprelay_sdk.BillingApi(api_client)

    try:
        # Get the org subscription status and quota usage
        api_response = api_instance.get_subscription()
        print("The response of BillingApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_subscription: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Subscription**](Subscription.md)

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

# **list_deposits**
> ListDeposits200Response list_deposits()

List stablecoin deposits

Returns the organization's stablecoin deposits, newest first, capped at 50. Requires the `billing:read` scope. The organization is taken from the authenticated API key, never from a parameter. Returns 404 when stablecoin deposits are not enabled for this deployment.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.list_deposits200_response import ListDeposits200Response
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
    api_instance = deeprelay_sdk.BillingApi(api_client)

    try:
        # List stablecoin deposits
        api_response = api_instance.list_deposits()
        print("The response of BillingApi->list_deposits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_deposits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDeposits200Response**](ListDeposits200Response.md)

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

# **update_spending_limit**
> SpendingLimit update_spending_limit(update_spending_limit_request)

Set the org spending limit

Sets the monthly spending limit and optionally sets or clears the opt-in daily spend cap. Requires the `billing:write` scope AND org-admin privileges (a non-admin member gets 403). `daily_limit_dollars` uses pointer semantics: omit to leave the cap unchanged, 0 to clear it, a positive value to set it.


### Example

* Bearer (deeprelay_live_<24-base62>) Authentication (bearerAuth):

```python
import deeprelay_sdk
from deeprelay_sdk.models.spending_limit import SpendingLimit
from deeprelay_sdk.models.update_spending_limit_request import UpdateSpendingLimitRequest
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
    api_instance = deeprelay_sdk.BillingApi(api_client)
    update_spending_limit_request = deeprelay_sdk.UpdateSpendingLimitRequest() # UpdateSpendingLimitRequest | 

    try:
        # Set the org spending limit
        api_response = api_instance.update_spending_limit(update_spending_limit_request)
        print("The response of BillingApi->update_spending_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_spending_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_spending_limit_request** | [**UpdateSpendingLimitRequest**](UpdateSpendingLimitRequest.md)|  | 

### Return type

[**SpendingLimit**](SpendingLimit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Error response (RFC 7807) |  -  |
**422** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

