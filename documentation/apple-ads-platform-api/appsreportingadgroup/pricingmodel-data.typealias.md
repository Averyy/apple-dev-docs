# AppsReportingAdGroup.PricingModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The pricing model of the ad group at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AppsReportingAdGroup.PricingModel
```

#### Discussion

This determines which report metrics are directly tied to cost: `CPM` pairs with impression-based billing and `CPT` with tap-based billing.

##### Example

```json
{
  "pricingModel": "CPT"
}
```

See [`ReportingPricingModel`](reportingpricingmodel.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingadgroup/pricingmodel-data.typealias)*