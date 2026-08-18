# AppsReportingAdGroup

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad group metadata for APPS report rows.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsReportingAdGroup
```

#### Discussion

`AppsReportingAdGroup` is the ad group metadata object embedded in APPS ad group report rows. It captures the ad group’s configuration at report time, including its `pricingModel` (`CPA`, `CPM`, or `CPT`) and `bidStrategy`. The `campaign` field provides a lightweight `ReportingCampaignMin` summary for quick access to the parent campaign context.

The response populates the dimension fields (`countryOrRegion`, `deviceClass`, `gender`, `ageRange`, `locality`, `countryCode`, `adminArea`) based on which `groupBy` dimensions you specify in the report request. Each populated dimension field generates one report row per unique value of that dimension.

##### Example

```json
{
  "id": 555666777,
  "campaignId": 123456789,
  "adAccountId": 987654321,
  "name": "AwayFinder - Search Ad Group",
  "status": "ENABLED",
  "deleted": false,
  "systemStatus": "RUNNING",
  "systemStatusReasons": [],
  "systemStatusLimitingReasons": [],
  "automatedKeywordsOptIn": false,
  "automatedKeywordsRequired": false,
  "pricingModel": "CPT",
  "displayStatus": "RUNNING",
  "modificationTime": "2025-01-10T08:00:00.000",
  "creationTime": "2025-01-05T08:00:00.000",
  "startTime": "2025-01-05T08:00:00.000",
  "endTime": null,
  "campaign": {},
  "cpaCap": {
    "value": {
      "amount": "5.00",
      "currency": "USD"
    }
  },
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bid": {
      "amount": "2.50",
      "currency": "USD"
    }
  },
  "countryOrRegion": "US",
  "deviceClass": "IPHONE",
  "gender": "M",
  "ageRange": "25-34",
  "locality": "San Francisco",
  "countryCode": "US",
  "adminArea": "CA"
}
```

## Topics

### Type Aliases
- [type AppsReportingAdGroup.PricingModel](appsreportingadgroup/pricingmodel-data.typealias.md)
  The pricing model of the ad group at report time.
- [type AppsReportingAdGroup.Status](appsreportingadgroup/status-data.typealias.md)
  Advertiser-configurable serving state of the ad group at report time.
- [type AppsReportingAdGroup.SystemStatus](appsreportingadgroup/systemstatus-data.typealias.md)
  System-evaluated delivery state of the ad group at report time.

## Properties

- `id` (int64): The ad group’s unique identifier.
- `campaignId` (int64): The campaign this ad group belongs to.
- `adAccountId` (int64): The ad account this ad group belongs to.
- `name` (string): The ad group name as configured at report time.
- `status` (AppsReportingAdGroup.Status): Possible values: `ENABLED`, `PAUSED`.
- `deleted` (boolean): Whether the ad group has been soft-deleted.
- `systemStatus` (AppsReportingAdGroup.SystemStatus): Possible values: `RUNNING`, `NOT_RUNNING`.
- `systemStatusReasons` ([AdGroupSystemStatusReason]): System-applied reasons contributing to the current `systemStatus`.
- `systemStatusLimitingReasons` ([string]): Status-limiting reasons applied based on advertiser and system factors.
- `automatedKeywordsOptIn` (boolean): Whether the ad group opted in to automated keywords.
- `automatedKeywordsRequired` (boolean): Whether automated keywords are required for this ad group.
- `pricingModel` (AppsReportingAdGroup.PricingModel): Possible values: `CPA`, `CPM`, `CPT`.
- `displayStatus` (string): System-computed, rolled-up delivery state combining ad group and campaign conditions.
- `modificationTime` (date-time): Timestamp of the ad group’s last modification (ISO 8601).
- `creationTime` (date-time): Timestamp when the ad group was created (ISO 8601).
- `startTime` (date-time): Ad group start time.
- `endTime` (date-time): Ad group end time.
- `campaign` (ReportingCampaignMin): See [`ReportingCampaignMin`](reportingcampaignmin.md) for details.
- `cpaCap` (ReportingMoney): CPA cap amount. See [`ReportingMoney`](reportingmoney.md) for details.
- `bidStrategy` (ReportingBidStrategy): See [`ReportingBidStrategy`](reportingbidstrategy.md) for details.
- `countryOrRegion` (string): Country or region groupBy dimension value.
- `deviceClass` (string): Device class groupBy dimension value.
- `gender` (string): Gender groupBy dimension value.
- `ageRange` (string): Age range groupBy dimension value.
- `locality` (string): Locality groupBy dimension value.
- `countryCode` (string): Country code groupBy dimension value.
- `adminArea` (string): Administrative area groupBy dimension value.

## See Also

- [object AppsReportingRequest](appsreportingrequest.md)
  Request body for APPS reporting queries.
- [object AppsReportingCampaign](appsreportingcampaign.md)
  Campaign metadata for APPS report rows.
- [object AppsReportingAd](appsreportingad.md)
  Ad metadata for APPS report rows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingadgroup)*