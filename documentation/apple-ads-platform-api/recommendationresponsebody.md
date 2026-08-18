# ResponseEnvelope

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The standard response envelope for all Recommendations and Suggestions API endpoints.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationResponseBody
```

#### Discussion

The response envelope is the standard wrapper returned by all Recommendations and Suggestions endpoints.

The `result` field contains the response payload. It’s usually an array, but for the Target CPA suggestion query response ([`RecommendationQueryTargetCpaSuggestionResponse`](recommendationquerytargetcpasuggestionresponse.md)) specifically, it’s a single object, since that endpoint always returns one suggestion rather than a list.

The `pagination` field describes the current page position and is `null` for apply and dismiss responses.

##### Example

```json
{
  "result": [
    {
      "id": "rec-budget-001",
      "recommendationType": "DAILYCAP",
      "campaignId": 789012,
      "state": "AVAILABLE"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20,
    "totalCount": 1
  }
}
```

## Topics

### Dictionaries
- [object RecommendationResponseBody.Result](recommendationresponsebody/result-data.dictionary.md)
  Usually an array of recommendation, suggestion, or history objects returned by the endpoint. A single object for the Target CPA suggestion query response.

## Properties

- `result` (RecommendationResponseBody.Result): Usually an array of recommendation, suggestion, or history objects returned by the endpoint. A single object for the Target CPA suggestion query response. Read-only.
- `pagination` (RecommendationResponsePagination): Pagination metadata for the result set. See [`ResponsePagination`](recommendationresponsepagination.md). Read-only.
- `error` (RecommendationResponseError): Error information when the request fails. Absent on success. See [`ResponseError`](recommendationresponseerror.md). Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationresponsebody)*