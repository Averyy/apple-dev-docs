# CampaignUpdate.Targeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Targeting configuration for updating an existing campaign’s supply source, placement, and geographic markets.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignUpdate.Targeting
```

#### Discussion

Omit a field to leave its current value unchanged.

See [`CampaignTargetingUpdate`](campaigntargetingupdate.md) for the full field reference.

## Properties

- `supplySource` (CampaignTargetingUpdate.SupplySource): The supply source(s) where ads are eligible to appear. Omit to leave unchanged. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `supplyPlacement` (CampaignTargetingUpdate.SupplyPlacement): The specific placements within a supply source. Omit to leave unchanged. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `countryOrRegion` (CampaignTargetingUpdate.CountryOrRegion): The countries or regions where the campaign serves ads. Omit to leave unchanged. See [`TargetingDataUpdate`](targetingdataupdate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignupdate/targeting-data.dictionary)*