# BidStrategyUpdate.BidStrategyGoal

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Optimization objective a bid strategy targets during Apple Ads auction competition.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BidStrategyUpdate.BidStrategyGoal
```

## Possible Values

- `IMPRESSION`: The strategy optimizes for maximum ad impressions. Applies to impression-based pricing models such as `MANUAL_CPM`.
- `INSTALL`: The strategy optimizes for app installs. The system bids more aggressively for queries likely to result in a new install.
- `TAP`: The strategy optimizes for taps on the ad. Applies to tap-based pricing models such as `MANUAL_CPT`.

## Discussion

Changing this on an update must keep the goal compatible with the bid strategy’s existing `bidStrategyType`, since `IMPRESSION` and `TAP` map to different pricing models.

### Example

```json
{
  "bidStrategyType": "MANUAL_CPT",
  "bidStrategyGoal": "TAP"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bidstrategyupdate/bidstrategygoal-data.typealias)*