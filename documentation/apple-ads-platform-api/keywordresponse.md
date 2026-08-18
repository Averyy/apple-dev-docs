# KeywordResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a Keyword operation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object KeywordResponse
```

#### Discussion

`KeywordResponse` is the single-item response envelope returned by create and update keyword operations.

Check the `error` field to detect per-item failures, especially in bulk contexts where some items may succeed while others fail.

##### Example

```json
{
  "result": {
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
    "id": 111222333,
    "creationTime": "2025-01-10T08:00:00.000",
    "modificationTime": "2025-01-12T09:30:00.000",
    "deleted": false,
    "displayStatus": "RUNNING"
  }
}
```

## Properties

- `result` (Keyword): The affected `Keyword` object reflecting its post-operation state. Absent if the operation failed. See [`Keyword`](keyword.md). Read-only.
- `error` (Error): Structured error details if the operation failed. See [`Error`](error.md). Read-only.

## See Also

- [object Keyword](keyword.md)
  The targeting unit that connects a user’s App Store search query to an ad group’s ads.
- [object KeywordCreate](keywordcreate.md)
  The request body for creating a new Keyword object.
- [object KeywordUpdate](keywordupdate.md)
  The request body for updating an existing Keyword object.
- [object KeywordQueryResponse](keywordqueryresponse.md)
  The response object for a Keyword query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordresponse)*