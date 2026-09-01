# Creative.SystemStatusReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Reason codes explaining the ad creative’s current system status.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Creative.SystemStatusReasons
```

#### Discussion

These reasons span policy review, asset validation, and App Store product page issues that the platform surfaces when [`Creative.SystemStatus`](creative/systemstatus-data.typealias.md) is `INVALID`.

##### Example

```json
{
  "systemStatusReasons": ["NEEDS_REVIEW"]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creative/systemstatusreasons-data.typealias)*