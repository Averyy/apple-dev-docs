# Get Campaign-Level Reports

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches reports for campaigns.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 3](apple-search-ads-campaign-management-api-3.md)
- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to fetch reports for your campaigns. See [`ReportingCampaign`](reportingcampaign.md) and [`CampaignAppDetail`](campaignappdetail.md) for [`Condition`](condition.md) operators and field values to filter results with a [`Selector`](selector.md).

See the `groupBy` parameter description in the [`ReportingRequest`](reportingrequest.md) for supported values per targeting dimension.

The `orderBy` [`Selector`](selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingCampaign`](reportingcampaign.md) fields are available to the `orderBy` [`Selector`](selector.md) except `servingStateReasons`, `app`, `app:{appName}`, and `app:{adamId}`.

##### Payload Example 1 Get Campaign Level Reports for Campaigns with a Maximize Conversions Bid Strategy

In campaigns with a Maximize Conversions bid strategy, for filtering and ordering you can use `biddingStrategy` and `targetCpa` in a selector for conditions and ordering.

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns

{
  "startTime": "2025-08-01",
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
  "row": [
    {
      "granularity": [
        "..."
      ],
      "metadata": {
        "adChannelType": "SEARCH",
        "billingEvent": "TAPS",
        "biddingStrategy": "MAX_CONVERSIONS",
        "targetCpa": {
          "amount": "12",
          "currency": "USD"
        },
        "supplySources": [
          "APPSTORE_SEARCH_RESULTS"
        ],
        "campaignId": 542370539,
        "campaignName": "campaign name example",
        "deleted": false,
        "campaignStatus": "ENABLED",
        "app": {
          "appName": "Trip Trek example app name",
          "adamId": 427916203
        },
        "servingStatus": "RUNNING",
        "servingStateReasons": null,
        "countriesOrRegions": [
          "US"
        ],
        "modificationTime": "2025-01-08T15:51:14.500",
        "totalBudget": {
          "amount": "10000",
          "currency": "USD"
        },
        "dailyBudgetAmount": {
          "amount": "500",
          "currency": "USD"
        },
        "displayStatus": "RUNNING",
        "orgId": 40669820,
        "countryOrRegionServingStateReasons": {},
        "countryOrRegion": "US",
        "deviceClass": "iPhone"
      }
    }
  ]
}
```

##### Payload Example 2 Get Campaign Level Reports with Geo

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns

{
  "startTime": "2026-01-08",
  "endTime": "2026-01-09",
  "selector": {
    "orderBy": [
      {
        "field": "countryOrRegion",
        "sortOrder": "ASCENDING"
      }
    ],
    "conditions": [
      {
        "field": "countriesOrRegions",
        "operator": "CONTAINS_ANY",
        "values": [
          "US",
          "GB"
        ]
      },
      {
        "field": "countryOrRegion",
        "operator": "IN",
        "values": [
          "US"
        ]
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
          "impressions": 17,
          "taps": 6,
          "ttr": 0.2727,
          "avgCPT": {
            "amount": "0.1583",
            "currency": "USD"
          },
          "avgCPM": {
            "amount": "2500",
            "currency": "USD"
          },
          "localSpend": {
            "amount": "0.95",
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
            "amount": "0.19",
            "currency": "USD"
          },
          "tapInstallRate": 0.8333,
          "date": "2024-04-08"
        },
        {
          "impressions": 15,
          "taps": 7,
          "ttr": 0.4667,
          "avgCPT": {
            "amount": "0.1829",
            "currency": "USD"
          },
          "avgCPM": {
            "amount": "2500",
            "currency": "USD"
          },
          "localSpend": {
            "amount": "1.28",
            "currency": "USD"
          },
          "totalInstalls": 6,
          "totalNewDownloads": 3,
          "totalRedownloads": 7,
          "viewInstalls": 9,
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
            "amount": "0.2133",
            "currency": "USD"
          },
          "tapInstallRate": 0.8571,
          "date": "2026-01-08"
        }
      ],
      "metadata": {
        "adChannelType": "SEARCH",
        "billingEvent": "TAPS",
        "supplySources": [
          "APPSTORE_SEARCH_RESULTS"
        ],
        "campaignId": 542370539,
        "campaignName": "campaign name example",
        "deleted": false,
        "campaignStatus": "ENABLED",
        "app": {
          "appName": "Trip Trek example app name",
          "adamId": 427916203
        },
        "servingStatus": "RUNNING",
        "servingStateReasons": null,
        "countriesOrRegions": [
          "US"
        ],
        "modificationTime": "2026-01-08T15:51:14.500",
        "totalBudget": {
          "amount": "10000",
          "currency": "USD"
        },
        "dailyBudgetAmount": {
          "amount": "500",
          "currency": "USD"
        },
        "displayStatus": "RUNNING",
        "orgId": 40669820,
        "countryOrRegionServingStateReasons": {},
        "countryOrRegion": "US",
        "deviceClass": "iPhone"
      }
    }
  ]
}
```

##### Payload Example 3 Get Campaign Level Reports

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns

{
  "startTime": "2026-01-08",
  "endTime": "2026-01-09",
  "selector": {
    "orderBy": [
      {
        "field": "billingEvent",
        "sortOrder": "DESCENDING"
      }
    ],
    "conditions": [
      {
        "field": "billingEvent",
        "operator": "IN",
        "values": [
          "IMPRESSIONS",
          "TAPS"
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
            "impressions": 36,
            "taps": 14,
            "ttr": 4,
            "avgCPT": {
              "amount": "0.625",
              "currency": "USD"
            },
            "avgCPM": {
              "amount": "250",
              "currency": "USD"
            },
            "localSpend": {
              "amount": "900",
              "currency": "USD"
            },
             "totalInstalls": 10,
             "totalNewDownloads": 3,
             "totalRedownloads": 7,
             "viewInstalls": 18,
             "tapInstalls": 5,
             "tapNewDownloads": 10,
             "tapNewDownloads": 10,
             "tapRedownloads": 10,
             "viewNewDownloads": 10,
             "viewReDownloads": 10,
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
            "tapInstallRate": 0.75
          },
          "metadata": {
            "campaignId": 542370539,
            "campaignName": "campaign name example",
            "deleted": false,
            "campaignStatus": "ENABLED",
            "app": {
              "appName": "Trip Trek example app",
              "adamId": 427916203
            },
            "servingStatus": "RUNNING",
            "servingStateReasons": null,
            "countriesOrRegions": [
              "AU",
              "CA",
              "US"
            ],
            "modificationTime": "2026-01-08T09:55:36.265",
            "totalBudget": {
              "amount": "1000",
              "currency": "USD"
            },
            "dailyBudget": 100,
            "displayStatus": "RUNNING",
            "supplySources": [
              "APPSTORE_SEARCH_TAB"
            ],
            "adChannelType": "DISPLAY",
            "orgId": 40669820,
            "countryOrRegionServingStateReasons": {},
            "billingEvent": "IMPRESSIONS"
          }
          }
        ],
        "grandTotals": {
          "other": false,
          "total": {
            "impressions": 74,
            "taps": 29,
            "ttr": 4,
            "avgCPT": {
              "amount": "0.625",
              "currency": "USD"
            },
            "avgCPM": {
              "amount": "250",
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
             "tapNewDownloads": 3,
             "tapNewDownloads": 4,
             "tapRedownloads": 8,
             "viewNewDownloads": 12,
             "viewReDownloads": 10,
             "tapPreOrdersPlaced": 0,
             "viewPreOrdersPlaced": 0,
             "totalPreOrdersPlaced": 0,
             "totalAvgCPI": {
              "amount": "1.57",
              "currency": "USD"
           },
             "totalInstallRate": 0.843,
             "tapInstallCPI": {
              "amount": "0.4222",
              "currency": "USD"
            },       
           "tapInstallRate": 0.75
          },
          }
        }
    }
```

