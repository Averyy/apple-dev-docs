# BrandsReportingAd.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving status of the ad at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingAd.Status
```

## Possible Values

- `ENABLED`: The ad is set to run and can participate in auctions.
- `PAUSED`: The ad is paused by the advertiser and doesn’t participate in auctions.

#### Discussion

This reflects whether the advertiser had the ad set to run as of the report’s generation, distinct from the system-evaluated [`BrandsReportingAd.SystemStatus`](./systemstatus-data.typealias.md) reported alongside it.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdStatus`](../adstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingad/status-data.typealias)*