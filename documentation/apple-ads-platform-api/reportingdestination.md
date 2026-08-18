# ReportingDestination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Creative destination embedded in report rows.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ReportingDestination
```

#### Discussion

`ReportingDestination` captures the destination parameters of a creative as recorded at report time.

##### Example

```json
{
  "parameters": {
    "productPageId": "555666777",
    "url": "https://apps.apple.com/us/app/awayfinder/id123456789"
  }
}
```

## Topics

### Dictionaries
- [object ReportingDestination.Parameters](reportingdestination/parameters-data.dictionary.md)
  Destination-specific parameters for the creative’s post-tap experience, as recorded at report time.

## Properties

- `parameters` (ReportingDestination.Parameters): Destination parameters as a key-value map. Content varies by creative and destination type.

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
- [object ReportingAdGroupMin](reportingadgroupmin.md)
  Minimal ad group information included in nested report objects.
- [object ReportingCreativeSpec](reportingcreativespec.md)
  Creative specification embedded in report rows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/reportingdestination)*