# CPAGoal

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A deprecated cost-per-acquisition goal value. Use `bidStrategy` with `MAX_CONVERSIONS` instead.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CPAGoal
```

#### Discussion

`cpaCap` on `AdGroupCreate` and `AdGroupUpdate` is deprecated in favor of the `BidStrategy` object with `bidStrategyType` set to `MAX_CONVERSIONS`. Use `bidStrategy` to configure automated conversion-maximizing bidding instead of setting a standalone CPA cap.

##### Example

```json
{
  "value": {
    "amount": "50.00",
    "currency": "USD"
  }
}
```

## Properties

- `value` (Money): The target CPA monetary value. Object with `amount` (string) and `currency` (string) properties.

## See Also

- [object AdGroup](adgroup.md)
  Primary unit governing targeting, bid strategy, pricing model, and scheduling within a campaign.
- [object AdGroupCreate](adgroupcreate.md)
  The request body for creating a new ad group.
- [object AdGroupUpdate](adgroupupdate.md)
  The request body for updating an existing ad group.
- [object AdGroupResponse](adgroupresponse.md)
  The response object for an ad group operation.
- [object AdGroupQueryResponse](adgroupqueryresponse.md)
  The response object for an ad group query, containing matched results and pagination metadata.
- [object AdGroupTargeting](adgrouptargeting.md)
  The comprehensive audience and placement configuration for an ad group.
- [object AdGroupTargetingCreate](adgrouptargetingcreate.md)
  The targeting configuration for creating a new ad group, specifying audience dimensions to include or exclude.
- [object AdGroupTargetingUpdate](adgrouptargetingupdate.md)
  The targeting configuration for updating an existing ad group, specifying audience dimensions to include or exclude.
- [object BidStrategy](bidstrategy.md)
  Defines how an ad group or campaign competes in auctions, including bid type, optimization goal, and bid amount.
- [object BidStrategyCreate](bidstrategycreate.md)
  The creation payload for configuring a bid strategy on an ad group or campaign.
- [object BidStrategyUpdate](bidstrategyupdate.md)
  The request body for updating a bid strategy on an ad group or campaign.
- [object CPAGoalCreate](cpagoalcreate.md)
  The deprecated request payload for setting a cost-per-acquisition goal. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object CPAGoalUpdate](cpagoalupdate.md)
  The deprecated request payload for updating a cost-per-acquisition goal. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object TargetingData](targetingdata.md)
  The shared include and exclude pattern for all ad group and campaign targeting dimensions.
- [object TargetingDataCreate](targetingdatacreate.md)
  A targeting dimension value set for creating ad group or campaign targeting, specifying values to include or exclude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/cpagoal)*