##### Payload Example 4 Get Campaign Level Reports with Granularity

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns

{  
  "startTime": "2026-01-08",
  "endTime": "2026-01-18",
  "selector": {
    "orderBy": [
      {
        "field": "countryOrRegion",
        "sortOrder": "ASCENDING"
      }
    ],
    "conditions": [
      {
        "field": "countriesOrRegions",
        "operator": "CONTAINS_ANY",
        "values": [
          "US",
          "GB"
        ]
      },
      {
        "field": "countryOrRegion",
        "operator": "IN",
        "values": [
          "US"
        ]
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
  "timeZone": "UTC",
  "returnRecordsWithNoMetrics": true,
  "returnRowTotals": false,
  "granularity": "DAILY",
  "returnGrandTotals": false
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
            "date": "2024-04-08"
          },
          {
            "date": "2026-01-09"
          },
          {
            "date": "2026-01-10"
          },
          {
            "date": "2026-01-11"
          },
          {
            "date": "2026-01-12"
          },
          {
            "date": "2026-01-13"
          },
          {
            "date": "2026-01-14"
          },
          {
            "date": "2026-01-15"
          },
          {
            "date": "2026-01-16"
          },
          {
            "date": "2026-01-17"
          },
          {
            "date": "2026-01-18"
          }
        ],
        "total": {
           "impressions": 36,
           "taps": 14,
           "ttr": 4,
           "avgCPT": {
             "amount": "0.625",
             "currency": "USD"
            },
            "avgCPM": {
             "amount": "250",
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
             "tapNewDownloads": 10,
             "tapNewDownloads": 10,
             "tapRedownloads": 10,
             "viewNewDownloads": 10,
             "viewReDownloads": 10,
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
           "tapInstallRate": 0.75
          },
        "metadata": {
          "billingEvent": "TAPS",
          "supplySources": [
            "APPSTORE_SEARCH_RESULTS"
          ],
          "campaignId": 542370539,
          "campaignName": "Get campaign report name example",
          "deleted": false,
          "campaignStatus": "ENABLED",
          "app": {
            "appName": "Trip Trek example app",
            "adamId": 427916203
          },
          "servingStatus": "RUNNING",
          "servingStateReasons": null,
          "countriesOrRegions": [
            "US"
          ],
          "modificationTime": "2024-04-08T08:46:08.848",
          "totalBudget": {
            "amount": "1000",
            "currency": "USD"
          },
          "dailyBudgetAmount": {
            "amount": "200",
            "currency": "USD"
          },
          "displayStatus": "RUNNING",
          "orgId": 541231618,
          "countryOrRegionServingStateReasons": {},
          "countryOrRegion": "US"
        }
      }
    ]
  }
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/reports/campaigns`

## Request Body

The report request body consisting of metrics and dimensions to use as filters.

## See Also

- [Get Ad Group-Level Reports](get-ad-group-level-reports.md)
  Fetches reports for ad groups within a campaign.
- [Get Keyword-Level Reports](get-keyword-level-reports.md)
  Fetches reports for targeting keywords within a campaign.
- [Get Keyword-Level within Ad Group Reports](get-keyword-level-within-ad-group-reports.md)
  Fetches reports for targeting keywords within an ad group.
- [Get Search Term-Level Reports](get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Search Term-Level within Ad Group Reports](get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.
- [Get Ad-Level Reports](get-ad-level-reports.md)
  Fetches ad performance data within a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-campaign-level-reports)*