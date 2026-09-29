# Bulk Data Objects

**Framework**: Apple Ads Platform API

Use these objects to build bulk keyword and negative keyword requests and read their responses.

**Availability**:
- Apple Ads Platform API 1.0+

## Topics

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
- [object NegativeKeywordDeleteBulkResponse](negativekeyworddeletebulkresponse.md)
  The response from a bulk negative keyword deletion request.
- [object NegativeKeywordUpdateBulkRequest](negativekeywordupdatebulkrequest.md)
  A bulk request to update multiple negative keywords.
- [object NegativeKeywordUpdateBulkResponse](negativekeywordupdatebulkresponse.md)
  The response from a bulk negative keyword update request, containing results for each item.
- [object BulkEntityDeleteIdLong](bulkentitydeleteidlong.md)
  The `data` payload for a bulk delete item, containing the identifier of the entity to remove.
- [object BulkKeywordCreate](bulkkeywordcreate.md)
  The `data` payload for a single keyword-create item within a bulk create request.
- [object BulkKeywordUpdate](bulkkeywordupdate.md)
  The payload for a single keyword-update.
- [object BulkNegativeKeywordCreate](bulknegativekeywordcreate.md)
  The `data` payload for a single negative-keyword-create item within a bulk create request.
- [object BulkNegativeKeywordUpdate](bulknegativekeywordupdate.md)
  The `data` payload for a single negative-keyword-update item within a bulk update request, identifying the record by `id`.
- [object BulkOperationRequestItem](bulkoperationrequestitem.md)
  Base item wrapper for bulk operation requests, carrying only the client-supplied `correlationId`.
- [object KeywordCreateBulkRequestItem](keywordcreatebulkrequestitem.md)
  A single item in a keyword bulk-create request.
- [object KeywordDeleteBulkRequestItem](keyworddeletebulkrequestitem.md)
  A single item in a keyword bulk-delete request.
- [object KeywordUpdateBulkRequestItem](keywordupdatebulkrequestitem.md)
  A single item in a keyword bulk-update request.
- [object NegativeKeywordCreateBulkRequestItem](negativekeywordcreatebulkrequestitem.md)
  A single item in a negative-keyword bulk-create request.
- [object NegativeKeywordDeleteBulkRequestItem](negativekeyworddeletebulkrequestitem.md)
  A single item in a negative-keyword bulk-delete request.
- [object NegativeKeywordUpdateBulkRequestItem](negativekeywordupdatebulkrequestitem.md)
  A single item in a negative-keyword bulk-update request.

## See Also

- [Bulk Operations Endpoints](bulk-operations-endpoints.md)
  Create, update, and delete keywords and negative keywords in bulk through these endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulk-data-objects)*