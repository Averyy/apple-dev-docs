# AppsReportingAd.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-evaluated delivery state of the ad at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AppsReportingAd.SystemStatus
```

#### Discussion

This reflects delivery conditions evaluated at the moment the report was generated, separate from the advertiser-set [`AppsReportingAd.Status`](appsreportingad/status-data.typealias.md) reported alongside it.

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`AdSystemStatus`](adsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingad/systemstatus-data.typealias)*