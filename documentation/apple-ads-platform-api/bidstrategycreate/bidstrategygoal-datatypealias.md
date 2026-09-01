# BidStrategyCreate.BidStrategyGoal

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Optimization objective a bid strategy targets during Apple Ads auction competition.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string BidStrategyCreate.BidStrategyGoal
```

#### Discussion

Set this alongside `bidStrategyType` when creating a bid strategy, matching `IMPRESSION` or `TAP` goals to the corresponding `MANUAL_CPM` or `MANUAL_CPT` type.

##### Example

```json
{
  "bidStrategyType": "MANUAL_CPT",
  "bidStrategyGoal": "TAP"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bidstrategycreate/bidstrategygoal-data.typealias)*