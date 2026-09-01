# BrandsReportingAdGroup.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-derived operational status of the ad group at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string BrandsReportingAdGroup.SystemStatus
```

#### Discussion

This is a point-in-time snapshot; an ad group that later changes to `NOT_RUNNING` won’t retroactively update in an already-generated report.

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`AdGroupSystemStatus`](adgroupsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingadgroup/systemstatus-data.typealias)*