# QueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Response wrapper for paginated query results.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object QueryResponse
```

#### Discussion

`QueryResponse` is the generic paginated response envelope returned by query endpoints.

This wrapper is the base type for all query responses. Specific entity query responses extend this pattern with a typed `result` array.

##### Example

```json
{
  "result": [
    {
      "id": "123456789",
      "name": "AwayFinder Campaign"
    }
  ],
  "pagination": {
    "totalCount": 1,
    "offset": 0,
    "pageSize": 20
  }
}
```

## Topics

### Dictionaries
- [object QueryResponse.Result](queryresponse/result-data.dictionary.md)
  The untyped placeholder item shape for the base `QueryResponse` envelope’s `result` array.

## Properties

- `result` ([QueryResponse.Result]): The matching entity records for this query. Read-only.
- `pagination` (QueryPaginationResult): Offset metadata for the result set. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error details if the request failed. Absent on success. See [`Error`](error.md). Read-only.

## See Also

- [object QueryRequest](queryrequest.md)
  The standard request body used across all query endpoints, supporting filters, sorting, pagination, and field selection.
- [object QueryFilter](queryfilter.md)
  A single filter condition in a query request, specifying a field, comparison operator, and one or more values to match against.
- [object QuerySort](querysort.md)
  A sort directive in a query request, specifying a field and direction.
- [object QueryPagination](querypagination.md)
  Controls the page size and starting offset for query results.
- [object QueryPaginationResult](querypaginationresult.md)
  Pagination metadata returned in query responses, including page size, offset, and optional total count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/queryresponse)*