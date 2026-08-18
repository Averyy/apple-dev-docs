# PricingModel

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The unit of ad delivery that determines billing for an ad group, independent of how the account funds spend.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string PricingModel
```

#### Discussion

`PricingModel` controls which event triggers billing for an ad group’s delivery: a tap, an impression, or an install action. You set it on `AdGroup`/`AdGroupCreate`, and it must match the parent campaign’s `billingEvent`.

`PricingModel` is distinct from `PaymentModel`. `PricingModel` (`CPA`/`CPM`/`CPT`) determines the delivery unit that triggers billing for an ad group. `PaymentModel` (`PAYG`/`LOC`) determines how the advertiser’s account funds that spend, pay-as-you-go billing versus a line of credit. The two are unrelated enums on unrelated resources. Do not use one where the documentation calls for the other.

## See Also

- [type AdGroupStatus](adgroupstatus.md)
  Advertiser-configurable serving status for an ad group.
- [type AdGroupSystemStatus](adgroupsystemstatus.md)
  System-derived operational status reflecting whether an ad group is actively serving.
- [type AdGroupDisplayStatus](adgroupdisplaystatus.md)
  Derived display status for an ad group, combining advertiser-set status with system status.
- [type AdGroupSystemStatusReason](adgroupsystemstatusreason.md)
  Reasons that can cause an ad group’s system status to be `NOT_RUNNING`.
- [type AdGroupSystemLimitedStatusReason](adgroupsystemlimitedstatusreason.md)
  Reasons that limit delivery for an ad group without fully stopping it.
- [type BidStrategyType](bidstrategytype.md)
  Auction participation approach controlling how an ad group or campaign sets and adjusts bids.
- [type BidStrategyGoal](bidstrategygoal.md)
  Optimization objective a bid strategy targets during Apple Ads auction competition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/pricingmodel)*