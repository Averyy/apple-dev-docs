# BidStrategy

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Defines how an ad group or campaign competes in auctions, including bid type, optimization goal, and bid amount.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BidStrategy
```

#### Discussion

`BidStrategy` defines how an ad group or campaign competes in auctions.

You must send `bidStrategyType` and `bidStrategyGoal` together and match one of the pairings listed in the properties below, whether creating a bid strategy or updating one. See [`BidStrategyCreate`](bidstrategycreate.md) and [`BidStrategyUpdate`](bidstrategyupdate.md). See [`AdGroupUpdate.BidStrategy`](adgroupupdate/bidstrategy-data.dictionary.md) for how ad groups under an auto-bidding campaign can echo the campaign’s bid strategy.

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
- [type BidStrategy.BidStrategyGoal](bidstrategy/bidstrategygoal-data.typealias.md)
  Optimization objective a bid strategy targets during Apple Ads auction competition.
- [type BidStrategy.BidStrategyType](bidstrategy/bidstrategytype-data.typealias.md)
  Auction participation approach controlling how an ad group or campaign sets and adjusts bids.

## Properties

- `bidStrategyType` (BidStrategy.BidStrategyType): The bid strategy type. Values: `MANUAL_CPT` (goal `TAP`, supported on App Store and Apple Maps), `MANUAL_CPM` (goal `IMPRESSION`, Apple Maps only), `MAX_CONVERSIONS` (goal `INSTALL`, App Store only), `MAX_ENGAGEMENTS` (goal `TAP`, Apple Maps only). See [`BidStrategy.BidStrategyType`](bidstrategy/bidstrategytype-data.typealias.md). Mutable.
- `bidStrategyGoal` (BidStrategy.BidStrategyGoal): The optimization goal for this bid strategy. Values: `TAP` (pairs with `MANUAL_CPT` or `MAX_ENGAGEMENTS`), `IMPRESSION` (pairs with `MANUAL_CPM`), `INSTALL` (pairs with `MAX_CONVERSIONS`). See [`BidStrategy.BidStrategyGoal`](bidstrategy/bidstrategygoal-data.typealias.md). Mutable. Must be paired with a matching `bidStrategyType`.
- `bid` (Money): The bid amount, setting the monetary ceiling for each auction entry. For `MANUAL_CPT` strategies, this value directly governs auction participation. For automated strategies, it acts as an upper bound. See [`Money`](money.md). Mutable.

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
- [object BidStrategyCreate](bidstrategycreate.md)
  The creation payload for configuring a bid strategy on an ad group or campaign.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bidstrategy)*