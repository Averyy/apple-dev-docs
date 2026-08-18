# Shared Objects

**Framework**: Apple Ads Platform API

Shared request and response objects used across Apps and Brands report endpoints.

**Availability**:
- Apple Ads Platform API 1.0+

## Topics

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
- [type ReportingBillingEvent](reportingbillingevent.md)
  The billing event of the campaign a report row belongs to.
- [type ReportingPricingModel](reportingpricingmodel.md)
  The pricing model of the ad group a report row belongs to.

## See Also

- [Managing Reports](reports.md)
  Retrieve performance data for campaigns, ad groups, ads, keywords, and search terms.
- [App Store Reports Endpoints](apps-reports-endpoints.md)
  Endpoints for retrieving App Store campaign, ad group, ad, keyword, and search term performance data.
- [Brands Reports Endpoints](brands-reports-endpoints.md)
  Retrieve performance data for Apple Maps campaigns, ad groups, ads, keywords, and search terms.
- [Apps Data Objects](apps-reports-objects.md)
  Request, response, and metadata objects for Apps report endpoints.
- [Brands Data Objects](brands-reports-objects.md)
  Explore the request, response, and metadata objects that Brands report endpoints use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/reports-shared-objects)*