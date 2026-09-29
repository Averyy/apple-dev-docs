# NegativeKeywordCreateBulkRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A bulk request to create multiple negative keywords.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object NegativeKeywordCreateBulkRequest
```

#### Discussion

The `NegativeKeywordCreateBulkRequest` object allows creating multiple negative keywords in a single API call.

##### Example

```json
{
  "allowPartialSuccess": true,
  "items": [
    {
      "correlationId": 123456789,
      "data": {
        "campaignId": 987654321,
        "adGroupId": 555666777,
        "text": "free AwayFinder",
        "matchType": "BROAD",
        "status": "ENABLED"
      }
    },
    {
      "correlationId": 123456790,
      "data": {
        "campaignId": 987654321,
        "adGroupId": null,
        "text": "AwayFinder discount",
        "matchType": "EXACT",
        "status": "ENABLED"
      }
    }
  ]
}
```

## Properties

- `allowPartialSuccess` (boolean): If `true`, allows some operations in the batch to succeed. Other operations can still fail without blocking the successful ones.
- `items` ([NegativeKeywordCreateBulkRequestItem]): Array of bulk item objects to create. Each item has the shape `{ correlationId: int64, data: BulkNegativeKeywordCreate }`.

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
- [object NegativeKeywordCreateBulkResponse](negativekeywordcreatebulkresponse.md)
  The response from a bulk negative keyword creation request, containing results for each item.
- [object NegativeKeywordDeleteBulkRequest](negativekeyworddeletebulkrequest.md)
  A bulk request to delete multiple negative keywords by their identifiers.
- [object NegativeKeywordDeleteBulkResponse](negativekeyworddeletebulkresponse.md)
  The response from a bulk negative keyword deletion request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordcreatebulkrequest)*