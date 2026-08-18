# ReportingBidStrategy

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Bid strategy configuration as reported in report rows.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ReportingBidStrategy
```

#### Discussion

`ReportingBidStrategy` captures the bid strategy type and optional bid amount for a campaign or ad group at report time. It is embedded in reporting objects where the bid configuration is needed for analysis alongside performance data.

##### Example

```json
{
  "bidStrategyType": "MANUAL_CPT",
  "bid": {
    "amount": "2.50",
    "currency": "USD"
  }
}
```

## Topics

### Type Aliases
- [type ReportingBidStrategy.BidStrategyType](reportingbidstrategy/bidstrategytype-data.typealias.md)
  Auction participation approach applied to the campaign or ad group at report time.

## Properties

- `bidStrategyType` (ReportingBidStrategy.BidStrategyType): The bid strategy applied. Possible values: `MANUAL_CPT`, `MAX_CONVERSIONS`, `MANUAL_CPM`, `MAX_ENGAGEMENTS`. Note: `MAX_CONVERSIONS` ad groups no longer use the deprecated `cpaCap` field. You configure conversion targeting via the `bidStrategy` object.
- `bid` (Money): The bid amount for manual bid strategies. `null` for automated strategies. See [`Money`](money.md).

## See Also

- [object TimeRange](timerange.md)
  Date range, time zone, and granularity settings for reporting requests.
- [object Filter](filter.md)
  Filter condition for reporting requests.
- [object Sorting](sorting.md)
  Sort condition for reporting requests.
- [object RequestPagination](requestpagination.md)
  Pagination settings specific to reporting requests.
- [object ReportingMoney](reportingmoney.md)
  A monetary value wrapper used in reporting contexts, capturing bid amounts and budgets at report time.
- [object ReportingCampaignMin](reportingcampaignmin.md)
  Minimal campaign information included in nested report objects.
- [object ReportingAdGroupMin](reportingadgroupmin.md)
  Minimal ad group information included in nested report objects.
- [object ReportingCreativeSpec](reportingcreativespec.md)
  Creative specification embedded in report rows.
- [object ReportingDestination](reportingdestination.md)
  Creative destination embedded in report rows.
- [object ReportingKeyword](reportingkeyword.md)
  Keyword metadata in a report row.
- [object ReportingSearchTerm](reportingsearchterm.md)
  Search term metadata in a report row.
- [object ActionMetrics](actionmetrics.md)
  Action count metrics breakdown by attribution type.
- [object CostMetrics](costmetrics.md)
  Cost metrics breakdown by attribution type.
- [object RateMetrics](ratemetrics.md)
  Rate metrics breakdown by attribution type.
- [type ReportingAdChannelType](reportingadchanneltype.md)
  The ad channel that served a report row’s metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/reportingbidstrategy)*