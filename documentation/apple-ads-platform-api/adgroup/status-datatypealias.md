# AdGroup.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable serving status for an ad group.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AdGroup.Status
```

#### Discussion

This field directly controls auction eligibility for the ad group, independent of the system-computed [`AdGroup.SystemStatus`](adgroup/systemstatus-data.typealias.md).

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdGroupStatus`](adgroupstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/status-data.typealias)*