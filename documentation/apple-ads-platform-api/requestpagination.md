# RequestPagination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Pagination settings specific to reporting requests.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RequestPagination
```

#### Discussion

`RequestPagination` controls which page of results is returned for a reporting request.

The `ResponsePagination` object on the report response returns the total number of available results. Use it to calculate how many additional pages exist and to determine the `offset` for subsequent requests when iterating through large result sets.

##### Example

```json
{
  "offset": 0,
  "pageSize": 50
}
```

## Properties

- `offset` (integer): The starting position (zero-based index) for the result set (e.g., `0` for the first page, `50` for the second page when `pageSize` is `50`).
- `pageSize` (integer): The number of records to return per page. Maximum 5000, default 100.

## See Also

- [object TimeRange](timerange.md)
  Date range, time zone, and granularity settings for reporting requests.
- [object Filter](filter.md)
  Filter condition for reporting requests.
- [object Sorting](sorting.md)
  Sort condition for reporting requests.
- [object ReportingMoney](reportingmoney.md)
  A monetary value wrapper used in reporting contexts, capturing bid amounts and budgets at report time.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/requestpagination)*