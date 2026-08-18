# NegativeKeywordResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a negative keyword operation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object NegativeKeywordResponse
```

#### Discussion

`NegativeKeywordResponse` is the single-item response envelope returned by create and update negative keyword operations.

This wrapper follows the same pattern as other single-object response types in the API. Inspect `error` to detect failures before accessing `result`.

##### Example

```json
{
  "result": {
    "id": 777888999,
    "adAccountId": 123456789,
    "campaignId": 444555666,
    "text": "free app",
    "matchType": "BROAD",
    "status": "ENABLED",
    "creationTime": "2025-01-10T08:00:00.000",
    "modificationTime": "2025-01-10T08:00:00.000",
    "deleted": false
  }
}
```

## Properties

- `result` (NegativeKeyword): The affected `NegativeKeyword` object in its post-operation state. Absent if the operation failed. See [`NegativeKeyword`](negativekeyword.md). Read-only.
- `error` (Error): Structured error details if the operation failed. See [`Error`](error.md). Read-only.

## See Also

- [object NegativeKeyword](negativekeyword.md)
  A keyword exclusion that prevents ads from showing when a search query matches the excluded term.
- [object NegativeKeywordCreate](negativekeywordcreate.md)
  The request body for creating a new negative keyword.
- [object NegativeKeywordUpdate](negativekeywordupdate.md)
  The request body for updating an existing negative keyword.
- [object NegativeKeywordQueryResponse](negativekeywordqueryresponse.md)
  The response object for a negative keyword query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordresponse)*