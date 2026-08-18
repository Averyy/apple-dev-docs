# BidStrategyUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating a bid strategy on an ad group or campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BidStrategyUpdate
```

#### Discussion

Use `BidStrategyUpdate` as the `bidStrategy` field value when updating an ad group (`PUT /v1/adgroups/{id}`) or a campaign (`PUT /v1/campaigns/{id}`). Include only the fields you want to change. The `bidStrategyType` must remain compatible with the parent campaign’s `billingEvent`. Changing the type to an incompatible combination returns a 400 error.

`bidStrategyGoal` can be changed together with `bidStrategyType`. Omitting one, or sending a goal that doesn’t match the type, returns an error. For ad group-specific behavior when the parent campaign uses an automated `bidStrategyType` (`MAX_CONVERSIONS` or `MAX_ENGAGEMENTS`), see [`AdGroupUpdate.BidStrategy`](adgroupupdate/bidstrategy-data.dictionary.md).

##### Example

```json
{
  "bidStrategyType": "MANUAL_CPT",
  "bidStrategyGoal": "TAP",
  "bid": {
    "amount": "2.50",
    "currency": "USD"
  }
}
```

## Topics

### Type Aliases
- [type BidStrategyUpdate.BidStrategyGoal](bidstrategyupdate/bidstrategygoal-data.typealias.md)
  Optimization objective a bid strategy targets during Apple Ads auction competition.
- [type BidStrategyUpdate.BidStrategyType](bidstrategyupdate/bidstrategytype-data.typealias.md)
  Auction participation approach controlling how an ad group or campaign sets and adjusts bids.

## Properties

- `bidStrategyType` (BidStrategyUpdate.BidStrategyType): The bid strategy type to apply. See [`BidStrategyUpdate.BidStrategyType`](bidstrategyupdate/bidstrategytype-data.typealias.md).
- `bidStrategyGoal` (BidStrategyUpdate.BidStrategyGoal): The optimization goal to apply. Must match `bidStrategyType` per the pairings in [`BidStrategy`](bidstrategy.md). See [`BidStrategyUpdate.BidStrategyGoal`](bidstrategyupdate/bidstrategygoal-data.typealias.md).
- `bid` (Money): The monetary bid amount for manual bid strategies, setting the per-auction monetary ceiling. For `MANUAL_CPT`, this value directly governs auction participation. For automated strategies, it acts as an upper bound. See [`Money`](money.md).

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
- [object CPAGoal](cpagoal.md)
  A deprecated cost-per-acquisition goal value. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object CPAGoalCreate](cpagoalcreate.md)
  The deprecated request payload for setting a cost-per-acquisition goal. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object CPAGoalUpdate](cpagoalupdate.md)
  The deprecated request payload for updating a cost-per-acquisition goal. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object TargetingData](targetingdata.md)
  The shared include and exclude pattern for all ad group and campaign targeting dimensions.
- [object TargetingDataCreate](targetingdatacreate.md)
  A targeting dimension value set for creating ad group or campaign targeting, specifying values to include or exclude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bidstrategyupdate)*