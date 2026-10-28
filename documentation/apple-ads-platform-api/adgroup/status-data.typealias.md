# AdGroup.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving status for an ad group.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroup.Status
```

## Possible Values

- `ENABLED`: The ad group is active and eligible to serve ads.
- `PAUSED`: The ad group is paused and will not serve ads.

## Discussion

This field directly controls auction eligibility for the ad group, independent of the system-computed [`AdGroup.SystemStatus`](./systemstatus-data.typealias.md).

### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdGroupStatus`](../adgroupstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/status-data.typealias)*