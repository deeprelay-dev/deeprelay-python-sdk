# BatchDeeprelay

When the batch runs, at what rate, and for how much. Money is in micro-cents (1e-6 cent); timestamps are Unix seconds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_for** | **int** | When the batch starts (or started) running. Equal to the submit time when the model was off-peak then. | 
**current_window** | [**BatchDeeprelayCurrentWindow**](BatchDeeprelayCurrentWindow.md) |  | 
**next_window_at** | **int** | When the next off-peak run starts, for a batch that is waiting or paused at a window close. | 
**estimated_completion_at** | **int** | An estimate from the batch&#39;s place in the queue, the window schedule and the observed drain rate. Null when the drain rate is not known yet. Never a promise. | 
**expires_at** | **int** | The deadline (72 hours after submit by default). Lines not run by then expire with &#x60;batch_expired&#x60;. | 
**rate_tier** | **str** | The rate quoted at &#x60;scheduled_for&#x60;: &#x60;off_peak&#x60; (the model&#39;s off-peak rate, half of peak on models with a peak schedule), &#x60;batch&#x60; (a batch price set for the model, never above the synchronous rate) or &#x60;normal&#x60; (the model&#39;s standard rate). Each line is billed at the rate in effect when it runs. | 
**batch_price** | [**BatchDeeprelayBatchPrice**](BatchDeeprelayBatchPrice.md) |  | 
**estimated_cost** | [**BatchMoney**](BatchMoney.md) | The submit estimate: input tokens plus each line&#39;s &#x60;max_tokens&#x60; at the batch rate. An estimate, not a hold; set &#x60;max_tokens&#x60; to lower it. | 
**estimated_tokens** | [**BatchDeeprelayEstimatedTokens**](BatchDeeprelayEstimatedTokens.md) |  | 
**cost** | [**BatchMoney**](BatchMoney.md) | What the batch has cost so far, summed from the billed lines. | 
**pause_reason** | **str** | Why an &#x60;in_progress&#x60; batch is not running: &#x60;peak_window&#x60;, &#x60;upstream_backoff&#x60;, &#x60;no_drain_budget&#x60;, or a balance or spend gate (&#x60;insufficient_balance&#x60;, &#x60;api_key_budget_exceeded&#x60;, &#x60;member_spend_limit_reached&#x60;, &#x60;daily_limit_reached&#x60;, &#x60;spending_limit_reached&#x60;, &#x60;account_frozen&#x60;) that clears after a top-up, a raised limit or a new period. Null while running. | 
**windows_ran_in** | **List[int]** | Start times of the off-peak runs the batch has run in. | 
**request_counts** | [**BatchDeeprelayRequestCounts**](BatchDeeprelayRequestCounts.md) |  | 
**limits** | [**BatchLimits**](BatchLimits.md) |  | 

## Example

```python
from deeprelay_sdk.models.batch_deeprelay import BatchDeeprelay

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeeprelay from a JSON string
batch_deeprelay_instance = BatchDeeprelay.from_json(json)
# print the JSON string representation of the object
print(BatchDeeprelay.to_json())

# convert the object into a dict
batch_deeprelay_dict = batch_deeprelay_instance.to_dict()
# create an instance of BatchDeeprelay from a dict
batch_deeprelay_from_dict = BatchDeeprelay.from_dict(batch_deeprelay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


