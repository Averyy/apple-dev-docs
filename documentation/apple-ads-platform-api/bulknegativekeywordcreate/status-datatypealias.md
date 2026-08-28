# BulkNegativeKeywordCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The negative keyword’s status for a bulk negative-keyword create item.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BulkNegativeKeywordCreate.Status
```

#### Discussion

Set this within each item’s `data` to determine whether the negative keyword begins suppressing matching search queries as soon as the bulk create request completes.

##### Example

```json
{
  "status": "ENABLED"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulknegativekeywordcreate/status-data.typealias)*