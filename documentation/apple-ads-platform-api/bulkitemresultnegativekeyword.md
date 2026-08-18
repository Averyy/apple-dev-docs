# BulkItemResultNegativeKeyword

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A bulk operation result item that includes the affected NegativeKeyword entity.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BulkItemResultNegativeKeyword
```

#### Discussion

`BulkItemResultNegativeKeyword` extends [`BulkItemResult`](bulkitemresult.md) with a typed `result` field containing the `NegativeKeyword` object the operation created or updated. This type appears as array items in `NegativeKeywordCreateBulkResponse` and `NegativeKeywordUpdateBulkResponse`.

On success, `result` contains the full `NegativeKeyword` entity as it exists after the operation. On failure, `success` is `false` and `error` carries per-item details.

##### Example

```json
{
  "correlationId": 1,
  "operation": "CREATE",
  "success": true,
  "result": {
    "id": 555666777,
    "adAccountId": 123456789,
    "campaignId": 987654321,
    "adGroupId": null,
    "text": "AwayFinder competitor app",
    "matchType": "EXACT",
    "status": "ENABLED",
    "creationTime": "2025-01-10T08:00:00.000",
    "modificationTime": "2025-01-10T08:00:00.000",
    "deleted": false
  }
}
```

## Properties

- `correlationId` (int64): Client-supplied integer from the corresponding request item. Read-only.
- `operation` (string): The operation performed: `CREATE` or `UPDATE`. Read-only.
- `success` (boolean): Whether this item operation succeeded. Read-only.
- `result` (NegativeKeyword): The NegativeKeyword entity affected by this operation. Null when `success` is `false`. See [`NegativeKeyword`](negativekeyword.md). Read-only.
- `error` (Error): Per-item error details when this item failed. Null on success. See [`Error`](error.md). Read-only.

## See Also

- [object BaseBulkRequest](basebulkrequest.md)
  Base type for all bulk operation requests.
- [object BulkOperationRequest](bulkoperationrequest.md)
  Container for a bulk operation request.
- [object BulkItemResult](bulkitemresult.md)
  The base result envelope for a single item in a bulk operation response.
- [object BulkItemResultKeyword](bulkitemresultkeyword.md)
  A bulk operation result item that includes the affected Keyword entity.
- [object BulkResponse](bulkresponse.md)
  The generic response envelope returned by all bulk operations.
- [object KeywordCreateBulkRequest](keywordcreatebulkrequest.md)
  A bulk request to create multiple Keyword objects.
- [object KeywordCreateBulkResponse](keywordcreatebulkresponse.md)
  The response from a bulk Keyword creation request, containing results for each item.
- [object KeywordUpdateBulkRequest](keywordupdatebulkrequest.md)
  A bulk request to update multiple Keyword objects.
- [object KeywordUpdateBulkResponse](keywordupdatebulkresponse.md)
  The response from a bulk Keyword update request, containing results for each item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkitemresultnegativekeyword)*