# CampaignDisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string CampaignDisplayStatus
```

## Possible Values

- `RUNNING`: The campaign is actively delivering ads.
- `PAUSED`: The advertiser paused the campaign.
- `ON_HOLD`: Delivery is stopped due to a system or account condition.
- `LIMITED`: The campaign is serving but at reduced capacity due to a system condition.
- `PROCESSING`: The campaign was recently created or modified and is being processed.
- `DELETED`: The campaign has been soft-deleted.

## Discussion

The `CampaignDisplayStatus` is a read-only, derived field on [`Campaign`](./campaign.md) that surfaces the effective delivery state. It combines `CampaignStatus` (advertiser intent) and `CampaignSystemStatus` (system evaluation) into one actionable label. Use this field when displaying campaign health in a UI. Inspect `CampaignSystemStatusReason` for the root cause when the status isn’t `RUNNING`.

## See Also

- [type CampaignStatus](./campaignstatus.md)
  Advertiser-configurable run state for a campaign.
- [type CampaignSystemStatus](./campaignsystemstatus.md)
  System-evaluated delivery state indicating whether a campaign is currently running.
- [type CampaignSystemStatusReason](./campaignsystemstatusreason.md)
  A reason code explaining why a campaign is not currently running.
- [type CampaignSystemLimitedStatusReason](./campaignsystemlimitedstatusreason.md)
  A reason code indicating that a campaign is running but delivering at reduced capacity.
- [type BillingEvent](./billingevent.md)
  The user interaction that triggers a charge for a campaign.
- [type PromotedObjectType](./promotedobjecttype.md)
  The category of entity that a campaign promotes, determining which values apply.
- [type Currency](./currency.md)
  The currency code used for monetary values in the Apple Ads Platform API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigndisplaystatus)*