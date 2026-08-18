# QueryPagination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Controls the page size and starting offset for query results.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object QueryPagination
```

#### Discussion

`QueryPagination` controls the page size and starting offset for query results.

##### Example

```json
{
  "pageSize": 25,
  "offset": 50,
  "fetchTotalCount": true
}
```

## Properties

- `pageSize` (int32): The number of items per page.
- `offset` (int32): The starting position for pagination, zero-based.
- `fetchTotalCount` (boolean): Whether to include the total count in the pagination response. Set to `true` to include the total result count in the `QueryPaginationResult` response.

## See Also

- [object QueryRequest](queryrequest.md)
  The standard request body used across all query endpoints, supporting filters, sorting, pagination, and field selection.
- [object QueryFilter](queryfilter.md)
  A single filter condition in a query request, specifying a field, comparison operator, and one or more values to match against.
- [object QuerySort](querysort.md)
  A sort directive in a query request, specifying a field and direction.
- [object QueryResponse](queryresponse.md)
  Response wrapper for paginated query results.
- [object QueryPaginationResult](querypaginationresult.md)
  Pagination metadata returned in query responses, including page size, offset, and optional total count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/querypagination)*