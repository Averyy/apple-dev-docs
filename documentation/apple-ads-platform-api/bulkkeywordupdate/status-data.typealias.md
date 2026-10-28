# BulkKeywordUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The updated keyword status for a bulk keyword update item.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BulkKeywordUpdate.Status
```

## Possible Values

- `ENABLED`: Keyword is active and eligible to serve.
- `PAUSED`: Keyword is paused and will not serve.

## Discussion

Include this field within an item’s `data` to enable or pause the keyword as part of the same bulk update request.

### Example

```json
{
  "status": "PAUSED"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkkeywordupdate/status-data.typealias)*