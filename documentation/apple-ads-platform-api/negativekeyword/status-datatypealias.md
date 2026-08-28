# NegativeKeyword.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable active state for this negative keyword.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string NegativeKeyword.Status
```

#### Discussion

This field controls suppression directly; pausing it lets matching search queries resume triggering ads again.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`NegativeKeywordStatus`](negativekeywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeyword/status-data.typealias)*