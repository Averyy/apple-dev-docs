# AppsKeywordReportResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The top-level response envelope for APPS keyword-level reports.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsKeywordReportResponse
```

#### Discussion

`AppsKeywordReportResponse` is the top-level response envelope for APPS keyword-level reports.

Keyword reports support `groupBy` dimensions such as `countryOrRegion` and `deviceClass`, which adds those dimension values to each row’s metadata.

##### Example

```json
{
  "result": {
    "rows": [
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
    ],
    "summary": {
      "grandTotal": {
        "localSpend": {
          "amount": "482.50",
          "currency": "USD"
        },
        "impressions": 152300,
        "taps": 3210,
        "ttr": 0.021,
        "totalInstalls": 768
      }
    }
  },
  "pagination": {
    "pageSize": 20,
    "offset": 0,
    "totalCount": 1
  }
}
```

## Properties

- `result` (AppsKeywordResultContainer): Contains the array of keyword report rows, each including keyword metadata, associated performance metrics, and an optional `insights.bidRecommendation`. See [`AppsKeywordResultContainer`](appskeywordresultcontainer.md) for details.
- `pagination` (ResponsePagination): Provides pagination state for navigating large result sets. See [`ResponsePagination`](responsepagination.md) for details.
- `error` (Error): See [`ErrorResponse`](errorresponse.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appskeywordreportresponse)*