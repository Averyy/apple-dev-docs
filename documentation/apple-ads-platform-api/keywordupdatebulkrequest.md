# KeywordUpdateBulkRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A bulk request to update multiple Keyword objects.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object KeywordUpdateBulkRequest
```

#### Discussion

The `KeywordUpdateBulkRequest` object allows updating multiple keywords in a single API call.

##### Example

```json
{
  "allowPartialSuccess": true,
  "items": [
    {
      "correlationId": 123456789,
      "data": {
        "id": 555666777,
        "bid": {
          "amount": "2.50",
          "currency": "USD"
        },
        "status": "ENABLED"
      }
    },
    {
      "correlationId": 987654321,
      "data": {
        "id": 111222333,
        "bid": {
          "amount": "1.75",
          "currency": "USD"
        },
        "status": "PAUSED"
      }
    }
  ]
}
```

## Properties

- `allowPartialSuccess` (boolean): If `true`, allows some operations in the batch to succeed. Other operations can still fail without blocking the successful ones.
- `items` ([KeywordUpdateBulkRequestItem]): Array of bulk item objects to update. Each item has the shape `{ correlationId: int64, data: BulkKeywordUpdate }`. The `id` field is required in `BulkKeywordUpdate`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordupdatebulkrequest)*