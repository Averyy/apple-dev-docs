# Brands Data Objects

**Framework**: Apple Ads Platform API

Explore the request, response, and metadata objects that Brands report endpoints use.

**Availability**:
- apple-ads-platform-api 1.0+

#### Overview

Brands reports cover the five `business-brands` reporting entities: campaigns, ad groups, ads, keywords, and search terms. Each entity has its own endpoint, request/response pair, and metadata schema, but all five share the same row shape and request structure described below.

The five Brands reporting entities each have a dedicated endpoint.

| Entity | Endpoint |
| --- | --- |
| Campaign | [`Campaigns Report (Brands)`](get-brand-campaign-reports.md) |
| Ad Group | [`Ad Groups Report (Brands)`](get-brand-ad-group-reports.md) |
| Ad | [`Ads Report (Brands)`](get-brand-ad-reports.md) |
| Keyword | [`Keywords Report (Brands)`](get-brand-keyword-reports.md) |
| Search Term | [`Search Terms Report (Brands)`](get-brand-search-term-reports.md) |

##### Shared Object Model

Every Brands report request uses [`BrandsReportingRequest`](brandsreportingrequest.md) as its body. Each response row follows the same three-part shape:

- `metadata`: entity attributes (name, status, identifiers) plus any `groupBy` dimension value (`deviceClass`, `locationId`, or `supplyPlacement`) applied to that row. Entity-specific metadata schemas define the fields available for each entity, including [`BrandsReportingCampaign`](brandsreportingcampaign.md), [`BrandsReportingAdGroup`](brandsreportingadgroup.md), [`BrandsReportingAd`](brandsreportingad.md), [`BrandsReportingKeyword`](brandsreportingkeyword.md), and [`BrandsReportingSearchTerm`](brandsreportingsearchterm.md). Ad metadata nests creative details in a [`BrandsReportingCreative`](brandsreportingcreative.md) object rather than a flat creative ID.
- `totalMetrics`: aggregate [`BrandsMetrics`](brandsmetrics.md) (or entity variant, e.g. [`BrandsAdGroupMetrics`](brandsadgroupmetrics.md)) values for the row over the full requested date range.
- `granularMetrics`: an array of pure metrics objects, one per period in the requested `granularity`, with no dimension fields of their own. Only present when `granularity` is specified in the request.

Action-count fields (`actions`, `firstActions`, `getDirections`, `tapURL`, `call`, `share`, `getTheApp`, `galleryEngagement`) are objects keyed by attribution type (for example `{"tap": 170}`), not bare integers, in both `totalMetrics` and `granularMetrics`.

Each endpoint’s response envelope, row, and summary objects follow a consistent per-entity naming pattern, for example [`BrandsCampaignReportResponse`](brandscampaignreportresponse.md), [`BrandsCampaignReportRow`](brandscampaignreportrow.md), and [`BrandsCampaignResultContainer`](brandscampaignresultcontainer.md) for campaigns, with equivalent objects for ad groups, ads, keywords, and search terms.

For a side-by-side comparison of Brands and Apps reporting differences (groupBy dimensions, options, creative metadata), see [`Managing Reports`](reports.md).

## Topics

- [object BrandsReportingRequest](brandsreportingrequest.md)
  Request body for brands reporting queries.
- [object BrandsReportingCampaign](brandsreportingcampaign.md)
  Campaign metadata for Apple Maps report rows.
- [object BrandsReportingAdGroup](brandsreportingadgroup.md)
  Ad group metadata for brands report rows.
- [object BrandsReportingAd](brandsreportingad.md)
  Ad metadata for brands report rows.
- [object BrandsReportingCreative](brandsreportingcreative.md)
  Creative metadata for brands ads.
- [object BrandsReportingKeyword](brandsreportingkeyword.md)
  Keyword metadata for brands report rows, extending the base reporting keyword with brands-only internal fields.
- [object BrandsReportingSearchTerm](brandsreportingsearchterm.md)
  Search term metadata for brands report rows, extending the base reporting search term with brands-only internal fields.
