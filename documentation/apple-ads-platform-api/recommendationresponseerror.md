# ResponseError

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Error information returned in the response body when a Recommendations or Suggestions request fails.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationResponseError
```

#### Discussion

`ResponseError` is the error object embedded in the `error` field of the response envelope when a Recommendations or Suggestions request fails.

When the error involves multiple field-level issues (for example, validation failures on several request fields), inspect the `details` array to identify and correct each specific problem before retrying the request.

##### Example

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Invalid query request",
  "details": [
    {
      "code": "MISSING_REQUIRED_FILTER",
      "message": "Filter 'promotedObjectId' is required"
    }
  ]
}
```

## Properties

- `code` (string): A machine-readable error code identifying the failure type, useful for programmatic error handling. Read-only.
- `message` (string): A human-readable summary of what went wrong. Read-only.
- `details` ([RecommendationResponseErrorDetail]): An array of granular error detail objects providing field-level context, one per issue. See [`ResponseErrorDetail`](recommendationresponseerrordetail.md). Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationresponseerror)*