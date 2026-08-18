# AppsKeywordReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in an APPS keyword report, containing keyword metadata, performance metrics, and optional bid recommendation insights.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsKeywordReportRow
```

#### Discussion

`AppsKeywordReportRow` is a single row in an APPS keyword report response. The `metadata` field captures keyword identifiers and configuration at report time, and `totalMetrics` contains the aggregated performance figures across the full reporting period.

##### Example

```json
{
  "metadata": {
    "id": 888999000,
    "text": "productivity app",
    "matchType": "BROAD",
    "adAccountId": 123456789,
    "campaignId": 444555666,
    "adGroupId": 555666777,
    "status": "ACTIVE",
    "deleted": false
  },
  "totalMetrics": {
    "localSpend": {
      "amount": "75.00",
      "currency": "USD"
    },
    "impressions": 5000,
    "taps": 250,
    "ttr": 0.05,
    "cpt": {
      "amount": "0.30",
      "currency": "USD"
    },
    "tapInstalls": 60,
    "totalInstalls": 72
  },
  "granularMetrics": [
    {
      "date": "2025-01-01",
      "localSpend": {
        "amount": "2.40",
        "currency": "USD"
      },
      "impressions": 160,
      "taps": 8,
      "tapInstalls": 2
    }
  ],
  "insights": {
    "bidRecommendation": {
      "suggestedBidAmount": 1.25
    }
  }
}
```

## Properties

- `totalMetrics` (AppsMetrics): See [`AppsMetrics`](appsmetrics.md) for details.
- `granularMetrics` ([AppsMetrics]): Time-series metrics broken down by the requested granularity (e.g., `DAILY`, `WEEKLY`). Present only when a `granularity` is specified in the request. When it isn’t, this field is absent and all data appears in `totalMetrics` instead.
- `metadata` (ReportingKeyword): See [`ReportingKeyword`](reportingkeyword.md) for details.
- `insights` (KeywordInsights): Optional keyword insights, including a `bidRecommendation` suggested bid amount for the keyword. See [`KeywordInsights`](keywordinsights.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appskeywordreportrow)*