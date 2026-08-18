# DailyCapRecommendation

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A daily budget recommendation for a campaign that is frequently hitting its spending ceiling.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object DailyCapRecommendation
```

#### Discussion

When a campaign frequently exhausts its daily budget, `DailyCapRecommendation` provides a system-calculated `suggestedDailyBudgetAmount` to unlock constrained growth. The `expectedInstalls`, `expectedSpend`, and `expectedCpa` fields provide projected seven-day performance estimates. Recommendations expire (`expirationTime`) and transition to `APPLIED` or `DISMISSED` once actioned.

##### Example

```json
{
  "id": "rec-budget-001",
  "recommendationType": "DAILYCAP",
  "promotedObjectId": "123456789",
  "promotedObjectType": "APPSTORE_APP",
  "campaignId": 987654321,
  "campaignName": "AwayFinder Q1 Growth Campaign",
  "state": "AVAILABLE",
  "status": "ENABLED",
  "suggestedDailyBudgetAmount": {
    "amount": "500.00",
    "currency": "USD"
  },
  "dailyBudget": {
    "amount": "250.00",
    "currency": "USD"
  },
  "bidStrategy": {
    "bidStrategyType": "MAX_CONVERSIONS",
    "bidStrategyGoal": "INSTALL",
    "bidAmount": {
      "amount": "1.50",
      "currency": "USD"
    }
  },
  "installs": 500,
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
  "impression": 50000,
  "taps": 2500,
  "ttr": 0.05,
  "expectedImpressions": 60000,
  "expectedInstalls": 600,
  "expectedSpend": {
    "amount": "2700.00",
    "currency": "USD"
  },
  "expectedTaps": 3000,
  "expectedCpa": {
    "amount": "4.50",
    "currency": "USD"
  },
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000",
  "expirationTime": "2025-02-10T08:00:00.000"
}
```

## Properties

- `id` (string): Unique identifier for the recommendation. Read-only.
- `recommendationType` (RecommendationCategory): The recommendation category. Value: `DAILYCAP`. Read-only.
- `promotedObjectId` (string): The ID of the promoted object. For `APPSTORE_APP`, this is the app Adam ID. For `BUSINESS_BRAND`, this is the brand ID. Read-only.
- `promotedObjectType` (PromotedObjectType): The type of the promoted object. Read-only.
- `campaignId` (int64): The campaign the recommendation is for. Read-only.
- `campaignName` (string): Display name of the campaign. Read-only.
- `state` (RecommendationState): Current state. Values: `AVAILABLE`, `APPLIED`, `DISMISSED`, `DELETE`. Read-only.
- `status` (RecommendationStatus): Operational status. Read-only.
- `suggestedDailyBudgetAmount` (RecommendationMoney): The recommended new daily budget. See [`Money`](money.md). Read-only.
- `dailyBudget` (RecommendationMoney): The campaign’s current daily budget. See [`Money`](money.md). Read-only.
- `bidStrategy` (RecommendationBidStrategy): The campaign’s current bid strategy. See [`BidStrategy`](bidstrategy.md). Read-only.
- `installs` (int64): Historical install count. Read-only.
- `spend` (RecommendationMoney): Historical spend. See [`Money`](money.md). Read-only.
- `averageCPA` (RecommendationMoney): Historical average cost per acquisition. See [`Money`](money.md). Read-only.
- `averageCPT` (RecommendationMoney): Historical average cost per tap. See [`Money`](money.md). Read-only.
- `impression` (int64): Historical impression count. Read-only.
- `taps` (int64): Historical tap count. Read-only.
- `ttr` (double): Historical tap-through rate. Read-only.
- `expectedImpressions` (int64): The estimated impressions you could see over a seven-day period after applying a recommendation, based on historical data. Read-only.
- `expectedInstalls` (int64): The estimated installs you could see over a seven-day period after applying a recommendation, based on historical data. Read-only.
- `expectedSpend` (RecommendationMoney): The estimated amount you could spend over a seven-day period after applying a recommendation, based on historical data. See [`Money`](money.md). Read-only.
- `expectedTaps` (int64): The estimated taps you could see over a seven-day period after applying a recommendation, based on historical data. Read-only.
- `expectedCpa` (RecommendationMoney): The estimated average cost-per-acquisition you could see over a seven-day period after applying a recommendation, based on historical data. See [`Money`](money.md). Read-only.
- `creationTime` (date-time): When the recommendation was created. Read-only.
- `modificationTime` (date-time): When the recommendation was last modified. Read-only.
- `expirationTime` (date-time): When the recommendation expires. Read-only.

## See Also

- [object TargetCpaRecommendation](targetcparecommendation.md)
  A target CPA recommendation for a campaign using a Maximize Conversions bid strategy.
- [object TargetCpaRecommendationHistory](targetcparecommendationhistory.md)
  History record created when a target CPA recommendation is applied or dismissed.
- [object DailyCapRecommendationHistory](dailycaprecommendationhistory.md)
  History record created when you apply or dismiss a daily budget recommendation.
- [object ApplyTargetCpaRecommendation](applytargetcparecommendation.md)
  Request object for applying or dismissing a target CPA recommendation.
- [object ApplyDailyCapRecommendation](applydailycaprecommendation.md)
  Request object for applying or dismissing a daily budget recommendation.
- [object RecommendationResponseBody](recommendationresponsebody.md)
  The standard response envelope for all Recommendations and Suggestions API endpoints.
- [object RecommendationResponseError](recommendationresponseerror.md)
  Error information returned in the response body when a Recommendations or Suggestions request fails.
- [object RecommendationResponseErrorDetail](recommendationresponseerrordetail.md)
  Granular error detail for a single field or condition within a failed Recommendations or Suggestions request.
- [object RecommendationResponsePagination](recommendationresponsepagination.md)
  Pagination metadata returned in list responses from Recommendations and Suggestions endpoints.
- [object RecommendationMoney](recommendationmoney.md)
  A monetary amount with currency used throughout the Recommendations and Suggestions APIs.
- [object RecommendationApplyDailyBudgetResponse](recommendationapplydailybudgetresponse.md)
  Response envelope returned when applying or dismissing a daily budget recommendation, containing the resulting history record(s).
- [object RecommendationApplyTargetCpaResponse](recommendationapplytargetcparesponse.md)
  Response envelope returned when applying or dismissing a target CPA recommendation, containing the resulting history record(s).
- [object RecommendationBidStrategy](recommendationbidstrategy.md)
  Bid strategy configuration (type, goal, and amount) associated with a recommendation.
- [object RecommendationDismissDailyBudgetResponse](recommendationdismissdailybudgetresponse.md)
  Response envelope returned when dismissing a daily budget recommendation, containing the resulting history record(s).
- [object RecommendationDismissTargetCpaResponse](recommendationdismisstargetcparesponse.md)
  Response envelope returned when dismissing a target CPA recommendation, containing the resulting history record(s).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/dailycaprecommendation)*