# CampaignCreate.BidStrategy

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The creation payload for configuring a bid strategy on an ad group or campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignCreate.BidStrategy
```

#### Discussion

On campaign creation, `bidStrategyType` and `bidStrategyGoal` are both required: you must send both fields, and the goal must match the type per these pairings: `MANUAL_CPT`↔`TAP`, `MANUAL_CPM`↔`IMPRESSION`, `MAX_CONVERSIONS`↔`INSTALL`, `MAX_ENGAGEMENTS`↔`TAP`. Omitting either field, or sending a goal that doesn’t correspond to the type, returns an error.

See [`BidStrategyCreate`](bidstrategycreate.md) for the full field reference.

## Properties

- `bid` (Money): The bid amount for this bid strategy. See [`Money`](money.md).
- `bidStrategyGoal` (BidStrategyCreate.BidStrategyGoal): The optimization goal for the bid strategy. Must match `bidStrategyType` per the pairings above. See [`BidStrategyGoal`](bidstrategygoal.md). Required when `bidStrategyType` is set. Mutable after creation via [`BidStrategyUpdate`](bidstrategyupdate.md).
- `bidStrategyType` (BidStrategyCreate.BidStrategyType): The type of bid strategy. See [`BidStrategyType`](bidstrategytype.md). Required when `bidStrategyGoal` is set. Mutable after creation via [`BidStrategyUpdate`](bidstrategyupdate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate/bidstrategy-data.dictionary)*