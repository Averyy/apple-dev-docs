# CampaignSystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-evaluated delivery state indicating whether a campaign is currently running.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string CampaignSystemStatus
```

#### Discussion

`CampaignSystemStatus` is a read-only field set by the platform. It reflects whether the campaign is actively delivering ads based on all system-evaluated conditions. When `NOT_RUNNING`, inspect `systemStatusReasons` on the [`Campaign`](campaign.md) object for the specific blocking condition.

## See Also

- [type CampaignStatus](campaignstatus.md)
  Advertiser-configurable run state for a campaign.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignsystemstatus)*