# CampaignCreate.Targeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Targeting configuration supplied when creating a campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignCreate.Targeting
```

#### Discussion

Sets the supply source, placement, and geographic markets a new campaign is eligible to serve on. These values establish the campaign-level targeting boundary within which ad group targeting must operate.

See [`CampaignTargetingCreate`](campaigntargetingcreate.md) for the full field reference.

## Properties

- `supplySource` (CampaignTargetingCreate.SupplySource): The supply source(s) where ads are eligible to appear (for example, `APPSTORE`, `MAPS`). See [`TargetingDataCreate`](targetingdatacreate.md) for details.
- `supplyPlacement` (CampaignTargetingCreate.SupplyPlacement): The specific placements within a supply source. See [`CampaignTargetingCreate.SupplyPlacement`](campaigntargetingcreate/supplyplacement-data.dictionary.md) for possible values and which supply source each belongs to. See [`TargetingDataCreate`](targetingdatacreate.md) for details.
- `countryOrRegion` (CampaignTargetingCreate.CountryOrRegion): The countries or regions where the campaign serves ads. Uses ISO 3166-1 alpha-2 country codes. See [`TargetingDataCreate`](targetingdatacreate.md) for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate/targeting-data.dictionary)*