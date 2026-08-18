# Query Target CPA Recommendations

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve target cost-per-acquisition recommendations for campaigns using a Maximize Conversions bid strategy.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Each [`TargetCpaRecommendation`](targetcparecommendation.md) result includes:

- `recommendedTargetCPA`: the suggested new target CPA
- `bidStrategy`: the campaign’s current bid strategy context
- Historical metrics: `installs`, `spend`, `taps`, `averageCPA`, `averageCPT`, `impression`, `ttr`
- Expected metrics: projected `expectedInstalls`, `expectedSpend`, `expectedTaps`, `expectedCPA`

Only campaigns using a Maximize Conversions bid strategy will receive recommendations.

> **Note**: A target CPA is a goal the system optimizes toward, not a bid. The auto-bidder sets bids internally to try to meet the target.

#### Request Body

#### Payload Examples

This example queries available target CPA recommendations for an app, sorted by creation time. The response includes the recommended CPA alongside historical performance metrics and projected results if the recommendation is applied.

##### Request

```json
POST /v1/recommendations/target-cpas/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 20
 },
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": [
       "123456"
     ]
   },
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": [
       "APPSTORE_APP"
     ]
   },
   {
     "field": "state",
     "operator": "EQUALS",
     "value": [
       "AVAILABLE"
     ]
   }
 ],
 "sorting": [
   {
     "field": "creationTime",
     "order": "DESC"
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "id": "rec-tcpa-001",
     "state": "AVAILABLE",
     "status": "ENABLED",
     "promotedObjectId": "123456",
     "promotedObjectType": "APPSTORE_APP",
     "recommendationType": "TCPA",
     "campaignId": 789012,
     "campaignName": "Q1 Productivity Campaign",
     "recommendedTargetCPA": {
       "amount": "5.00",
       "currency": "USD"
     },
     "averageCPT": {
       "amount": "0.50",
       "currency": "USD"
     },
     "averageCPA": {
       "amount": "4.50",
       "currency": "USD"
     },
     "installs": 500,
     "taps": 2500,
     "impression": 50000,
     "spend": {
       "amount": "2250.00",
       "currency": "USD"
     },
     "ttr": 0.05,
     "expectedTaps": 3000,
     "expectedInstalls": 600,
     "expectedSpend": {
       "amount": "3000.00",
       "currency": "USD"
     },
     "expectedCPA": {
       "amount": "5.00",
       "currency": "USD"
     },
     "creationTime": "2026-02-20T10:30:00Z",
     "modificationTime": "2026-02-20T10:30:00Z",
     "expirationTime": "2026-03-20T10:30:00Z"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "totalCount": 1
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/recommendations/target-cpas/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

See [`RecommendationQueryRequest`](recommendationqueryrequest.md).

## See Also

- [Apply Target CPA Recommendations](apply-target-cpa-recommendations.md)
  Apply one or more target CPA recommendations.
- [Dismiss Target CPA Recommendations](dismiss-target-cpa-recommendations.md)
  Dismiss one or more target CPA recommendations without changing the campaign’s bid strategy.
- [Query Daily Budget Recommendations](query-daily-budget-recommendations.md)
  Retrieve daily budget recommendations for campaigns that may have more opportunities.
- [Apply Daily Budget Recommendations](apply-daily-budget-recommendations.md)
  Apply one or more daily budget recommendations, updating the campaign’s daily budget to the suggested amount.
- [Dismiss Daily Budget Recommendations](dismiss-daily-budget-recommendations.md)
  Dismiss one or more daily budget recommendations without changing the campaign’s budget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-target-cpa-recommendations)*