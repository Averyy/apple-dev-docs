# CampaignUpdate.BidStrategy

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating a bid strategy on an ad group or campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignUpdate.BidStrategy
```

#### Discussion

To change a campaign’s bid strategy after creation, use this object. `bidStrategyType` and `bidStrategyGoal` must be sent together and matched per the pairings in `BidStrategy`.

See [`BidStrategyUpdate`](bidstrategyupdate.md) for the full field reference.

## Properties

- `bidStrategyType` (BidStrategyUpdate.BidStrategyType): The bid strategy type to apply. See [`BidStrategyType`](bidstrategytype.md).
- `bidStrategyGoal` (BidStrategyUpdate.BidStrategyGoal): The optimization goal to apply. Must match `bidStrategyType` per the pairings above. See [`BidStrategyGoal`](bidstrategygoal.md).
- `bid` (Money): The monetary bid amount for manual bid strategies, setting the per-auction monetary ceiling. For `MANUAL_CPT`, this value directly governs auction participation. For automated strategies, it acts as an upper bound. See [`Money`](money.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignupdate/bidstrategy-data.dictionary)*