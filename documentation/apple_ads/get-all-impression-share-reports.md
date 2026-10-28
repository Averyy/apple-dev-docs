# Get All Impression Share Reports

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches all Impression Share reports containing metrics and metadata.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

Use this endpoint to return all Impression Share reports containing metrics and metadata. Use query parameters as needed.

The rate limit for this endpoint is 150 reports within 15 minutes.

### Payload example:  All Impression Share reports

**Request**:

```
HTTP GET https://api.searchads.apple.com/api/v5/custom-reports
```

**Response**:

```json
{
  "data": [
    {
      "id": 965992,
      "name": "impression_share_report_example_3",
      "startTime": "2024-10-14",
      "endTime": "2024-11-12",
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
          },
          {
            "field": "adamId",
            "operator": "IN",
            "values": [
              "1252497129",
              "282614216"
            ]
          }
        ]
      },
      "state": "COMPLETED",
      "creationTime": "2024-02-07T09:23:03.532",
      "modificationTime": "2024-02-07T09:23:09.774",
      "dateRange": "LAST_2_WEEKS"
    },
    {
      "id": 16627,
      "name": "impression_share_report_4",
      "startTime": "2024-09-15",
      "endTime": "2024-10-10",
      "granularity": "DAILY",
      "downloadUri": "http://blobstore.apple.com...",
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
          },
          {
            "field": "adamId",
            "operator": "IN",
            "values": [
              "1252497129",
              "282614216"
            ]
          }
        ]
      },
      "state": "COMPLETED",
      "creationTime": "2024-02-07T09:14:46.235",
      "modificationTime": "2024-02-07T09:14:53.173",
      "dateRange": "LAST_2_WEEKS"
    }
  ],
  "pagination": {
    "totalResults": 2,
    "startIndex": 0,
    "itemsPerPage": 2
  },
  "error": null
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/custom-reports`

## Parameters

### Query Parameters

- `field` (string): The name of a field.

  **Default**: `creationTime`
- `limit` (integer): The number of items to return per request. For most objects, the default is `20` and the maximum is `50`.

  **Default**: `20`; **Minimum**: `1`
- `offset` (integer): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.

  **Default**: `0`; **Minimum**: `0`
- `sortOrder` (string): The order of grouped results.

  **Default**: `DESCENDING`

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
- [Impression Share Report](./impression-share-report.md)
  Obtain a report ID.
- [Get a Single Impression Share Report](./get-a-single-impression-share-report.md)
  Fetches a single Impression Share report containing metrics and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-impression-share-reports)*