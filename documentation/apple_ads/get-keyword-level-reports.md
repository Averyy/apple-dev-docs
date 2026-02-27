# Get Keyword-Level Reports

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches reports for targeting keywords within a campaign.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 3](apple-search-ads-campaign-management-api-3.md)

#### Discussion

Use this endpoint to fetch reports for targeting keywords in your campaigns. See [`ReportingKeyword`](reportingkeyword.md) for [`Condition`](condition.md) operators and field values to filter results with a [`Selector`](selector.md).

The `orderBy` [`Selector`](selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingKeyword`](reportingkeyword.md) fields are available to the `orderBy` [`Selector`](selector.md).

##### Payload Example Get Keyword Level Reports

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/keywords

{
  "returnRowTotals": true,
  "granularity": "DAILY",
  "timeZone": "UTC",
  "returnGrandTotals": true,
  "startTime": "2024-04-08",
  "selector": {
    "orderBy": [
      {
        "field": "localSpend",
        "sortOrder": "ASCENDING"
      }
    ],
    "conditions": [
      {
        "field": "deleted",
        "operator": "IN",
        "values": [
          "false",
          "true"
        ]
      }
    ],
    "pagination": {
      "offset": 0,
      "limit": 1000
    }
  },
  "endTime": "2025-04-09",
  "returnRecordsWithNoMetrics": true
}
```

**Response**:

```json
{
  "row": [
    {
      "other": false,
      "total": {
        "impressions": 76,
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
        "totalInstallRate": 2.962,
        "tapInstallCPI": {
          "amount": "0",
          "currency": "USD"
        },
       "tapInstallRate": 0.8571,
       "date": "2024-05-08"
      },
      "metadata": {
        "keywordId": 87675432,
        "keyword": "keyword 1",
        "keywordStatus": "ACTIVE",
        "matchType": "BROAD",
        "bidAmount": {
          "amount": "100",
          "currency": "USD"
        },
        "deleted": false,
        "keywordDisplayStatus": "RUNNING",
        "adGroupId": 542317095,
        "adGroupName": "Ad Group 1",
        "adGroupDeleted": false,
        "modificationTime": "2025-04-08T09:33:45.387"
      },
      "insights": {
        "bidRecommendation": {
          "bidMin": {
            "amount": "null",
            "currency": "null"
          },
          "bidMax": {
            "amount": "null",
            "currency": "null"
          },
          "suggestedBidAmount": {
            "amount": "2.40",
            "currency": "USD"
          }
        }
      }
    },
    {
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
          "amount": “0”,
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
        "totalInstallRate": 2.962,
        "tapInstallCPI": {
          "amount": "0",
          "currency": "USD"
        },
       "tapInstallRate": 0.7654,
       "date": "2024-05-08"
      },
       "metadata": {
        "keywordId": 87675432,
        "keyword": "keyword 1",
        "keywordStatus": "ACTIVE",
        "matchType": "BROAD",
        "bidAmount": {
          "amount": "100",
          "currency": "USD"
        },
        "deleted": false,
        "keywordDisplayStatus": "RUNNING",
        "adGroupId": 300452963,
        "adGroupName": "Ad Group 2",
        "adGroupDeleted": false,
        "modificationTime": "2024-04-10T09:33:50.668"
      },
      "insights": {
        "bidRecommendation": {
          "bidMin": null,
          "bidMax": null,
          "suggestedBidAmount": {
            "amount": "2.40",
            "currency": "USD"
          }
        }
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
        "totalInstallRate": 2.962,
        "tapInstallCPI": {
          "amount": "0",
          "currency": "USD"
        },
       "tapInstallRate": 0.7654,
       "date": "2024-05-10"
      },
     }
  }
}
```

##### Payload Example Get Keyword Level Reports

In Maximize Conversions campaigns, `bidAmount` is `0` for keywords.

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/keywords

{
  "startTime": "2025-08-01",
  "endTime": "2025-10-25",
  "selector": {
    "orderBy": [
      {
        "field": "bidAmount",
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
  "data": {
    "reportingDataResponse": {
      "row": [
        {
          "other": false,
          "metadata": {
            "campaignId": 886644762,
            "orgId": 19173940,
            "deleted": false,
            "modificationTime": "2025-10-13T16:58:21.582",
            "campaignName": "Keyword-level report with Maximize Campaigns",
            "campaignStatus": "ENABLED",
            "app": {
              "appName": "Uber - Driver: Drive & Deliver",
              "adamId": 1131342792
            },
            "servingStatus": "RUNNING",
            "servingStateReasons": null,
            "countriesOrRegions": [
              "US"
            ],
            "totalBudget": null,
            "dailyBudget": {
              "amount": "3232",
              "currency": "USD"
            },
            "displayStatus": "RUNNING",
            "supplySources": [
              "APPSTORE_SEARCH_RESULTS"
            ],
            "adChannelType": "SEARCH",
            "countryOrRegionServingStateReasons": {},
            "billingEvent": "TAPS",
            "biddingStrategy": "MAX_CONVERSIONS",
            "targetCpa": {
              "amount": "12",
              "currency": "USD"
            }
          },
          "total": {
            "localSpend": {
              "amount": "0",
              "currency": "MXN"
            },
            "tapInstalls": 0,
            "tapInstallCPI": {
              "amount": "0",
              "currency": "MXN"
            },
            "impressions": 0,
            "taps": 0,
            "ttr": 0,
            "avgCPT": {
              "amount": "0",
              "currency": "MXN"
            },
            "totalNewDownloads": 0,
            "totalRedownloads": 0,
            "viewInstalls": 0,
            "totalInstalls": 0,
            "tapNewDownloads": 0,
            "tapRedownloads": 0,
            "viewNewDownloads": 0,
            "viewRedownloads": 0,
            "tapPreOrdersPlaced": 0,
            "viewPreOrdersPlaced": 0,
            "totalPreOrdersPlaced": 0,
            "totalAvgCPI": {
              "amount": "0",
              "currency": "MXN"
            },
            "totalInstallRate": 0,
            "tapInstallRate": 0,
            "avgCPM": {
              "amount": "0",
              "currency": "MXN"
            }
          }
        },
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/keywords`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The report request body consisting of metrics and dimensions to use as filters.

## See Also

- [Get Campaign-Level Reports](get-campaign-level-reports.md)
  Fetches reports for campaigns.
- [Get Ad Group-Level Reports](get-ad-group-level-reports.md)
  Fetches reports for ad groups within a campaign.
- [Get Keyword-Level within Ad Group Reports](get-keyword-level-within-ad-group-reports.md)
  Fetches reports for targeting keywords within an ad group.
- [Get Search Term-Level Reports](get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Search Term-Level within Ad Group Reports](get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.
- [Get Ad-Level Reports](get-ad-level-reports.md)
  Fetches ad performance data within a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-keyword-level-reports)*