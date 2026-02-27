# Get Keyword-Level within Ad Group Reports

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches reports for targeting keywords within an ad group.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to fetch reports for a high volume of targeting keywords in your campaigns. See [`ReportingKeyword`](reportingkeyword.md) for [`Condition`](condition.md) operators and field values to filter results with a [`Selector`](selector.md). The `orderBy` [`Selector`](selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingKeyword`](reportingkeyword.md) fields are available to the `orderBy` [`Selector`](selector.md).

##### Payload Example Get Keyword Level Within Ad Group Reports

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/adgroups/{adgroupId}/keywords

{
  "startTime": "2024-04-08",
  "endTime": "2024-04-09",
  "timeZone": "UTC",
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
  "groupBy" null
}

```

**Response**:

```json
{
    "row": [
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
          "currency": “USD”
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
          "adGroupId": 542317095,
          "adGroupName": "Ad Group 1",
          "adGroupDeleted": false,
          "modificationTime": "2024-04-08T09:33:45.387"
        },
        "insights": {
          "bidRecommendation": {
            "bidMin": {
              "amount": "null",
              "currency": "null"
            },
            "bidMax": {
              "amount": "400",
              "currency": "USD"
           },
          "suggestedBidAmount": {
            "amount": "2.40",
            "currency": "USD"
             }
        }
      }
    }
  ]
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/adgroups/{adgroupId}/keywords`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The report request body consisting of metrics and dimensions to use as filters.

## See Also

- [Get Campaign-Level Reports](get-campaign-level-reports.md)
  Fetches reports for campaigns.
- [Get Ad Group-Level Reports](get-ad-group-level-reports.md)
  Fetches reports for ad groups within a campaign.
- [Get Keyword-Level Reports](get-keyword-level-reports.md)
  Fetches reports for targeting keywords within a campaign.
- [Get Search Term-Level Reports](get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Search Term-Level within Ad Group Reports](get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.
- [Get Ad-Level Reports](get-ad-level-reports.md)
  Fetches ad performance data within a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-keyword-level-within-ad-group-reports)*