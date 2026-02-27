# ReportingAd

**Framework**: Apple Ads  
**Kind**: dictionary

The response to a request to fetch ad-level reports.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
object ReportingAd
```

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

## Properties

- `adDisplayStatus` (string): The `DisplayStatus` that derives from the ad’s serving status. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Ad-Level Reports`](get-ad-level-reports.md) within a campaign.
- `adGroupId` (int64): The unique identifier for the ad group the [`Creative`](creative.md) belongs to. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Ad-Level Reports`](get-ad-level-reports.md) within a campaign. You can use this field with the `orderBy` selector.
- `adId` (int64): A unique identifier that represents the assignment relationship between an ad group and an [`Ad`](ad.md). You can use the `EQUALS`, `IN`, and `STARTSWITH` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Ad-Level Reports`](get-ad-level-reports.md) within a campaign.
- `adName` (string): The unique name of a custom product page. The `adName` has to be unique within its ad group. You can use this field with the `orderBy` selector.
- `adServingStateReasons` (string): A list of reasons that displays when an ad isn’t running. You can use this field with the `orderBy` selector.
- `campaignId` (int64): The unique identifier for a campaign. You can use this field with the `orderBy` selector.
- `creationTime` (date-time): The date and time of the creation of the [`Ad`](ad.md) object. You can use this field with the `orderBy` selector.
- `creativeId` (int64): The unique identifier for a creative. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Ad-Level Reports`](get-ad-level-reports.md) within a campaign.
- `creativeType` (string): The type of creative asset. Synonymous with `type` in the [`Creative`](creative.md) object. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Ad-Level Reports`](get-ad-level-reports.md) within a campaign.
- `deleted` (boolean): An indicator of whether a creative asset is soft-deleted.. You can use the `EQUALS` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Ad-Level Reports`](get-ad-level-reports.md) within a campaign.
- `language` (string): The language of the [`Creative`](creative.md).
- `modificationTime` (date-time): The date and time of the most recent modification of the object. You can use this field with the `orderBy` selector.
- `orgId` (int64): The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/). You can use this field with the `orderBy` selector.
- `productPageId` (string): A unique string to identify a product page on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com), such as `45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.
- `status` (string): The status of creative assets. You can use this field with the `orderBy` selector.

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
- [object CampaignAppDetail](campaignappdetail.md)
  The app data to fetch from campaign-level reports.
- [object InsightsObject](insightsobject.md)
  The container object for bid recommendations.
- [object KeywordInsights](keywordinsights.md)
  The object that contains bid recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/reportingad)*