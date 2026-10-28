# Get Search Term-Level within Ad Group Reports

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches reports for search terms within an ad group.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)

## Discussion

Use this endpoint to fetch reports with a high volume of search terms in your campaign. See [`ReportingSearchTerm`](./reportingsearchterm.md) for [`Condition`](./condition.md) operators and field values to filter results with a [`Selector`](./selector.md).

The limit for search term-level reports is 10 impressions. Search term-level reports only support a `timeZone` value of `ORTZ`. The `orderBy` [`Selector`](./selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingSearchTerm`](./reportingsearchterm.md) fields are available to the `orderBy` [`Selector`](./selector.md).

### Payload example: Get search term-level within ad group reports

**Request**:

```
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/adgroups/{adgroupId}/searchterms

{
  "startTime": "2024-04-08",
  "endTime": "2024-04-09",
  "timeZone": "ORTZ",
  "returnRowTotals": true,
  "returnGrandTotals": true,
  "returnRecordsWithNoMetrics": false,
  "selector": {
    "orderBy": [
      {
        "field": "localSpend",
        "sortOrder": "DESCENDING"
      }
    ],
    "conditions": [],
    "pagination": {
      "offset": null,
      "limit": null
    }
  },
  "groupBy": null
}
```

**Response**:

```json
{
      "row": [
        {
          "other": true,
          "total": {
          "impressions": 41,
          "taps": 1,
          "totalInstalls": 1,
          "totalNewDownloads": 2,
          "totalRedownloads": 1,
          "viewInstalls": 1,
          "tapInstalls": 5,
          "tapNewDownloads": 2,
          "tapRedownloads": 3,
          "viewNewDownloads": 6,
          "viewReDownloads": 3,
          "tapPreOrdersPlaced": 0,
          "viewPreOrdersPlaced": 0,
          "totalPreOrdersPlaced": 0,
          "totalInstallRate": 2.962 
          "ttr": 0.0244,
          "tapInstallCPI": {
            "amount": "0",
            "currency": "USD"
            },
          "avgCPT": {
            "amount": "0.88",
            "currency": "USD"
            },
          "localSpend": {
            "amount": "0.88",
            "currency": "USD"
            },
          "tapInstallRate": 0.873,
          "date": "2024-08-10"
          },
          "metadata": {
            "keywordId": 87675434,
            "keyword": "keyword 2",
            "matchType": "EXACT",
            "bidAmount": {
              "amount": "2",
              "currency": "USD"
            },
            "deleted": false,
            "keywordDisplayStatus": "RUNNING",
            "adGroupId": 427916203,
            "adGroupName": "ad group 1",
            "adGroupDeleted": false,
            "searchTermText": null,
            "searchTermSource": "TARGETED"
         }
      }
    ]
  }

```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/adgroups/{adgroupId}/searchterms`

## Parameters

### Path Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `ReportingRequest`

The report request body consisting of metrics and dimensions to use as filters.

## Responses

- `200` OK (`ReportingResponseBody`, `application/json`): If the call succeeds, the API returns the [`ReportingResponse`](./reportingresponse.md) object in the response payload with an HTTP status code of `200 (OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ErrorResponseBody`, `application/json`): An invalid query or missing required parameters.
- `404` Not Found (`ErrorResponseBody`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ErrorResponseBody`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Reports Endpoints
- [Get Campaign-Level Reports](./get-campaign-level-reports.md)
  Fetches reports for campaigns.
- [Get Ad Group-Level Reports](./get-ad-group-level-reports.md)
  Fetches reports for ad groups within a campaign.
- [Get Keyword-Level Reports](./get-keyword-level-reports.md)
  Fetches reports for targeting keywords within a campaign.
- [Get Keyword-Level within Ad Group Reports](./get-keyword-level-within-ad-group-reports.md)
  Fetches reports for targeting keywords within an ad group.
- [Get Search Term-Level Reports](./get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Ad-Level Reports](./get-ad-level-reports.md)
  Fetches ad performance data within a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-search-term-level-within-ad-group-reports)*