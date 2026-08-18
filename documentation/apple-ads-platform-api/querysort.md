# QuerySort

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A sort directive in a query request, specifying a field and direction.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object QuerySort
```

#### Discussion

`QuerySort` defines one sort directive in a `QueryRequest.sorting` array. The query applies multiple `QuerySort` entries in order: the first entry is the primary sort, subsequent entries are tiebreakers.

##### Example

```json
{
  "field": "name",
  "order": "ASC"
}
```

## Properties

- `field` (string): The name of the field to sort on (e.g., id, name).
- `order` (QuerySortOrder): The sort direction for the specified field. Valid values: `ASC`, `DESC`.

## See Also

- [object QueryRequest](queryrequest.md)
  The standard request body used across all query endpoints, supporting filters, sorting, pagination, and field selection.
- [object QueryFilter](queryfilter.md)
  A single filter condition in a query request, specifying a field, comparison operator, and one or more values to match against.
- [object QueryPagination](querypagination.md)
  Controls the page size and starting offset for query results.
- [object QueryResponse](queryresponse.md)
  Response wrapper for paginated query results.
- [object QueryPaginationResult](querypaginationresult.md)
  Pagination metadata returned in query responses, including page size, offset, and optional total count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/querysort)*