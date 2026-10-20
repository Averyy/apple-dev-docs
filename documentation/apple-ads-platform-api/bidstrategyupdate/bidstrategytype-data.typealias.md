# BidStrategyUpdate.BidStrategyType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Auction participation approach controlling how an ad group or campaign sets and adjusts bids.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BidStrategyUpdate.BidStrategyType
```

## Possible Values

- `MANUAL_CPT`: Manual cost-per-tap strategy. You set the maximum amount you are willing to pay for each tap on your ad.
- `MANUAL_CPM`: Manual cost-per-thousand-impressions strategy. You set a fixed bid for every 1,000 ad impressions served.
- `MAX_CONVERSIONS`: Automated strategy that maximizes the total number of conversions within the available budget, using Search Match to identify optimal search queries. Configure conversion targeting via the `bidStrategy` object. The `cpaCap` ad group field is deprecated.
- `MAX_ENGAGEMENTS`: Automated bidding strategy that automatically sets bids to maximize taps on your place card using cost-per-tap (CPT) billing.

#### Discussion

The `MANUAL_CPT` and `MANUAL_CPM` values are manual bidding strategies with a fixed bid. The `MAX_CONVERSIONS` and `MAX_ENGAGEMENTS` values are automated strategies that adjust bids to maximize conversions or engagements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bidstrategyupdate/bidstrategytype-data.typealias)*