# Apply Target CPA Recommendations

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Apply one or more target CPA recommendations.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Applying a target CPA recommendation applies the recommendation’s `recommendedTargetCPA` value and moves the recommendation to `APPLIED` state. You can override the suggested value by passing `appliedTargetCPA` in the request. The response is a history record with both the recommended and applied values, plus the performance context behind the recommendation.

#### Request Body

#### Payload Examples

This example applies a target CPA recommendation, overriding the suggested CPA with $5.00. The response confirms the recommendation is now `APPLIED`.

##### Request

```json
POST /v1/recommendations/target-cpas/apply

[
 {
   "id": "rec-tcpa-001",
   "appliedTargetCPA": {
     "amount": "5.00",
     "currency": "USD"
   },
   "promotedObjectId": "123456",
   "promotedObjectType": "APPSTORE_APP"
 }
]
```

##### Response

```json
{
 "result": [
   {
     "recommendationId": "rec-tcpa-001",
     "recommendationType": "TCPA",
     "promotedObjectId": "123456",
     "promotedObjectType": "APPSTORE_APP",
     "campaignId": 789012,
     "state": "APPLIED",
     "appliedTargetCPA": {
       "amount": "5.00",
       "currency": "USD"
     },
     "appliedTime": "2026-02-23T14:30:00Z"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/recommendations/target-cpas/apply`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

Send an array of [`ApplyTargetCpaRecommendation`](applytargetcparecommendation.md) objects, one per recommendation you want to apply. All items must share the same `promotedObjectId`, and each item needs `id`, `promotedObjectId`, and `promotedObjectType`. `appliedTargetCPA` is optional, use it to override the suggested value.

## See Also

- [Query Target CPA Recommendations](query-target-cpa-recommendations.md)
  Retrieve target cost-per-acquisition recommendations for campaigns using a Maximize Conversions bid strategy.
- [Dismiss Target CPA Recommendations](dismiss-target-cpa-recommendations.md)
  Dismiss one or more target CPA recommendations without changing the campaign’s bid strategy.
- [Query Daily Budget Recommendations](query-daily-budget-recommendations.md)
  Retrieve daily budget recommendations for campaigns that may have more opportunities.
- [Apply Daily Budget Recommendations](apply-daily-budget-recommendations.md)
  Apply one or more daily budget recommendations, updating the campaign’s daily budget to the suggested amount.
- [Dismiss Daily Budget Recommendations](dismiss-daily-budget-recommendations.md)
  Dismiss one or more daily budget recommendations without changing the campaign’s budget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/apply-target-cpa-recommendations)*