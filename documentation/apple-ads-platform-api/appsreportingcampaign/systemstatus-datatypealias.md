# AppsReportingCampaign.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-evaluated delivery state of the campaign at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AppsReportingCampaign.SystemStatus
```

#### Discussion

This is a point-in-time snapshot; a campaign that later changes to `NOT_RUNNING` won’t retroactively update in an already-generated report.

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`CampaignSystemStatus`](campaignsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingcampaign/systemstatus-data.typealias)*