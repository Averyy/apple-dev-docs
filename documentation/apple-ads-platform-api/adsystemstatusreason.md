# AdSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias

A reason code explaining why an ad is not currently running.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AdSystemStatusReason
```

#### Discussion

One or more `AdSystemStatusReason` values appear in the `systemStatusReasons` array on an [`Ad`](ad.md) when `systemStatus` is `NOT_RUNNING`. These codes are read-only and system-applied. They provide the specific cause behind a non-running state and indicate what action, if any, is required to resume delivery.

## See Also

- [type AdStatus](adstatus.md)
  Enumeration of advertiser-configurable serving states for an ad.
- [type AdSystemStatus](adsystemstatus.md)
  Enumeration of system-evaluated delivery states for an ad.
- [type AdDisplayStatus](addisplaystatus.md)
  Rolled-up delivery state for an ad, combining advertiser settings and system conditions into a single user-facing label.
- [type AdSystemLimitedStatusReason](adsystemlimitedstatusreason.md)
  A reason code indicating that an ad is running but at reduced delivery capacity due to a policy condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adsystemstatusreason)*