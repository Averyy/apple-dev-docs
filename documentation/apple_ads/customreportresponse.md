# CustomReportResponse

**Framework**: Apple Ads  
**Kind**: dictionary

A container for Impression Share report metrics.

**Availability**:
- Search Ads 4.7+

## Declaration

```swift
object CustomReportResponse
```

#### Discussion

See also [`Impression Share Report`](impression-share-report.md),  [`Get a Single Impression Share Report`](get-a-single-impression-share-report.md), [`Get All Impression Share Reports`](get-all-impression-share-reports.md), and [`CustomReportRequest`](customreportrequest.md).

## Topics

### Objects
- [object CustomReportResponse.Selector](customreportresponse/selector-data.dictionary.md)
  A list of condition objects.

## Properties

- `creationTime` (string): The timestamp for the creation of the report in the format of `YYYY-MM-DD’T’HH:mm:ss.SSS`.
- `dimensions` ([string]): - **`adamId`**: Your unique App Store app identifier.
- **`appName`**: The name of the app.
- **[`CountryOrRegion`](countryorregion.md)**: The App Store geoterritory where you’re promoting your app.
- **`searchTerm`**: The search terms to use for app searches.
- `downloadUri` (string): The report download link.  The `state` of the report needs to be `COMPLETED` for a valid URL to return when calling [`Get a Single Impression Share Report`](get-a-single-impression-share-report.md) or [`Get All Impression Share Reports`](get-all-impression-share-reports.md). A response of `null` means the report generation is still in progress. URLs expire 90 seconds after creation. Reports remain active for 2 days.
- `endTime` (string): The end time of the report. The format is `YYYY-MM-DD`, such as `2024-06-30`.
- `granularity` (string): The report data organized by day or week.
- `id` (int64): The report `id` is a unique identifier per report.
- `metrics` ([string]): Impression Share is a daily aggregation with a range in deciles, such as 11–20% and 21–30%. App impressions for search terms correlate by country or region and organization against the total requests for country- or region-search term combinations. Search terms need to have more than 10 impressions per day for inclusion in a daily  Impression Share report. - **`lowImpressionShare`**: If impression share is 11–20%, `lowImpressionShare` is 0.11 and `highImpressionShare` is 0.2.
- **`highImpressionShare`**: If impression share is 91–100%, `lowImpressionShare` is 0.91 and `highImpressionShare` is 1.
- **`rank`**: The ranking of your app in terms of impression share compared to other apps in the same countries or regions. The rank displays from `ONE` to `FIVE` or `GREATER_THAN_FIVE`, with `ONE` being the highest rank.
- **`searchPopularity`**: The total search volume of keyword popularity. The popularity of search terms is based on country or region. The ranking is 1–5, with 5 as the most search volume.
- `modificationTime` (string): The most recent timestamp of report modifications in the format of `YYYY-MM-DD’T’HH:mm:ss.SSS`.
- `name` (string): A free-text field. The maximum length is 50 characters.
- `selector` (CustomReportResponse.Selector): [`Selector`](selector.md) is an optional parameter to filter API results using the [`CountryOrRegion`](countryorregion.md) and `adamId` fields. For [`CountryOrRegion`](countryorregion.md), use alpha-2 country code values. The `IN` operator is available to use with Impression Share reports. See [`SovCondition`](sovcondition.md) for selector descriptions and see [`Selector`](selector.md) for structural guidance with selectors.
- `startTime` (string): The start time of the report. The format is `YYYY-MM-DD`, such as `2024-06-01`.
- `state` (string): The state of the report. A value of `COMPLETED` has a report link in the `downloadUri` field.

## See Also

- [object CustomReportRequest](customreportrequest.md)
  The Impression Share report request body.
- [object CustomReportResponseBody](customreportresponsebody.md)
  A container for the Impression Share report response body.
- [object SovCondition](sovcondition.md)
  The list of condition objects that allow users to filter a list of records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/customreportresponse)*