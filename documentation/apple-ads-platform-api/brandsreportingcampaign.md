# BrandsReportingCampaign

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Campaign metadata for Apple Maps report rows.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsReportingCampaign
```

#### Discussion

`BrandsReportingCampaign` is the campaign metadata object embedded in `BRANDS` campaign report rows. It captures the campaign’s full configuration at report time: identity, budget (`dailyBudget`), bid strategy, billing event, and the `BrandsTargetingProjection` snapshot of active supply placement and location targeting.

`promotedObjectType` is always `BUSINESS_BRAND` for Maps-based campaigns. The system populates the `BRANDS` dimension fields (`deviceClass`, `locationId`, `supplyPlacement`) based on the `groupBy` dimensions in the report request.

##### Example

```json
{
  "id": 555666777,
  "promotedObject": {
    "name": "AwayFinder Downtown"
  },
  "promotedObjectType": "BUSINESS_BRAND",
  "promotedObjectId": "123456789",
  "name": "AwayFinder Apple Maps Campaign",
  "status": "ENABLED",
  "deleted": false,
  "displayStatus": "RUNNING",
  "modificationTime": "2025-01-10T08:00:00.000",
  "creationTime": "2025-01-05T08:00:00.000",
  "adAccountId": 987654321,
  "systemStatus": "RUNNING",
  "systemStatusReasons": [],
  "billingEvent": "IMPRESSIONS",
  "systemStatusLimitingReasons": [],
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
  "dailyBudget": {
    "value": {
      "amount": "50.00",
      "currency": "USD"
    }
  },
  "startTime": "2025-01-10T08:00:00.000",
  "endTime": "2025-12-31T08:00:00.000",
  "lifetimeBudget": {
    "value": {
      "amount": "5000.00",
      "currency": "USD"
    }
  },
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bid": {
      "amount": "1.50",
      "currency": "USD"
    }
  },
  "adChannelType": "SEARCH",
  "deviceClass": "IPHONE",
  "locationId": "123456789",
  "supplyPlacement": "MAPS_SEARCH_RESULTS"
}
```

## Topics

### Type Aliases
- [type BrandsReportingCampaign.AdChannelType](brandsreportingcampaign/adchanneltype-data.typealias.md)
  The advertising channel type of the campaign at report time.
- [type BrandsReportingCampaign.BillingEvent](brandsreportingcampaign/billingevent-data.typealias.md)
  The billing event of the campaign at report time.
- [type BrandsReportingCampaign.Status](brandsreportingcampaign/status-data.typealias.md)
  Advertiser-configurable serving status of the campaign at report time.
- [type BrandsReportingCampaign.SystemStatus](brandsreportingcampaign/systemstatus-data.typealias.md)
  System-evaluated delivery state of the campaign at report time.

## Properties

- `id` (int64): The campaign’s unique identifier.
- `promotedObject` (PromotedObject): See [`PromotedObject`](promotedobject.md) for details.
- `promotedObjectType` (string): Possible values: `BUSINESS_BRAND`.
- `promotedObjectId` (string): The brand ID of the promoted Maps business.
- `name` (string): The campaign name as configured at report time.
- `status` (BrandsReportingCampaign.Status): Possible values: `ENABLED`, `PAUSED`.
- `deleted` (boolean): Whether the campaign has been soft-deleted.
- `displayStatus` (string): System-computed, rolled-up delivery state combining `status` and `systemStatus` into a single label. See [`CampaignDisplayStatus`](campaigndisplaystatus.md).
- `modificationTime` (date-time): Timestamp of the campaign’s last modification (ISO 8601).
- `creationTime` (date-time): Timestamp when the campaign was created (ISO 8601).
- `adAccountId` (int64): The ad account this campaign belongs to.
- `systemStatus` (BrandsReportingCampaign.SystemStatus): Possible values: `RUNNING`, `NOT_RUNNING`.
- `systemStatusReasons` ([CampaignSystemStatusReason]): System-applied reasons contributing to the current `systemStatus`. See [`CampaignSystemStatusReason`](campaignsystemstatusreason.md) for possible values.
- `billingEvent` (BrandsReportingCampaign.BillingEvent): Possible values: `TAPS`, `IMPRESSIONS`.
- `systemStatusLimitingReasons` ([string]): System-applied reasons limiting delivery below maximum potential. See [`CampaignSystemLimitedStatusReason`](campaignsystemlimitedstatusreason.md) for possible values.
- `targeting` (BrandsTargetingProjection): See [`BrandsTargetingProjection`](brandstargetingprojection.md) for details.
- `dailyBudget` (ReportingMoney): See [`ReportingMoney`](reportingmoney.md) for details.
- `startTime` (date-time): Campaign start time.
- `endTime` (date-time): Campaign end time.
- `lifetimeBudget` (ReportingMoney): Lifetime budget for the campaign. See [`ReportingMoney`](reportingmoney.md) for details.
- `bidStrategy` (ReportingBidStrategy): See [`ReportingBidStrategy`](reportingbidstrategy.md) for details.
- `adChannelType` (BrandsReportingCampaign.AdChannelType): The advertising channel type for this campaign. Possible values: `SEARCH`, `DISPLAY`.
- `deviceClass` (string): Device class groupBy dimension value.
- `locationId` (string): Location ID groupBy dimension value.
- `supplyPlacement` (string): Supply placement groupBy dimension value.

## See Also

- [object BrandsReportingRequest](brandsreportingrequest.md)
  Request body for brands reporting queries.
- [object BrandsReportingAdGroup](brandsreportingadgroup.md)
  Ad group metadata for brands report rows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcampaign)*