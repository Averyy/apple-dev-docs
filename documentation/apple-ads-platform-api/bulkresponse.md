# BulkResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The generic response envelope returned by all bulk operations.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BulkResponse
```

#### Discussion

`BulkResponse` is the standard response wrapper for bulk create, update, and delete operations. The `result` array is parallel to the `items` array in the corresponding `BulkOperationRequest`: element at index `n` in `result` corresponds to element at index `n` in the request. To correlate results back to their originating request item, use the `correlationId` field on each result entry.

When `allowPartialSuccess` is `true` in the request, individual item failures appear in the `result` array rather than the top-level `error`.

##### Example

```json
{
  "result": [
    {
      "correlationId": 0,
      "operation": "CREATE",
      "success": true
    }
  ]
}
```

## Properties

- `result` (Response.Result): `BulkResponse` inherits `result` as a generic nullable object from the `Response` base schema. The array-of-items typing (e.g., array of `BulkItemResultKeyword`) is defined by typed response subclasses such as `KeywordCreateBulkResponse`, not by `BulkResponse` itself. Each entry contains the operation outcome and, on failure, per-item error details. Read-only.
- `error` (Error): Top-level error if the entire bulk request was rejected before processing. `null` when the request was accepted (even with per-item failures). See [`Error`](error.md). Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkresponse)*