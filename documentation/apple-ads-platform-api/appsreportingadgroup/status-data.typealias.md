# AppsReportingAdGroup.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving state of the ad group at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AppsReportingAdGroup.Status
```

## Possible Values

- `ENABLED`: The ad group is active and eligible to serve ads.
- `PAUSED`: The ad group is paused and won’t serve ads.

#### Discussion

This captures the advertiser-set status as of the report’s generation, separate from the system-evaluated [`AppsReportingAdGroup.SystemStatus`](./systemstatus-data.typealias.md) reported alongside it.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdGroupStatus`](../adgroupstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingadgroup/status-data.typealias)*