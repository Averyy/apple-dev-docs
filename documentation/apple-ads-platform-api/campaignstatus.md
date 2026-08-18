# CampaignStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable run state for a campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string CampaignStatus
```

#### Discussion

`CampaignStatus` is the only campaign field that directly controls whether the campaign is eligible to serve ads. Set it to `PAUSED` to stop delivery without deleting the campaign. The system status (`CampaignSystemStatus`) reflects actual delivery. A campaign can be `ENABLED` but `NOT_RUNNING` due to system conditions.

## See Also

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
- [type PromotedObjectType](promotedobjecttype.md)
  The category of entity that a campaign promotes, determining which values apply.
- [type Currency](currency.md)
  The currency code used for monetary values in the Apple Ads Platform API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignstatus)*