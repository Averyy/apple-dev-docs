# ResponseErrorDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Granular error detail for a single field or condition within a failed Recommendations or Suggestions request.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationResponseErrorDetail
```

#### Discussion

`ResponseErrorDetail` provides field-level granularity for errors returned in a `ResponseError`. Each detail entry identifies one specific condition that caused the request to fail. For example, this occurs for a missing required field, an invalid value, or a constraint violation.

The `code` and `message` fields identify the nature of the issue. When `details` contains multiple entries, correct all issues before retrying. The API rejects the request atomically on the first validation pass.

##### Example

```json
{
  "code": "MISSING_REQUIRED_FILTER",
  "message": "Filter 'promotedObjectId' is required",
  "info": {
    "field": "promotedObjectId",
    "location": "filters"
  }
}
```

## Topics

### Dictionaries
- [object RecommendationResponseErrorDetail.Info](recommendationresponseerrordetail/info-data.dictionary.md)
  Additional context that supplements the error message, varying by endpoint and error type.

## Properties

- `code` (string): A machine-readable code identifying the specific error condition. Read-only.
- `message` (string): A human-readable description of the specific error. Read-only.
- `info` (RecommendationResponseErrorDetail.Info): Additional context that supplements the message, such as the field name, the invalid value, or acceptable alternatives. Content varies by endpoint and error type. Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationresponseerrordetail)*