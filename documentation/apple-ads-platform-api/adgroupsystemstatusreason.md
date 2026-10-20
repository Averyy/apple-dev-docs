# AdGroupSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Reasons that can cause an ad group’s system status to be `NOT_RUNNING`.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroupSystemStatusReason
```

## Possible Values

- `PROCESSING`: The ad group is being processed and is not yet active.
- `PAUSED_BY_SYSTEM`: The ad group was paused by the system.
- `PAUSED_BY_USER`: The ad group was paused by the advertiser.
- `DELETED_BY_USER`: The ad group was deleted by the advertiser.
- `SCHEDULE_PENDING`: The ad group schedule has not yet started.
- `SCHEDULE_EXPIRED`: The ad group schedule has ended.
- `TARGETED_DEVICE_CLASS_NOT_SUPPORTED_SUPPLY_PLACEMENT`: The targeted device class is not supported by the supply placement.
- `PENDING_AUDIENCE_VERIFICATION`: The ad group’s audience targeting is pending verification.
- `AUDIENCE_BELOW_THRESHOLD`: The targeted audience is below the minimum threshold required to serve.
- `CAMPAIGN_NOT_RUNNING`: The parent campaign is not running.
- `ADS_NOT_RUNNING`: All ads in the ad group are not running.
- `AUTOMATED_KEYWORDS_REQUIRED_AD_GROUP_NOT_ALLOWED_IN_MANUAL_CAMPAIGNS`: Automated keyword ad groups are not allowed in manually managed campaigns.
- `KEYWORDS_MISSING`: The ad group requires keywords but none have been added.

## See Also

- [type AdGroupStatus](./adgroupstatus.md)
  Advertiser-configurable serving status for an ad group.
- [type AdGroupSystemStatus](./adgroupsystemstatus.md)
  System-derived operational status reflecting whether an ad group is actively serving.
- [type AdGroupDisplayStatus](./adgroupdisplaystatus.md)
  Derived display status for an ad group, combining advertiser-set status with system status.
- [type AdGroupSystemLimitedStatusReason](./adgroupsystemlimitedstatusreason.md)
  Reasons that limit delivery for an ad group without fully stopping it.
- [type BidStrategyType](./bidstrategytype.md)
  Auction participation approach controlling how an ad group or campaign sets and adjusts bids.
- [type BidStrategyGoal](./bidstrategygoal.md)
  Optimization objective a bid strategy targets during Apple Ads auction competition.
- [type PricingModel](./pricingmodel.md)
  The unit of ad delivery that determines billing for an ad group, independent of how the account funds spend.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupsystemstatusreason)*