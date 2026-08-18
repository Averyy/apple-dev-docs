# RecommendationApplyTargetCpaResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Response envelope returned when applying or dismissing a target CPA recommendation, containing the resulting history record(s).

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationApplyTargetCpaResponse
```

## Properties

- `result` ([TargetCpaRecommendationHistory]): The target CPA recommendation history record(s) created by applying the recommendation. Array of [`TargetCpaRecommendationHistory`](targetcparecommendationhistory.md). Read-only.
- `pagination` (RecommendationResponsePagination): Pagination metadata. `null` for apply and dismiss responses. See [`ResponsePagination`](recommendationresponsepagination.md). Read-only.
- `error` (RecommendationResponseError): Error details when the request fails. Absent on success. See [`ResponseError`](recommendationresponseerror.md). Read-only.

## See Also

- [object TargetCpaRecommendation](targetcparecommendation.md)
  A target CPA recommendation for a campaign using a Maximize Conversions bid strategy.
- [object TargetCpaRecommendationHistory](targetcparecommendationhistory.md)
  History record created when a target CPA recommendation is applied or dismissed.
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
- [object RecommendationBidStrategy](recommendationbidstrategy.md)
  Bid strategy configuration (type, goal, and amount) associated with a recommendation.
- [object RecommendationDismissDailyBudgetResponse](recommendationdismissdailybudgetresponse.md)
  Response envelope returned when dismissing a daily budget recommendation, containing the resulting history record(s).
- [object RecommendationDismissTargetCpaResponse](recommendationdismisstargetcparesponse.md)
  Response envelope returned when dismissing a target CPA recommendation, containing the resulting history record(s).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationapplytargetcparesponse)*