# AppsSearchTermReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in an Apps search term report, pairing search-term metadata with total and granular performance metrics.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsSearchTermReportRow
```

#### Discussion

`AppsSearchTermReportRow` is a single row in an APPS search term report response. The `metadata` field captures the search term text and its associated keyword and ad group context at report time, while `totalMetrics` contains the aggregated performance figures across the full reporting period.

##### Example

```json
{
  "totalMetrics": {
    "localSpend": {
      "amount": "482.50",
      "currency": "USD"
    },
    "impressions": 152300,
    "taps": 3210,
    "ttr": 0.021,
    "cpt": {
      "amount": "0.15",
      "currency": "USD"
    },
    "cpm": {
      "amount": "3.17",
      "currency": "USD"
    },
    "tapInstalls": 640,
    "tapInstallCPI": {
      "amount": "0.75",
      "currency": "USD"
    },
    "totalNewDownloads": 710,
    "totalRedownloads": 58,
    "viewInstalls": 128,
    "totalInstalls": 768,
    "tapNewDownloads": 592,
    "tapRedownloads": 48,
    "viewNewDownloads": 118,
    "viewRedownloads": 10,
    "totalAvgCPI": {
      "amount": "0.63",
      "currency": "USD"
    },
    "totalInstallRate": 0.2393,
    "tapInstallRate": 0.1994,
    "tapPreOrdersPlaced": 22,
    "viewPreOrdersPlaced": 4,
    "totalPreOrdersPlaced": 26
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
      "cpt": {
        "amount": "0.15",
        "currency": "USD"
      },
      "cpm": {
        "amount": "3.17",
        "currency": "USD"
      },
      "tapInstalls": 320,
      "tapInstallCPI": {
        "amount": "0.75",
        "currency": "USD"
      },
      "totalNewDownloads": 355,
      "totalRedownloads": 29,
      "viewInstalls": 64,
      "totalInstalls": 384,
      "tapNewDownloads": 296,
      "tapRedownloads": 24,
      "viewNewDownloads": 59,
      "viewRedownloads": 5,
      "totalAvgCPI": {
        "amount": "0.63",
        "currency": "USD"
      },
      "totalInstallRate": 0.2393,
      "tapInstallRate": 0.1994,
      "tapPreOrdersPlaced": 11,
      "viewPreOrdersPlaced": 2,
      "totalPreOrdersPlaced": 13
    }
  ],
  "metadata": {
    "campaignId": 123456789,
    "adAccountId": 987654321,
    "searchTermText": "awayfinder travel app",
    "searchTermSource": "SEARCH",
    "keyword": {
      "id": 555666777,
      "campaignId": 123456789,
      "adAccountId": 987654321,
      "deleted": false,
      "text": "awayfinder travel app",
      "status": "ACTIVE",
      "matchType": "BROAD",
      "bid": {
        "currency": "USD",
        "amount": "1.50"
      },
      "adGroupId": 234567891,
      "modificationTime": "2025-01-10T08:00:00.000",
      "creationTime": "2025-01-05T08:00:00.000",
      "displayStatus": "RUNNING",
      "adGroup": {
        "name": "AwayFinder Search - Broad",
        "deleted": false
      },
      "countryOrRegion": "US",
      "deviceClass": "IPHONE"
    },
    "adGroupId": 234567891,
    "adGroup": {
      "name": "AwayFinder Search - Broad",
      "deleted": false
    },
    "countryOrRegion": "US",
    "deviceClass": "IPHONE"
  }
}
```

## Properties

- `totalMetrics` (AppsMetrics): See [`AppsMetrics`](appsmetrics.md) for details.
- `granularMetrics` ([AppsMetrics]): Time-series metrics broken down by the requested granularity (e.g., `DAILY`, `WEEKLY`). Present only when a `granularity` is specified in the request. When it isn’t, this field is absent and all data appears in `totalMetrics` instead.
- `metadata` (ReportingSearchTerm): See [`ReportingSearchTerm`](reportingsearchterm.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appssearchtermreportrow)*