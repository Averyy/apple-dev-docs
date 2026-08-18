# Recommendations Query and Filter Objects

**Framework**: Apple Ads Platform API

Query, filter, pagination, and sorting objects for recommendation requests.

**Availability**:
- apple-ads-platform-api 1.0+

## Topics

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
- [type RecommendationStatus](recommendationstatus.md)
  The operational status of a recommendation record, independent of its lifecycle state.
- [type RecommendationCategory](recommendationcategory.md)
  Enumeration that categorizes a recommendation by optimization area and origin.

## See Also

- [Recommendations Endpoints](recommendations-endpoints.md)
  Endpoints for querying, applying, and dismissing budget and Target CPA recommendations.
- [Recommendations Data Objects](recommendations-data-objects.md)
  Request and response objects for recommendation endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendations-query-filter-objects)*