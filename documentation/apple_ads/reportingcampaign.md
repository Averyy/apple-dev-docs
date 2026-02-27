# ReportingCampaign

**Framework**: Apple Ads  
**Kind**: dictionary

The response to a request to fetch campaign-level reports.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object ReportingCampaign
```

## Mentions

- [Apple Ads Campaign Management API 2](apple-search-ads-campaign-management-api-2.md)

## Topics

### Objects
- [object Campaign.CountryOrRegionServingStateReasons](campaign/countryorregionservingstatereasons-data.dictionary.md)
  Reasons why a campaign can’t run.
### Dictionaries
- [object ReportingCampaign.CountryOrRegionServingStateReasons](reportingcampaign/countryorregionservingstatereasons-data.dictionary.md)
  Reasons that return when a campaign can’t run.
- [object ReportingCampaign.TargetCpa](reportingcampaign/targetcpa-data.dictionary.md)

## Properties

- `adChannelType` (string): The channel type of ad in a campaign. See [`AdChannelType`](adchanneltype.md) for value descriptions. You can use the `EQUALS` [`Selector`](selector.md) [`Condition`](condition.md) operator with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `app` (CampaignAppDetail): The name of the app and the `adamId`.
- `campaignId` (int64): The identifier for the campaign. You can use the `EQUALS`, `IN`, and `STARTSWITH` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `biddingStrategy` (string): The bid strategy for the campaign. See [`Campaigns`](campaigns.md). You can use the `EQUALS`, `IN`, and `STARTSWITH` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `campaignName` (string): The unique name of the campaign. You can use the `EQUALS`, `IN`, and `STARTSWITH` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `campaignStatus` (string): The status of the campaign. See [`CampaignStatus`](campaignstatus.md) for value descriptions. You can use the `EQUALS` [`Selector`](selector.md) [`Condition`](condition.md) operator with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `countriesOrRegions` ([string]): The App Store geoterritories where you’re promoting your app. This field requires an ISO 3166-1 alpha-2 country code value for the locations where you’re promoting. The default value is `US`. You can use the `EQUALS`, `CONTAINS_ANY`, and `CONTAINS_ALL` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `countryOrRegionServingStateReasons` (ReportingCampaign.CountryOrRegionServingStateReasons): The map of reasons that returns when a campaign isn’t running.
- `dailyBudget` (Money): The daily budget amount available to the campaign. This is the equivalent of `dailyBudgetAmount` in your [`Campaign`](campaign.md).
- `deleted` (boolean): The indicator of whether the campaign is soft-deleted. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `displayStatus` (string): The status of the campaign. The status resolves according to `servingStatus` and additional criteria.
- `modificationTime` (date-time): The date and time of the most recent modification of the object.
- `orgId` (int64): The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/).
- `servingStateReasons` ([string]): A list of reasons that displays when a campaign can’t run. See [`CampaignServingStateReasons`](campaignservingstatereasons.md) for value descriptions.
- `servingStatus` (string): The status of the campaign. You can use the `EQUALS` [`Selector`](selector.md) [`Condition`](condition.md) operator with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `supplySources` ([string]): The ad placements for a campaign. See [`SupplySource`](supplysource.md) for value descriptions and validations. You can use the `CONTAINS_ANY`, `CONTAINS_ALL`, and `EQUALS` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Get Campaign-Level Reports`](get-campaign-level-reports.md).
- `targetCpa` (ReportingCampaign.TargetCpa): The target cost-per-acquisition for `MAX_CONVERSIONS` campaigns. The Target CPA is the average amount you want to spend per tap-through install. This amount is used to calculate optimal bids for each search query, with the goal of maximizing the number of installs near your target CPA.
- `totalBudget` (Money): The total campaign budget amount. This is the equivalent of `budgetAmount` in your [`Campaign`](campaign.md).

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/reportingcampaign)*