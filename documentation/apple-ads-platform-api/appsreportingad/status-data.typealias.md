# AppsReportingAd.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving state of the ad at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AppsReportingAd.Status
```

## Possible Values

- `ENABLED`: The ad is set to run and can participate in auctions.
- `PAUSED`: The ad is paused by the advertiser and doesn’t participate in auctions.

## Discussion

This captures the advertiser’s run-or-pause choice as of the report’s generation, separate from the system-evaluated [`AppsReportingAd.SystemStatus`](./systemstatus-data.typealias.md) reported in the same row.

### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdStatus`](../adstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingad/status-data.typealias)*