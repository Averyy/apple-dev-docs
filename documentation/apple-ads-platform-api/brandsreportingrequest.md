# BrandsReportingRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request body for brands reporting queries.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsReportingRequest
```

#### Discussion

`BrandsReportingRequest` is the request body for all `BRANDS` entity-level report endpoints.

##### Example

```json
{
  "pagination": {
    "offset": 0,
    "pageSize": 100
  },
  "sorting": [
    {
      "field": "impressions",
      "order": "DESC"
    }
  ],
  "filters": [
    {
      "field": "campaignId",
      "operator": "EQUALS",
      "value": "555666777"
    }
  ],
  "fields": [
    "campaignId",
    "impressions",
    "taps",
    "installs",
    "localSpend"
  ],
  "groupBy": [
    "deviceClass"
  ],
  "timeRange": {
    "start": "2025-01-01",
    "end": "2025-01-10",
    "timeZone": "ORTZ",
    "granularity": "DAILY"
  },
  "options": {
    "includeRows": [
      "GRAND_TOTAL"
    ]
  }
}
```

## Properties

- `pagination` (RequestPagination): Pagination settings for the report results. See [`RequestPagination`](requestpagination.md) for details.
- `sorting` ([Sorting]): Sort entities in ascending or descending order. The default behavior is to sort by ID, ascending. See [`Sorting`](sorting.md) for details.
- `filters` ([Filter]): Filter field conditions for the report. See [`Filter`](filter.md) for details.
- `fields` ([string]): A list of field names to return in the response. If omitted, all fields are returned.
- `groupBy` ([string]): Groups responses by selected dimensions. Supported values for `BRANDS` campaign, ad group, and ad entities: deviceClass, locationId, supplyPlacement. Note: KEYWORD and SEARCHTERM entities exclude both supplyPlacement and locationId.
- `timeRange` (TimeRange): The date range, timezone, and granularity for report data. Defines the start and end dates for the reporting period. See [`TimeRange`](timerange.md) for details.
- `options` (BrandsOptions): Options to include additional rows in the report. Note: EMPTY_METRICS is not supported for any `BRANDS` entity. See [`BrandsOptions`](brandsoptions.md) for details.

## See Also

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
- [object BrandsAdReportResponse](brandsadreportresponse.md)
  The top-level response envelope for brands ad-level reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingrequest)*