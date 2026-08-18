# FilterCondition

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single filter condition used in a recommendation query request to narrow results.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationFilterCondition
```

#### Discussion

`FilterCondition` is the building block of query filters in the Recommendations API. The API combines multiple conditions in the `filters` array with AND logic. All conditions must match for a recommendation to appear in results.

Every query request requires two filters:

| Field | Operator | Description |
| --- | --- | --- |
| `promotedObjectId` | `EQUALS` | The ID of the promoted object. Interpreted in combination with `promotedObjectType`. |
| `promotedObjectType` | `EQUALS` | The type of promoted object, for example `APPSTORE_APP`. |

Which operators are valid for a given `field` depends on that field’s underlying type.

| Field Type | Supported Operators |
| --- | --- |
| String | `EQUALS`, `NOT_EQUALS`, `IN`, `STARTS_WITH`, `ENDS_WITH`, `LIKE` |
| Numeric | `EQUALS`, `NOT_EQUALS`, `IN`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO`, `BETWEEN` |
| Date | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` |
| Enum | `EQUALS`, `NOT_EQUALS`, `IN` |
| List | `CONTAINS_ANY`, `CONTAINS_ALL` |

Always pass `value` as an array.

##### Example

```json
{
  "field": "state",
  "operator": "EQUALS",
  "value": [
    "AVAILABLE"
  ],
  "ignoreCase": false
}
```

## Properties

- `field` (string) *(required)*: The name of the field to filter on. Must match a field name on the recommendation object being queried, for example `state`, `promotedObjectId`, `campaignId`.
- `operator` (RecommendationFilterOperator) *(required)*: The comparison operator to apply. See [`FilterOperator`](recommendationfilteroperator.md).
- `value` ([string]) *(required)*: An array of one or more filter values. Always supplied as an array, even when filtering with a single value, for example `value: [AVAILABLE]`.
- `ignoreCase` (boolean): When `true`, string matching is case-insensitive. Defaults to `false`.

## See Also

- [object RecommendationQueryRequest](recommendationqueryrequest.md)
  The structured request body for all recommendation query endpoints.
- [object RecommendationQueryRequestPagination](recommendationqueryrequestpagination.md)
  Pagination parameters for a recommendation query request.
- [object RecommendationSorting](recommendationsorting.md)
  A sort specification used in a recommendation query request to order results.
- [type RecommendationSortingOrder](recommendationsortingorder.md)
  The sort direction used in a recommendation sorting specification.
- [type RecommendationFilterOperator](recommendationfilteroperator.md)
  The comparison operator applied in a recommendation filter condition.
- [type RecommendationState](recommendationstate.md)
  The lifecycle state of a recommendation, indicating whether it is available to act on or has already been accepted or rejected.
- [type RecommendationStatus](recommendationstatus.md)
  The operational status of a recommendation record, independent of its lifecycle state.
- [type RecommendationCategory](recommendationcategory.md)
  Enumeration that categorizes a recommendation by optimization area and origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationfiltercondition)*