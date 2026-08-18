# ReportingMoney

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A monetary value wrapper used in reporting contexts, capturing bid amounts and budgets at report time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ReportingMoney
```

#### Discussion

`ReportingMoney` is a thin wrapper around the `Money` type. The `value` field holds a `Money` object with the currency amount and currency code.

To read the numeric value and currency code, use the `amount` and `currency` fields within the nested `Money` object.

##### Example

```json
{
  "value": {
    "amount": "100.00",
    "currency": "USD"
  }
}
```

## Properties

- `value` (Money): See [`Money`](money.md) for details.

## See Also

- [object TimeRange](timerange.md)
  Date range, time zone, and granularity settings for reporting requests.
- [object Filter](filter.md)
  Filter condition for reporting requests.
- [object Sorting](sorting.md)
  Sort condition for reporting requests.
- [object RequestPagination](requestpagination.md)
  Pagination settings specific to reporting requests.
- [object ReportingBidStrategy](reportingbidstrategy.md)
  Bid strategy configuration as reported in report rows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/reportingmoney)*