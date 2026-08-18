# BidStrategyCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The creation payload for configuring a bid strategy on an ad group or campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BidStrategyCreate
```

#### Discussion

`BidStrategyCreate` is the creation payload for configuring a bid strategy on an ad group or campaign.

Whenever you include `bidStrategyType`, you must also include the matching `bidStrategyGoal` (and vice versa), using the pairings in [`BidStrategy`](bidstrategy.md). Omitting one, or sending a goal that doesn’t match the type, returns an error. This pairing is always required on campaign creation. On ad group creation, you can omit `bidStrategy` entirely to inherit the parent campaign’s defaults, but the same pairing rule applies if you include it.

For manual CPT strategies, set `bidStrategyType` to `MANUAL_CPT` and supply a `bid` value that represents the maximum you’re willing to pay per tap. For automated strategies, set `bidStrategyType` to `MAX_CONVERSIONS` and optionally set a `bid` ceiling.

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
- [type BidStrategyCreate.BidStrategyGoal](bidstrategycreate/bidstrategygoal-data.typealias.md)
  Optimization objective a bid strategy targets during Apple Ads auction competition.
- [type BidStrategyCreate.BidStrategyType](bidstrategycreate/bidstrategytype-data.typealias.md)
  Auction participation approach controlling how an ad group or campaign sets and adjusts bids.

## Properties

- `bid` (Money): The bid amount for this bid strategy. See [`Money`](money.md).
- `bidStrategyGoal` (BidStrategyCreate.BidStrategyGoal): The optimization goal for the bid strategy. Must match `bidStrategyType` per [`BidStrategy`](bidstrategy.md). See [`BidStrategyCreate.BidStrategyGoal`](bidstrategycreate/bidstrategygoal-data.typealias.md). Required when `bidStrategyType` is set. Mutable after creation via [`BidStrategyUpdate`](bidstrategyupdate.md).
- `bidStrategyType` (BidStrategyCreate.BidStrategyType): The type of bid strategy. See [`BidStrategyCreate.BidStrategyType`](bidstrategycreate/bidstrategytype-data.typealias.md). Required when `bidStrategyGoal` is set. Mutable after creation via [`BidStrategyUpdate`](bidstrategyupdate.md).

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
- [object BidStrategyUpdate](bidstrategyupdate.md)
  The request body for updating a bid strategy on an ad group or campaign.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bidstrategycreate)*