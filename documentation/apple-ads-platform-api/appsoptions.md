# AppsOptions

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Reporting options for apps promoted object type reports.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object AppsOptions
```

#### Discussion

The `AppsOptions` configures optional row behavior for apps report responses. Omitting `options` entirely returns only rows with actual metric data and no summary row.

##### Example

```json
{
  "includeRows": ["GRAND_TOTAL"]
}
```

## Properties

- `includeRows` ([string]): Row inclusion options. Values: `GRAND_TOTAL` (include grand total rows), `EMPTY_METRICS` (include rows with empty metrics, equivalent to `returnRowsWithNoMetrics=true` in v5). Note: `EMPTY_METRICS` cannot be specified if `groupBy` is also specified.

## See Also

- [object AppsReportingRequest](appsreportingrequest.md)
  Request body for apps reporting queries.
- [object AppsReportingCampaign](appsreportingcampaign.md)
  Campaign metadata for apps report rows.
- [object AppsReportingAdGroup](appsreportingadgroup.md)
  Ad group metadata for apps report rows.
- [object AppsReportingAd](appsreportingad.md)
  Ad metadata for apps report rows.
- [object AppsReportingCreative](appsreportingcreative.md)
  Creative metadata for apps ads.
- [object AppsCampaignReportResponse](appscampaignreportresponse.md)
  The top-level response envelope for apps campaign-level reports.
- [object AppsCampaignReportRow](appscampaignreportrow.md)
  A single row in an apps campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object AppsCampaignReportSummary](appscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps campaign report.
- [object AppsCampaignResultContainer](appscampaignresultcontainer.md)
  Wraps the array of Apps campaign report rows along with a grand-total summary.
- [object AppsAdGroupReportResponse](appsadgroupreportresponse.md)
  The top-level response envelope for apps ad group reports.
- [object AppsAdGroupReportRow](appsadgroupreportrow.md)
  A single row in an Apps ad group report, containing ad group metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdGroupReportSummary](appsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad group report.
- [object AppsAdGroupResultContainer](appsadgroupresultcontainer.md)
  Wraps the array of Apps ad group report rows along with a grand-total summary.
- [object AppsAdReportResponse](appsadreportresponse.md)
  The top-level response envelope for apps ad-level reports.
- [object AppsAdReportRow](appsadreportrow.md)
  A single row in an Apps ad-level report, containing ad metadata, total metrics, and optional granular time-series metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsoptions)*