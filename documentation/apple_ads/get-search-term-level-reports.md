# Get Search Term-Level Reports

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches reports for search terms within a campaign.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)

## Discussion

Use this endpoint to fetch reports for search terms in your campaigns. See [`ReportingSearchTerm`](./reportingsearchterm.md) for [`Condition`](./condition.md) operators and field values to filter results with a [`Selector`](./selector.md).

The limit for search term-level reports is 10 impressions. Search term-level reports only support a `timeZone` value of `ORTZ`. The `orderBy` [`Selector`](./selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingSearchTerm`](./reportingsearchterm.md) fields are available to the `orderBy` [`Selector`](./selector.md).

### Payload example: Get search term-level reports

**Request**:

```
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/searchterms

{
    "startTime": "2024-04-08",
    "endTime": "2024-04-09",
    "timeZone": "ORTZ",
    "selector": {
        "orderBy": [
            {
                "field": "impressions",
                "sortOrder": "DESCENDING"
            }
        ],
        "pagination": {
            "offset": 0,
            "limit": 1000
        }
    },
    "groupBy": [
        "countryOrRegion"
    ],
    "returnRecordsWithNoMetrics": "false",
    "returnRowTotals": true,
    "returnGrandTotals": true
}
```

**Response**:

```json
{
      "row": [
        {
          "other": true,
          "total": {
          "impressions": 53,
          "taps": 45,
          "ttr": 0.45,
          "avgCPT": {
            "amount": "0",
            "currency": "USD"
        },
         "avgCPM": {
           "amount": "0",
           "currency": "USD"
        },
        "localSpend": {
          "amount": "0",
          "currency":"USD"
        },
        "totalInstalls": 16,
        "totalNewDownloads": 23,
        "totalRedownloads": 17,
        "viewInstalls": 18,
        "tapInstalls": 59,
        "tapNewDownloads": 22,
        "tapRedownloads": 35,
        "viewNewDownloads": 67,
        "viewReDownloads": 53,
        "tapPreOrdersPlaced": 0,
        "viewPreOrdersPlaced": 0,
        "totalPreOrdersPlaced": 0,
        "totalAvgCPI": {
           "amount": "1.57",
           "currency": "USD"
           },
        "totalInstallRate": 2.962
        "tapInstallCPI": {
          "amount": "0",
          "currency": "USD"
        },
       "tapInstallRate": 0.7654,
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
            "countryOrRegion": "US",
            "searchTermSource": "TARGETED"
          }
        },
        {
          "other": false,
          "total": {
          "taps": 45,
          "ttr": 0.45,
          "avgCPT": {
            "amount": "0",
            "currency": "USD"
        },
         "avgCPM": {
           "amount": "0",
           "currency": "USD"
        },
        "localSpend": {
          "amount": "0",
          "currency":"USD"
        },
        "totalInstalls": 16,
        "totalNewDownloads": 23,
        "totalRedownloads": 17,
        "viewInstalls": 18,
        "tapInstalls": 59,
        "tapNewDownloads": 22,
        "tapRedownloads": 35,
        "viewNewDownloads": 67,
        "viewReDownloads": 53,
        "tapPreOrdersPlaced": 0,
        "viewPreOrdersPlaced": 0,
        "totalPreOrdersPlaced": 0,
        "totalAvgCPI": {
           "amount": "1.57",
           "currency": "USD"
           },
        "totalInstallRate": 2.962
        "tapInstallCPI": {
          "amount": "0",
          "currency": "USD"
        },
       "tapInstallRate": 0.7654,
       "date": "2024-08-10"
      },
           "metadata": {
            "keywordId": 87675433,
            "keyword": "keyword name example 4",
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
            "searchTermText": "trip trek",
            "countryOrRegion": "US",
            "searchTermSource": "TARGETED"
          }
        },
        {
          "other": true,
          "total": {
            "impressions": 53,
            "taps": 45,
            "ttr": 0.45,
            "avgCPT": {
            "amount": “0”,
            "currency": “USD”
        },
           "avgCPM": {
             "amount": "0",
             "currency": "USD"
        },
        "localSpend": {
            "amount": "0",
            "currency":"USD"
        },
        "totalInstalls": 16,
        "totalNewDownloads": 23,
        "totalRedownloads": 17,
        "viewInstalls": 18,
        "tapInstalls": 59,
        "tapNewDownloads": 22,
        "tapRedownloads": 35,
        "viewNewDownloads": 67,
        "viewReDownloads": 53,
        "tapPreOrdersPlaced": 0,
        "viewPreOrdersPlaced": 0,
        "totalPreOrdersPlaced": 0,
        "totalAvgCPI": {
           "amount": "1.57",
           "currency": "USD"
           },
        "totalInstallRate": 2.962
        "tapInstallCPI": {
          "amount": “0”,
          "currency": "USD"
        },
       "tapInstallRate": 0.7654,
       "date": "2024-08-10"
      },
           "metadata": {
            "keywordId": 87675432,
            "keyword": "keyword 3",
            "matchType": "EXACT",
            "bidAmount": {
              "amount": "2",
              "currency": "USD"
            },
            "deleted": false,
            "keywordDisplayStatus": "PAUSED",
            "adGroupId": 427916203,
            "adGroupName": "ad group 1",
            "adGroupDeleted": false,
            "searchTermText": null,
            "countryOrRegion": "US",
            "searchTermSource": "TARGETED"
          }
        }
      ],
      "grandTotals": {
        "other": false,
        "total": {
          "impressions": 53,
          "taps": 45,
          "ttr": 0.45,
          "avgCPT": {
            "amount": "0",
            "currency": "USD"
        },
         "avgCPM": {
           "amount": "0",
           "currency": "USD"
        },
        "localSpend": {
          "amount": "0",
          "currency":"USD"
        },
        "totalInstalls": 16,
        "totalNewDownloads": 23,
        "totalRedownloads": 17,
        "viewInstalls": 18,
        "tapInstalls": 59,
        "tapNewDownloads": 22,
        "tapRedownloads": 35,
        "viewNewDownloads": 67,
        "viewReDownloads": 53,
        "tapPreOrdersPlaced": 0,
        "viewPreOrdersPlaced": 0,
        "totalPreOrdersPlaced": 0,
        "totalAvgCPI": {
           "amount": "1.57",
           "currency": "USD"
           },
        "totalInstallRate": 2.962
        "tapInstallCPI": {
          "amount": "0",
          "currency": "USD"
        },
       "tapInstallRate": 0.7654,
       "date": "2024-08-10"
      },
 
    }
   }
 }
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/searchterms`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `ReportingRequest`

The report request body consisting of metrics and dimensions to use as filters.

## Responses

- `200` OK (`ReportingResponseBody`, `application/json`): If the call succeeds, the API returns the [`ReportingResponse`](./reportingresponse.md) object in the response payload with an HTTP status code of `200 (OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

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
- [Get Search Term-Level within Ad Group Reports](./get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.
- [Get Ad-Level Reports](./get-ad-level-reports.md)
  Fetches ad performance data within a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-search-term-level-reports)*