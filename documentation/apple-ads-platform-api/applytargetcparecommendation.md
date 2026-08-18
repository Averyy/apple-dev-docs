# ApplyTargetCpaRecommendation

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request object for applying or dismissing a target CPA recommendation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ApplyTargetCpaRecommendation
```

#### Discussion

`ApplyTargetCpaRecommendation` is the request body for applying or dismissing a target CPA recommendation.

##### Example

```json
{
  "id": "rec-tcpa-001",
  "promotedObjectId": "123456",
  "promotedObjectType": "APPSTORE_APP",
  "appliedTargetCPA": {
    "amount": "5.00",
    "currency": "USD"
  },
  "historyId": "hist-tcpa-001"
}
```

## Properties

- `id` (string) *(required)*: The unique identifier of the recommendation to act on.
- `promotedObjectId` (string) *(required)*: The ID of the promoted object. For `APPSTORE_APP`, this is the app Adam ID. For `BUSINESS_BRAND`, this is the brand ID.
- `promotedObjectType` (string) *(required)*: The type of the promoted object.
- `appliedTargetCPA` (RecommendationMoney): The target CPA value to apply. Overrides `recommendedTargetCPA` if provided. Ignored on dismiss. See [`Money`](recommendationmoney.md).
- `historyId` (string): Optional reference to a prior history record.

## See Also

- [object TargetCpaRecommendation](targetcparecommendation.md)
  A target CPA recommendation for a campaign using a Maximize Conversions bid strategy.
- [object TargetCpaRecommendationHistory](targetcparecommendationhistory.md)
  History record created when a target CPA recommendation is applied or dismissed.
- [object DailyCapRecommendation](dailycaprecommendation.md)
  A daily budget recommendation for a campaign that is frequently hitting its spending ceiling.
- [object DailyCapRecommendationHistory](dailycaprecommendationhistory.md)
  History record created when you apply or dismiss a daily budget recommendation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/applytargetcparecommendation)*