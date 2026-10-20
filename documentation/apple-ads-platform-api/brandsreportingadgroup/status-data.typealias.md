# BrandsReportingAdGroup.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving status of the ad group at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingAdGroup.Status
```

## Possible Values

- `ENABLED`: The ad group is active and eligible to serve ads.
- `PAUSED`: The ad group is paused and won’t serve ads.

#### Discussion

This reflects whether the advertiser had the ad group set to run as of the report’s generation, distinct from the system-evaluated [`BrandsReportingAdGroup.SystemStatus`](./systemstatus-data.typealias.md) reported alongside it.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdGroupStatus`](../adgroupstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingadgroup/status-data.typealias)*