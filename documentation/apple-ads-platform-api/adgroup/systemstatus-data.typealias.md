# AdGroup.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

System-derived operational status reflecting whether an ad group is actively serving.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroup.SystemStatus
```

## Possible Values

- `RUNNING`: The ad group is active and serving ads.
- `NOT_RUNNING`: The ad group is not serving ads. Check `systemStatusReasons` for the specific cause.

## Discussion

This status reflects the ad group specifically, separate from the advertiser-set [`AdGroup.Status`](./status-data.typealias.md) and the system status of ads within it.

### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`AdGroupSystemStatus`](../adgroupsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/systemstatus-data.typealias)*