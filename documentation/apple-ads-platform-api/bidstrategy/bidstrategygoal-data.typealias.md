# BidStrategy.BidStrategyGoal

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Optimization objective a bid strategy targets during Apple Ads auction competition.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BidStrategy.BidStrategyGoal
```

## Possible Values

- `IMPRESSION`: The strategy optimizes for maximum ad impressions. Applies to impression-based pricing models such as `MANUAL_CPM`.
- `INSTALL`: The strategy optimizes for app installs. The system bids more aggressively for queries likely to result in a new install.
- `TAP`: The strategy optimizes for taps on the ad. Applies to tap-based pricing models such as `MANUAL_CPT`.

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