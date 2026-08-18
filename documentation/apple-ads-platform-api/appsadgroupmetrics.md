# AppsAdGroupMetrics

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad group-level metrics for APPS, inheriting all properties from `AppsMetrics`.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsAdGroupMetrics
```

#### Discussion

`AppsAdGroupMetrics` extends [`AppsMetrics`](appsmetrics.md) with no additional fields. It is the metrics object embedded in APPS ad group report rows.

## Properties

- `cpm` (Money)
- `cpt` (Money)
- `date` (date)
- `impressions` (int64)
- `localSpend` (Money)
- `tapInstallCPI` (Money)
- `tapInstallRate` (number)
- `tapInstalls` (int64)
- `tapNewDownloads` (int64)
- `tapPreOrdersPlaced` (int64)
- `tapRedownloads` (int64)
- `taps` (int64)
- `totalAvgCPI` (Money)
- `totalInstallRate` (number)
- `totalInstalls` (int64)
- `totalNewDownloads` (int64)
- `totalPreOrdersPlaced` (int64)
- `totalRedownloads` (int64)
- `ttr` (number)
- `viewInstalls` (int64)
- `viewNewDownloads` (int64)
- `viewPreOrdersPlaced` (int64)
- `viewRedownloads` (int64)

## See Also

- [object AppsReportingRequest](appsreportingrequest.md)
  Request body for APPS reporting queries.
- [object AppsReportingCampaign](appsreportingcampaign.md)
  Campaign metadata for APPS report rows.
- [object AppsReportingAdGroup](appsreportingadgroup.md)
  Ad group metadata for APPS report rows.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsadgroupmetrics)*