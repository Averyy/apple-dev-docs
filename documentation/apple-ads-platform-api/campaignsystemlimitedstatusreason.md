# CampaignSystemLimitedStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias

A reason code indicating that a campaign is running but delivering at reduced capacity.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string CampaignSystemLimitedStatusReason
```

#### Discussion

`CampaignSystemLimitedStatusReason` values appear in the `systemStatusLimitingReasons` array on a [`Campaign`](campaign.md) alongside an active `systemStatus`. Unlike `CampaignSystemStatusReason`, these codes do not stop delivery. They indicate conditions that constrain reach or impression volume.

## See Also

- [type CampaignStatus](campaignstatus.md)
  Advertiser-configurable run state for a campaign.
- [type CampaignSystemStatus](campaignsystemstatus.md)
  System-evaluated delivery state indicating whether a campaign is currently running.
- [type CampaignDisplayStatus](campaigndisplaystatus.md)
  Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.
- [type CampaignSystemStatusReason](campaignsystemstatusreason.md)
  A reason code explaining why a campaign is not currently running.
- [type BillingEvent](billingevent.md)
  The user interaction that triggers a charge for a campaign.
- [type PromotedObjectType](promotedobjecttype.md)
  The category of entity that a campaign promotes, determining which values apply.
- [type Currency](currency.md)
  The currency code used for monetary values in the Apple Ads Platform API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignsystemlimitedstatusreason)*