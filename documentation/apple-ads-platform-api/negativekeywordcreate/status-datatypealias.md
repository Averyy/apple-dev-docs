# NegativeKeywordCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Whether this negative keyword is active at creation.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string NegativeKeywordCreate.Status
```

#### Discussion

Include `status` in the create request to determine whether the negative keyword begins suppressing matching search queries immediately or starts paused.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`NegativeKeywordStatus`](negativekeywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordcreate/status-data.typealias)*