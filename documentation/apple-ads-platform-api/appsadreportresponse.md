# AppsAdReportResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The top-level response envelope for APPS ad-level reports.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsAdReportResponse
```

#### Discussion

`AppsAdReportResponse` is the top-level response envelope for APPS ad-level reports.

Check for `error` before processing `result`. Note that ad-level reports do not support `HOURLY` granularity.

##### Example

```json
{
  "result": {
    "rows": [
      {
        "metadata": {
          "id": 234567891,
          "name": "AwayFinder Default Ad",
          "adAccountId": 123456789,
          "campaignId": 444555666,
          "adGroupId": 555666777,
          "status": "ENABLED",
          "deleted": false
        },
        "totalMetrics": {
          "localSpend": {
            "amount": "150.00",
            "currency": "USD"
          },
          "impressions": 10000,
          "taps": 500,
          "ttr": 0.05,
          "cpt": {
            "amount": "0.30",
            "currency": "USD"
          },
          "tapInstalls": 120,
          "totalInstalls": 145
        },
        "granularMetrics": [
          {
            "date": "2025-01-01",
            "localSpend": {
              "amount": "4.80",
              "currency": "USD"
            },
            "impressions": 330,
            "taps": 16,
            "tapInstalls": 4
          }
        ]
      }
    ],
    "summary": {
      "grandTotal": {
        "localSpend": {
          "amount": "150.00",
          "currency": "USD"
        },
        "impressions": 10000,
        "taps": 500,
        "tapInstalls": 120
      }
    }
  },
  "pagination": {
    "offset": 0,
    "pageSize": 20,
    "totalCount": 1
  }
}
```

## Properties

- `result` (AppsAdResultContainer): Wraps the array of ad report rows, each containing ad metadata and associated metrics. See [`AppsAdResultContainer`](appsadresultcontainer.md) for details.
- `pagination` (ResponsePagination): Allows paging through all matching ads. See [`ResponsePagination`](responsepagination.md) for details.
- `error` (Error): Populated with an `ErrorResponse` when the request fails. See [`ErrorResponse`](errorresponse.md) for details.

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
- [object AppsAdReportRow](appsadreportrow.md)
  A single row in an Apps ad-level report, containing ad metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdReportSummary](appsadreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad-level report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsadreportresponse)*