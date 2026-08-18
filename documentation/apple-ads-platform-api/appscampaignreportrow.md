# AppsCampaignReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in an APPS campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsCampaignReportRow
```

#### Discussion

`AppsCampaignReportRow` is a single row in an APPS campaign report response. The `metadata` field captures campaign identifiers and configuration at report time, while `totalMetrics` contains the aggregated performance figures across the full reporting period.

##### Example

```json
{
  "metadata": {
    "id": 555666777,
    "promotedObjectType": "APPSTORE_APP",
    "promotedObjectId": "987654321",
    "name": "AwayFinder - App Campaign",
    "status": "ENABLED",
    "deleted": false,
    "displayStatus": "RUNNING",
    "modificationTime": "2025-01-10T08:00:00.000",
    "creationTime": "2024-11-01T08:00:00.000",
    "adAccountId": 123456789,
    "systemStatus": "RUNNING",
    "systemStatusReasons": [],
    "billingEvent": "TAPS",
    "systemStatusLimitingReasons": [],
    "dailyBudget": {
      "value": {
        "amount": "100.00",
        "currency": "USD"
      }
    },
    "startTime": "2024-11-01T08:00:00.000",
    "endTime": null,
    "bidStrategy": {
      "bidStrategyType": "MANUAL_CPT",
      "bid": {
        "amount": "1.50",
        "currency": "USD"
      }
    },
    "adChannelType": "SEARCH"
  },
  "totalMetrics": {
    "localSpend": {
      "amount": "482.50",
      "currency": "USD"
    },
    "impressions": 152300,
    "taps": 3210,
    "ttr": 0.021,
    "totalInstalls": 768
  },
  "granularMetrics": [
    {
      "date": "2025-01-10",
      "localSpend": {
        "amount": "241.25",
        "currency": "USD"
      },
      "impressions": 76150,
      "taps": 1605,
      "ttr": 0.021,
      "totalInstalls": 384
    },
    {
      "date": "2025-01-11",
      "localSpend": {
        "amount": "241.25",
        "currency": "USD"
      },
      "impressions": 76150,
      "taps": 1605,
      "ttr": 0.021,
      "totalInstalls": 384
    }
  ]
}
```

## Properties

- `totalMetrics` (AppsCampaignMetrics): See [`AppsCampaignMetrics`](appscampaignmetrics.md) for details.
- `granularMetrics` ([AppsCampaignMetrics]): Time-series metrics broken down by the requested granularity (e.g., `DAILY`, `WEEKLY`). Present only when a `granularity` is specified in the request. When it isn’t, this field is absent and all data appears in `totalMetrics` instead.
- `metadata` (AppsReportingCampaign): See [`AppsReportingCampaign`](appsreportingcampaign.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appscampaignreportrow)*