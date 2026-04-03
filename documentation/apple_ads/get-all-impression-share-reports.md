# Get All Impression Share Reports

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches all Impression Share reports containing metrics and metadata.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to return all Impression Share reports containing metrics and metadata. Use query parameters as needed.

The rate limit for this endpoint is 150 reports within 15 minutes.

##### Payload Example All Impression Share Reports

**Request**:

```None
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

- `field` (string): The name of a field.
- `limit` (integer): The number of items to return per request. For most objects, the default is `20` and the maximum is `50`.
- `offset` (integer): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.
- `sortOrder` (string): The order of grouped results.

## See Also

- [Impression Share Report](impression-share-report.md)
  Obtain a report ID.
- [Get a Single Impression Share Report](get-a-single-impression-share-report.md)
  Fetches a single Impression Share report containing metrics and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-impression-share-reports)*