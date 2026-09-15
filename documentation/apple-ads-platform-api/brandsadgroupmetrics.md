# BrandsAdGroupMetrics

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad group-level metrics for brands, inheriting all properties from `BrandsMetrics`.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object BrandsAdGroupMetrics
```

#### Discussion

The `BrandsAdGroupMetrics` extends [`BrandsMetrics`](brandsmetrics.md) with no additional fields. It’s the metrics object embedded in brands ad group report rows.

## Properties

- `date` (date): Report date in YYYY-MM-DD format.
- `localSpend` (Money): Total spend. See [`Money`](money.md).
- `impressions` (int64): Total ad impressions.
- `taps` (int64): Total ad taps.
- `ttr` (number): Tap-through rate.
- `cpt` (Money): Average cost per tap. See [`Money`](money.md).
- `cpm` (Money): Average cost per thousand impressions. See [`Money`](money.md).
- `firstActions` (ActionMetrics): First-time action counts. See [`ActionMetrics`](actionmetrics.md).
- `firstActionsPerTap` (RateMetrics): First-action rates per tap. See [`RateMetrics`](ratemetrics.md).
- `firstActionsPerImpression` (RateMetrics): First-action rates per impression. See [`RateMetrics`](ratemetrics.md).
- `costPerFirstAction` (CostMetrics): Cost per first action. See [`CostMetrics`](costmetrics.md).
- `actions` (ActionMetrics): Total action counts. See [`ActionMetrics`](actionmetrics.md).
- `costPerAction` (CostMetrics): Cost per action. See [`CostMetrics`](costmetrics.md).
- `getDirections` (ActionMetrics): Get-directions action counts. See [`ActionMetrics`](actionmetrics.md).
- `tapURL` (ActionMetrics): Tap-URL action counts. See [`ActionMetrics`](actionmetrics.md).
- `call` (ActionMetrics): Call action counts. See [`ActionMetrics`](actionmetrics.md).
- `share` (ActionMetrics): Share action counts. See [`ActionMetrics`](actionmetrics.md).
- `getTheApp` (ActionMetrics): Get-the-app action counts. See [`ActionMetrics`](actionmetrics.md).
- `galleryEngagement` (ActionMetrics): Gallery engagement action counts. See [`ActionMetrics`](actionmetrics.md).
- `actionsPerTap` (RateMetrics): Total actions per tap rate. See [`RateMetrics`](ratemetrics.md).
- `actionsPerImpression` (RateMetrics): Total actions per impression rate. See [`RateMetrics`](ratemetrics.md).

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