# Update an Ad Group

**Framework**: Apple Ads  
**Kind**: httpRequest

Updates an ad group with an ad group identifier.

**Availability**:
- Search Ads 5.0+

#### Discussion

To update ad groups, use the associated `campaignId` and `adgroupId` in the resource path.

In the request, specify [`TargetingDimensions`](targetingdimensions.md) and apply it to ad groups. If you’re not updating [`TargetingDimensions`](targetingdimensions.md), don’t include them in the payload. Use partial updates as necessary. For more information, see the Use Partial Updates section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

> **Note**:  You can’t create or update ad groups with geotargeting for campaigns with multiple countries or regions. Use [`UpdateCampaignRequest`](updatecampaignrequest.md) to clear your geotargeting parameters. Then apply [`TargetingDimensions`](targetingdimensions.md) in the request payload.

##### Payload Example Update an Ad Group with Targeting

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups

{
  "targetingDimensions": {
    "age": {
      "included": [
        {
          "minAge": 20,
          "maxAge": 25
        }
      ]
    },
    "gender": {
      "included": [
        "F",
        "M"
      ]
    },
    "country": {
      "included": [
        "US"
      ]
    },
    "adminArea": {
      "included": [
        "US|CA"
      ]
    },
    "locality": {
      "included": [
        "US|CA|Cupertino"
      ]
    },
    "deviceClass": {
      "included": [
        "IPAD",
        "IPHONE"
      ]
    },
    "daypart": {
      "userTime": {
        "included": [
          1,
          3,
          22
        ]
      }
    }
  }
}
```

**Response**:

```json
{
  "id": 542370539,
  "campaignId": 542370539,
  "name": "ad group with targeting",
  "cpaGoal": {
    "amount": "100",
    "currency": "USD"
  },
  "startTime": "2025-04-08T16:20:31.650",
  "endTime": "2025-04-09T19:33:31.650",
  "automatedKeywordsOptIn": false,
  "defaultBidAmount": {
    "amount": "100",
    "currency": "USD"
  },
  "pricingModel": "CPC",
  "targetingDimensions": {
    "age": {
      "included": [
        {
          "minAge": 20,
          "maxAge": 25
        }
      ]
    },
    "gender": {
      "included": [
        "M",
        "F"
      ]
    },
    "country": {
      "included": [
        "US"
      ]
    },
    "adminArea": {
      "included": [
        "US|CA"
      ]
    },
    "locality": {
      "included": [
        "US|CA|Cupertino"
      ]
    },
    "deviceClass": {
      "included": [
        "IPAD",
        "IPHONE"
      ]
    },
    "daypart": {
      "userTime": {
        "included": [
          1,
          3,
          22
        ]
      }
    },
    "appDownloaders": null
  },
  "orgId": 40669820,
  "modificationTime": "2025-04-08T17:15:56.956",
  "status": "ENABLED",
  "servingStatus": "NOT_RUNNING",
  "servingStateReasons": [
    "START_DATE_IN_THE_FUTURE"
  ],
  "displayStatus": "ON_HOLD",
  "deleted": `false`
}
```

##### Payload Example Update an Ad Group Without Targeting

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}

{
  "name": "ad group without targeting",
  "startTime": "2025-05-08T17:00:00.000"
}

```

**Response**:

```json
{
    "data": {
        "id": 585885654,
        "campaignId": 585885088,
        "name": "ad group without targeting",
        "cpaGoal": null,
        "startTime": “2025-05-08T17:00:00.000”,
        "endTime": null,
        "automatedKeywordsOptIn": false,
        "targetingDimensions": {
            "age": null,
            "gender": null,
            "country": null,
            "adminArea": null,
            "locality": null,
            "deviceClass": {
                "included": [
                    "IPHONE",
                    "IPAD"
                ]
            },
            "daypart": null,
            "appDownloaders": null
        },
        "orgId": 39879640,
        "creationTime": "2025-05-04T20:49:47.286",
        "pricingModel": "CPC",
        "modificationTime": "2025-05-04T20:49:47.286",
        "status": "ENABLED",
        "servingStatus": "NOT_RUNNING",
        "servingStateReasons": [
            "START_DATE_IN_THE_FUTURE"
        ],
        "displayStatus": "ON_HOLD",
        "deleted": false,
        "defaultBidAmount": {
            "amount": "1",
            "currency": "USD"
        }
    },
    "pagination": null,
    "error": null
}
```

##### Payload Example Update an Ad Group Cpa Goal

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}

{
  "campaignId": 585885088,
  "name": "update CPA goal",
  "cpaGoal": {
    "amount": "5.00",
    "currency": "USD"
  },
  "startTime": "2025-05-08T10:00:00.000",
  "endTime": "2025-05-09T10:00:00.000",
  "automatedKeywordsOptIn": false,
  "pricingModel": "CPC",
  "defaultBidAmount": {
    "amount": "1",
    "currency": "USD"
  },
  "orgId": 39879640,
  "status": "ENABLED"
}

