# ReportingKeyword

**Framework**: Apple Ads  
**Kind**: dictionary

The response to a request to fetch keyword-level reports.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object ReportingKeyword
```

## Properties

- `adGroupDeleted` (boolean): An indicator of whether the ad group is soft-deleted. You can use the `EQUALS` and `IN` selector [`Condition`](condition.md) operators with [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- `adGroupId` (int64): The unique identifier for the ad group. You can use the `EQUALS`, `IN`, and `STARTSWITH` selector [`Condition`](condition.md) operators with [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- `adGroupName` (string): The name of the ad group, which is unique within the campaign. Responses don’t include deleted ad groups. You can use the `EQUALS`, `IN`, and `STARTSWITH` selector [`Condition`](condition.md) operators with [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- `bidAmount` (Money): This is the offer price for a keyword in a bidding auction. If the `bidAmount` field is `null`, the `bidAmount` uses the `defaultBidAmount` of the corresponding ad group.
- `campaignId` (int64): The unique identifier for the campaign. You can use the `EQUALS`, `IN`, and `STARTSWITH` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- `deleted` (boolean): An indicator of whether the keyword is soft-deleted. You can use the `EQUALS` and `IN` selector [`Condition`](condition.md) operators with [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- `keyword` (string): The name of a keyword that belongs to an ad group. You can use the `EQUALS`, `IN`, and `STARTSWITH` selector [`Condition`](condition.md) operators with [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- `keywordDisplayStatus` (string): The state of the keyword display operation. You can use the `EQUALS` and `IN` selector [`Condition`](condition.md) operators with [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- `keywordId` (int64): The unique identifier of a keyword that belongs to an ad group.
- `keywordStatus` (string): The status of the keyword.
- `matchType` (string): An automated keyword and bidding strategy. See [`Ad Groups`](ad-groups.md) for Search Match use cases. - **`Auto`**: Specifies the system serves impressions with optimized keywords, in addition to those you explicitly add to the ad group.
- **`Broad`**: Ensures your ads don’t run on relevant, close variants of a keyword, such as singulars, plurals, misspellings, synonyms, related searches, and phrases that include that term (fully or partially).
- **`Exact`**: Offers the most control over searches  your ad may appear in. You can target a specific term and its close variants, such as common misspellings and plurals. Your ad may receive fewer impressions as a result, but your tap-through rates (TTRs) and conversions on those impressions may be higher because you’re reaching users most interested in your app. You can use the `EQUALS` selector [`Condition`](condition.md) operator with [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- `modificationTime` (date-time): The date and time of the most recent modification of the object.
- `orgId` (int64): The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com).

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/reportingkeyword)*