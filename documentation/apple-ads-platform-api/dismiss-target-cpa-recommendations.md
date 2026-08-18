# Dismiss Target CPA Recommendations

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Dismiss one or more target CPA recommendations without changing the campaign’s bid strategy.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Dismissing a target CPA recommendation just means you’ve reviewed it and decided not to apply it. The campaign’s target CPA stays unchanged, and the recommendation moves to `DISMISSED` state. The response is a history record that preserves the recommended value you passed on.

#### Request Body

#### Payload Examples

This example dismisses a target CPA recommendation. The campaign’s target CPA stays the same, and the response confirms the recommendation is now in `DISMISSED` state, along with the recommended value that was passed on.

##### Request

```json
POST /v1/recommendations/target-cpas/dismiss

[
 {
   "id": "rec-tcpa-001",
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
     "state": "DISMISSED",
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

`POST https://api.ads.apple.com/v1/recommendations/target-cpas/dismiss`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

Send an array of [`ApplyTargetCpaRecommendation`](applytargetcparecommendation.md) objects, one per recommendation you want to dismiss. All items must share the same `promotedObjectId`, and each item needs `id`, `promotedObjectId`, and `promotedObjectType`.

## See Also

- [Query Target CPA Recommendations](query-target-cpa-recommendations.md)
  Retrieve target cost-per-acquisition recommendations for campaigns using a Maximize Conversions bid strategy.
- [Apply Target CPA Recommendations](apply-target-cpa-recommendations.md)
  Apply one or more target CPA recommendations.
- [Query Daily Budget Recommendations](query-daily-budget-recommendations.md)
  Retrieve daily budget recommendations for campaigns that may have more opportunities.
- [Apply Daily Budget Recommendations](apply-daily-budget-recommendations.md)
  Apply one or more daily budget recommendations, updating the campaign’s daily budget to the suggested amount.
- [Dismiss Daily Budget Recommendations](dismiss-daily-budget-recommendations.md)
  Dismiss one or more daily budget recommendations without changing the campaign’s budget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/dismiss-target-cpa-recommendations)*