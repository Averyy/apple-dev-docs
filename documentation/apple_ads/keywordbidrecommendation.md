# KeywordBidRecommendation

**Framework**: Apple Ads  
**Kind**: dictionary

The suggested bid amount for a keyword.

**Availability**:
- Search Ads 3.0+

## Declaration

```swift
object KeywordBidRecommendation
```

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Overview

For keywords in Maximize Conversions campaigns, the `suggestedBidAmount` field is returned as `null`.

#### Discussion

In [`Apple Ads Campaign Management API 5`](apple-search-ads-campaign-management-api-5.md), the `suggestedBidAmount` field  replaces the deprecated `bidMin` and `bidMax` fields.

## Properties

- `suggestedBidAmount` (Money): An indicator that varies over time to help you incrementally increase the likelihood of your ad showing in searches in the App Store. A `suggestedBidAmount` isn’t a representation of a bid floor or ceiling.  A `suggestedBidAmount` is based on various factors, including, but not limited to, historical data related to past performance and recommendations. Actual outcomes, including changes in spend and average CPA, may vary.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/keywordbidrecommendation)*