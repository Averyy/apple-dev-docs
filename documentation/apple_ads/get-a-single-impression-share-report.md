# Get a Single Impression Share Report

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches a single Impression Share report containing metrics and metadata.

**Availability**:
- Search Ads 5.0+

#### Discussion

##### Payload Example a Single Impression Share Report

**Request**:

```None
HTTP GET https://api.searchads.apple.com/api/v5/custom-reports/{reportId}
```

**Response**:

```json
{
  "data": {
    "id": 7615231,
    "name": "impression_share_API_report_example_2",
    "startTime": "2024-06-01",
    "endTime": "2024-06-30",
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
          "field": "adamId",
          "operator": "IN",
          "values": [
            "1252497129",
            "282614216"
          ]
        },
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
    "state": "COMPLETED",
    "creationTime": "2024-02-07T09:14:46.235",
    "modificationTime": "2024-02-07T09:14:53.173",
    "dateRange": "LAST_2_WEEKS"
  },
  "pagination": null,
  "error": null
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/custom-reports/{reportId}`

## Parameters

- `reportId` (int64) *(required)*: Use a `reportId` as a resource in the URI.

## See Also

- [Impression Share Report](impression-share-report.md)
  Obtain a report ID.
- [Get All Impression Share Reports](get-all-impression-share-reports.md)
  Fetches all Impression Share reports containing metrics and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-single-impression-share-report)*