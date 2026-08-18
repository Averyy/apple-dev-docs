# Ad Groups Data Types

**Framework**: Apple Ads Platform API

Reference the enumerations and scalar types for ad groups.

**Availability**:
- Apple Ads Platform API 1.0+

## Topics

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
- [type PricingModel](pricingmodel.md)
  The unit of ad delivery that determines billing for an ad group, independent of how the account funds spend.

## See Also

- [Ad Groups Endpoints](adgroups-endpoints.md)
  Create, retrieve, update, and delete ad groups.
- [Ad Groups Data Objects](adgroups-data-objects.md)
  Reference the request and response objects for ad group endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroups-data-types)*