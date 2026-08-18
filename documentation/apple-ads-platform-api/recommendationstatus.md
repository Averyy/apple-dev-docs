# RecommendationStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The operational status of a recommendation record, independent of its lifecycle state.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string RecommendationStatus
```

#### Discussion

`RecommendationStatus` reflects the system-level status of the recommendation record itself, in contrast to [`RecommendationState`](recommendationstate.md) which tracks the advertiser’s response. In most workflows `state` is the relevant field. `status` primarily serves internal record management.

A recommendation can be `ENABLED` while in `APPLIED` or `DISMISSED` state. The status reflects the record’s persistence in the system, not its actionability.

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
- [type RecommendationState](recommendationstate.md)
  The lifecycle state of a recommendation, indicating whether it is available to act on or has already been accepted or rejected.
- [type RecommendationCategory](recommendationcategory.md)
  Enumeration that categorizes a recommendation by optimization area and origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationstatus)*