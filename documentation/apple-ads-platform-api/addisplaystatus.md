# AdDisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Rolled-up delivery state for an ad, combining advertiser settings and system conditions into a single user-facing label.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AdDisplayStatus
```

#### Discussion

`AdDisplayStatus` is a read-only derived field on [`Ad`](ad.md) that summarizes the effective delivery state of the ad. It accounts for the ad’s own `AdStatus`, parent ad group status, and parent campaign status. When displaying ad health in a UI, use this field.

## See Also

- [type AdStatus](adstatus.md)
  Enumeration of advertiser-configurable serving states for an ad.
- [type AdSystemStatus](adsystemstatus.md)
  Enumeration of system-evaluated delivery states for an ad.
- [type AdSystemStatusReason](adsystemstatusreason.md)
  A reason code explaining why an ad is not currently running.
- [type AdSystemLimitedStatusReason](adsystemlimitedstatusreason.md)
  A reason code indicating that an ad is running but at reduced delivery capacity due to a policy condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/addisplaystatus)*