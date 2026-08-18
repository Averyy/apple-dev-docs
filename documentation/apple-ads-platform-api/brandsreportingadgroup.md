# BrandsReportingAdGroup

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad group metadata for brands report rows.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsReportingAdGroup
```

#### Discussion

`BrandsReportingAdGroup` is the ad group metadata object embedded in `BRANDS` ad group report rows. It captures configuration at report time, including the `pricingModel`, `bidStrategy`, and the `BRANDS`-specific `targeting` projection with supply placement and location group details.

The `campaign` field embeds a lightweight `ReportingCampaignMin` for parent campaign context. The system populates the `BRANDS` dimension fields (`deviceClass`, `locationId`, `supplyPlacement`) based on the `groupBy` dimensions in the report request. Note that keyword and search term entities exclude `supplyPlacement` and `locationId` as `groupBy` options.

##### Example

```json
{
  "id": 123456789,
  "campaignId": 987654321,
  "adAccountId": 555666777,
  "name": "AwayFinder - Brands Ad Group",
  "status": "ENABLED",
  "deleted": false,
  "systemStatus": "RUNNING",
  "systemStatusReasons": ["PROCESSING"],
  "systemStatusLimitingReasons": [],
  "automatedKeywordsOptIn": false,
  "automatedKeywordsRequired": false,
  "pricingModel": "CPT",
  "displayStatus": "RUNNING",
  "modificationTime": "2025-01-10T08:00:00.000",
  "creationTime": "2025-01-05T08:00:00.000",
  "startTime": "2025-01-05T08:00:00.000",
  "endTime": "2025-06-30T08:00:00.000",
  "campaign": {},
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bid": {
      "amount": "2.50",
      "currency": "USD"
    }
  },
  "targeting": {
    "supplyPlacement": {
      "include": ["MAPS_SEARCH_RESULTS", "MAPS_SEARCH_HOME"]
    },
    "lifetimeStorefronts": {
      "include": ["US", "CA"]
    },
    "supplySource": {
      "include": ["MAPS"]
    },
    "promotedLocationGroup": {
      "include": ["555666777"]
    },
    "promotedLocation": {
      "include": ["123456789"]
    }
  },
  "deviceClass": "IPHONE",
  "locationId": "123456789",
  "supplyPlacement": "MAPS_SEARCH_RESULTS"
}
```

## Topics

### Type Aliases
- [type BrandsReportingAdGroup.PricingModel](brandsreportingadgroup/pricingmodel-data.typealias.md)
  The unit of ad delivery the ad group is charged for, as captured at report time.
- [type BrandsReportingAdGroup.Status](brandsreportingadgroup/status-data.typealias.md)
  Advertiser-configurable serving status of the ad group at report time.
- [type BrandsReportingAdGroup.SystemStatus](brandsreportingadgroup/systemstatus-data.typealias.md)
  System-derived operational status of the ad group at report time.

## Properties

- `id` (int64): The ad group’s unique identifier.
- `campaignId` (int64): The campaign this ad group belongs to.
- `adAccountId` (int64): The ad account this ad group belongs to.
- `name` (string): The ad group name as configured at report time.
- `status` (BrandsReportingAdGroup.Status): Possible values: `ENABLED`, `PAUSED`.
- `deleted` (boolean): Whether the ad group has been soft-deleted.
- `systemStatus` (BrandsReportingAdGroup.SystemStatus): Possible values: `RUNNING`, `NOT_RUNNING`.
- `systemStatusReasons` ([AdGroupSystemStatusReason]): System-applied reasons contributing to the current `systemStatus`.
- `systemStatusLimitingReasons` ([string]): Status-limiting reasons applied based on advertiser and system factors.
- `automatedKeywordsOptIn` (boolean): Whether the ad group opted in to automated keywords.
- `automatedKeywordsRequired` (boolean): Whether automated keywords are required for this ad group.
- `pricingModel` (BrandsReportingAdGroup.PricingModel): Possible values: `CPA`, `CPM`, `CPT`.
- `displayStatus` (string): System-computed, rolled-up delivery state combining ad group and campaign conditions.
- `modificationTime` (date-time): Timestamp of the ad group’s last modification (ISO 8601).
- `creationTime` (date-time): Timestamp when the ad group was created (ISO 8601).
- `startTime` (date-time): Ad group start time.
- `endTime` (date-time): Ad group end time.
- `campaign` (ReportingCampaignMin): See [`ReportingCampaignMin`](reportingcampaignmin.md) for details.
- `bidStrategy` (ReportingBidStrategy): See [`ReportingBidStrategy`](reportingbidstrategy.md) for details.
- `targeting` (BrandsTargetingProjection): See [`BrandsTargetingProjection`](brandstargetingprojection.md) for details.
- `deviceClass` (string): Device class groupBy dimension value.
- `locationId` (string): Location ID groupBy dimension value.
- `supplyPlacement` (string): Supply placement groupBy dimension value.

## See Also

- [object BrandsReportingRequest](brandsreportingrequest.md)
  Request body for brands reporting queries.
- [object BrandsReportingCampaign](brandsreportingcampaign.md)
  Campaign metadata for Apple Maps report rows.
- [object BrandsReportingAd](brandsreportingad.md)
  Ad metadata for brands report rows.
- [object BrandsReportingCreative](brandsreportingcreative.md)
  Creative metadata for brands ads.
- [object BrandsReportingKeyword](brandsreportingkeyword.md)
  Keyword metadata for brands report rows, extending the base reporting keyword with brands-only internal fields.
- [object BrandsReportingSearchTerm](brandsreportingsearchterm.md)
  Search term metadata for brands report rows, extending the base reporting search term with brands-only internal fields.
- [object BrandsCampaignReportResponse](brandscampaignreportresponse.md)
  The top-level response envelope for Apple Maps campaign-level reports.
- [object BrandsCampaignReportRow](brandscampaignreportrow.md)
  A single row in an Apple Maps campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object BrandsCampaignReportSummary](brandscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apple Maps campaign report.
- [object BrandsCampaignResultContainer](brandscampaignresultcontainer.md)
  Wraps the array of Apple Maps campaign report rows along with a grand-total summary.
- [object BrandsAdGroupReportResponse](brandsadgroupreportresponse.md)
  The top-level response envelope for brands ad group reports.
- [object BrandsAdGroupReportRow](brandsadgroupreportrow.md)
  A single row in a Brands (Apple Maps) ad group report, pairing ad group metadata with total and granular performance metrics.
- [object BrandsAdGroupReportSummary](brandsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands ad group report.
- [object BrandsAdGroupResultContainer](brandsadgroupresultcontainer.md)
  Wraps the array of Brands ad group report rows along with a grand-total summary.
- [object BrandsAdReportResponse](brandsadreportresponse.md)
  The top-level response envelope for brands ad-level reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingadgroup)*