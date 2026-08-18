# QueryRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The standard request body used across all query endpoints, supporting filters, sorting, pagination, and field selection.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object QueryRequest
```

#### Discussion

`QueryRequest` is the standard request body used across all query endpoints in the Apple Ads Platform API.

To filter on fields marked **Filterable** in each entity’s dictionary keys, use `QueryFilter` entries. The query combines multiple filters with logical AND.

##### Example

```json
{
  "filters": [
    {
      "field": "name",
      "operator": "CONTAINS_ANY",
      "value": ["AwayFinder", "AwayFinder Promo"],
      "ignoreCase": true
    }
  ],
  "sorting": [
    {
      "field": "id",
      "order": "DESC"
    }
  ],
  "pagination": {
    "pageSize": 25,
    "offset": 0,
    "fetchTotalCount": true
  }
}
```

## Properties

- `filters` ([QueryFilter]): Filter field conditions. If no filters are in the request, all non-deleted entities within the current ad account scope are returned. Deleted entities are not returned unless specified to be included. See [`QueryFilter`](queryfilter.md).
- `sorting` ([QuerySort]): Sort entities in ascending or descending order. The default behavior is to sort by ID, ascending. See [`QuerySort`](querysort.md).
- `pagination` (QueryPagination): Controls pagination settings for results using offset and size. See [`QueryPagination`](querypagination.md).

## See Also

- [object QueryFilter](queryfilter.md)
  A single filter condition in a query request, specifying a field, comparison operator, and one or more values to match against.
- [object QuerySort](querysort.md)
  A sort directive in a query request, specifying a field and direction.
- [object QueryPagination](querypagination.md)
  Controls the page size and starting offset for query results.
- [object QueryResponse](queryresponse.md)
  Response wrapper for paginated query results.
- [object QueryPaginationResult](querypaginationresult.md)
  Pagination metadata returned in query responses, including page size, offset, and optional total count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/queryrequest)*