- [object BrandsCampaignReportResponse](brandscampaignreportresponse.md)
  The top-level response envelope for Apple Maps campaign-level reports.
- [object BrandsCampaignReportRow](brandscampaignreportrow.md)
  A single row in an Apple Maps campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object BrandsCampaignReportSummary](brandscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apple Maps campaign report.
- [object BrandsCampaignResultContainer](brandscampaignresultcontainer.md)
  Wraps the array of Apple Maps campaign report rows along with a grand-total summary.
- [object BrandsAdGroupReportResponse](brandsadgroupreportresponse.md)
  The top-level response envelope for brands ad group reports.
- [object BrandsAdGroupReportRow](brandsadgroupreportrow.md)
  A single row in a Brands (Apple Maps) ad group report, pairing ad group metadata with total and granular performance metrics.
- [object BrandsAdGroupReportSummary](brandsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands ad group report.
- [object BrandsAdGroupResultContainer](brandsadgroupresultcontainer.md)
  Wraps the array of Brands ad group report rows along with a grand-total summary.
- [object BrandsAdReportResponse](brandsadreportresponse.md)
  The top-level response envelope for brands ad-level reports.
- [object BrandsAdReportRow](brandsadreportrow.md)
  A single row in a Brands (Apple Maps) ad-level report, pairing ad metadata with total and granular performance metrics.
- [object BrandsAdReportSummary](brandsadreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands ad-level report.
- [object BrandsAdResultContainer](brandsadresultcontainer.md)
  Wraps the array of Brands ad-level report rows along with a grand-total summary.
- [object BrandsKeywordReportResponse](brandskeywordreportresponse.md)
  The top-level response envelope for brands keyword-level reports.
- [object BrandsKeywordReportRow](brandskeywordreportrow.md)
  A single row in a Brands keyword report response.
- [object BrandsKeywordReportSummary](brandskeywordreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands keyword report.
- [object BrandsKeywordResultContainer](brandskeywordresultcontainer.md)
  Wraps the array of Brands keyword report rows along with a grand-total summary.
- [object BrandsSearchTermReportResponse](brandssearchtermreportresponse.md)
  The top-level response envelope for brands search term reports.
- [object BrandsSearchTermReportRow](brandssearchtermreportrow.md)
  A single row in a Brands search term report, pairing search-term metadata with total and granular performance metrics.
- [object BrandsSearchTermReportSummary](brandssearchtermreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands search term report.
- [object BrandsSearchTermResultContainer](brandssearchtermresultcontainer.md)
  Wraps the array of Brands search term report rows along with a grand-total summary.
- [object BrandsMetrics](brandsmetrics.md)
  Metrics for BRANDS promoted object type.
- [object BrandsCampaignMetrics](brandscampaignmetrics.md)
  Campaign-level metrics for BRANDS, inheriting all properties from `BrandsMetrics`.
- [object BrandsAdGroupMetrics](brandsadgroupmetrics.md)
  Ad group-level metrics for BRANDS, inheriting all properties from `BrandsMetrics`.
- [object BrandsOptions](brandsoptions.md)
  Report options for brands promoted object campaigns.
- [object BrandsTargetingProjection](brandstargetingprojection.md)
  Targeting projection for brands ad groups and campaigns.

## See Also

- [Managing Reports](reports.md)
  Retrieve performance data for campaigns, ad groups, ads, keywords, and search terms.
- [App Store Reports Endpoints](apps-reports-endpoints.md)
  Endpoints for retrieving App Store campaign, ad group, ad, keyword, and search term performance data.
- [Brands Reports Endpoints](brands-reports-endpoints.md)
  Retrieve performance data for Apple Maps campaigns, ad groups, ads, keywords, and search terms.
- [Apps Data Objects](apps-reports-objects.md)
  Request, response, and metadata objects for Apps report endpoints.
- [Shared Objects](reports-shared-objects.md)
  Shared request and response objects used across Apps and Brands report endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brands-reports-objects)*