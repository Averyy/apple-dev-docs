# Apps Data Objects

**Framework**: Apple Ads Platform API

Request, response, and metadata objects for Apps report endpoints.

**Availability**:
- apple-ads-platform-api 1.0+

#### Overview

Apps reports cover the five `apps` reporting entities: campaigns, ad groups, ads, keywords, and search terms. Each entity has its own endpoint, request/response pair, and metadata schema, but all five share the same row shape and request structure described below.

The five Apps reporting entities each have a dedicated endpoint.

| Entity | Endpoint |
| --- | --- |
| Campaign | [`Campaigns Report`](get-app-campaign-reports.md) |
| Ad Group | [`Ad Groups Report`](get-app-ad-group-reports.md) |
| Ad | [`Ads Report`](get-app-ad-reports.md) |
| Keyword | [`Keywords Report`](get-app-keyword-reports.md) |
| Search Term | [`Search Terms Report`](get-app-search-term-reports.md) |

##### Shared Object Model

Every Apps report request uses [`AppsReportingRequest`](appsreportingrequest.md) as its body. Each response row follows the same three-part shape:

- `metadata`: entity attributes (name, status, identifiers) plus any `groupBy` dimension value (`deviceClass`, `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`, `storefront`, or `countryOrRegion`, with entity-level restrictions) applied to that row. Entity-specific metadata schemas define the fields available for each entity, including [`AppsReportingCampaign`](appsreportingcampaign.md), [`AppsReportingAdGroup`](appsreportingadgroup.md), [`AppsReportingAd`](appsreportingad.md), [`ReportingKeyword`](reportingkeyword.md), and [`ReportingSearchTerm`](reportingsearchterm.md). Ad metadata nests creative details in an [`AppsReportingCreative`](appsreportingcreative.md) object rather than a flat creative ID.
- `totalMetrics`: aggregate [`AppsMetrics`](appsmetrics.md) (or entity variant, e.g. [`AppsAdGroupMetrics`](appsadgroupmetrics.md)) values for the row over the full requested date range.
- `granularMetrics`: an array of pure metrics objects, one per period in the requested `granularity`, with no dimension fields of their own. Only present when `granularity` is specified in the request.

Each endpoint’s response envelope, row, and summary objects follow a consistent per-entity naming pattern, for example [`AppsCampaignReportResponse`](appscampaignreportresponse.md), [`AppsCampaignReportRow`](appscampaignreportrow.md), and [`AppsCampaignResultContainer`](appscampaignresultcontainer.md) for campaigns, with equivalent objects for ad groups, ads, keywords, and search terms.

For a side-by-side comparison of Apps and Brands reporting differences (groupBy dimensions, options, creative metadata), see [`Managing Reports`](reports.md).

## Topics

- [object AppsReportingRequest](appsreportingrequest.md)
  Request body for APPS reporting queries.
- [object AppsReportingCampaign](appsreportingcampaign.md)
  Campaign metadata for APPS report rows.
- [object AppsReportingAdGroup](appsreportingadgroup.md)
  Ad group metadata for APPS report rows.
- [object AppsReportingAd](appsreportingad.md)
  Ad metadata for APPS report rows.
- [object AppsReportingCreative](appsreportingcreative.md)
  Creative metadata for APPS ads.
- [object AppsCampaignReportResponse](appscampaignreportresponse.md)
  The top-level response envelope for APPS campaign-level reports.
- [object AppsCampaignReportRow](appscampaignreportrow.md)
  A single row in an APPS campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object AppsCampaignReportSummary](appscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps campaign report.
- [object AppsCampaignResultContainer](appscampaignresultcontainer.md)
  Wraps the array of Apps campaign report rows along with a grand-total summary.
- [object AppsAdGroupReportResponse](appsadgroupreportresponse.md)
  The top-level response envelope for APPS ad group reports.
- [object AppsAdGroupReportRow](appsadgroupreportrow.md)
  A single row in an Apps ad group report, containing ad group metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdGroupReportSummary](appsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad group report.
- [object AppsAdGroupResultContainer](appsadgroupresultcontainer.md)
  Wraps the array of Apps ad group report rows along with a grand-total summary.
- [object AppsAdReportResponse](appsadreportresponse.md)
  The top-level response envelope for APPS ad-level reports.
- [object AppsAdReportRow](appsadreportrow.md)
  A single row in an Apps ad-level report, containing ad metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdReportSummary](appsadreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad-level report.
- [object AppsAdResultContainer](appsadresultcontainer.md)
  Wraps the array of Apps ad-level report rows along with a grand-total summary.
- [object AppsKeywordReportResponse](appskeywordreportresponse.md)
  The top-level response envelope for APPS keyword-level reports.
- [object AppsKeywordReportRow](appskeywordreportrow.md)
  A single row in an APPS keyword report, containing keyword metadata, performance metrics, and optional bid recommendation insights.
- [object AppsKeywordReportSummary](appskeywordreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps keyword report.
- [object AppsKeywordResultContainer](appskeywordresultcontainer.md)
  Wraps the array of Apps keyword report rows along with a grand-total summary.
- [object AppsSearchTermReportResponse](appssearchtermreportresponse.md)
  The top-level response envelope for APPS search term reports.
- [object AppsSearchTermReportRow](appssearchtermreportrow.md)
  A single row in an Apps search term report, pairing search-term metadata with total and granular performance metrics.
- [object AppsSearchTermReportSummary](appssearchtermreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps search term report.
- [object AppsSearchTermResultContainer](appssearchtermresultcontainer.md)
  Wraps the array of Apps search term report rows along with a grand-total summary.
- [object AppsMetrics](appsmetrics.md)
  Metrics for APPS promoted object type.
- [object AppsCampaignMetrics](appscampaignmetrics.md)
  Campaign-level metrics for APPS, inheriting all properties from `AppsMetrics`.
- [object AppsAdGroupMetrics](appsadgroupmetrics.md)
  Ad group-level metrics for APPS, inheriting all properties from `AppsMetrics`.
- [object AppsOptions](appsoptions.md)
  Reporting options for APPS promoted object type reports.
- [object AppsTargetingProjection](appstargetingprojection.md)
  Targeting projection for APPS campaigns.

## See Also

- [Managing Reports](reports.md)
  Retrieve performance data for campaigns, ad groups, ads, keywords, and search terms.
- [App Store Reports Endpoints](apps-reports-endpoints.md)
  Endpoints for retrieving App Store campaign, ad group, ad, keyword, and search term performance data.
- [Brands Reports Endpoints](brands-reports-endpoints.md)
  Retrieve performance data for Apple Maps campaigns, ad groups, ads, keywords, and search terms.
- [Brands Data Objects](brands-reports-objects.md)
  Explore the request, response, and metadata objects that Brands report endpoints use.
- [Shared Objects](reports-shared-objects.md)
  Shared request and response objects used across Apps and Brands report endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/apps-reports-objects)*