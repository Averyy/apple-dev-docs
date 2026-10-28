# DailyCapRecommendationHistory

**Framework**: Apple Ads Platform API  
**Kind**: dictionary  
**Role**: Object

History record created when you apply or dismiss a daily budget recommendation.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
object DailyCapRecommendationHistory
```

## Discussion

The `DailyCapRecommendationHistory` object is an immutable record created when you apply or dismiss a daily budget recommendation. The record preserves both `suggestedDailyBudgetAmount` and the `appliedDailyBudgetAmount` actually used, so you can check whether you overrode the suggestion.

### Example

```json
{
  "recommendationId": "123456789",
  "recommendationType": "DAILYCAP",
  "promotedObjectId": "987654321",
  "promotedObjectType": "APPSTORE_APP",
  "campaignId": 555666777,
  "campaignName": "AwayFinder - Search Campaign",
  "state": "APPLIED",
  "status": "ENABLED",
  "appliedDailyBudgetAmount": {
    "amount": "150.00",
    "currency": "USD"
  },
  "suggestedDailyBudgetAmount": {
    "amount": "150.00",
    "currency": "USD"
  },
  "rank": 1,
  "installs": 420,
  "spend": {
    "amount": "980.50",
    "currency": "USD"
  },
  "averageCPA": {
    "amount": "2.33",
    "currency": "USD"
  },
  "averageCPT": {
    "amount": "0.85",
    "currency": "USD"
  },
  "impression": 154000,
  "taps": 3200,
  "ttr": 0.0208,
  "expectedInstalls": 600,
  "expectedSpend": {
    "amount": "1400.00",
    "currency": "USD"
  },
  "expectedCpa": {
    "amount": "2.33",
    "currency": "USD"
  },
  "creationTime": "2025-01-08T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000",
  "appliedTime": "2025-01-10T08:00:00.000",
  "expirationTime": "2025-01-15T08:00:00.000"
}
```

## Properties

- `recommendationId` (string): The ID of the original recommendation. Read-only.
- `recommendationType` (RecommendationCategory): The recommendation category. Value: `DAILYCAP`. Read-only.
- `promotedObjectId` (string): The ID of the promoted object. For `APPSTORE_APP`, this is the app Adam ID. For `BUSINESS_BRAND`, this is the brand ID. Read-only.
- `promotedObjectType` (PromotedObjectType): The type of the promoted object. Read-only.
- `campaignId` (int64): The campaign ID. Read-only.
- `campaignName` (string): Display name of the campaign. Read-only.
- `state` (RecommendationState): Terminal state. Values: `APPLIED`, `DISMISSED`. Read-only.
- `status` (RecommendationStatus): Operational status. Read-only.
- `appliedDailyBudgetAmount` (RecommendationMoney): The daily budget that was applied. Null on dismiss. See [`Money`](./recommendationmoney.md). Read-only.
- `suggestedDailyBudgetAmount` (RecommendationMoney): The originally suggested daily budget. See [`Money`](./recommendationmoney.md). Read-only.
- `rank` (int32): Rank at time of action. Read-only.
- `installs` (int64): Historical install count at time of action. Read-only.
- `spend` (RecommendationMoney): Historical spend at time of action. See [`Money`](./recommendationmoney.md). Read-only.
- `averageCPA` (RecommendationMoney): Historical average CPA at time of action. See [`Money`](./recommendationmoney.md). Read-only.
- `averageCPT` (RecommendationMoney): Historical average CPT at time of action. See [`Money`](./recommendationmoney.md). Read-only.
- `impression` (int64): Historical impression count. Read-only.
- `taps` (int64): Historical tap count. Read-only.
- `ttr` (double): Historical tap-through rate. Read-only.
- `expectedInstalls` (int64): Expected installs from the original recommendation. Read-only.
- `expectedSpend` (RecommendationMoney): Expected spend from the original recommendation. See [`Money`](./recommendationmoney.md). Read-only.
- `expectedCpa` (RecommendationMoney): Expected CPA from the original recommendation. See [`Money`](./recommendationmoney.md). Read-only.
- `creationTime` (date-time): When the original recommendation was created. Read-only.
- `modificationTime` (date-time): When this history record was last modified. Read-only.
- `appliedTime` (date-time): When the action was taken. Read-only.
- `expirationTime` (date-time): When the original recommendation would have expired. Read-only.

## See Also

- [object TargetCpaRecommendation](./targetcparecommendation.md)
  A target CPA recommendation for a campaign using a Maximize Conversions bid strategy.
- [object TargetCpaRecommendationHistory](./targetcparecommendationhistory.md)
  History record created when a target CPA recommendation is applied or dismissed.
- [object DailyCapRecommendation](./dailycaprecommendation.md)
  A daily budget recommendation for a campaign that’s frequently hitting its spending ceiling.
- [object ApplyTargetCpaRecommendation](./applytargetcparecommendation.md)
  Request object for applying or dismissing a target CPA recommendation.
- [object ApplyDailyCapRecommendation](./applydailycaprecommendation.md)
  Request object for applying or dismissing a daily budget recommendation.
- [object RecommendationResponseBody](./recommendationresponsebody.md)
  The standard response envelope for all Recommendations and Suggestions API endpoints.
- [object RecommendationResponseError](./recommendationresponseerror.md)
  Error information returned in the response body when a Recommendations or Suggestions request fails.
- [object RecommendationResponseErrorDetail](./recommendationresponseerrordetail.md)
  Granular error detail for a single field or condition within a failed Recommendations or Suggestions request.
- [object RecommendationResponsePagination](./recommendationresponsepagination.md)
  Pagination metadata returned in list responses from Recommendations and Suggestions endpoints.
- [object RecommendationMoney](./recommendationmoney.md)
  A monetary amount with currency used throughout the Recommendations and Suggestions APIs.
- [object RecommendationApplyDailyBudgetResponse](./recommendationapplydailybudgetresponse.md)
  Response envelope returned when applying or dismissing a daily budget recommendation, containing the resulting history record(s).
- [object RecommendationApplyTargetCpaResponse](./recommendationapplytargetcparesponse.md)
  Response envelope returned when applying or dismissing a target CPA recommendation, containing the resulting history record(s).
- [object RecommendationBidStrategy](./recommendationbidstrategy.md)
  Bid strategy configuration (type, goal, and amount) associated with a recommendation.
- [object RecommendationDismissDailyBudgetResponse](./recommendationdismissdailybudgetresponse.md)
  Response envelope returned when dismissing a daily budget recommendation, containing the resulting history record(s).
- [object RecommendationDismissTargetCpaResponse](./recommendationdismisstargetcparesponse.md)
  Response envelope returned when dismissing a target CPA recommendation, containing the resulting history record(s).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/dailycaprecommendationhistory)*