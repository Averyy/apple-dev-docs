# BrandsTargetingProjection

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Targeting projection for brands ad groups and campaigns.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsTargetingProjection
```

#### Discussion

`BrandsTargetingProjection` appears in `BRANDS` report rows, capturing the targeting configuration at the time of the report. All fields use `IncludeExclude` objects containing an `include` array of string values.

##### Example

```json
{
  "supplyPlacement": {
    "include": ["MAPS_SEARCH_RESULTS", "MAPS_SEARCH_HOME"]
  },
  "lifetimeStorefronts": {
    "include": ["US", "CA"]
  },
  "supplySource": {
    "include": ["MAPS"]
  },
  "promotedLocationGroup": {
    "include": ["555666777"]
  },
  "promotedLocation": {
    "include": ["123456789"]
  }
}
```

## Properties

- `supplyPlacement` (IncludeExclude): Restricts delivery to specific placement slots within Maps supply. Supported values: `MAPS_SEARCH_RESULTS`, `MAPS_SEARCH_HOME`. See [`IncludeExclude`](includeexclude.md) for details.
- `lifetimeStorefronts` (IncludeExclude): Controls country or region targeting over the lifetime of the campaign. See [`IncludeExclude`](includeexclude.md) for details.
- `supplySource` (IncludeExclude): Restricts delivery to a specific supply source. Use `MAPS` for Apple Maps placements. See [`IncludeExclude`](includeexclude.md) for details.
- `promotedLocationGroup` (IncludeExclude): Targets a specific location group. Use for campaigns targeting many locations at once. The location group ID identifies a saved set of brand locations. See [`IncludeExclude`](includeexclude.md) for details.
- `promotedLocation` (IncludeExclude): Targets an individual brand location by location ID. Use for single-location targeting. See [`IncludeExclude`](includeexclude.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandstargetingprojection)*