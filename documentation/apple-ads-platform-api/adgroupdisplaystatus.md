# AdGroupDisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Derived display status for an ad group, combining advertiser-set status with system status.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroupDisplayStatus
```

## Possible Values

- `CAMPAIGN_ON_HOLD`: The ad group is on hold because its parent campaign is on hold.
- `DELETED`: The ad group has been deleted.
- `LIMITED`: The ad group is serving but delivery is restricted. Check `systemStatusLimitingReasons` for details.
- `ON_HOLD`: The ad group is on hold due to a system issue. Check `systemStatusReasons` for details.
- `PAUSED`: The ad group has been paused by the advertiser.
- `PROCESSING`: The ad group is being processed and is not yet serving.
- `RUNNING`: The ad group is active and eligible to serve ads.

## See Also

- [type AdGroupStatus](./adgroupstatus.md)
  Advertiser-configurable serving status for an ad group.
- [type AdGroupSystemStatus](./adgroupsystemstatus.md)
  System-derived operational status reflecting whether an ad group is actively serving.
- [type AdGroupSystemStatusReason](./adgroupsystemstatusreason.md)
  Reasons that can cause an ad group’s system status to be `NOT_RUNNING`.
- [type AdGroupSystemLimitedStatusReason](./adgroupsystemlimitedstatusreason.md)
  Reasons that limit delivery for an ad group without fully stopping it.
- [type BidStrategyType](./bidstrategytype.md)
  Auction participation approach controlling how an ad group or campaign sets and adjusts bids.
- [type BidStrategyGoal](./bidstrategygoal.md)
  Optimization objective a bid strategy targets during Apple Ads auction competition.
- [type PricingModel](./pricingmodel.md)
  The unit of ad delivery that determines billing for an ad group, independent of how the account funds spend.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupdisplaystatus)*