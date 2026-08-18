# BrandsSearchTermReportResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The top-level response envelope for brands search term reports.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsSearchTermReportResponse
```

#### Discussion

`BrandsSearchTermReportResponse` is the top-level response envelope for `BRANDS` search term reports. The `result` field contains a `BrandsSearchTermResultContainer` with the array of search term rows, each capturing the actual user query text and associated `BRANDS` performance metrics.

Like all search term reports, `BRANDS` search term reports require the ORTZ timezone. UTC is not supported. Search term entity reports also exclude the `supplyPlacement` and `locationId` dimensions from `groupBy`. The `pagination` field provides the pagination state.

##### Example

```json
{
  "result": {
    "rows": [
      {
        "totalMetrics": {
          "date": "2025-01-10",
          "localSpend": {
            "amount": "245.50",
            "currency": "USD"
          },
          "impressions": 18400,
          "taps": 620
        },
        "metadata": {
          "searchTermText": "awayfinder travel app",
          "locationId": "555666777"
        }
      }
    ],
    "summary": {
      "grandTotal": {
        "localSpend": {
          "amount": "245.50",
          "currency": "USD"
        },
        "impressions": 18400,
        "taps": 620
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

- `result` (BrandsSearchTermResultContainer): See [`BrandsSearchTermResultContainer`](brandssearchtermresultcontainer.md) for details.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandssearchtermreportresponse)*