# BulkItemResult

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The base result envelope for a single item in a bulk operation response.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BulkItemResult
```

#### Discussion

`BulkItemResult` is the shared result wrapper that the API returns for each item in a bulk create, update, or delete response. It extends the standard `Response` envelope with per-item operation metadata. All keyword and negative keyword bulk response types extend this schema by adding a typed `result` field.

When `allowPartialSuccess` is `true` in the request, inspect `success` on each entry individually. A `false` value indicates that the specific item failed.

##### Example

```json
{
  "correlationId": 2,
  "operation": "UPDATE",
  "success": false,
  "error": {
    "code": "INVALID_FIELD",
    "message": "bid.amount must be greater than 0",
    "details": []
  }
}
```

## Properties

- `correlationId` (int64): The client-supplied integer from the corresponding request item. Use this to map each response entry back to its input. Read-only.
- `operation` (string): The operation performed on this item: `CREATE`, `UPDATE`, or `DELETE`. Read-only.
- `success` (boolean): Whether this individual item operation succeeded. Read-only.
- `error` (Error): Per-item error details when this item failed. Null on success. See [`Error`](error.md). Read-only.
- `result` (Response.Result)

## See Also

- [object BaseBulkRequest](basebulkrequest.md)
  Base type for all bulk operation requests.
- [object BulkOperationRequest](bulkoperationrequest.md)
  Container for a bulk operation request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkitemresult)*