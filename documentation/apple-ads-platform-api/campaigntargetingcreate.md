# CampaignTargetingCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Targeting configuration supplied when creating a campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargetingCreate
```

#### Discussion

`CampaignTargetingCreate` is the create-time counterpart to [`CampaignTargeting`](campaigntargeting.md). It defines the supply source, placement, and geographic markets for a new campaign using [`TargetingDataCreate`](targetingdatacreate.md) objects for each dimension. All three dimensions are include-only: the `exclude` array is not supported at the campaign level. [`TargetingDataCreate`](targetingdatacreate.md) at creation time corresponds to [`TargetingData`](targetingdata.md) in read and update responses. Once the campaign is created, use [`CampaignTargeting`](campaigntargeting.md) to read or update any of the three dimensions.

##### Example

```json
{
  "supplySource": {
    "include": ["APPSTORE"]
  },
  "supplyPlacement": {
    "include": ["APPSTORE_SEARCH_RESULTS", "APPSTORE_SEARCH_TAB"]
  },
  "countryOrRegion": {
    "include": ["US", "CA"]
  }
}
```

| Value | Supply source | Placement |
| --- | --- | --- |
| `APPSTORE_SEARCH_RESULTS` | `APPSTORE` | App Store Search results |
| `APPSTORE_SEARCH_TAB` | `APPSTORE` | App Store Search tab |
| `APPSTORE_TODAY_TAB` | `APPSTORE` | App Store Today tab |
| `APPSTORE_PRODUCT_PAGES` | `APPSTORE` | App Store Product pages |
| `MAPS_SEARCH_RESULTS` | `MAPS` | Apple Maps Search results |
| `MAPS_SEARCH_HOME` | `MAPS` | Apple Maps Search home |

## Topics

### Dictionaries
- [object CampaignTargetingCreate.CountryOrRegion](campaigntargetingcreate/countryorregion-data.dictionary.md)
  The countries or regions where a new campaign’s ads are eligible to serve.
- [object CampaignTargetingCreate.SupplyPlacement](campaigntargetingcreate/supplyplacement-data.dictionary.md)
  The specific placement within a supply source where a new campaign’s ads are eligible to appear.
- [object CampaignTargetingCreate.SupplySource](campaigntargetingcreate/supplysource-data.dictionary.md)
  The supply source where a new campaign’s ads are eligible to appear.

## Properties

- `supplySource` (CampaignTargetingCreate.SupplySource): The supply source(s) where ads are eligible to appear (for example, `APPSTORE`, `MAPS`). See [`TargetingDataCreate`](targetingdatacreate.md) for details.
- `supplyPlacement` (CampaignTargetingCreate.SupplyPlacement): The specific placements within a supply source. See accepted values below. See [`TargetingDataCreate`](targetingdatacreate.md) for details.
- `countryOrRegion` (CampaignTargetingCreate.CountryOrRegion): The countries or regions where the campaign serves ads. Uses ISO 3166-1 alpha-2 country codes. See [`TargetingDataCreate`](targetingdatacreate.md) for details.

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
- [object CampaignTargeting](campaigntargeting.md)
  Defines where a campaign is eligible to serve ads, including supply source, placement, and geographic markets.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingcreate)*