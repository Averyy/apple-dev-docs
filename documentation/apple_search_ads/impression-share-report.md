# Impression Share Report

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Obtain a report ID.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to obtain a `reportId` to use in a [`Get a Single Impression Share Report`](get-a-single-impression-share-report.md) request. This endopoint supports selectors. See [`CustomReportRequest`](customreportrequest.md) for selector structure.

- You can generate up to 10 reports within 24 hours.
- You can create reports for a range of up to 30 days for any time period after `2020-04-12`.
- You can’t edit or remove report fields.
- Impression Share reports with a `WEEKLY` granularity value can’t have custom `startTime` and `endTime` in the request payload. Use `dateRange` instead. See [`CustomReportRequest`](customreportrequest.md).

##### Payload Example Obtain a Report Id

## Request Body

The impression share report request body, consisting of metrics and dimensions to filter on.

## See Also

- [Get a Single Impression Share Report](get-a-single-impression-share-report.md)
  Fetches a single Impression Share report containing metrics and metadata.
- [Get All Impression Share Reports](get-all-impression-share-reports.md)
  Fetches all Impression Share reports containing metrics and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/impression-share-report)*