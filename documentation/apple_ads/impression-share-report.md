# Impression Share Report

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Obtain a report ID.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

Use this endpoint to obtain a `reportId` to use in a [`Get a Single Impression Share Report`](./get-a-single-impression-share-report.md) request. This endopoint supports selectors. See [`CustomReportRequest`](./customreportrequest.md) for selector structure.

- You can generate up to 10 reports within 24 hours.
- You can create reports for a range of up to 30 days for any time period after `2020-04-12`.
- You can’t edit or remove report fields.
- Impression Share reports with a `WEEKLY` granularity value can’t have custom `startTime` and `endTime` in the request payload. Use `dateRange` instead. See [`CustomReportRequest`](./customreportrequest.md).

##### Payload example: Obtain a report ID

**Request**:

```
POST https://api.searchads.apple.com/api/v5/custom-reports

{
  "name": "impression_share_API_report_example_1",
  "startTime": "2024-01-20",
  "endTime": "2024-01-29",
  "granularity": "DAILY",
  "selector": {
    "conditions": [
      {
        "field": "countryOrRegion",
        "operator": "IN",
        "values": [
          "US",
          "AU"
        ]
      }
    ]
  }
}
```

**Response**:

```json
{
  "data": {
    "id": 986235,
    "name": "impression_share_API_report_example_1",
    "startTime": "2024-01-20",
    "endTime": "2024-01-29",
    "granularity": "DAILY",
    "downloadUri": "https://ads-...us-west-2.amazonaws.com/ext-sov-reports/",
    "dimensions": [
      "appName",
      "adamId",
      "countryOrRegion",
      "searchTerm"
    ],
    "metrics": [
      "lowImpressionShare",
      "highImpressionShare",
      "rank",
      "searchPopularity"
    ],
    "selector": {
      "conditions": [
        {
          "field": "countryOrRegion",
          "operator": "IN",
          "values": [
            "US",
            "AU"
          ]
        }
      ]
    },
    "state": "QUEUED",
    "creationTime": "2024-01-12T04:47:27.782",
    "modificationTime": "2024-01-12T04:47:27.782"
  },
  "pagination": null,
  "error": null
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/custom-reports`

## Request Body

**Content-Type**: `application/json`  
**Type**: `CustomReportRequest`

The impression share report request body, consisting of metrics and dimensions to filter on.

## Responses

- `200` OK (`CustomReportResponseBody`, `application/json`): If the call succeeds, the API returns the [`CustomReportResponseBody`](./customreportresponsebody.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Impression Share Report Endpoints
- [Get a Single Impression Share Report](./get-a-single-impression-share-report.md)
  Fetches a single Impression Share report containing metrics and metadata.
- [Get All Impression Share Reports](./get-all-impression-share-reports.md)
  Fetches all Impression Share reports containing metrics and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/impression-share-report)*