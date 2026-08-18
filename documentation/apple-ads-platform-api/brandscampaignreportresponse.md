# BrandsCampaignReportResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The top-level response envelope for Apple Maps campaign-level reports.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsCampaignReportResponse
```

#### Discussion

`BrandsCampaignReportResponse` is the top-level response envelope for `BRANDS` campaign-level reports.

`BRANDS` campaign reports support `groupBy` dimensions `deviceClass`, `locationId`, and `supplyPlacement`.

##### Example

```json
{
  "result": {
    "rows": [
      {
        "metadata": {
          "id": 444555999,
          "name": "AwayFinder - Brand Q1",
          "adAccountId": 123456789,
          "promotedObjectType": "BUSINESS_BRAND",
          "promotedObjectId": "9151314442816847872",
          "promotedObject": {
            "name": "AwayFinder"
          },
          "bidStrategy": {
            "bidStrategyType": "MAX_ENGAGEMENTS"
          },
          "status": "ENABLED",
          "deleted": false,
          "locationId": "loc-001"
        },
        "totalMetrics": {
          "localSpend": {
            "amount": "4200.00",
            "currency": "USD"
          },
          "impressions": 420000,
          "taps": 8400,
          "ttr": 0.02,
          "cpt": {
            "amount": "0.50",
            "currency": "USD"
          },
          "firstActions": {
            "tap": 170
          },
          "actions": {
            "tap": 170
          },
          "getDirections": {
            "tap": 1260
          }
        },
        "granularMetrics": [
          {
            "date": "2025-01-10",
            "localSpend": {
              "amount": "42.00",
              "currency": "USD"
            },
            "impressions": 4200,
            "taps": 84,
            "actions": {
              "tap": 21
            },
            "getDirections": {
              "tap": 13
            }
          }
        ]
      }
    ],
    "summary": {
      "grandTotal": {
        "localSpend": {
          "amount": "4200.00",
          "currency": "USD"
        },
        "impressions": 420000,
        "taps": 8400
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

- `result` (BrandsCampaignResultContainer): Contains the array of campaign report rows. Each row includes the campaign `metadata`, capturing targeting, budget, and status at report time, along with `totalMetrics` and optional `granularMetrics`. See [`BrandsCampaignResultContainer`](brandscampaignresultcontainer.md) for details.
- `pagination` (ResponsePagination): Provided for iterating through large result sets. See [`ResponsePagination`](responsepagination.md) for details.
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
- [object BrandsAdReportResponse](brandsadreportresponse.md)
  The top-level response envelope for brands ad-level reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandscampaignreportresponse)*