# QueryPaginationResult

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Pagination metadata returned in query responses, including page size, offset, and optional total count.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object QueryPaginationResult
```

#### Discussion

`QueryPaginationResult` is returned in the `pagination` field of query responses. It echoes the `pageSize` and `offset` from the request and provides `totalCount` when requested. To calculate the total number of pages, use `totalCount` with `pageSize`.

##### Example

```json
{
  "pageSize": 20,
  "offset": 0,
  "totalCount": 137
}
```

## Properties

- `pageSize` (int32): The page size for this response.
- `offset` (int32): The offset position for this response page.
- `totalCount` (int64): The total number of results matching the query. Only populated when `fetchTotalCount` is `true` in the request.

## See Also

- [object QueryRequest](queryrequest.md)
  The standard request body used across all query endpoints, supporting filters, sorting, pagination, and field selection.
- [object QueryFilter](queryfilter.md)
  A single filter condition in a query request, specifying a field, comparison operator, and one or more values to match against.
- [object QuerySort](querysort.md)
  A sort directive in a query request, specifying a field and direction.
- [object QueryPagination](querypagination.md)
  Controls the page size and starting offset for query results.
- [object QueryResponse](queryresponse.md)
  Response wrapper for paginated query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/querypaginationresult)*