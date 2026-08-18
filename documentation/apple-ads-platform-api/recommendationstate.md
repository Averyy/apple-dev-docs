# RecommendationState

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The lifecycle state of a recommendation, indicating whether it is available to act on or has already been accepted or rejected.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string RecommendationState
```

#### Discussion

`RecommendationState` tracks the advertiser’s response to a recommendation. Only recommendations in `AVAILABLE` state can be acted on. Applying or dismissing a recommendation moves it to `APPLIED` or `DISMISSED`, respectively, and creates a corresponding history record.

To retrieve only actionable recommendations, use the `state` filter in query requests:

```json
{
  "field": "state",
  "operator": "EQUALS",
  "value": [
    "AVAILABLE"
  ]
}
```

## See Also

- [object RecommendationQueryRequest](recommendationqueryrequest.md)
  The structured request body for all recommendation query endpoints.
- [object RecommendationQueryRequestPagination](recommendationqueryrequestpagination.md)
  Pagination parameters for a recommendation query request.
- [object RecommendationSorting](recommendationsorting.md)
  A sort specification used in a recommendation query request to order results.
- [type RecommendationSortingOrder](recommendationsortingorder.md)
  The sort direction used in a recommendation sorting specification.
- [object RecommendationFilterCondition](recommendationfiltercondition.md)
  A single filter condition used in a recommendation query request to narrow results.
- [type RecommendationFilterOperator](recommendationfilteroperator.md)
  The comparison operator applied in a recommendation filter condition.
- [type RecommendationStatus](recommendationstatus.md)
  The operational status of a recommendation record, independent of its lifecycle state.
- [type RecommendationCategory](recommendationcategory.md)
  Enumeration that categorizes a recommendation by optimization area and origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationstate)*