# BulkKeywordCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The `data` payload for a single keyword-create item within a bulk create request.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BulkKeywordCreate
```

## Topics

### Dictionaries
- [object BulkKeywordCreate.Bid](bulkkeywordcreate/bid-data.dictionary.md)
  The keyword-level bid amount for a bulk keyword create item.
### Type Aliases
- [type BulkKeywordCreate.MatchType](bulkkeywordcreate/matchtype-data.typealias.md)
  The keyword’s match type for a bulk keyword create item.
- [type BulkKeywordCreate.Status](bulkkeywordcreate/status-data.typealias.md)
  The keyword’s status for a bulk keyword create item.

## Properties

- `adGroupId` (int64) *(required)*: The ad group in which the keyword is created.
- `text` (string) *(required)*: The keyword text. Minimum length of 1.
- `matchType` (BulkKeywordCreate.MatchType): The keyword’s match type. See [`KeywordMatchType`](keywordmatchtype.md).
- `bid` (BulkKeywordCreate.Bid): The keyword-level bid amount. Nullable. See [`Money`](money.md).
- `status` (BulkKeywordCreate.Status): The keyword’s status. See [`KeywordStatus`](keywordstatus.md).

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
- [object BulkKeywordUpdate](bulkkeywordupdate.md)
  The payload for a single keyword-update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkkeywordcreate)*