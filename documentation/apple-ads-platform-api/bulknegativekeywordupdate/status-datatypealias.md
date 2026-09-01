# BulkNegativeKeywordUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The updated negative keyword status for a bulk negative-keyword update item.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string BulkNegativeKeywordUpdate.Status
```

#### Discussion

Include this field within an item’s `data` to re-enable or pause the negative keyword’s suppression as part of the same bulk update request.

##### Example

```json
{
  "status": "PAUSED"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulknegativekeywordupdate/status-data.typealias)*