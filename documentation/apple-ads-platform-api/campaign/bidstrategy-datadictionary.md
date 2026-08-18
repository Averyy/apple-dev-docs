# Campaign.BidStrategy

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Defines how this campaign competes in auctions, including bid type, optimization goal, and bid amount.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Campaign.BidStrategy
```

#### Discussion

You must send `bidStrategyType` and `bidStrategyGoal` together, matching one of these pairings: `MANUAL_CPT`↔`TAP`, `MANUAL_CPM`↔`IMPRESSION`, `MAX_CONVERSIONS`↔`INSTALL`, `MAX_ENGAGEMENTS`↔`TAP`.

## Properties

- `bidStrategyType` (BidStrategy.BidStrategyType): The bid strategy type. Values: `MANUAL_CPT` (goal `TAP`, supported on App Store and Apple Maps), `MANUAL_CPM` (goal `IMPRESSION`, Apple Maps only), `MAX_CONVERSIONS` (goal `INSTALL`, App Store only), `MAX_ENGAGEMENTS` (goal `TAP`, Apple Maps only). See [`BidStrategyType`](bidstrategytype.md). Mutable.
- `bidStrategyGoal` (BidStrategy.BidStrategyGoal): The optimization goal for this bid strategy. Values: `TAP` (pairs with `MANUAL_CPT` or `MAX_ENGAGEMENTS`), `IMPRESSION` (pairs with `MANUAL_CPM`), `INSTALL` (pairs with `MAX_CONVERSIONS`). See [`BidStrategyGoal`](bidstrategygoal.md). Mutable. Must be paired with a matching `bidStrategyType`.
- `bid` (Money): The bid amount, setting the monetary ceiling for each auction entry. For `MANUAL_CPT` strategies, this value directly governs auction participation. For automated strategies, it acts as an upper bound. See [`Money`](money.md). Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/bidstrategy-data.dictionary)*