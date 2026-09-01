# BrandsReportingAd.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable serving status of the ad at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string BrandsReportingAd.Status
```

#### Discussion

This reflects whether the advertiser had the ad set to run as of the report’s generation, distinct from the system-evaluated [`BrandsReportingAd.SystemStatus`](brandsreportingad/systemstatus-data.typealias.md) reported alongside it.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdStatus`](adstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingad/status-data.typealias)*