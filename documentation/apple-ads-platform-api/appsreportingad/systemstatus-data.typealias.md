# AppsReportingAd.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

System-evaluated delivery state of the ad at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AppsReportingAd.SystemStatus
```

## Possible Values

- `RUNNING`: The ad is active and eligible to serve.
- `NOT_RUNNING`: The system has identified a condition preventing the ad from delivering.

#### Discussion

This reflects delivery conditions evaluated at the moment the report was generated, separate from the advertiser-set [`AppsReportingAd.Status`](./status-data.typealias.md) reported alongside it.

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`AdSystemStatus`](../adsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingad/systemstatus-data.typealias)*