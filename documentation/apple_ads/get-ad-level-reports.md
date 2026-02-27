# Get Ad-Level Reports

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches ad performance data within a campaign.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to return performance data for `ads` within your campaigns. The `orderBy` [`Selector`](selector.md) is required in ad-level report requests. See [`ReportingAd`](reportingad.md) to identify fields you can use with `orderBy`. To filter results, use selector [`Condition`](condition.md) operators and field values that the `ReportingAd` object specifies. You can only perform `GroupBy` on the [`CountryOrRegion`](countryorregion.md) field. See [`ReportingRequest`](reportingrequest.md).

Historical ad-level metrics for the `APPSTORE_SEARCH_TAB` placement from before API version 5.2 release are reported against `adId=-1`. For `APPSTORE_SEARCH_TAB` ad-level metrics after API version 5.2 release, all default product page ads are reported against a new, real `adId` in reporting payloads.

You can map your campaign installations by `adId` through the [`AdServices`](https://developer.apple.com/documentation/AdServices) attribution framework.

##### Payload Example Get Ad Level Reports

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/ads

{
  "startTime": "2025-10-07",
  "endTime": "2025-10-09",
  "selector": {
  "orderBy": [
      {
        "field": "creativeType",
        "sortOrder": "ASCENDING"
      }
    ],
    "conditions": [
      {
        "field": "adId",
        "operator": "EQUALS",
        "values": [
          "573408745"
        ]
      }
    ],
    "pagination": {
      "offset": 0,
      "limit": 1000
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
          "viewReDownloads": 4,
          "tapPreOrdersPlaced": 1,
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
          "date": "2025-08-10"
        },
        "metadata": {
          "orgId": 39872140,
          "campaignId": 570798765,
          "adGroupId": 427916203,
          "adId": 573408745,
          "productPageId": 45812c9b-c296-43d3-c6a0-c5a02f74bf6e,
          "language": "English",
          "creativeId": 94895512,
          "adName": "Trip Trek custom product page variation 1",
          "creativeType": "CUSTOM_PRODUCT_PAGE",
          "status": "VALID",
          "displayStatus": "ACTIVE",
          "adServingStateReasons": null,
          "deleted": false,
          "creationTime": "2025-10-08T06:48:22.812Z",
          "modificationTime": "2025-08-09T06:48:22.812Z"
        }
      }
    ]
  }
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/reports/campaigns/{campaignId}/ads`

## Parameters

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
- [Get Keyword-Level within Ad Group Reports](get-keyword-level-within-ad-group-reports.md)
  Fetches reports for targeting keywords within an ad group.
- [Get Search Term-Level Reports](get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Search Term-Level within Ad Group Reports](get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-ad-level-reports)*