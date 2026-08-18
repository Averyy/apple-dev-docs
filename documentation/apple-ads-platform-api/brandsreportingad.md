# BrandsReportingAd

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad metadata for brands report rows.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsReportingAd
```

#### Discussion

`BrandsReportingAd` is the ad metadata object embedded in `BRANDS` ad report rows. It provides the full organizational context (`adAccountId`, `campaignId`, `adGroupId`) and the ad’s operational state (`status`, `systemStatus`, `displayStatus`) as captured at report time.

The `creative` field embeds a `BrandsReportingCreative` summary with the creative type and validity status. The system populates the `BRANDS`-specific dimension fields (`deviceClass`, `locationId`, `supplyPlacement`) when the report’s `groupBy` specification includes those dimensions.

##### Example

```json
{
  "id": 555666777,
  "name": "AwayFinder - Brands Ad",
  "deleted": false,
  "status": "ENABLED",
  "systemStatus": "RUNNING",
  "systemStatusReasons": [],
  "systemStatusLimitingReasons": [],
  "adAccountId": 123456789,
  "campaignId": 987654321,
  "adGroupId": 246813579,
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-15T09:30:00.000",
  "displayStatus": "RUNNING",
  "creative": {
    "id": 135792468,
    "creativeType": "LOCAL_ADS_SEARCH_CREATIVE",
    "systemStatus": "VALID"
  },
  "deviceClass": "IPHONE",
  "locationId": "1",
  "supplyPlacement": "MAPS_SEARCH_RESULTS"
}
```

## Topics

### Type Aliases
- [type BrandsReportingAd.Status](brandsreportingad/status-data.typealias.md)
  Advertiser-configurable serving status of the ad at report time.
- [type BrandsReportingAd.SystemStatus](brandsreportingad/systemstatus-data.typealias.md)
  System-evaluated delivery state of the ad at report time.

## Properties

- `id` (int64): The ad’s unique identifier.
- `name` (string): The ad name as configured at report time.
- `deleted` (boolean): Whether the ad has been soft-deleted.
- `status` (BrandsReportingAd.Status): Possible values: `ENABLED`, `PAUSED`.
- `systemStatus` (BrandsReportingAd.SystemStatus): Possible values: `RUNNING`, `NOT_RUNNING`.
- `systemStatusReasons` ([AdSystemStatusReason]): System-applied reasons contributing to the current `systemStatus`.
- `systemStatusLimitingReasons` ([string]): Status-limiting reasons applied based on advertiser and system factors.
- `adAccountId` (int64): The ad account this ad belongs to.
- `campaignId` (int64): The campaign this ad belongs to.
- `adGroupId` (int64): The ad group this ad belongs to.
- `creationTime` (date-time): Timestamp when the ad was created (ISO 8601).
- `modificationTime` (date-time): Timestamp of the ad’s last modification (ISO 8601).
- `displayStatus` (string): System-computed, rolled-up delivery state combining ad, ad group, and campaign conditions.
- `creative` (BrandsReportingCreative): See [`BrandsReportingCreative`](brandsreportingcreative.md) for details.
- `deviceClass` (string): Device class groupBy dimension value.
- `locationId` (string): Location ID groupBy dimension value.
- `supplyPlacement` (string): Supply placement groupBy dimension value.

## See Also

- [object BrandsReportingRequest](brandsreportingrequest.md)
  Request body for brands reporting queries.
- [object BrandsReportingCampaign](brandsreportingcampaign.md)
  Campaign metadata for Apple Maps report rows.
- [object BrandsReportingAdGroup](brandsreportingadgroup.md)
  Ad group metadata for brands report rows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingad)*