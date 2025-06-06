# Reports

**Framework**: Apple Search Ads

Generate performance metrics for your campaigns.

#### Overview

You can fetch reports for campaigns, ad groups, targeting keywords, search terms, and creative sets. See the [`ReportingRequest`](reportingrequest.md) object for guidance for setting up your report request payloads.

## Topics

### Reports Endpoints
- [Get Campaign-Level Reports](get-campaign-level-reports.md)
  Fetches reports for campaigns.
- [Get Ad Group-Level Reports](get-ad-group-level-reports.md)
  Fetches reports for ad groups within a campaign.
- [Get Keyword-Level Reports](get-keyword-level-reports.md)
  Fetches reports for targeting keywords within a campaign.
- [Get Keyword-Level within Ad Group Reports](get-keyword-level-within-ad-group-reports.md)
  Fetches reports for targeting keywords within an ad group.
- [Get Search Term-Level Reports](get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Search Term-Level within Ad Group Reports](get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.
- [Get Ad-Level Reports](get-ad-level-reports.md)
  Fetches ad performance data within a campaign.
### Reports Request and Response Objects
- [object ReportingRequest](reportingrequest.md)
  The report request body.
- [object ReportingResponseBody](reportingresponsebody.md)
  The container object for the report response body.
- [object ReportingResponse](reportingresponse.md)
  The container object of report metrics.
- [object ReportingDataResponse](reportingdataresponse.md)
  The total metrics for a report.
- [object GrandTotalsRow](grandtotalsrow.md)
  The summary of cumulative metrics.
- [object SpendRow](spendrow.md)
  The reporting response metrics.
- [object ExtendedSpendRow](extendedspendrow.md)
  The descriptions of metrics with dates.
- [object Row](row.md)
  The report metrics by time granularity.
- [object ReportingCampaign](reportingcampaign.md)
  The response to a request to fetch campaign-level reports.
- [object ReportingAdGroup](reportingadgroup.md)
  The response to a request to fetch ad group-level reports.
- [object ReportingKeyword](reportingkeyword.md)
  The response to a request to fetch keyword-level reports.
- [object ReportingSearchTerm](reportingsearchterm.md)
  The response to a request to fetch search term-level reports.
- [object ReportingAd](reportingad.md)
  The response to a request to fetch ad-level reports.
- [object CampaignAppDetail](campaignappdetail.md)
  The app data to fetch from campaign-level reports.
- [object InsightsObject](insightsobject.md)
  The container object for bid recommendations.
- [object KeywordInsights](keywordinsights.md)
  The object that contains bid recommendations.
- [object KeywordBidRecommendation](keywordbidrecommendation.md)
  The suggested bid amount for a keyword.
### Data Types
- [type MetaDataObject](metadataobject.md)
  The report response objects.

## See Also

- [Impression Share Reports](impression-share-reports.md)
  Obtain metrics with impression share insights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/reports)*