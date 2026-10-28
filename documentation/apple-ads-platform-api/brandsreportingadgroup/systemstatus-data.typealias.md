# BrandsReportingAdGroup.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

System-derived operational status of the ad group at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingAdGroup.SystemStatus
```

## Possible Values

- `RUNNING`: The ad group is active and serving ads.
- `NOT_RUNNING`: The ad group isn’t serving ads. Check `systemStatusReasons` for the specific cause.

## Discussion

This is a point-in-time snapshot; an ad group that later changes to `NOT_RUNNING` won’t retroactively update in an already-generated report.

### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`AdGroupSystemStatus`](../adgroupsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingadgroup/systemstatus-data.typealias)*