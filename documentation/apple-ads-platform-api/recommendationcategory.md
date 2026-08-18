# RecommendationCategory

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Enumeration that categorizes a recommendation by optimization area and origin.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string RecommendationCategory
```

#### Discussion

> **Note**: The `KEYWORD`/`SKEYWORD` and `BID`/`SBID` categories are defined in this enum, but this API version doesn’t expose dedicated query, apply, or dismiss endpoints for keyword or bid recommendations. Only daily budget (`DAILYCAP`) and Target CPA (`TCPA`) recommendations have corresponding endpoints. See [`Recommendations Endpoints`](recommendations-endpoints.md) for the available endpoints.

The `recommendationType` field appears on every recommendation read object and always holds one specific category value. For example, [`TargetCpaRecommendation`](targetcparecommendation.md) always carries `TCPA` and [`DailyCapRecommendation`](dailycaprecommendation.md) always carries `DAILYCAP`. Apply and dismiss request bodies do not include a `recommendationType` field.

Each optimization area has a merged category and a system (`S`) category. To retrieve all recommendations for that area regardless of origin, use the merged category (no prefix) in query filters. The system prefix variant allows filtering to only algorithm-generated recommendations.

When filtering a query for recommendations, always use the merged category (no prefix) unless you specifically need to distinguish system-generated recommendations.

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
- [type RecommendationStatus](recommendationstatus.md)
  The operational status of a recommendation record, independent of its lifecycle state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationcategory)*