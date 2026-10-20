# AdStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Enumeration of advertiser-configurable serving states for an ad.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdStatus
```

## Possible Values

- `ENABLED`: The advertiser has set the ad to run, so it can participate in auctions.
- `PAUSED`: The advertiser has paused the ad, so it does not participate in auctions.

## See Also

- [type AdSystemStatus](./adsystemstatus.md)
  Enumeration of system-evaluated delivery states for an ad.
- [type AdDisplayStatus](./addisplaystatus.md)
  Rolled-up delivery state for an ad, combining advertiser settings and system conditions into a single user-facing label.
- [type AdSystemStatusReason](./adsystemstatusreason.md)
  A reason code explaining why an ad is not currently running.
- [type AdSystemLimitedStatusReason](./adsystemlimitedstatusreason.md)
  A reason code indicating that an ad is running but at reduced delivery capacity due to a policy condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adstatus)*