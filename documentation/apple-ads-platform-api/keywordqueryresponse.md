# KeywordQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a Keyword query, containing matched results and pagination metadata.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object KeywordQueryResponse
```

#### Discussion

`KeywordQueryResponse` is returned by the keyword query endpoint and contains the filtered, sorted, and paginated set of `Keyword` objects matching the request.

To narrow results to a specific ad group, campaign, or set of keyword IDs, use the `QueryRequest` body with `filters`, `sorting`, and `pagination`. Multiple filter conditions are combined with AND logic.

##### Example

```json
{
  "result": [
    {
      "id": 888999001,
      "adAccountId": 123456789,
      "campaignId": 987654321,
      "adGroupId": 555666777,
      "text": "awayfinder travel app",
      "matchType": "EXACT",
      "bid": {
        "amount": "2.50",
        "currency": "USD"
      },
      "status": "ENABLED",
      "displayStatus": "RUNNING",
      "creationTime": "2025-01-10T08:00:00.000",
      "modificationTime": "2025-01-12T09:30:00.000",
      "deleted": false
    },
    {
      "id": 888999000,
      "adAccountId": 123456789,
      "campaignId": 987654321,
      "adGroupId": 555666777,
      "text": "photo editor",
      "matchType": "BROAD",
      "bid": {
        "amount": "1.50",
        "currency": "USD"
      },
      "status": "PAUSED",
      "displayStatus": "PAUSED",
      "creationTime": "2025-01-10T08:05:00.000",
      "modificationTime": "2025-03-01T14:00:00.000",
      "deleted": false
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20,
    "totalCount": 2
  }
}
```

## Properties

- `result` ([Keyword]): Array of matching `Keyword` objects. Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the query result, indicating total count and offset for offset-based navigation through large result sets. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error details if the request failed. See [`Error`](error.md). Read-only.

## See Also

- [object Keyword](keyword.md)
  The targeting unit that connects a user’s App Store search query to an ad group’s ads.
- [object KeywordCreate](keywordcreate.md)
  The request body for creating a new Keyword object.
- [object KeywordUpdate](keywordupdate.md)
  The request body for updating an existing Keyword object.
- [object KeywordResponse](keywordresponse.md)
  The response object for a Keyword operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordqueryresponse)*