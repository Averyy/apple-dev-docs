# CampaignTargeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Defines where a campaign is eligible to serve ads, including supply source, placement, and geographic markets.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargeting
```

#### Discussion

`CampaignTargeting` defines where a campaign is eligible to serve ads, using three `TargetingData` fields: `supplySource`, `supplyPlacement`, and `countryOrRegion`.

`supplySource`, `supplyPlacement`, and `countryOrRegion` are all include-only at the campaign level: the `exclude` array is not supported for any of the three dimensions. Use [`CampaignTargetingCreate`](campaigntargetingcreate.md) to supply these values when creating a new campaign. Once the campaign exists, all three dimensions remain mutable via [`CampaignTargetingUpdate`](campaigntargetingupdate.md). After campaign-level targeting is in place, [`AdGroupTargeting`](adgrouptargeting.md) provides further audience and delivery refinements at the ad group level.

##### Example

```json
{
  "supplySource": {
    "include": [
      "APPSTORE"
    ]
  },
  "supplyPlacement": {
    "include": [
      "APPSTORE_SEARCH_RESULTS",
      "APPSTORE_SEARCH_TAB"
    ]
  },
  "countryOrRegion": {
    "include": [
      "US",
      "CA"
    ]
  }
}
```

## Topics

### Dictionaries
- [object CampaignTargeting.CountryOrRegion](campaigntargeting/countryorregion-data.dictionary.md)
  The countries or regions where a campaign’s ads are eligible to serve.
- [object CampaignTargeting.SupplyPlacement](campaigntargeting/supplyplacement-data.dictionary.md)
  The specific placement within a supply source where a campaign’s ads are eligible to appear.
- [object CampaignTargeting.SupplySource](campaigntargeting/supplysource-data.dictionary.md)
  The supply source where a campaign’s ads are eligible to appear.

## Properties

- `supplySource` (CampaignTargeting.SupplySource): The supply source(s) where ads are eligible to appear. Possible values: `APPSTORE`, `MAPS`. See [`TargetingData`](targetingdata.md) for details. Mutable.
- `supplyPlacement` (CampaignTargeting.SupplyPlacement): The specific placements within a supply source. Possible values: `APPSTORE_SEARCH_RESULTS`, `APPSTORE_SEARCH_TAB`, `APPSTORE_TODAY_TAB`, `APPSTORE_PRODUCT_PAGES`, `MAPS_SEARCH_RESULTS`, `MAPS_SEARCH_HOME`. See [`CampaignTargeting.SupplyPlacement`](campaigntargeting/supplyplacement-data.dictionary.md) for the supply source each placement belongs to. See [`TargetingData`](targetingdata.md) for details. Mutable.
- `countryOrRegion` (CampaignTargeting.CountryOrRegion): The countries or regions where the campaign serves ads. Uses ISO 3166-1 alpha-2 country codes. See [`TargetingData`](targetingdata.md) for details. Mutable.

## See Also

- [object Campaign](campaign.md)
  The top-level container that defines a campaign’s promoted object, billing, scheduling, and targeting.
- [object CampaignCreate](campaigncreate.md)
  The request body for creating a new campaign.
- [object CampaignUpdate](campaignupdate.md)
  The request body for updating an existing Campaign object.
- [object CampaignResponse](campaignresponse.md)
  The response object for a Campaign operation.
- [object CampaignQueryResponse](campaignqueryresponse.md)
  The response object for a Campaign query, containing matched results and pagination metadata.
- [object CampaignTargetingCreate](campaigntargetingcreate.md)
  Targeting configuration supplied when creating a campaign.
- [object DailyBudget](dailybudget.md)
  Daily budget cap for a campaign.
- [object DailyBudgetCreate](dailybudgetcreate.md)
  Request wrapper for setting a campaign’s daily budget at creation time.
- [object Money](money.md)
  Monetary representation with currency.
- [object InvoiceDetailCreate](invoicedetailcreate.md)
  Invoice billing contact details supplied when creating a campaign or budget order.
- [object LegacyAppLimitedStatusReasonDetailsResponse](legacyapplimitedstatusreasondetailsresponse.md)
  Response wrapper returning per-country or per-region limited-status reasons for legacy app campaigns.
- [object CampaignTargetingUpdate](campaigntargetingupdate.md)
  Targeting configuration for updating an existing campaign’s supply source, placement, and geographic markets.
- [object DailyBudgetUpdate](dailybudgetupdate.md)
  Request wrapper for updating a campaign’s daily budget amount.
- [object LegacyAppLimitedStatusReasonDetails](legacyapplimitedstatusreasondetails.md)
  Per-country or per-region limited-status reasons for legacy app campaigns.
- [object ResponsePagination](responsepagination.md)
  Pagination metadata returned in Campaign list responses, supporting offset-based navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargeting)*