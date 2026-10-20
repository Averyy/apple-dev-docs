# AppsReportingAdGroup.PricingModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The pricing model of the ad group at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AppsReportingAdGroup.PricingModel
```

## Possible Values

- `CPA`: Cost-per-acquisition.
- `CPM`: Cost-per-thousand-impressions.
- `CPT`: Cost-per-tap.

#### Discussion

This determines which report metrics are directly tied to cost: `CPM` pairs with impression-based billing and `CPT` with tap-based billing.

##### Example

```json
{
  "pricingModel": "CPT"
}
```

See [`ReportingPricingModel`](../reportingpricingmodel.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingadgroup/pricingmodel-data.typealias)*