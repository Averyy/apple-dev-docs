# Currency

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The currency code used for monetary values in the Apple Ads Platform API.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Currency
```

## Possible Values

- `USD`: United States Dollar.
- `RMB`: Renminbi. A legacy alias for `CNY`, not an ISO 4217 code. Prefer `CNY`.
- `AUD`: Australian Dollar.
- `CAD`: Canadian Dollar.
- `EUR`: Euro.
- `GBP`: British Pound Sterling.
- `JPY`: Japanese Yen.
- `MXN`: Mexican Peso.
- `NZD`: New Zealand Dollar.
- `RUB`: Russian Ruble.
- `CNY`: Chinese Yuan. The ISO 4217 code for the same currency as `RMB`.
- `INR`: Indian Rupee.
- `BRL`: Brazilian Real.
- `IDR`: Indonesian Rupiah.

## See Also

- [type CampaignStatus](./campaignstatus.md)
  Advertiser-configurable run state for a campaign.
- [type CampaignSystemStatus](./campaignsystemstatus.md)
  System-evaluated delivery state indicating whether a campaign is currently running.
- [type CampaignDisplayStatus](./campaigndisplaystatus.md)
  Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.
- [type CampaignSystemStatusReason](./campaignsystemstatusreason.md)
  A reason code explaining why a campaign is not currently running.
- [type CampaignSystemLimitedStatusReason](./campaignsystemlimitedstatusreason.md)
  A reason code indicating that a campaign is running but delivering at reduced capacity.
- [type BillingEvent](./billingevent.md)
  The user interaction that triggers a charge for a campaign.
- [type PromotedObjectType](./promotedobjecttype.md)
  The category of entity that a campaign promotes, determining which values apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/currency)*