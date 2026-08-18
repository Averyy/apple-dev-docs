# BrandsAdReportResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The top-level response envelope for brands ad-level reports.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsAdReportResponse
```

#### Discussion

`BrandsAdReportResponse` is the top-level response envelope for `BRANDS` ad-level reports.

Note that ad-level reports do not support `HOURLY` granularity.

##### Example

```json
{
  "result": {
    "rows": [
      {
        "totalMetrics": {
          "date": "2025-01-10",
          "localSpend": {
            "amount": "845.50",
            "currency": "USD"
          },
          "impressions": 620000,
          "taps": 9800,
          "ttr": 0.0158,
          "cpt": {
            "amount": "0.09",
            "currency": "USD"
          },
          "cpm": {
            "amount": "1.36",
            "currency": "USD"
          }
        },
        "granularMetrics": [],
        "metadata": {
          "id": 555666777,
          "name": "AwayFinder - Brands Ad",
          "deleted": false,
          "status": "ENABLED",
          "systemStatus": "RUNNING",
          "adAccountId": 123456789,
          "campaignId": 987654321,
          "adGroupId": 111222333,
          "creationTime": "2025-01-10T08:00:00.000",
          "modificationTime": "2025-01-10T08:00:00.000",
          "displayStatus": "RUNNING",
          "creative": {
            "creativeType": "LOCAL_ADS_SEARCH_CREATIVE"
          },
          "deviceClass": "IPHONE",
          "locationId": 444555666,
          "supplyPlacement": "MAPS_SEARCH_RESULTS"
        }
      }
    ],
    "summary": {
      "grandTotal": {
        "date": "2025-01-10",
        "localSpend": {
          "amount": "845.50",
          "currency": "USD"
        },
        "impressions": 620000,
        "taps": 9800,
        "ttr": 0.0158,
        "cpt": {
          "amount": "0.09",
          "currency": "USD"
        },
        "cpm": {
          "amount": "1.36",
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

- `result` (BrandsAdResultContainer): Wraps the report rows, each including ad metadata (including creative type and the `BRANDS`-specific groupBy dimensions `deviceClass`, `locationId`, and `supplyPlacement`) and associated performance metrics. See [`BrandsAdResultContainer`](brandsadresultcontainer.md) for details.
- `pagination` (ResponsePagination): See [`ResponsePagination`](responsepagination.md) for details.
- `error` (Error): See [`ErrorResponse`](errorresponse.md) for details.

## See Also

- [object BrandsReportingRequest](brandsreportingrequest.md)
  Request body for brands reporting queries.
- [object BrandsReportingCampaign](brandsreportingcampaign.md)
  Campaign metadata for Apple Maps report rows.
- [object BrandsReportingAdGroup](brandsreportingadgroup.md)
  Ad group metadata for brands report rows.
- [object BrandsReportingAd](brandsreportingad.md)
  Ad metadata for brands report rows.
- [object BrandsReportingCreative](brandsreportingcreative.md)
  Creative metadata for brands ads.
- [object BrandsReportingKeyword](brandsreportingkeyword.md)
  Keyword metadata for brands report rows, extending the base reporting keyword with brands-only internal fields.
- [object BrandsReportingSearchTerm](brandsreportingsearchterm.md)
  Search term metadata for brands report rows, extending the base reporting search term with brands-only internal fields.
- [object BrandsCampaignReportResponse](brandscampaignreportresponse.md)
  The top-level response envelope for Apple Maps campaign-level reports.
- [object BrandsCampaignReportRow](brandscampaignreportrow.md)
  A single row in an Apple Maps campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object BrandsCampaignReportSummary](brandscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apple Maps campaign report.
- [object BrandsCampaignResultContainer](brandscampaignresultcontainer.md)
  Wraps the array of Apple Maps campaign report rows along with a grand-total summary.
- [object BrandsAdGroupReportResponse](brandsadgroupreportresponse.md)
  The top-level response envelope for brands ad group reports.
- [object BrandsAdGroupReportRow](brandsadgroupreportrow.md)
  A single row in a Brands (Apple Maps) ad group report, pairing ad group metadata with total and granular performance metrics.
- [object BrandsAdGroupReportSummary](brandsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands ad group report.
- [object BrandsAdGroupResultContainer](brandsadgroupresultcontainer.md)
  Wraps the array of Brands ad group report rows along with a grand-total summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsadreportresponse)*