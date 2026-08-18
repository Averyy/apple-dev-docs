# AppsReportingAd

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad metadata for APPS report rows.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsReportingAd
```

#### Discussion

`AppsReportingAd` is the ad metadata object embedded in APPS ad report rows. It captures the configuration and status of the ad at report time, providing the full organizational context (`adAccountId`, `campaignId`, `adGroupId`) alongside the ad’s operational state (`status`, `systemStatus`, `displayStatus`).

The `creative` field embeds an `AppsReportingCreative` summary capturing the creative type and system status, without needing a separate lookup.

##### Example

```json
{
  "id": 555666777,
  "name": "AwayFinder - Search Ad",
  "deleted": false,
  "status": "ENABLED",
  "systemStatus": "RUNNING",
  "systemStatusReasons": [],
  "systemStatusLimitingReasons": [],
  "adAccountId": 123456789,
  "campaignId": 234567890,
  "adGroupId": 345678901,
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-02-01T12:30:00.000",
  "displayStatus": "RUNNING",
  "creative": {
    "id": 456789012,
    "creativeType": "DEFAULT_PRODUCT_PAGE",
    "systemStatus": "VALID"
  },
  "countryOrRegion": "US",
  "deviceClass": "IPHONE"
}
```

## Topics

### Type Aliases
- [type AppsReportingAd.Status](appsreportingad/status-data.typealias.md)
  Advertiser-configurable serving state of the ad at report time.
- [type AppsReportingAd.SystemStatus](appsreportingad/systemstatus-data.typealias.md)
  System-evaluated delivery state of the ad at report time.

## Properties

- `id` (int64): The ad’s unique identifier.
- `name` (string): The ad name as configured at report time.
- `deleted` (boolean): Whether the ad has been soft-deleted.
- `status` (AppsReportingAd.Status): Possible values: `ENABLED`, `PAUSED`.
- `systemStatus` (AppsReportingAd.SystemStatus): Possible values: `RUNNING`, `NOT_RUNNING`.
- `systemStatusReasons` ([AdSystemStatusReason]): System-applied reasons contributing to the current `systemStatus`.
- `systemStatusLimitingReasons` ([string]): Status-limiting reasons applied based on advertiser and system factors.
- `adAccountId` (int64): The ad account this ad belongs to.
- `campaignId` (int64): The campaign this ad belongs to.
- `adGroupId` (int64): The ad group this ad belongs to.
- `creationTime` (date-time): Timestamp when the ad was created (ISO 8601).
- `modificationTime` (date-time): Timestamp of the ad’s last modification (ISO 8601).
- `displayStatus` (string): System-computed, rolled-up delivery state combining ad, ad group, and campaign conditions.
- `creative` (AppsReportingCreative): See [`AppsReportingCreative`](appsreportingcreative.md) for details.
- `countryOrRegion` (string): Country or region groupBy dimension value, populated when `countryOrRegion` is specified in the request’s `groupBy`.
- `deviceClass` (string): Device class groupBy dimension value, populated when `deviceClass` is specified in the request’s `groupBy`.

## See Also

- [object AppsReportingRequest](appsreportingrequest.md)
  Request body for APPS reporting queries.
- [object AppsReportingCampaign](appsreportingcampaign.md)
  Campaign metadata for APPS report rows.
- [object AppsReportingAdGroup](appsreportingadgroup.md)
  Ad group metadata for APPS report rows.
- [object AppsReportingCreative](appsreportingcreative.md)
  Creative metadata for APPS ads.
- [object AppsCampaignReportResponse](appscampaignreportresponse.md)
  The top-level response envelope for APPS campaign-level reports.
- [object AppsCampaignReportRow](appscampaignreportrow.md)
  A single row in an APPS campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object AppsCampaignReportSummary](appscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps campaign report.
- [object AppsCampaignResultContainer](appscampaignresultcontainer.md)
  Wraps the array of Apps campaign report rows along with a grand-total summary.
- [object AppsAdGroupReportResponse](appsadgroupreportresponse.md)
  The top-level response envelope for APPS ad group reports.
- [object AppsAdGroupReportRow](appsadgroupreportrow.md)
  A single row in an Apps ad group report, containing ad group metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdGroupReportSummary](appsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad group report.
- [object AppsAdGroupResultContainer](appsadgroupresultcontainer.md)
  Wraps the array of Apps ad group report rows along with a grand-total summary.
- [object AppsAdReportResponse](appsadreportresponse.md)
  The top-level response envelope for APPS ad-level reports.
- [object AppsAdReportRow](appsadreportrow.md)
  A single row in an Apps ad-level report, containing ad metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdReportSummary](appsadreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad-level report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingad)*