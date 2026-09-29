# CampaignTargetingUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Targeting configuration for updating an existing campaign’s supply source, placement, and geographic markets.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object CampaignTargetingUpdate
```

#### Discussion

The `CampaignTargetingUpdate` object is the update-time counterpart to [`CampaignTargeting`](campaigntargeting.md). `supplyPlacement` and `countryOrRegion` are optional and nullable; only the fields you supply are changed, and any omitted field retains its current value. `supplySource` is immutable after campaign creation: including it in an update request, even with its current unchanged value, is unsupported. Each updatable field uses a [`TargetingDataUpdate`](targetingdataupdate.md) object to express `include`/`exclude` changes for that dimension.

> **Note**: For `supplyPlacement`, omitting the field leaves the current placement(s) unchanged rather than switching targeting to every placement. An Apple Maps campaign created with a single `MAPS` placement can’t be widened to target both `MAPS_SEARCH_RESULTS` and `MAPS_SEARCH_HOME` via update. That requires creating a new campaign without `supplyPlacement` set. See [`CampaignTargetingCreate.SupplyPlacement`](campaigntargetingcreate/supplyplacement-data.dictionary.md).

##### Example

```json
{
  "supplyPlacement": {
    "include": ["APPSTORE_SEARCH_RESULTS", "APPSTORE_TODAY_TAB"],
    "exclude": null
  },
  "countryOrRegion": {
    "include": ["US", "CA"]
  }
}
```

## Topics

### Dictionaries
- [object CampaignTargetingUpdate.CountryOrRegion](campaigntargetingupdate/countryorregion-data.dictionary.md)
  The countries or regions where an existing campaign’s ads are eligible to serve.
- [object CampaignTargetingUpdate.SupplyPlacement](campaigntargetingupdate/supplyplacement-data.dictionary.md)
  The specific placement within a supply source where an existing campaign’s ads are eligible to appear.
- [object CampaignTargetingUpdate.SupplySource](campaigntargetingupdate/supplysource-data.dictionary.md)
  The supply source where an existing campaign’s ads are eligible to appear.

## Properties

- `supplySource` (CampaignTargetingUpdate.SupplySource): The supply source(s) where ads are eligible to appear. Fixed at creation. Don’t include this field in an update request, since doing so is unsupported regardless of the value sent.
- `supplyPlacement` (CampaignTargetingUpdate.SupplyPlacement): The specific placements within a supply source. Omit to leave unchanged. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `countryOrRegion` (CampaignTargetingUpdate.CountryOrRegion): The countries or regions where the campaign serves ads. Omit to leave unchanged. See [`TargetingDataUpdate`](targetingdataupdate.md).

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
- [object DailyBudgetUpdate](dailybudgetupdate.md)
  Request wrapper for updating a campaign’s daily budget amount.
- [object LegacyAppLimitedStatusReasonDetails](legacyapplimitedstatusreasondetails.md)
  Per-country or per-region limited-status reasons for legacy app campaigns.
- [object ResponsePagination](responsepagination.md)
  Pagination metadata returned in Campaign list responses, supporting offset-based navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingupdate)*