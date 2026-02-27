# ExtendedSpendRow

**Framework**: Apple Ads  
**Kind**: dictionary

The descriptions of metrics with dates.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object ExtendedSpendRow
```

## Mentions

- [Apple Ads Campaign Management API 2](apple-search-ads-campaign-management-api-2.md)
- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

## Properties

- `avgCPM` (Money): The average CPM is the average amount you pay per one thousand ad impressions.
- `avgCPT` (Money): The average cost-per-tap (CPT) is the ratio of spend over taps.
- `date` (string): The date range of the report. The format is `MM-DD-YYYY HH`.
- `impressions` (int64): The number of times your ad appears in App Store search results within the reporting period.
- `localSpend` (Money): The total spend of a campaign in the currency the organization uses.
- `tapInstallCPI` (Money): Prior to API 5, this was the `avgCPA` field. The total campaign spend divided by the number of tap-through installs within the reporting period.
- `tapInstallRate` (double): Prior to API 5, this was the `conversionRate` field. The total number of tap-through installs divided by the total number of taps within the reporting period.
- `tapInstalls` (int64): Prior to API 5, this was the `installs` field. The total number of new downloads and redownloads from people who tapped your ad within a 30-day attribution window.
- `tapNewDownloads` (int64): Prior to API 5, this was the `newDownloads` field. New downloads from people who tapped your ad within a 30-day attribution window. The API counts new downloads when someone downloads your app to a device where your app hasn’t previously been installed.
- `tapRedownloads` (int64): Prior to API 5, this was the `redownloads` field. Redownloads from people who tapped your ad within a 30-day attribution window. The API counts redownloads when someone downloads your app, deletes it, and downloads it again on the same device, or a different one, following an ad tap.
- `taps` (int64): The number of times people tap your ad within the reporting period.
- `tapPreOrdersPlaced` (int64): The total number of pre-orders placed by users who tapped your ad. A pre-order placed (tap-through) is counted when a user has tapped your ad and authenticated with Face ID, Touch ID, or their passcode to allow the app to be downloaded on release day, within a 30-day window of the ad tap, and within 60 days of the app download. This does not account for any pre-orders canceled after the pre-order has been placed.
- `totalAvgCPI` (Money): The total campaign spend divided by the total number of installs within the reporting period.
- `totalInstallRate` (double): The total number of installs divided by the total number of taps within the reporting period.
- `totalInstalls` (int64): The total number of tap-through and view-through new downloads and redownloads within the reporting period.
- `totalNewDownloads` (int64): The total number of tap-through and view-through new downloads within the reporting period.
- `totalRedownloads` (int64): The total number of tap-through and view-through redownloads within the reporting period.
- `totalPreOrdersPlaced` (int64): The total number of tap-through and view-through pre-orders placed resulting from an ad within the reporting period.
- `ttr` (double): The tap-through rate (TTR) is the number of times people tap your ad divided by the total impressions your ad receives.
- `viewInstalls` (int64): The total number of new downloads and redownloads from people who viewed your ad, but didn’t tap it, within a 1-day attribution window.
- `viewNewDownloads` (int64): New downloads from people who viewed your ad, but didn’t tap it, within a 1-day attribution window. The API counts new downloads when someone downloads your app to a device where your app hasn’t previously been installed.
- `viewPreOrdersPlaced` (int64): The total number of pre-orders placed from users who viewed your ad, but didn’t tap it. A pre-order placed (view-through) is counted within 24 hours of viewing your ad, and within 60 days of the app download. This does not account for any pre-orders canceled after the pre-order has been placed.
- `viewRedownloads` (int64): Redownloads from people who viewed your ad, but didn’t tap it, within a 1-day attribution window. The API counts redownloads when someone downloads your app, deletes it, and downloads it again on the same device, or a different one, following an ad view.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/extendedspendrow)*