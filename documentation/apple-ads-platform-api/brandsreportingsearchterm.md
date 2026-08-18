# BrandsReportingSearchTerm

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Search term metadata for brands report rows, extending the base reporting search term with brands-only internal fields.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsReportingSearchTerm
```

#### Discussion

`BrandsReportingSearchTerm` extends the base `ReportingSearchTerm` object with a `BRANDS`-specific `keyword` field. While the base object provides the `searchTermText` and `searchTermSource`, the `keyword` field here is a `BrandsReportingKeyword` rather than the standard `ReportingKeyword`, capturing the `BRANDS` keyword context that the search term matched against.

Search term reports require the ORTZ timezone. `BRANDS` search term reports exclude the `supplyPlacement` and `locationId` dimensions from `groupBy`. Only `deviceClass` is available if dimensioned grouping is needed.

##### Example

```json
{
  "keyword": {
    "locationId": "555666777",
    "matchType": "PHRASE"
  },
  "locationId": "555666777"
}
```

## Properties

- `adAccountId` (int64)
- `adGroup` (ReportingAdGroupMin)
- `adGroupId` (int64)
- `campaignId` (int64)
- `countryOrRegion` (string)
- `deviceClass` (string)
- `keyword` (BrandsReportingKeyword): See [`BrandsReportingKeyword`](brandsreportingkeyword.md) for details.
- `locationId` (string): Location ID groupBy dimension value.
- `searchTermSource` (string)
- `searchTermText` (string)

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingsearchterm)*