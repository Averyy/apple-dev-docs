# Recommendations Query and Filter Objects

**Framework**: Apple Ads Platform API

Filter, sort, and paginate recommendation queries by status, state, and category.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Every recommendation query request builds on [`RecommendationQueryRequest`](recommendationqueryrequest.md), which requires `promotedObjectId` and `promotedObjectType` filters. Add [`FilterCondition`](recommendationfiltercondition.md) entries to narrow results, and use [`Sorting`](recommendationsorting.md) and [`QueryRequestPagination`](recommendationqueryrequestpagination.md) to order and page them. The suggestion query endpoints reuse these objects.

For the calls that use them, see [`Recommendations Endpoints`](recommendations-endpoints.md) and [`Suggestions Endpoints`](suggestions-endpoints.md).

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
  The lifecycle state of a recommendation, indicating whether it’s available to act on or has already been accepted or rejected.
- [type RecommendationStatus](recommendationstatus.md)
  The operational status of a recommendation record, independent of its lifecycle state.
- [type RecommendationCategory](recommendationcategory.md)
  Enumeration that categorizes a recommendation by optimization area and origin.

## See Also

- [Recommendations Endpoints](recommendations-endpoints.md)
  Query budget and Target CPA recommendations, then apply or dismiss them to adjust campaign spend and bids.
- [Recommendations Data Objects](recommendations-data-objects.md)
  Read budget and Target CPA recommendations and their history, and build the requests that apply them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendations-query-filter-objects)*