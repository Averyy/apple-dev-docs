# AppsReportingAd.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable serving state of the ad at report time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AppsReportingAd.Status
```

#### Discussion

This captures the advertiser’s run-or-pause choice as of the report’s generation, separate from the system-evaluated [`AppsReportingAd.SystemStatus`](appsreportingad/systemstatus-data.typealias.md) reported in the same row.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdStatus`](adstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingad/status-data.typealias)*