# CampaignUpdate.Targeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Targeting configuration for updating an existing campaign’s supply source, placement, and geographic markets.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object CampaignUpdate.Targeting
```

#### Discussion

Omit `supplyPlacement` or `countryOrRegion` to leave its current value unchanged. `supplySource` is fixed at creation; don’t include it in an update request.

See [`CampaignTargetingUpdate`](campaigntargetingupdate.md) for the full field reference.

## Properties

- `supplySource` (CampaignTargetingUpdate.SupplySource): The supply source(s) where ads are eligible to appear. Fixed at creation. Don’t include this field in an update request, since doing so is unsupported regardless of the value sent.
- `supplyPlacement` (CampaignTargetingUpdate.SupplyPlacement): The specific placements within a supply source. Omit to leave unchanged. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `countryOrRegion` (CampaignTargetingUpdate.CountryOrRegion): The countries or regions where the campaign serves ads. Omit to leave unchanged. See [`TargetingDataUpdate`](targetingdataupdate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignupdate/targeting-data.dictionary)*