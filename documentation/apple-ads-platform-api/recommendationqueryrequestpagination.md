# QueryRequestPagination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Pagination parameters for a recommendation query request.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationQueryRequestPagination
```

#### Discussion

`QueryRequestPagination` controls pagination in recommendation query requests. The response includes a `pagination` envelope with `offset`, `pageSize`, and `totalCount` indicating how many records matched the filters in total.

To retrieve the next page, increment `offset` by `pageSize`:

```json
{
  "offset": 20,
  "pageSize": 20
}
```

Continue until `offset + pageSize >= totalCount`. New recommendations may appear or disappear between pages because the result set is not snapshotted.

## Properties

- `offset` (int32): The zero-based index of the first result to return. Use with `pageSize` to page through large result sets. Defaults to `0`.
- `pageSize` (int32): The maximum number of results to return per page. Minimum `1`, maximum `1000`. Defaults to `20`.

## See Also

- [object RecommendationQueryRequest](recommendationqueryrequest.md)
  The structured request body for all recommendation query endpoints.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationqueryrequestpagination)*