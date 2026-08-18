# FilterOperator

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The comparison operator applied in a recommendation filter condition.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string RecommendationFilterOperator
```

#### Discussion

Use these operators in the `operator` field of a [`FilterCondition`](recommendationfiltercondition.md). Not all operators are valid for all field types. Applying an incompatible operator returns a 400 error with a validation detail identifying the invalid condition.

For example, here’s a `BETWEEN` filter on a campaign ID range:

```json
{
  "field": "campaignId",
  "operator": "BETWEEN",
  "value": [
    "10000",
    "20000"
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
- [type RecommendationState](recommendationstate.md)
  The lifecycle state of a recommendation, indicating whether it is available to act on or has already been accepted or rejected.
- [type RecommendationStatus](recommendationstatus.md)
  The operational status of a recommendation record, independent of its lifecycle state.
- [type RecommendationCategory](recommendationcategory.md)
  Enumeration that categorizes a recommendation by optimization area and origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationfilteroperator)*