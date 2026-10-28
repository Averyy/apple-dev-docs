# AdDisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Rolled-up delivery state for an ad, combining advertiser settings and system conditions into a single user-facing label.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdDisplayStatus
```

## Possible Values

- `RUNNING`: The ad is actively delivering.
- `PAUSED`: The advertiser paused the ad.
- `ON_HOLD`: A system or account condition stops delivery.
- `LIMITED`: The ad is serving but at reduced capacity.
- `PROCESSING`: The system is processing the ad after a recent creation or update.
- `DELETED`: The advertiser soft-deleted the ad.
- `AD_GROUP_ON_HOLD`: Delivery stops because the parent ad group is on hold.
- `CAMPAIGN_ON_HOLD`: Delivery stops because the parent campaign is on hold.

## Discussion

The `AdDisplayStatus` is a read-only derived field on [`Ad`](./ad.md) that summarizes the effective delivery state of the ad. It accounts for the ad’s own `AdStatus`, parent ad group status, and parent campaign status. When displaying ad health in a UI, use this field.

## See Also

- [type AdStatus](./adstatus.md)
  Enumeration of advertiser-configurable serving states for an ad.
- [type AdSystemStatus](./adsystemstatus.md)
  Enumeration of system-evaluated delivery states for an ad.
- [type AdSystemStatusReason](./adsystemstatusreason.md)
  A reason code explaining why an ad is not currently running.
- [type AdSystemLimitedStatusReason](./adsystemlimitedstatusreason.md)
  A reason code indicating that an ad is running but at reduced delivery capacity due to a policy condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/addisplaystatus)*