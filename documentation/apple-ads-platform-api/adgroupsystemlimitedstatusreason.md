# AdGroupSystemLimitedStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Reasons that limit delivery for an ad group without fully stopping it.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroupSystemLimitedStatusReason
```

## Possible Values

- `LOCATION_POLICY_ISSUES`: The ad group’s location targeting contains areas with policy restrictions.
- `LOCATION_GROUP_ISSUES`: The ad group’s location group targeting has issues that limit delivery.
- `ADS_LIMITED`: One or more ads in the ad group are limited, reducing overall delivery.

## See Also

- [type AdGroupStatus](./adgroupstatus.md)
  Advertiser-configurable serving status for an ad group.
- [type AdGroupSystemStatus](./adgroupsystemstatus.md)
  System-derived operational status reflecting whether an ad group is actively serving.
- [type AdGroupDisplayStatus](./adgroupdisplaystatus.md)
  Derived display status for an ad group, combining advertiser-set status with system status.
- [type AdGroupSystemStatusReason](./adgroupsystemstatusreason.md)
  Reasons that can cause an ad group’s system status to be `NOT_RUNNING`.
- [type BidStrategyType](./bidstrategytype.md)
  Auction participation approach controlling how an ad group or campaign sets and adjusts bids.
- [type BidStrategyGoal](./bidstrategygoal.md)
  Optimization objective a bid strategy targets during Apple Ads auction competition.
- [type PricingModel](./pricingmodel.md)
  The unit of ad delivery that determines billing for an ad group, independent of how the account funds spend.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupsystemlimitedstatusreason)*