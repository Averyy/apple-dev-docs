# AdGroup.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-derived operational status reflecting whether an ad group is actively serving.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AdGroup.SystemStatus
```

#### Discussion

This status reflects the ad group specifically, separate from the advertiser-set [`AdGroup.Status`](adgroup/status-data.typealias.md) and the system status of ads within it.

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`AdGroupSystemStatus`](adgroupsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/systemstatus-data.typealias)*