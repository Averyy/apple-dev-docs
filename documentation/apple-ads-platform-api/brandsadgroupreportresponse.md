# BrandsAdGroupReportResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The top-level response envelope for brands ad group reports.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsAdGroupReportResponse
```

#### Discussion

`BrandsAdGroupReportResponse` is the top-level response envelope for `BRANDS` ad group reports.

`BRANDS` ad group reports support `groupBy` dimensions `deviceClass`, `locationId`, and `supplyPlacement`.

##### Example

```json
{
  "result": {
    "rows": [
      {
        "metadata": {
          "id": 555666888,
          "name": "AwayFinder - SF Metro Locations",
          "adAccountId": 123456789,
          "campaignId": 444555999,
          "status": "ENABLED",
          "deleted": false,
          "locationId": "loc-002"
        },
        "totalMetrics": {
          "localSpend": {
            "amount": "4200.00",
            "currency": "USD"
          },
          "impressions": 420000,
          "taps": 8400,
          "ttr": 0.02
        },
        "granularMetrics": [
          {
            "date": "2025-01-10",
            "localSpend": {
              "amount": "420.00",
              "currency": "USD"
            },
            "impressions": 42000,
            "taps": 840
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
    "offset": 0,
    "pageSize": 20,
    "totalCount": 1
  }
}
```

## Properties

- `result` (BrandsAdGroupResultContainer): Wraps the array of report rows, each containing the ad group `metadata` (including targeting configuration) and performance metrics segmented by the requested `groupBy` dimensions. See [`BrandsAdGroupResultContainer`](brandsadgroupresultcontainer.md) for details.
- `pagination` (ResponsePagination): Returned for paging through large result sets. See [`ResponsePagination`](responsepagination.md) for details.
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
- [object BrandsAdGroupReportRow](brandsadgroupreportrow.md)
  A single row in a Brands (Apple Maps) ad group report, pairing ad group metadata with total and granular performance metrics.
- [object BrandsAdGroupReportSummary](brandsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands ad group report.
- [object BrandsAdGroupResultContainer](brandsadgroupresultcontainer.md)
  Wraps the array of Brands ad group report rows along with a grand-total summary.
- [object BrandsAdReportResponse](brandsadreportresponse.md)
  The top-level response envelope for brands ad-level reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsadgroupreportresponse)*