# CampaignDisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string CampaignDisplayStatus
```

#### Discussion

`CampaignDisplayStatus` is a read-only, derived field on [`Campaign`](campaign.md) that surfaces the effective delivery state. It combines `CampaignStatus` (advertiser intent) and `CampaignSystemStatus` (system evaluation) into one actionable label. Use this field when displaying campaign health in a UI. Inspect `CampaignSystemStatusReason` for the root cause when the status is not `RUNNING`.

## See Also

- [type CampaignStatus](campaignstatus.md)
  Advertiser-configurable run state for a campaign.
- [type CampaignSystemStatus](campaignsystemstatus.md)
  System-evaluated delivery state indicating whether a campaign is currently running.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigndisplaystatus)*