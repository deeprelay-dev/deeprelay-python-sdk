# RefereeStatus

Present only when the organization signed up through someone else's invite link: where that referral sits and how far the organization is from unlocking its own reward. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Lifecycle state. &#x60;pending&#x60; until the gate is met; &#x60;qualified&#x60; inside the hold; &#x60;settled&#x60; once paid; &#x60;reversed&#x60; when the qualifying deposit was refunded after payout and both rewards were taken back. | 
**gate** | **str** | What qualifies this referral. &#x60;deposit&#x60; (net real deposits) for current referrals; &#x60;spend&#x60; (inference usage) for referrals made under the earlier program, which keep their original terms. | [optional] 
**progress_cents** | **int** | Progress toward the gate so far — net deposits for &#x60;deposit&#x60;, inference spend for &#x60;spend&#x60;. | [optional] 
**goal_cents** | **int** | The amount that qualifies the referral. | [optional] 
**spent_cents** | **int** | Deprecated alias of &#x60;progress_cents&#x60;. | 
**qualify_spend_cents** | **int** | Deprecated alias of &#x60;goal_cents&#x60;. | 
**reward_cents** | **int** | What this organization receives on settlement. | 
**qualified_at** | **datetime** | When the gate was met. Absent while pending. | [optional] 
**hold_until** | **datetime** | When the hold ends and both halves pay out. Absent while pending. | [optional] 
**settled_at** | **datetime** | When the reward was paid. Absent until settled. | [optional] 

## Example

```python
from deeprelay_sdk.models.referee_status import RefereeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RefereeStatus from a JSON string
referee_status_instance = RefereeStatus.from_json(json)
# print the JSON string representation of the object
print(RefereeStatus.to_json())

# convert the object into a dict
referee_status_dict = referee_status_instance.to_dict()
# create an instance of RefereeStatus from a dict
referee_status_from_dict = RefereeStatus.from_dict(referee_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


