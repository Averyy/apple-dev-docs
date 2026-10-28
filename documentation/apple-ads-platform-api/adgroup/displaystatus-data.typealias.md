# AdGroup.DisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Derived display status for an ad group, combining advertiser-set status with system status.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroup.DisplayStatus
```

## Possible Values

- `CAMPAIGN_ON_HOLD`: The ad group is on hold because its parent campaign is on hold.
- `DELETED`: The ad group has been deleted.
- `LIMITED`: The ad group is serving but delivery is restricted. Check `systemStatusLimitingReasons` for details.
- `ON_HOLD`: The ad group is on hold due to a system issue. Check `systemStatusReasons` for details.
- `PAUSED`: The ad group has been paused by the advertiser.
- `PROCESSING`: The ad group is being processed and is not yet serving.
- `RUNNING`: The ad group is active and eligible to serve ads.

## Discussion

Because it rolls up the full hierarchy, an ad group can show `CAMPAIGN_ON_HOLD` even when its own status and system conditions are otherwise fine.

### Example

```json
{
  "displayStatus": "RUNNING"
}
```

See [`AdGroupDisplayStatus`](../adgroupdisplaystatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/displaystatus-data.typealias)*