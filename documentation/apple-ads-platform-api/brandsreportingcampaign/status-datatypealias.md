# BrandsReportingCampaign.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable serving status of the campaign at report time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BrandsReportingCampaign.Status
```

#### Discussion

This captures the advertiser-set status as of the report’s generation, separate from the system-evaluated [`BrandsReportingCampaign.SystemStatus`](brandsreportingcampaign/systemstatus-data.typealias.md) alongside it.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`CampaignStatus`](campaignstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcampaign/status-data.typealias)*