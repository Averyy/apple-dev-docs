# AdGroup.PricingModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The unit of ad delivery an ad group is charged for, independent of how the account funds spend.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AdGroup.PricingModel
```

#### Discussion

- The `CPM` value pairs with `billingEvent: IMPRESSIONS`.
- The `CPT` value pairs with `billingEvent: TAPS`.

##### Example

```json
{
  "pricingModel": "CPA"
}
```

```json
{
  "pricingModel": "CPM"
}
```

```json
{
  "pricingModel": "CPT"
}
```

The `PricingModel` is distinct from `PaymentModel`. The `PricingModel` (`CPA`, `CPM`, or `CPT`) determines the delivery unit an ad group is charged for. The `PaymentModel` (`PAYG` or `LOC`) determines how the advertiser’s account funds that spend. The two are unrelated enums on unrelated resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/pricingmodel-data.typealias)*