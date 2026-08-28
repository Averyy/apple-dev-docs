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

The `Filter` specifies a single field-level filter condition for a reporting request. The `field` name must match a filterable field on the target entity (for example, `localSpend`, `impressions`, `campaignId`). The `operator` determines the comparison type, and `value` supplies the comparison operand.

You can include multiple `Filter` objects in the `filters` array of a `AppsReportingRequest` or `BrandsReportingRequest` to narrow results by several criteria simultaneously. Supported operators vary by endpoint and field type: numeric fields support range operators like `GREATER_THAN` and `BETWEEN`. String fields support `EQUALS`, `IN`, and pattern operators like `STARTS_WITH`.

Endpoints that accept a `Filter` are: [`Campaigns Report`](get-app-campaign-reports.md), [`Ad Groups Report`](get-app-ad-group-reports.md), [`Ads Report`](get-app-ad-reports.md), [`Keywords Report`](get-app-keyword-reports.md), [`Search Terms Report`](get-app-search-term-reports.md), [`Campaigns Report (Brands)`](get-brand-campaign-reports.md), [`Ad Groups Report (Brands)`](get-brand-ad-group-reports.md), [`Ads Report (Brands)`](get-brand-ad-reports.md), [`Keywords Report (Brands)`](get-brand-keyword-reports.md), [`Search Terms Report (Brands)`](get-brand-search-term-reports.md), [`Impression Share Query`](query-app-impression-share-data.md), and [`Search Term Popularity Query`](query-app-search-term-popularity-data.md).

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

- `field` (string): The name of the field to filter on (for example, localSpend, impressions).
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