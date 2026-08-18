# BrandsReportingCreative

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Creative metadata for brands ads.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsReportingCreative
```

#### Discussion

`BrandsReportingCreative` is the creative metadata snapshot embedded within `BrandsReportingAd` in `BRANDS` ad report rows. The `creativeType` field uses the shared `CreativeType` enum, but Brands (Apple Maps) creative reports only ever return `LOCAL_ADS_SEARCH_CREATIVE`.

`systemStatus` reflects whether the creative was valid at report time. Creatives with `INVALID` status were not eligible to serve during the reporting period and will not contribute to impression or engagement metrics.

##### Example

```json
{
  "id": 555666777,
  "creativeType": "LOCAL_ADS_SEARCH_CREATIVE",
  "systemStatus": "VALID"
}
```

## Topics

### Type Aliases
- [type BrandsReportingCreative.CreativeType](brandsreportingcreative/creativetype-data.typealias.md)
  The visual format and placement context of the creative at report time.
- [type BrandsReportingCreative.SystemStatus](brandsreportingcreative/systemstatus-data.typealias.md)
  System-evaluated validation state of the creative at report time.

## Properties

- `id` (int64): The creative’s unique identifier.
- `creativeType` (BrandsReportingCreative.CreativeType): Possible values: `LOCAL_ADS_SEARCH_CREATIVE`.
- `systemStatus` (BrandsReportingCreative.SystemStatus): Possible values: `VALID`, `INVALID`, `PENDING`.

## See Also

- [object BrandsReportingRequest](brandsreportingrequest.md)
  Request body for brands reporting queries.
- [object BrandsReportingCampaign](brandsreportingcampaign.md)
  Campaign metadata for Apple Maps report rows.
- [object BrandsReportingAdGroup](brandsreportingadgroup.md)
  Ad group metadata for brands report rows.
- [object BrandsReportingAd](brandsreportingad.md)
  Ad metadata for brands report rows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcreative)*