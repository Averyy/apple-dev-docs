# TimeRange

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Date range, time zone, and granularity settings for reporting requests.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object TimeRange
```

#### Discussion

`TimeRange` defines the date window, timezone, and optional time-series breakdown for a reporting request.

##### Example

```json
{
  "start": "2025-01-01",
  "end": "2025-01-10",
  "timeZone": "ORTZ",
  "granularity": "DAILY"
}
```

## Properties

- `start` (date): The start date in YYYY-MM-DD format. The range is inclusive of this date.
- `end` (date): The end date in YYYY-MM-DD format. The range is inclusive of this date.
- `timeZone` (string): The time zone for the report date range. The default is ORTZ (org timezone). Both ORTZ and UTC are supported for all reports except search term-level, which only supports ORTZ.
- `granularity` (string): Time period breakdown for granularMetrics in the response. When specified, the response includes granularMetrics broken down by this period. Possible values: `HOURLY`, `DAILY`, `WEEKLY`, `MONTHLY`. HOURLY granularity is not supported for ad-level or search term-level reports.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/timerange)*