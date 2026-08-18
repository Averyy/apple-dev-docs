# PromotedObjectType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The category of entity that a campaign promotes, determining which values apply.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string PromotedObjectType
```

#### Discussion

You set `PromotedObjectType` when you create the campaign, and it stays fixed afterward. It determines the advertising placement, creative format, and available targeting options for the campaign. All campaigns, ad groups, and creatives under a campaign share the same promoted object type.

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
- [type BillingEvent](billingevent.md)
  The user interaction that triggers a charge for a campaign.
- [type Currency](currency.md)
  The currency code used for monetary values in the Apple Ads Platform API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/promotedobjecttype)*