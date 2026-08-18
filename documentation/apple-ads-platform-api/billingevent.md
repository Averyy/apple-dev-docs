# BillingEvent

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The user interaction that triggers a charge for a campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BillingEvent
```

#### Discussion

You set `BillingEvent` at campaign creation, and it stays fixed afterward. The value you choose constrains which bid strategies are available and applies uniformly to all ad groups in the campaign.

App Store campaigns use `TAPS`. Apple Maps campaigns support both `TAPS` (for tap-based strategies) and `IMPRESSIONS` (for `MANUAL_CPM`).

## See Also

- [type CampaignStatus](campaignstatus.md)
  Advertiser-configurable run state for a campaign.
- [type CampaignSystemStatus](campaignsystemstatus.md)
  System-evaluated delivery state indicating whether a campaign is currently running.
- [type CampaignDisplayStatus](campaigndisplaystatus.md)
  Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.
- [type CampaignSystemStatusReason](campaignsystemstatusreason.md)
  A reason code explaining why a campaign is not currently running.
- [type CampaignSystemLimitedStatusReason](campaignsystemlimitedstatusreason.md)
  A reason code indicating that a campaign is running but delivering at reduced capacity.
- [type PromotedObjectType](promotedobjecttype.md)
  The category of entity that a campaign promotes, determining which values apply.
- [type Currency](currency.md)
  The currency code used for monetary values in the Apple Ads Platform API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/billingevent)*