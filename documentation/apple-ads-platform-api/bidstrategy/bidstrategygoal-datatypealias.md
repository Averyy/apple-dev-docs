# BidStrategy.BidStrategyGoal

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Optimization objective a bid strategy targets during Apple Ads auction competition.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string BidStrategy.BidStrategyGoal
```

#### Discussion

The goal must match the ad group’s pricing model, since `IMPRESSION` and `TAP` goals apply only under `MANUAL_CPM` and `MANUAL_CPT` respectively.

##### Example

```json
{
  "bidStrategyType": "MANUAL_CPT",
  "bidStrategyGoal": "TAP"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bidstrategy/bidstrategygoal-data.typealias)*