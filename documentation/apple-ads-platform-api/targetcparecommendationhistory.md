# TargetCpaRecommendationHistory

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

History record created when a target CPA recommendation is applied or dismissed.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object TargetCpaRecommendationHistory
```

#### Discussion

`TargetCpaRecommendationHistory` is an immutable record that the system creates when you apply or dismiss a target CPA recommendation. The record preserves both `recommendedTargetCPA` and `appliedTargetCPA` (the value actually used, which may differ if the advertiser supplied a custom override).

##### Example

```json
{
  "recommendationId": "123456789",
  "recommendationType": "TCPA",
  "promotedObjectId": "987654321",
  "promotedObjectType": "APPSTORE_APP",
  "campaignId": 555666777,
  "campaignName": "AwayFinder - US - Search",
  "state": "APPLIED",
  "status": "ENABLED",
  "appliedTargetCPA": {
    "amount": "5.50",
    "currency": "USD"
  },
  "recommendedTargetCPA": {
    "amount": "6.00",
    "currency": "USD"
  },
  "rank": 1,
  "installs": 1240,
  "spend": {
    "amount": "6820.00",
    "currency": "USD"
  },
  "averageCPA": {
    "amount": "5.50",
    "currency": "USD"
  },
  "averageCPT": {
    "amount": "0.85",
    "currency": "USD"
  },
  "impression": 980000,
  "taps": 8025,
  "ttr": 0.0082,
  "expectedInstalls": 1400,
  "expectedSpend": {
    "amount": "8400.00",
    "currency": "USD"
  },
  "expectedTaps": 9100,
  "expectedCPA": {
    "amount": "6.00",
    "currency": "USD"
  },
  "creationTime": "2025-01-05T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000",
  "appliedTime": "2025-01-10T08:00:00.000",
  "expirationTime": "2025-01-20T08:00:00.000"
}
```

## Properties

- `recommendationId` (string): The ID of the original recommendation. Read-only.
- `recommendationType` (RecommendationCategory): The recommendation category. Value: `TCPA`. Read-only.
- `promotedObjectId` (string): The ID of the promoted object. For `APPSTORE_APP`, this is the app Adam ID. For `BUSINESS_BRAND`, this is the brand ID. Read-only.
- `promotedObjectType` (PromotedObjectType): The type of the promoted object. Read-only.
- `campaignId` (int64): The campaign ID. Read-only.
- `campaignName` (string): Display name of the campaign. Read-only.
- `state` (RecommendationState): Terminal state. Values: `APPLIED`, `DISMISSED`. Read-only.
- `status` (RecommendationStatus): Operational status. Read-only.
- `appliedTargetCPA` (RecommendationMoney): The target CPA that was applied. Null on dismiss. See [`Money`](recommendationmoney.md). Read-only.
- `recommendedTargetCPA` (RecommendationMoney): The originally recommended target CPA. See [`Money`](recommendationmoney.md). Read-only.
- `rank` (int32): Rank at time of action. Read-only.
- `installs` (int64): Historical install count. Read-only.
- `spend` (RecommendationMoney): Historical spend. See [`Money`](recommendationmoney.md). Read-only.
- `averageCPA` (RecommendationMoney): Historical average CPA. See [`Money`](recommendationmoney.md). Read-only.
- `averageCPT` (RecommendationMoney): Historical average CPT. See [`Money`](recommendationmoney.md). Read-only.
- `impression` (int64): Historical impression count. Read-only.
- `taps` (int64): Historical tap count. Read-only.
- `ttr` (double): Historical tap-through rate. Read-only.
- `expectedInstalls` (int64): Expected installs from the original recommendation. Read-only.
- `expectedSpend` (RecommendationMoney): Expected spend from the original recommendation. See [`Money`](recommendationmoney.md). Read-only.
- `expectedTaps` (int64): Expected taps from the original recommendation. Read-only.
- `expectedCPA` (RecommendationMoney): Expected CPA from the original recommendation. See [`Money`](recommendationmoney.md). Read-only.
- `creationTime` (date-time): When the original recommendation was created. Read-only.
- `modificationTime` (date-time): When this history record was last modified. Read-only.
- `appliedTime` (date-time): When the action was taken. Read-only.
- `expirationTime` (date-time): When the original recommendation would have expired. Read-only.

## See Also

- [object TargetCpaRecommendation](targetcparecommendation.md)
  A target CPA recommendation for a campaign using a Maximize Conversions bid strategy.
- [object DailyCapRecommendation](dailycaprecommendation.md)
  A daily budget recommendation for a campaign that is frequently hitting its spending ceiling.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/targetcparecommendationhistory)*