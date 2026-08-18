# Filter

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Filter condition for reporting requests.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Filter
```

#### Discussion

`Filter` specifies a single field-level filter condition for a reporting request. The `field` name must match a filterable field on the target entity (e.g., `localSpend`, `impressions`, `campaignId`). The `operator` determines the comparison type, and `value` supplies the comparison operand.

You can include multiple `Filter` objects in the `filters` array of a `AppsReportingRequest` or `BrandsReportingRequest` to narrow results by several criteria simultaneously. Supported operators vary by endpoint and field type: numeric fields support range operators like `GREATER_THAN` and `BETWEEN`, while string fields support `EQUALS`, `IN`, and pattern operators like `STARTS_WITH`.

##### Example

```json
{
  "field": "localSpend",
  "operator": "GREATER_THAN",
  "value": [
    "100.00"
  ]
}
```

## Topics

### Dictionaries
- [object Filter.Value](filter/value-data.dictionary.md)
  The comparison operand supplied for the filter condition.

## Properties

- `field` (string): The name of the field to filter on (e.g. localSpend, impressions).
- `operator` (string): Comparison operator. Supported operators (may vary by endpoint): BETWEEN, CONTAINS, CONTAINS_ANY, CONTAINS_ALL, ENDS_WITH, EQUALS, GREATER_THAN, GREATER_THAN_OR_EQUAL_TO, IN, LESS_THAN, LESS_THAN_OR_EQUAL_TO, LIKE, NOT_EQUALS, STARTS_WITH.
- `value` (Filter.Value): One or more filter conditions applied to the result set.

## See Also

- [object TimeRange](timerange.md)
  Date range, time zone, and granularity settings for reporting requests.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/filter)*