# CampaignCreate.BillingEvent

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The user interaction that triggers a charge for a campaign.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string CampaignCreate.BillingEvent
```

## Possible Values

- `TAPS`: The campaign is charged each time a user taps an ad. For App Ads campaigns, compatible with `MANUAL_CPT` and `MAX_CONVERSIONS`. For Apple Maps campaigns, compatible with `MANUAL_CPT` and `MAX_ENGAGEMENTS`.
- `IMPRESSIONS`: The campaign is charged per thousand impressions (CPM). Required for the `MANUAL_CPM` bid strategy. Available only for Apple Maps campaigns (`promotedObjectType: BUSINESS_BRAND`).

## Discussion

Set at campaign creation and immutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate/billingevent-data.typealias)*