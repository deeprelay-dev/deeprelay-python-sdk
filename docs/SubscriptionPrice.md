# SubscriptionPrice

The plan's recurring charge, read live from the billing provider — the single source of truth, never a number embedded in code.  ABSENT means \"price unavailable right now\" (billing unconfigured, or the provider could not be reached). It NEVER means free. Render the plan without a figure rather than substituting one; the hosted checkout page always shows the real amount. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** | Amount in the currency&#39;s minor unit (299 &#x3D; $2.99). | 
**currency** | **str** | ISO 4217 currency code, lower-case (e.g. \&quot;usd\&quot;). | 
**interval** | **str** | Recurrence unit — \&quot;day\&quot;, \&quot;week\&quot;, \&quot;month\&quot; or \&quot;year\&quot;. | 
**interval_count** | **int** | How many intervals between charges (\&quot;month\&quot;, 1 &#x3D; monthly). | 

## Example

```python
from deeprelay_sdk.models.subscription_price import SubscriptionPrice

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPrice from a JSON string
subscription_price_instance = SubscriptionPrice.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPrice.to_json())

# convert the object into a dict
subscription_price_dict = subscription_price_instance.to_dict()
# create an instance of SubscriptionPrice from a dict
subscription_price_from_dict = SubscriptionPrice.from_dict(subscription_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


