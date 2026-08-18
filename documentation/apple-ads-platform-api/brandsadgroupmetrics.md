# BrandsAdGroupMetrics

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad group-level metrics for BRANDS, inheriting all properties from `BrandsMetrics`.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsAdGroupMetrics
```

#### Discussion

`BrandsAdGroupMetrics` extends [`BrandsMetrics`](brandsmetrics.md) with no additional fields. It is the metrics object embedded in BRANDS ad group report rows.

## Properties

- `actions` (ActionMetrics)
- `actionsPerImpression` (RateMetrics)
- `actionsPerTap` (RateMetrics)
- `call` (ActionMetrics)
- `costPerAction` (CostMetrics)
- `costPerFirstAction` (CostMetrics)
- `cpm` (Money)
- `cpt` (Money)
- `date` (date)
- `firstActions` (ActionMetrics)
- `firstActionsPerImpression` (RateMetrics)
- `firstActionsPerTap` (RateMetrics)
- `galleryEngagement` (ActionMetrics)
- `getDirections` (ActionMetrics)
- `getTheApp` (ActionMetrics)
- `impressions` (int64)
- `localSpend` (Money)
- `share` (ActionMetrics)
- `tapURL` (ActionMetrics)
- `taps` (int64)
- `ttr` (number)

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsadgroupmetrics)*