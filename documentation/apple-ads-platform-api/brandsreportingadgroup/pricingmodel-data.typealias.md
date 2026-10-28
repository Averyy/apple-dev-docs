# BrandsReportingAdGroup.PricingModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The unit of ad delivery the ad group is charged for, as captured at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingAdGroup.PricingModel
```

## Possible Values

- `CPA`: Cost-per-acquisition.
- `CPM`: Cost-per-thousand-impressions. Pairs with `billingEvent: IMPRESSIONS`.
- `CPT`: Cost-per-tap. Pairs with `billingEvent: TAPS`.

## Discussion

The `pricingModel` field reflects the ad group’s charge unit at the time the system generated the report row. See [`ReportingPricingModel`](../reportingpricingmodel.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingadgroup/pricingmodel-data.typealias)*