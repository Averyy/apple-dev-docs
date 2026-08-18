# Sorting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Sort condition for reporting requests.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Sorting
```

#### Discussion

`Sorting` specifies a single sort condition for a reporting request.

Multiple `Sorting` objects can be included in the `sorting` array of a reporting request to apply multi-level sorting: results are sorted by the first entry first, then by subsequent entries for ties. When you omit `sorting`, the API sorts results by entity `id` in ascending order by default.

##### Example

```json
{
  "field": "localSpend",
  "order": "DESC"
}
```

## Properties

- `field` (string): The name of the field to sort on (e.g. localSpend, impressions).
- `order` (string): The sort direction for the specified field. Possible values: `ASC` (lowest to highest), `DESC` (highest to lowest).

## See Also

- [object TimeRange](timerange.md)
  Date range, time zone, and granularity settings for reporting requests.
- [object Filter](filter.md)
  Filter condition for reporting requests.
- [object RequestPagination](requestpagination.md)
  Pagination settings specific to reporting requests.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sorting)*