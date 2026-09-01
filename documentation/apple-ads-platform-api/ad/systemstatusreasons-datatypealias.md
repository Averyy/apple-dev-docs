# Ad.SystemStatusReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Reasons that can cause an ad’s system status to be `NOT_RUNNING`.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Ad.SystemStatusReasons
```

#### Discussion

These codes span approval, creative, and product page conditions that the platform surfaces when [`Ad.SystemStatus`](ad/systemstatus-data.typealias.md) is `NOT_RUNNING`.

##### Example

```json
{
  "systemStatusReasons": ["AD_APPROVAL_PENDING"]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ad/systemstatusreasons-data.typealias)*