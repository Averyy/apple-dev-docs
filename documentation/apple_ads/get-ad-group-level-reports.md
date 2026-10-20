# Get Ad Group-Level Reports

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches reports for ad groups within a campaign.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to fetch reports for your ad groups in campaigns. See [`ReportingAdGroup`](./reportingadgroup.md) for [`Condition`](./condition.md) operators and field values to filter results with an object [`Selector`](./selector.md). See the `groupBy` parameter description in the [`ReportingRequest`](./reportingrequest.md) for supported values per targeting dimension. The `orderBy` [`Selector`](./selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingAdGroup`](./reportingadgroup.md) fields are available to the `orderBy` [`Selector`](./selector.md) except `adGroupServingStateReasons`.

##### Payload example: Ad group-level reports using targeting criteria

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/adgroups

{
  "startTime": "2025-04-08",
  "endTime": "2025-04-09",
  "selector": {
    "orderBy": [
      {
        "field": "deviceClass",
        "sortOrder": "ASCENDING"
      }
    ],
    "conditions": [
      {
        "field": "deviceClass",
        "operator": "CONTAINS_ANY",
        "values": [
          "IPAD",
          "IPHONE"
        ]
      },
      {
        "field": "ageRange",
        "operator": "IN",
        "values": [
          "18-24",
          "25-34",
          "35-44",
          "45-54"
        ]
      }
    ],
    "pagination": {
      "offset": 0,
      "limit": 1000
    }
  },
  "groupBy": [
    "deviceClass",
    "ageRange"
  ],
  "timeZone": "UTC",
  "returnRecordsWithNoMetrics": true,
  "returnRowTotals": true,
  "returnGrandTotals": true
}
```

**Response**:

```json
{
  "row": [
    {
      "other": false,
      "granularity": [
        {
          "impressions": 210,
          "taps": 30,
          "ttr": 0.1429,
          "avgCPT": {
            "amount": "0.3783",
            "currency": "USD"
          },
          "avgCPM": {
            "amount": "0.2500",
            "currency": "USD"
          },
          "localSpend": {
            "amount": "11.35",
            "currency": "USD"
          },
          "totalInstalls": 10,
          "totalNewDownloads": 3,
          "totalRedownloads": 7,
          "viewInstalls": 18,
          "tapInstalls": 5,
          "tapNewDownloads": 2,
          "tapRedownloads": 3,
          "viewNewDownloads": 0,
          "viewReDownloads": 5,
          "tapPreOrdersPlaced": 0,
          "viewPreOrdersPlaced": 0,
          "totalPreOrdersPlaced": 0,
          "totalAvgCPI": {
            "amount": "1.57",
            "currency": "USD"
          },
          "totalInstallRate": 0.962,
          "tapInstallCPI": {
            "amount": "0.5974",
            "currency": "USD"
          },
          "date": "2024-04-08"
        },
        {
          "impressions": 198,
          "taps": 31,
          "ttr": 0.652,
          "avgCPT": {
            "amount": "0.83",
            "currency": "USD"
          },
          "avgCPM": {
            "amount": "0.2500",
            "currency": "USD"
          },
          "localSpend": {
            "amount": "11.35",
            "currency": "USD"
          },
          "totalInstalls": 13,
          "totalNewDownloads": 3,
          "totalRedownloads": 7,
          "viewInstalls": 18,
          "tapInstalls": 5,
          "tapNewDownloads": 2,
          "tapRedownloads": 3,
          "viewNewDownloads": 2,
          "viewReDownloads": 5,
          "tapPreOrdersPlaced": 0,
          "viewPreOrdersPlaced": 0,
          "totalPreOrdersPlaced": 0,
          "totalAvgCPI": {
            "amount": "1.76",
            "currency": "USD"
          },
          "totalInstallRate": 0.54,
          "tapInstallCPI": {
            "amount": "0.74",
            "currency": "USD"
          },
          "tapInstallRate": 0.76,
          "date": "2024-05-08"
        },
        {
          "impressions": 236,
          "taps": 29,
          "ttr": 0.1229,
          "avgCPT": {
            "amount": "0.4231",
            "currency": "USD"
          },
          "avgCPM": {
            "amount": "0.2500",
            "currency": "USD"
          },
          "localSpend": {
            "amount": "12.27",
            "currency": "USD"
          },
          "totalInstalls": 10,
          "totalNewDownloads": 3,
          "totalRedownloads": 7,
          "viewInstalls": 18,
          "tapInstalls": 5,
          "tapNewDownloads": 2,
          "tapRedownloads": 3,
          "viewNewDownloads": 0,
          "viewReDownloads": 5,
          "tapPreOrdersPlaced": 0,
          "viewPreOrdersPlaced": 0,
          "totalPreOrdersPlaced": 0,
          "totalInstallRate": 0.962,
          "tapInstallCPI": {
            "amount": "0.4908",
            "currency": "USD"
          },
          "tapInstallRate": 0.91,
          "date": "2024-04-08"
        }
      ],
      "metadata": {
        "adGroupId": 427916204,
        "adGroupName": "ad group example name",
        "startTime": "2024-04-08T00:00:00.000",
        "endTime": null,
        "cpaGoal": null,
        "pricingModel": "CPC",
        "defaultBidAmount": {
          "amount": "100",
          "currency": "USD"
        },
        "deleted": false,
        "adGroupStatus": "ENABLED",
        "adGroupServingStatus": "RUNNING",
        "adGroupServingStateReasons": null,
        "modificationTime": "2024-04-08T10:35:50.194",
        "automatedKeywordsOptIn": false,
        "automatedKeywordsRequired": false,
        "adGroupDisplayStatus": "RUNNING",
        "campaignId": 542370539,
        "orgId": 40669820,
        "countryOrRegion": "US",
        "deviceClass": "iPhone"
      }
    }
  ]
}
```

##### Payload example: Ad group-level reports with manual ad groups

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/adgroups

{
  "startTime": "2025-04-08",
  "endTime": "2025-04-09",
  "selector": {
    "orderBy": [
      {
        "field": "defaultBidAmount",
        "sortOrder": "DESCENDING"
      }
    ],
    "conditions": [
      {
        "field": "defaultBidAmount",
        "operator": "BETWEEN",
        "values": [
          "99",
          "101"
        ]
      }
    ],
    "pagination": {
      "offset": 0,
      "limit": 34
    }
  },
  "timeZone": "UTC",
  "returnRecordsWithNoMetrics": false,
  "returnRowTotals": true,
  "returnGrandTotals": true
}
```

**Response**:

```json
{
      "row": [
        {
          "other": false,
          "total": {
            "impressions": 1200,
            "taps": 800,
            "ttr": 4,
            "avgCPT": {
              "amount": "0.625",
              "currency": "USD"
            },
            "avgCPM": {
              "amount": "2500",
              "currency": "USD"
            },
            "localSpend": {
              "amount": "3000",
              "currency": "USD"
            },
            "totalInstalls": 10,
            "totalNewDownloads": 3,
            "totalRedownloads": 7,
            "viewInstalls": 18,
            "tapInstalls": 5,
            "tapNewDownloads": 2,
            "tapRedownloads": 3,
            "viewNewDownloads": 0,
            "viewReDownloads": 5,
            "tapPreOrdersPlaced": 0,
            "viewPreOrdersPlaced": 0,
            "totalPreOrdersPlaced": 0,
            "totalAvgCPI": {
              "amount": "1.57",
              "currency": "USD"
           },
            "totalInstallRate": 0.962,
            "tapInstallCPI": {
              "amount": "0.8333",
              "currency": "USD"
            },
            "tapInstallRate": 0.91,
            "date": "2024-05-08"
          },
          "metadata": {
            "adGroupId": 427916203,
            "adGroupName": "ad group 2",
            "startTime": "2025-03-15T09:54:59.117",
            "endTime": "2025-09-11T09:54:59.117",
            "cpaGoal": null,
            "deleted": false,
            "adGroupStatus": "ENABLED",
            "adGroupServingStatus": "RUNNING",
            "adGroupServingStateReasons": null,
            "modificationTime": "2024-04-09T09:55:06.098",
            "automatedKeywordsOptIn": false,
            "automatedKeywordsRequired": false,
            "adGroupDisplayStatus": "RUNNING",
            "campaignId": 542370539,
            "orgId": 40669820,
            "pricingModel": "CPM",
            "defaultBidAmount": {
              "amount": "100",
              "currency": "USD"
            }
          }
        }
      ],
      "grandTotals": {
        "other": false,
        "total": {
            "impressions": 1020,
            "taps": 800,
            "ttr": 4,
            "avgCPT": {
              "amount": "0.625",
              "currency": "USD"
            },
            "avgCPM": {
              "amount": "2500",
              "currency": "USD"
            },
            "localSpend": {
              "amount": "300",
              "currency": "USD"
            },
            "totalInstalls": 10,
            "totalNewDownloads": 3,
            "totalRedownloads": 7,
            "viewInstalls": 18,
            "tapInstalls": 5,
            "tapNewDownloads": 2,
            "tapRedownloads": 3,
            "viewNewDownloads": 0,
            "viewReDownloads": 5,
            "tapPreOrdersPlaced": 0,
            "viewPreOrdersPlaced": 0,
            "totalPreOrdersPlaced": 0,
            "totalAvgCPI": {
              "amount": "1.57",
              "currency": "USD"
           },
            "totalInstallRate": 0.962,
            "tapInstallCPI": {
              "amount": "0.8333",
              "currency": "USD"
            },
            "tapInstallRate": 0.76,
            "date": "2024-05-09"
          }
      }
  }
```

##### Payload example: Ad group-level reports with a Maximize Campaigns bid strategy

In Maximize Conversions bidding strategy in campaigns, you can use `biddingStrategy` and `automatedKeywordsRequired` in a selector for conditions and ordering. The `defaultBidAmount` is `0` and `cpaGoal` is `null`.

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/adgroups

{
  "startTime": "2025-10-23",
  "endTime": "2025-10-25",
  "selector": {
    "orderBy": [
      {
        "field": "biddingStrategy",
        "sortOrder": "DESCENDING"
      }
    ]
  },
  "timeZone": "UTC",
  "returnRecordsWithNoMetrics": true,
  "returnRowTotals": true,
  "returnGrandTotals": true
}
```

**Response**:

```json
{
  "reportingDataResponse": {
    "row": [
      {
        "metadata": {
          "campaignId": 886644762,
          "orgId": 19173940,
          "deleted": false,
          "modificationTime": "2025-10-13T16:58:21.582",
          "campaignName": "Ad Groups in Maximize Campaigns",
          "campaignStatus": "ENABLED",
          "app": {
            "appName": "TripTrek - explore the world",
            "adamId": 1131342792
          },
          "servingStatus": "RUNNING",
          "servingStateReasons": null,
          "countriesOrRegions": [
            "US"
          ],
          "totalBudget": null,
          "dailyBudget": {
            "amount": "300",
            "currency": "USD"
          },
          "displayStatus": "RUNNING",
          "supplySources": [
            "APPSTORE_SEARCH_RESULTS"
          ],
          "adChannelType": "DISPLAY",
          "countryOrRegionServingStateReasons": {},
          "billingEvent": "TAPS",
          "automatedKeywordsRequired": "true",
          "cpaGoal": null,
          "defaultBidAmount": {
            "amount": "0",
            "currency": "USD"
          },
          "biddingStrategy": "MAX_CONVERSIONS",
          "targetCpa": {
            "amount": "12",
            "currency": "USD"
          }
        },
        "total": {
          "...": "..."
        }
      }
    ]
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/adgroups`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `ReportingRequest`

The report request body consisting of metrics and dimensions to use as filters.

## Responses

- `200` OK (`ReportingResponseBody`, `application/json`): If the call succeeds, the API returns the [`ReportingResponse`](./reportingresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
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
- [Get Keyword-Level Reports](./get-keyword-level-reports.md)
  Fetches reports for targeting keywords within a campaign.
- [Get Keyword-Level within Ad Group Reports](./get-keyword-level-within-ad-group-reports.md)
  Fetches reports for targeting keywords within an ad group.
- [Get Search Term-Level Reports](./get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Search Term-Level within Ad Group Reports](./get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.
- [Get Ad-Level Reports](./get-ad-level-reports.md)
  Fetches ad performance data within a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-ad-group-level-reports)*