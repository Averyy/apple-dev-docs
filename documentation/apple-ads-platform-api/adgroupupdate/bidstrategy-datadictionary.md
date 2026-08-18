# AdGroupUpdate.BidStrategy

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating a bid strategy on an ad group or campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupUpdate.BidStrategy
```

#### Discussion

Ad groups under an auto-bidding campaign (`bidStrategyType` of `MAX_CONVERSIONS` or `MAX_ENGAGEMENTS`) inherit their bid strategy from the campaign. For other ad groups, you can change both `bidStrategyType` and `bidStrategyGoal`, as long as you send them together and match one of these pairings: `MANUAL_CPT`↔`TAP`, `MANUAL_CPM`↔`IMPRESSION`, `MAX_CONVERSIONS`↔`INSTALL`, `MAX_ENGAGEMENTS`↔`TAP`.

See [`BidStrategyUpdate`](bidstrategyupdate.md) for the full field reference.

## Properties

- `bidStrategyType` (BidStrategyUpdate.BidStrategyType): The bid strategy type to apply. See [`BidStrategyType`](bidstrategytype.md).
- `bidStrategyGoal` (BidStrategyUpdate.BidStrategyGoal): The optimization goal to apply. Must match `bidStrategyType` per the pairings above. See [`BidStrategyUpdate.BidStrategyGoal`](bidstrategyupdate/bidstrategygoal-data.typealias.md).
- `bid` (Money): The monetary bid amount for manual bid strategies, setting the per-auction monetary ceiling. For `MANUAL_CPT`, this value directly governs auction participation. For automated strategies, it acts as an upper bound. See [`Money`](money.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupupdate/bidstrategy-data.dictionary)*