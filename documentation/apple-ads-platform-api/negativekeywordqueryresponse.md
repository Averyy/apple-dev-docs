# NegativeKeywordQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a negative keyword query, containing matched results and pagination metadata.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object NegativeKeywordQueryResponse
```

#### Discussion

`NegativeKeywordQueryResponse` is returned by the negative keyword query endpoint and contains the filtered, sorted, and paginated set of `NegativeKeyword` objects matching the request.

To scope results to a specific campaign or ad group, filter by status, or retrieve by ID, use the `QueryRequest` body with `filters`, `sorting`, and `pagination`.

##### Example

```json
{
  "result": [
    {
      "id": 777888999,
      "adAccountId": 123456789,
      "campaignId": 444555666,
      "text": "free app",
      "matchType": "BROAD",
      "status": "ENABLED",
      "deleted": false,
      "creationTime": "2025-01-10T08:00:00.000",
      "modificationTime": "2025-01-10T08:00:00.000"
    },
    {
      "id": 777888997,
      "adAccountId": 123456789,
      "campaignId": 444555666,
      "text": "free trial",
      "matchType": "EXACT",
      "status": "ENABLED",
      "deleted": false,
      "creationTime": "2025-01-09T10:00:00.000",
      "modificationTime": "2025-01-09T10:00:00.000"
    }
  ],
  "pagination": {
    "totalCount": 2,
    "offset": 0,
    "pageSize": 20
  }
}
```

## Properties

- `result` ([NegativeKeyword]): Array of matching `NegativeKeyword` objects. Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the query result, supporting offset-based navigation through large result sets. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error details if the request failed. See [`Error`](error.md). Read-only.

## See Also

- [object NegativeKeyword](negativekeyword.md)
  A keyword exclusion that prevents ads from showing when a search query matches the excluded term.
- [object NegativeKeywordCreate](negativekeywordcreate.md)
  The request body for creating a new negative keyword.
- [object NegativeKeywordUpdate](negativekeywordupdate.md)
  The request body for updating an existing negative keyword.
- [object NegativeKeywordResponse](negativekeywordresponse.md)
  The response object for a negative keyword operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordqueryresponse)*