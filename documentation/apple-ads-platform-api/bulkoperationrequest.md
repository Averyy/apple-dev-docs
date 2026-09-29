# BulkOperationRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Container for a bulk operation request.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object BulkOperationRequest
```

#### Discussion

The `BulkOperationRequest` object is the generic request container for bulk create, update, and delete operations. It extends `BaseBulkRequest` and adds an `items` array.

##### Example

```json
{
  "allowPartialSuccess": true,
  "items": [
    {
      "correlationId": 123456789
    },
    {
      "correlationId": 987654321
    }
  ]
}
```

## Properties

- `allowPartialSuccess` (boolean): If `true`, the request succeeds even if some items fail. Failed items return per-item errors. If `false` (the default), any single failure rejects the entire batch and populates the top-level `error`. Inherited from `BaseBulkRequest`.
- `items` ([BulkOperationRequestItem]): Array of operation items. Each item carries a `correlationId` (integer) for correlating with its result in `BulkResponse`.

## See Also

- [object BaseBulkRequest](basebulkrequest.md)
  Base type for all bulk operation requests.
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
- [object KeywordDeleteBulkRequest](keyworddeletebulkrequest.md)
  A bulk request to delete multiple Keyword objects by their identifiers.
- [object KeywordDeleteBulkResponse](keyworddeletebulkresponse.md)
  The response from a bulk Keyword deletion request.
- [object KeywordUpdateBulkRequest](keywordupdatebulkrequest.md)
  A bulk request to update multiple Keyword objects.
- [object KeywordUpdateBulkResponse](keywordupdatebulkresponse.md)
  The response from a bulk Keyword update request, containing results for each item.
- [object NegativeKeywordCreateBulkRequest](negativekeywordcreatebulkrequest.md)
  A bulk request to create multiple negative keywords.
- [object NegativeKeywordCreateBulkResponse](negativekeywordcreatebulkresponse.md)
  The response from a bulk negative keyword creation request, containing results for each item.
- [object NegativeKeywordDeleteBulkRequest](negativekeyworddeletebulkrequest.md)
  A bulk request to delete multiple negative keywords by their identifiers.
- [object NegativeKeywordDeleteBulkResponse](negativekeyworddeletebulkresponse.md)
  The response from a bulk negative keyword deletion request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkoperationrequest)*