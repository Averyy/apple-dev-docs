# BidStrategyType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Auction participation approach controlling how an ad group or campaign sets and adjusts bids.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BidStrategyType
```

## Possible Values

- `MANUAL_CPT`: Manual cost-per-tap strategy. You set the maximum amount you are willing to pay for each tap on your ad.
- `MANUAL_CPM`: Manual cost-per-thousand-impressions strategy. You set a fixed bid for every 1,000 ad impressions served.
- `MAX_CONVERSIONS`: Automated strategy that maximizes the total number of conversions within the available budget, using Search Match to identify optimal search queries. Configure conversion targeting via the `bidStrategy` object. The `cpaCap` ad group field is deprecated.
- `MAX_ENGAGEMENTS`: Automated bidding strategy that automatically sets bids to maximize taps on your place card using cost-per-tap (CPT) billing.

## See Also

- [type AdGroupStatus](./adgroupstatus.md)
  Advertiser-configurable serving status for an ad group.
- [type AdGroupSystemStatus](./adgroupsystemstatus.md)
  System-derived operational status reflecting whether an ad group is actively serving.
- [type AdGroupDisplayStatus](./adgroupdisplaystatus.md)
  Derived display status for an ad group, combining advertiser-set status with system status.
- [type AdGroupSystemStatusReason](./adgroupsystemstatusreason.md)
  Reasons that can cause an ad group’s system status to be `NOT_RUNNING`.
- [type AdGroupSystemLimitedStatusReason](./adgroupsystemlimitedstatusreason.md)
  Reasons that limit delivery for an ad group without fully stopping it.
- [type BidStrategyGoal](./bidstrategygoal.md)
  Optimization objective a bid strategy targets during Apple Ads auction competition.
- [type PricingModel](./pricingmodel.md)
  The unit of ad delivery that determines billing for an ad group, independent of how the account funds spend.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bidstrategytype)*