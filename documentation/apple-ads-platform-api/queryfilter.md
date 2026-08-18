# QueryFilter

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single filter condition in a query request, specifying a field, comparison operator, and one or more values to match against.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object QueryFilter
```

#### Discussion

`QueryFilter` defines one filter condition in a `QueryRequest.filters` array. Not all endpoints support all operators. Refer to each entity’s Properties section for the supported operators per field.

##### Example

```json
{
  "field": "name",
  "operator": "CONTAINS_ANY",
  "value": ["AwayFinder", "AwayFinder Promo"],
  "ignoreCase": true
}
```

## Topics

### Dictionaries
- [object QueryFilter.Value](queryfilter/value-data.dictionary.md)
  The comparison value or values for a `QueryFilter` condition.

## Properties

- `field` (string): The name of the field to filter on (e.g., id, name).
- `operator` (QueryFilterOperator): Comparison operator. Supported operators (may vary by endpoint): `BETWEEN`, `CONTAINS_ALL`, `CONTAINS_ANY`, `ENDS_WITH`, `EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `IN`, `IS_NOT_NULL`, `IS_NULL`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO`, `LIKE`, `NOT_CONTAINS_ALL`, `NOT_CONTAINS_ANY`, `NOT_EQUALS`, `NOT_IN`, `NOT_LIKE`, `STARTS_WITH`. See [`QueryFilterOperator`](queryfilteroperator.md).
- `value` (QueryFilter.Value): One or more filter conditions applied to the result set. Pass an array for operators that accept multiple values (`IN`, `NOT_IN`, `CONTAINS_ANY`, `CONTAINS_ALL`, `NOT_CONTAINS_ANY`, `NOT_CONTAINS_ALL`), an array of exactly two values ordered as `[minimum, maximum]` for `BETWEEN`, a scalar for operators that accept a single value (`EQUALS`, `STARTS_WITH`), or omit entirely for the null-check operators `IS_NULL` and `IS_NOT_NULL`.
- `ignoreCase` (boolean): Whether to perform case-insensitive filtering.

## See Also

- [object QueryRequest](queryrequest.md)
  The standard request body used across all query endpoints, supporting filters, sorting, pagination, and field selection.
- [object QuerySort](querysort.md)
  A sort directive in a query request, specifying a field and direction.
- [object QueryPagination](querypagination.md)
  Controls the page size and starting offset for query results.
- [object QueryResponse](queryresponse.md)
  Response wrapper for paginated query results.
- [object QueryPaginationResult](querypaginationresult.md)
  Pagination metadata returned in query responses, including page size, offset, and optional total count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/queryfilter)*