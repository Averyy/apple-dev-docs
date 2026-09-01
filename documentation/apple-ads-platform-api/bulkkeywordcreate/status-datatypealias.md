# BulkKeywordCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The keyword’s status for a bulk keyword create item.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string BulkKeywordCreate.Status
```

#### Discussion

Set this within each item’s `data` to determine whether the keyword begins serving as soon as the bulk create request completes.

##### Example

```json
{
  "status": "ENABLED"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkkeywordcreate/status-data.typealias)*