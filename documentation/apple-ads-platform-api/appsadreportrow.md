# AppsAdReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in an Apps ad-level report, containing ad metadata, total metrics, and optional granular time-series metrics.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsAdReportRow
```

#### Discussion

`AppsAdReportRow` is a single row in an APPS ad-level report response. The `metadata` field captures ad identifiers and configuration at report time, while `totalMetrics` contains the aggregated performance figures across the full reporting period.

##### Example

```json
{
  "metadata": {
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
    "storefront": "US"
  },
  "totalMetrics": {
    "localSpend": {
      "amount": "482.50",
      "currency": "USD"
    },
    "impressions": 41230,
    "taps": 980,
    "ttr": 0.0238,
    "cpt": {
      "amount": "0.49",
      "currency": "USD"
    },
    "cpm": {
      "amount": "11.71",
      "currency": "USD"
    },
    "tapInstalls": 312,
    "tapInstallCPI": {
      "amount": "1.55",
      "currency": "USD"
    },
    "totalNewDownloads": 298,
    "totalRedownloads": 41,
    "viewInstalls": 27,
    "totalInstalls": 339,
    "tapNewDownloads": 285,
    "tapRedownloads": 27,
    "viewNewDownloads": 13,
    "viewRedownloads": 14,
    "totalAvgCPI": {
      "amount": "1.42",
      "currency": "USD"
    },
    "totalInstallRate": 0.346,
    "tapInstallRate": 0.318,
    "tapPreOrdersPlaced": 5,
    "viewPreOrdersPlaced": 1,
    "totalPreOrdersPlaced": 6
  },
  "granularMetrics": [
    {
      "date": "2025-02-01",
      "localSpend": {
        "amount": "17.25",
        "currency": "USD"
      },
      "impressions": 1450,
      "taps": 34,
      "ttr": 0.0234,
      "cpt": {
        "amount": "0.51",
        "currency": "USD"
      },
      "cpm": {
        "amount": "11.90",
        "currency": "USD"
      },
      "tapInstalls": 11,
      "tapInstallCPI": {
        "amount": "1.57",
        "currency": "USD"
      },
      "totalNewDownloads": 10,
      "totalRedownloads": 2,
      "viewInstalls": 1,
      "totalInstalls": 12,
      "tapNewDownloads": 10,
      "tapRedownloads": 1,
      "viewNewDownloads": 0,
      "viewRedownloads": 1,
      "totalAvgCPI": {
        "amount": "1.44",
        "currency": "USD"
      },
      "totalInstallRate": 0.353,
      "tapInstallRate": 0.324,
      "tapPreOrdersPlaced": 0,
      "viewPreOrdersPlaced": 0,
      "totalPreOrdersPlaced": 0
    }
  ]
}
```

## Properties

- `totalMetrics` (AppsMetrics): See [`AppsMetrics`](appsmetrics.md) for details.
- `granularMetrics` ([AppsMetrics]): Time-series metrics broken down by the requested granularity (e.g., `DAILY`, `WEEKLY`). Present only when a `granularity` is specified in the request. When it isn’t, this field is absent and all data appears in `totalMetrics` instead.
- `metadata` (AppsReportingAd): See [`AppsReportingAd`](appsreportingad.md) for details.

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
- [object AppsAdReportSummary](appsadreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad-level report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsadreportrow)*