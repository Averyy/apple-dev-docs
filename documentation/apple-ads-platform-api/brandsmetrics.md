# BrandsMetrics

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Metrics for BRANDS promoted object type.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsMetrics
```

#### Discussion

`BrandsMetrics` is the base metrics object for BRANDS campaign reports. It includes spend, impression, and tap metrics shared with APPS, plus BRANDS-specific engagement actions (get directions, tap URL, call, share, get the app, gallery engagement) and their associated rate and cost breakdowns.

All action count fields reference [`ActionMetrics`](actionmetrics.md) objects. Cost fields reference [`CostMetrics`](costmetrics.md). Rate fields reference [`RateMetrics`](ratemetrics.md). Monetary spend fields reference [`Money`](money.md).

##### Example

```json
{
  "date": "2025-01-10",
  "localSpend": {
    "amount": "845.50",
    "currency": "USD"
  },
  "impressions": 620000,
  "taps": 9800,
  "ttr": 0.0158,
  "cpt": {
    "amount": "0.09",
    "currency": "USD"
  },
  "cpm": {
    "amount": "1.36",
    "currency": "USD"
  },
  "firstActions": {
    "tap": 1450
  },
  "firstActionsPerTap": {
    "tap": 0.1480
  },
  "firstActionsPerImpression": {
    "tap": 0.0023
  },
  "costPerFirstAction": {
    "tap": {
      "amount": "0.58",
      "currency": "USD"
    }
  },
  "actions": {
    "tap": 2100
  },
  "costPerAction": {
    "tap": {
      "amount": "0.40",
      "currency": "USD"
    }
  },
  "getDirections": {
    "tap": 320
  },
  "tapURL": {
    "tap": 610
  },
  "call": {
    "tap": 145
  },
  "share": {
    "tap": 95
  },
  "getTheApp": {
    "tap": 780
  },
  "galleryEngagement": {
    "tap": 150
  },
  "actionsPerTap": {
    "tap": 0.2143
  },
  "actionsPerImpression": {
    "tap": 0.0034
  }
}
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsmetrics)*