```

**Response**:

```json
{
  "data": {
    "id": 585887393,
    "campaignId": 585886890,
    "name": "update CPA goal",
    "cpaGoal": {
      "amount": "5.00",
      "currency": "USD"
    },
    "startTime": "2025-05-08T10:00:00.000",
    "endTime": "2025-05-09T10:00:00.000",
    "automatedKeywordsOptIn": false,
    "targetingDimensions": {
      "age": null,
      "gender": null,
      "country": null,
      "adminArea": null,
      "locality": null,
      "deviceClass": {
        "included": [
          "IPHONE",
          "IPAD"
        ]
      },
      "daypart": null,
      "appDownloaders": null
    },
    "orgId": 39879640,
    "creationTime": "2025-05-04T23:33:33.211",
    "pricingModel": "CPC",
    "modificationTime": "2025-05-04T23:33:33.211",
    "status": "ENABLED",
    "servingStatus": "NOT_RUNNING",
    "servingStateReasons": [
      "START_DATE_IN_THE_FUTURE"
    ],
    "displayStatus": "ON_HOLD",
    "deleted": false,
    "defaultBidAmount": {
      "amount": "1",
      "currency": "USD"
    },
    "biddingStrategy": "MANUAL_CPT",
    "automatedKeywordsRequired": false
  },
  "pagination": null,
  "error": null
}

```

##### Payload Example Update an Ad Group Search March Setting

Only the name field can be updated in automated ad groups.

- `defaultBidAmount` cannot be changed to a non-zero/non-null value.
- `cpaGoal` cannot be set to a non-null value.
- `biddingStrategy` is read-only.
- `automatedKeywordsOptIn` can be toggled true/false.
- `automatedKeywordsRequired` is read-only.

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}

{
    "automatedKeywordsOptIn": false
}

```

**Response**:

```json
{
  "data": {
    "id": 585887393,
    "campaignId": 585886890,
    "name": "update search match",
    "cpaGoal": {
      "amount": "5.00",
      "currency": "USD"
    },
    "startTime": "2025-05-08T10:00:00.000",
    "endTime": "2025-05-09T10:00:00.000",
    "automatedKeywordsOptIn": false,
    "automatedKeywordsRequired": false,
    "orgId": 39879640,
    "creationTime": "2025-05-04T23:33:33.211",
    "pricingModel": "CPC",
    "modificationTime": "2026-05-04T23:33:33.211",
    "status": "ENABLED",
    "servingStatus": "NOT_RUNNING",
    "servingStateReasons": [
      "START_DATE_IN_THE_FUTURE"
    ],
    "displayStatus": "ON_HOLD",
    "deleted": false,
    "defaultBidAmount": {
      "amount": "0",
      "currency": "USD"
    },
    "biddingStrategy": "MAX_CONVERSIONS",
    "automatedKeywordsRequired": true
  },
  "pagination": null,
  "error": null
}

```

##### Payload Example Update an Ad Group Default Bid Amount

Only the name field can be updated in automated ad groups.

- `defaultBidAmount` cannot be changed to a non-zero/non-null value.
- `cpaGoal` cannot be set to a non-null value.
- `automatedKeywordsOptIn` can be toggled true/false.
- `biddingStrategy` is read-only.
- `automatedKeywordsRequired` is read-only.

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}

{
  "defaultBidAmount": {
    "amount": "5.00",
    "currency": "USD"
  }
}

```

**Response**:

```json
{
  "data": {
    "id": 585887393,
    "campaignId": 585886890,
    "name": "update Default Bid Amount",
    "cpaGoal": {
      "amount": "null",
      "currency": "USD"
    },
    "startTime": "2025-05-08T10:00:00.000",
    "endTime": "2025-05-09T10:00:00.000",
    "automatedKeywordsOptIn": false,
    "orgId": 39879640,
    "creationTime": "2026-05-04T23:33:33.211",
    "pricingModel": "CPC",
    "modificationTime": "2026-05-04T23:33:33.211",
    "status": "ENABLED",
    "servingStatus": "NOT_RUNNING",
    "servingStateReasons": [
      "START_DATE_IN_THE_FUTURE"
    ],
    "displayStatus": "ON_HOLD",
    "deleted": false,
    "defaultBidAmount": {
      "amount": "5.00",
      "currency": "USD"
    }
    "biddingStrategy": "MANUAL_CPT",
    "automatedKeywordsRequired": `false`
  },
  "pagination": null,
  "error": null
}

```

## Endpoint

`PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes the details of the ad group and campaign.

## See Also

- [Create an Ad Group](create-an-ad-group.md)
  Creates an ad group as part of a campaign.
- [Find Ad Groups](find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Find Ad Groups (org-level)](find-ad-groups-(org-level).md)
  Fetches ad groups within an organization.
- [Get an Ad Group](get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Delete an Ad Group](delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-an-ad-group)*