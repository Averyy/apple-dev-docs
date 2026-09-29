# BulkOperationRequestItem

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Base item wrapper for bulk operation requests, carrying only the client-supplied `correlationId`.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object BulkOperationRequestItem
```

## Properties

- `correlationId` (int64): Client-supplied identifier used to correlate this request item with its corresponding result in the response.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkoperationrequestitem)*