# Referral

The organization's referral-program view: its invite link, the program terms, its referrer stats, and (only when it was itself referred) its referee progress. Amounts are USD cents. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The organization&#39;s shareable referral code, e.g. &#x60;GPU-7KQ2-M4XP&#x60;. | 
**invite_url** | **str** | The ready-to-share invite link, &#x60;{site}/r/{code}&#x60;. | 
**pending** | **int** | Friends who signed up through the link but have not yet reached the spend gate. | 
**qualified** | **int** | Friends past the spend gate whose reward is inside the chargeback hold. | 
**settled** | **int** | Referrals that have paid out. | 
**earned_cents** | **int** | Total credit paid to this organization as a referrer. | 
**reward_cents** | **int** | Credit paid to the referrer per settled referral. | 
**referee_reward_cents** | **int** | Credit paid to the referred friend per settled referral. | 
**qualify_spend_cents** | **int** | The friend&#39;s cumulative inference spend that qualifies a referral. | 
**hold_days** | **int** | Days between qualification and payout (chargeback hold). | 
**referred** | [**RefereeStatus**](RefereeStatus.md) |  | [optional] 

## Example

```python
from deeprelay_sdk.models.referral import Referral

# TODO update the JSON string below
json = "{}"
# create an instance of Referral from a JSON string
referral_instance = Referral.from_json(json)
# print the JSON string representation of the object
print(Referral.to_json())

# convert the object into a dict
referral_dict = referral_instance.to_dict()
# create an instance of Referral from a dict
referral_from_dict = Referral.from_dict(referral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


