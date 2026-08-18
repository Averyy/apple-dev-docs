# Sorting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A sort specification used in a recommendation query request to order results.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationSorting
```

#### Discussion

`Sorting` specifies one sort dimension in the `sorting` array of a QueryRequest. The `sorting` array supports multiple entries, which the system applies in order. The first entry is the primary sort, the second is the tiebreaker, and so on.

##### Example

```json
{
  "field": "creationTime",
  "order": "DESC"
}
```

## Properties

- `field` (string) *(required)*: The name of the field to sort by. Use `creationTime` to sort by when the recommendation was created, or `expirationTime` to sort by recommendation expiry and act on time-sensitive items first.
- `order` (RecommendationSortingOrder): The sort direction. Defaults to `ASC` when omitted. See [`SortingOrder`](recommendationsortingorder.md).

## See Also

- [object RecommendationQueryRequest](recommendationqueryrequest.md)
  The structured request body for all recommendation query endpoints.
- [object RecommendationQueryRequestPagination](recommendationqueryrequestpagination.md)
  Pagination parameters for a recommendation query request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationsorting)*