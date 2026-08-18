# CampaignSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias

A reason code explaining why a campaign is not currently running.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string CampaignSystemStatusReason
```

#### Discussion

One or more `CampaignSystemStatusReason` values appear in the `systemStatusReasons` array on a [`Campaign`](campaign.md) when `systemStatus` is `NOT_RUNNING`. These codes are read-only and system-applied. Use them to diagnose delivery issues and determine the appropriate corrective action.

## See Also

- [type CampaignStatus](campaignstatus.md)
  Advertiser-configurable run state for a campaign.
- [type CampaignSystemStatus](campaignsystemstatus.md)
  System-evaluated delivery state indicating whether a campaign is currently running.
- [type CampaignDisplayStatus](campaigndisplaystatus.md)
  Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.
- [type CampaignSystemLimitedStatusReason](campaignsystemlimitedstatusreason.md)
  A reason code indicating that a campaign is running but delivering at reduced capacity.
- [type BillingEvent](billingevent.md)
  The user interaction that triggers a charge for a campaign.
- [type PromotedObjectType](promotedobjecttype.md)
  The category of entity that a campaign promotes, determining which values apply.
- [type Currency](currency.md)
  The currency code used for monetary values in the Apple Ads Platform API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignsystemstatusreason)*