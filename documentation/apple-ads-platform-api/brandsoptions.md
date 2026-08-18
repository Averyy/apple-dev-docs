# BrandsOptions

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Report options for brands promoted object campaigns.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsOptions
```

#### Discussion

`BrandsOptions` configures optional row behavior for `BRANDS` report responses. The only supported value for `includeRows` is `GRAND_TOTAL`, which appends an aggregated summary row at the end of the result set. This totals all numeric metric fields across the full result page, giving a quick overview without requiring a client-side sum.

Note that `EMPTY_METRICS` (which is available for some other promoted object types) is explicitly unsupported for `BRANDS` entities. If you omit `BrandsOptions` entirely from the report request, the response returns only individual data rows with no summary.

##### Example

```json
{
  "includeRows": ["GRAND_TOTAL"]
}
```

## Properties

- `includeRows` ([string]): Row inclusion options for the report. Set to `GRAND_TOTAL` to append a summary row with aggregated totals across all result rows. `EMPTY_METRICS` is not a supported value for any `BRANDS` entity type.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsoptions)*