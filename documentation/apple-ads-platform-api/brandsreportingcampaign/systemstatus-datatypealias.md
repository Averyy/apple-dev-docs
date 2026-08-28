# BrandsReportingCampaign.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-evaluated delivery state of the campaign at report time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BrandsReportingCampaign.SystemStatus
```

#### Discussion

This reflects delivery conditions evaluated at the moment the report was generated, separate from the advertiser-set [`BrandsReportingCampaign.Status`](brandsreportingcampaign/status-data.typealias.md) reported alongside it.

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`CampaignSystemStatus`](campaignsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcampaign/systemstatus-data.typealias)*