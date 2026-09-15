# Query Daily Budget Recommendations

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve daily budget recommendations for campaigns that may have more opportunities.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

Each [`DailyCapRecommendation`](dailycaprecommendation.md) result includes:

- `suggestedDailyBudgetAmount`: the recommended new daily budget
- `dailyBudget`: the current budget for comparison
- Historical metrics: `installs`, `spend`, `impression`, `taps`, `averageCPA`, `averageCPT`, `ttr`
- Expected metrics: projected performance if the budget is raised

See [`FilterOperator`](recommendationfilteroperator.md) for the full set of supported comparison operators.

##### Filterable Fields

| Field | Type | Operators | Description |
| --- | --- | --- | --- |
| `promotedObjectId` | string | `EQUALS`, `IN` | Required. The ID of the promoted object. For `APPSTORE_APP`, this is the app Adam ID. For `BUSINESS_BRAND`, this is the brand ID. |
| `promotedObjectType` | string (enum) | `EQUALS` | Required. The type of promoted object. Accepts exactly one value. |
| `recommendationType` | string (enum) | `EQUALS`, `IN` | Optional. The recommendation category, for example `DAILYCAP` or `SDAILYCAP`. See [`RecommendationCategory`](recommendationcategory.md). |
| `campaignId` | integer | `EQUALS`, `IN` | Optional. Filter by a specific campaign. |
| `campaignName` | string | `EQUALS`, `CONTAINS_ANY`, `STARTS_WITH` | Optional. The campaign’s display name. |
| `suggestedDailyBudgetAmount` | money | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. The recommended new daily budget. |
| `dailyBudget` | money | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. The campaign’s current daily budget. |
| `state` | string (enum) | `EQUALS`, `IN` | Optional. `AVAILABLE`, `APPLIED`, `DISMISSED`, or `DELETE`. |
| `status` | string (enum) | `EQUALS`, `IN` | Optional. `ENABLED`, `DISABLED`, or `DELETED`. |
| `creationTime` | string (date-time) | `EQUALS`, `GREATER_THAN`, `LESS_THAN` | Optional. When the recommendation was created. |
| `modificationTime` | string (date-time) | `EQUALS`, `GREATER_THAN`, `LESS_THAN` | Optional. When the recommendation was last modified. |
| `expirationTime` | string (date-time) | `EQUALS`, `GREATER_THAN`, `LESS_THAN` | Optional. When the recommendation expires. |
| `installs` | integer | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Historical install count. |
| `spend` | money | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Historical spend. |
| `averageCPA` | money | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Historical average cost-per-acquisition. |
| `averageCPT` | money | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Historical average cost-per-tap. |
| `impression` | integer | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Historical impression count. |
| `ttr` | number | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Historical tap-through rate. |
| `taps` | integer | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Historical tap count. |
| `expectedImpressions` | integer | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Projected impression count if the recommendation is applied. |
| `expectedInstalls` | integer | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Projected install count if the recommendation is applied. |
| `expectedSpend` | money | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Projected spend if the recommendation is applied. |
| `expectedTaps` | integer | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Projected tap count if the recommendation is applied. |
| `expectedCpa` | money | `EQUALS`, `GREATER_THAN`, `LESS_THAN`, `BETWEEN` | Optional. Projected cost-per-acquisition if the recommendation is applied. |
| `bidStrategy` | object | `EQUALS`, `IN` | Optional. The campaign’s current bid strategy. |

> **Note**: `id` appears in every response but doesn’t support any filter operator on this endpoint.

#### Payload Examples

This example queries available daily budget recommendations for an app, sorted by the suggested budget amount in descending order. The response includes the current and suggested budgets alongside historical and projected performance metrics.

##### Request

```json
POST /v1/recommendations/daily-budgets/query

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
     "field": "suggestedDailyBudgetAmount",
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
     "id": "rec-budget-001",
     "recommendationType": "DAILYCAP",
     "promotedObjectId": "123456",
     "promotedObjectType": "APPSTORE_APP",
     "campaignId": 789012,
     "campaignName": "Q1 Productivity Campaign",
     "suggestedDailyBudgetAmount": {
       "amount": "500.00",
       "currency": "USD"
     },
     "dailyBudget": {
       "amount": "300.00",
       "currency": "USD"
     },
     "bidStrategy": {
       "bidStrategyType": "MAX_CONVERSIONS",
       "bidStrategyGoal": "INSTALL"
     },
     "state": "AVAILABLE",
     "status": "ENABLED",
     "installs": 500,
     "taps": 2500,
     "impression": 50000,
     "spend": {
       "amount": "2250.00",
       "currency": "USD"
     },
     "averageCPA": {
       "amount": "4.50",
       "currency": "USD"
     },
     "averageCPT": {
       "amount": "0.90",
       "currency": "USD"
     },
     "ttr": 0.05,
     "expectedInstalls": 600,
     "expectedTaps": 3000,
     "expectedImpressions": 60000,
     "expectedSpend": {
       "amount": "2700.00",
       "currency": "USD"
     },
     "expectedCpa": {
       "amount": "4.50",
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

`POST https://api.ads.apple.com/v1/recommendations/daily-budgets/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

See [`RecommendationQueryRequest`](recommendationqueryrequest.md).

## See Also

- [Query Target CPA Recommendations](query-target-cpa-recommendations.md)
  Retrieve target cost-per-acquisition recommendations for campaigns using a Maximize Conversions bid strategy.
- [Apply Target CPA Recommendations](apply-target-cpa-recommendations.md)
  Apply one or more target CPA recommendations.
- [Dismiss Target CPA Recommendations](dismiss-target-cpa-recommendations.md)
  Dismiss one or more target CPA recommendations without changing the campaign’s bid strategy.
- [Apply Daily Budget Recommendations](apply-daily-budget-recommendations.md)
  Apply one or more daily budget recommendations, updating the campaign’s daily budget to the suggested amount.
- [Dismiss Daily Budget Recommendations](dismiss-daily-budget-recommendations.md)
  Dismiss one or more daily budget recommendations without changing the campaign’s budget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-daily-budget-recommendations)*