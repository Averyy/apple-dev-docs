# ReportingAdGroupMin

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Minimal ad group information included in nested report objects.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ReportingAdGroupMin
```

#### Discussion

`ReportingAdGroupMin` is a lightweight ad group summary embedded in report row objects (for example, within [`ReportingKeyword`](reportingkeyword.md)). It provides enough context to identify the parent ad group without duplicating the full [`AdGroup`](adgroup.md) structure.

##### Example

```json
{
  "name": "AwayFinder Search - Brand",
  "deleted": false
}
```

## Properties

- `name` (string): The ad group name.
- `deleted` (boolean): `true` if the ad group has been deleted.

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
- [object ReportingBidStrategy](reportingbidstrategy.md)
  Bid strategy configuration as reported in report rows.
- [object ReportingCampaignMin](reportingcampaignmin.md)
  Minimal campaign information included in nested report objects.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/reportingadgroupmin)*