# AppsAdGroupReportResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The top-level response envelope for APPS ad group reports.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsAdGroupReportResponse
```

#### Discussion

`AppsAdGroupReportResponse` is the top-level response envelope for APPS ad group reports.

Check for the presence of `error` before processing `result` to handle failure cases cleanly.

##### Example

```json
{
  "result": {
    "rows": [
      {
        "totalMetrics": {
          "date": "2025-01-10",
          "localSpend": {
            "amount": "412.75",
            "currency": "USD"
          },
          "impressions": 305000,
          "taps": 5100,
          "ttr": 0.0167,
          "totalInstalls": 640,
          "totalAvgCPI": {
            "amount": "0.64",
            "currency": "USD"
          }
        },
        "granularMetrics": [],
        "metadata": {
          "id": 555666777,
          "campaignId": 987654321,
          "adAccountId": 123456789,
          "name": "AwayFinder - Apps Ad Group",
          "status": "ENABLED",
          "deleted": false,
          "creationTime": "2025-01-10T08:00:00.000",
          "modificationTime": "2025-01-10T08:00:00.000"
        }
      }
    ],
    "summary": {
      "grandTotal": {
        "date": "2025-01-10",
        "localSpend": {
          "amount": "412.75",
          "currency": "USD"
        },
        "impressions": 305000,
        "taps": 5100,
        "ttr": 0.0167,
        "totalInstalls": 640,
        "totalAvgCPI": {
          "amount": "0.64",
          "currency": "USD"
        }
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

- `result` (AppsAdGroupResultContainer): Wraps the array of report rows. See [`AppsAdGroupResultContainer`](appsadgroupresultcontainer.md) for details.
- `pagination` (ResponsePagination): Pagination metadata to support paging through large result sets. See [`ResponsePagination`](responsepagination.md) for details.
- `error` (Error): Populated with an `ErrorResponse` when the request fails or partially fails. See [`ErrorResponse`](errorresponse.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsadgroupreportresponse)*