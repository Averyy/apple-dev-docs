# Campaign.Targeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Defines where a campaign is eligible to serve ads, including supply source, placement, and geographic markets.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Campaign.Targeting
```

#### Discussion

Defines the supply source, placement, and geographic markets where this campaign is eligible to serve. Ad group targeting must operate within these campaign-level boundaries.

See [`CampaignTargeting`](campaigntargeting.md) for the full field reference.

## Properties

- `supplySource` (CampaignTargeting.SupplySource): The supply source(s) where ads are eligible to appear. Possible values: `APPSTORE`, `MAPS`. See [`TargetingData`](targetingdata.md) for details. Mutable.
- `supplyPlacement` (CampaignTargeting.SupplyPlacement): The specific placements within a supply source. Possible values: `APPSTORE_SEARCH_RESULTS`, `APPSTORE_SEARCH_TAB`, `APPSTORE_TODAY_TAB`, `APPSTORE_PRODUCT_PAGES`, `MAPS_SEARCH_RESULTS`, `MAPS_SEARCH_HOME`. See [`CampaignTargeting.SupplyPlacement`](campaigntargeting/supplyplacement-data.dictionary.md) for the supply source each placement belongs to. See [`TargetingData`](targetingdata.md) for details. Mutable.
- `countryOrRegion` (CampaignTargeting.CountryOrRegion): The countries or regions where the campaign serves ads. Uses ISO 3166-1 alpha-2 country codes. See [`TargetingData`](targetingdata.md) for details. Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/targeting-data.dictionary)*