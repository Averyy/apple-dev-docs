# CustomReportRequest

**Framework**: Apple Ads  
**Kind**: dictionary

The Impression Share report request body.

**Availability**:
- Search Ads 4.7+

## Declaration

```swift
object CustomReportRequest
```

#### Discussion

See also [`Impression Share Report`](impression-share-report.md),  [`Get a Single Impression Share Report`](get-a-single-impression-share-report.md), [`Get All Impression Share Reports`](get-all-impression-share-reports.md), and [`CustomReportResponse`](customreportresponse.md).

## Topics

### Objects
- [object CustomReportRequest.Selector](customreportrequest/selector-data.dictionary.md)
  A list of condition objects.

## Properties

- `dateRange` (string): The date range of the report request. A date range is required only when using `WEEKLY` granularity in [`Impression Share Report`](impression-share-report.md).
- `endTime` (string): The end time of the report. The format is `YYYY-MM-DD`, such as `2024-06-30`.
- `granularity` (string): The report data organized by day or week. Impression Share reports with a `WEEKLY` granularity value can’t have custom `startTime` and `endTime` in the request payload.
- `name` (string) *(required)*: A free-text field. The maximum length is 50 characters.
- `selector` (CustomReportRequest.Selector): [`Selector`](selector.md) is an optional parameter to filter API results using the [`CountryOrRegion`](countryorregion.md) and `adamId` fields.  For [`CountryOrRegion`](countryorregion.md), use an alpha-2 country code value. The `IN` operator is available to use with Impression Share reports. See [`SovCondition`](sovcondition.md) for [`Selector`](selector.md) descriptions and see [`Selector`](selector.md) for structural guidance with selectors. ```json
{
  "name": "impression_share_API_report_example",
  "granularity": "DAILY",
  "startTime": "2024-01-11",
  "endTime": "2024-02-08",
  "selector": {
    "conditions": [
      {
        "field": "adamId",
        "operator": "IN",
        "values": [
          1252497129,
          282614216
        ]
      },
      {
        "field": "countryOrRegion",
        "operator": "IN",
        "values": [
          "US",
          "CA"
        ]
      }
    ]
  }
}
```
- `startTime` (string): The start time of the report. The format is `YYYY-MM-DD`, such as `2024-06-01`.

## See Also

- [object CustomReportResponse](customreportresponse.md)
  A container for Impression Share report metrics.
- [object CustomReportResponseBody](customreportresponsebody.md)
  A container for the Impression Share report response body.
- [object SovCondition](sovcondition.md)
  The list of condition objects that allow users to filter a list of records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/customreportrequest)*