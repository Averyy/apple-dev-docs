# KeywordUpdateBulkResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response from a bulk Keyword update request, containing results for each item.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object KeywordUpdateBulkResponse
```

#### Discussion

The bulk keyword update endpoint returns `KeywordUpdateBulkResponse` as its response envelope. The response populates `error` only when the system rejects the overall request before processing any items.

##### Example

```json
{
  "result": [
    {
      "correlationId": 0,
      "operation": "UPDATE",
      "success": true,
      "result": {
        "id": 888999000,
        "adAccountId": 123456789,
        "campaignId": 444555666,
        "adGroupId": 555666777,
        "text": "photo editor",
        "matchType": "EXACT",
        "bid": {
          "amount": "3.00",
          "currency": "USD"
        },
        "status": "ENABLED",
        "displayStatus": "RUNNING",
        "deleted": false,
        "creationTime": "2025-06-01T10:00:00.000",
        "modificationTime": "2025-06-15T09:00:00.000"
      }
    },
    {
      "correlationId": 1,
      "operation": "UPDATE",
      "success": false,
      "result": null,
      "error": {
        "code": "INVALID_BID",
        "message": "Bid amount is below the minimum allowed value.",
        "details": []
      }
    }
  ]
}
```

## Properties

- `result` ([BulkItemResultKeyword]): Array of per-item keyword update results, one entry per item in the original request. Each entry includes `correlationId`, `operation`, `success`, and on success the full updated `Keyword` entity. See [`BulkItemResultKeyword`](bulkitemresultkeyword.md). Read-only.
- `error` (Error): See [`Error`](error.md). Read-only.

## See Also

- [object BaseBulkRequest](basebulkrequest.md)
  Base type for all bulk operation requests.
- [object BulkOperationRequest](bulkoperationrequest.md)
  Container for a bulk operation request.
- [object BulkItemResult](bulkitemresult.md)
  The base result envelope for a single item in a bulk operation response.
- [object BulkItemResultKeyword](bulkitemresultkeyword.md)
  A bulk operation result item that includes the affected Keyword entity.
- [object BulkItemResultNegativeKeyword](bulkitemresultnegativekeyword.md)
  A bulk operation result item that includes the affected NegativeKeyword entity.
- [object BulkResponse](bulkresponse.md)
  The generic response envelope returned by all bulk operations.
- [object KeywordCreateBulkRequest](keywordcreatebulkrequest.md)
  A bulk request to create multiple Keyword objects.
- [object KeywordCreateBulkResponse](keywordcreatebulkresponse.md)
  The response from a bulk Keyword creation request, containing results for each item.
- [object KeywordUpdateBulkRequest](keywordupdatebulkrequest.md)
  A bulk request to update multiple Keyword objects.
- [object NegativeKeywordCreateBulkRequest](negativekeywordcreatebulkrequest.md)
  A bulk request to create multiple negative keywords.
- [object NegativeKeywordCreateBulkResponse](negativekeywordcreatebulkresponse.md)
  The response from a bulk negative keyword creation request, containing results for each item.
- [object NegativeKeywordUpdateBulkRequest](negativekeywordupdatebulkrequest.md)
  A bulk request to update multiple negative keywords.
- [object NegativeKeywordUpdateBulkResponse](negativekeywordupdatebulkresponse.md)
  The response from a bulk negative keyword update request, containing results for each item.
- [object BulkKeywordCreate](bulkkeywordcreate.md)
  The `data` payload for a single keyword-create item within a bulk create request.
- [object BulkKeywordUpdate](bulkkeywordupdate.md)
  The payload for a single keyword-update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordupdatebulkresponse)*