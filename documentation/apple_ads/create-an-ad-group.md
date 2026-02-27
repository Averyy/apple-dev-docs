# Create an Ad Group

**Framework**: Apple Ads  
**Kind**: httpRequest

Creates an ad group as part of a campaign.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

To create ad groups, use the associated `campaignId` as a resource in the URI. In the request, specify [`TargetingDimensions`](targetingdimensions.md) and apply it to ad groups.

> **Note**:  You can’t create or update ad groups with geotargeting for campaigns with multiple `countriesOrRegions`.

##### Payload Example Create an Ad Group with Targeting

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups

{
  "campaignId": 56543219,
  "name": "TripTrek ad group",
  "cpaGoal": {
    "amount": "1",
    "currency": "USD"
  },
  "startTime": "2024-05-18T00:00:00.000",
  "endTime": "2024-05-22T00:00:00.000",
  "automatedKeywordsOptIn": true,
  "pricingModel": "CPC",
  "defaultBidAmount": {
    "amount": "1",
    "currency": "USD"
  },
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
    "deviceClass": {
      "included": [
        "IPAD",
        "IPHONE"
        ]
    }
  },
  "orgId": 39879640,
  "status": "ENABLED"
}
```

**Response**:

```json
{
  "id": 542370642,
  "campaignId": 56543219,
  "name": "TripTrek ad group",
  "cpaGoal": {
    "amount": "1",
    "currency": "USD"
  },
  "startTime": "2024-05-18T00:00:00.000",
  "endTime": "2024-05-22T00:00:00.000",
  "automatedKeywordsOptIn": true,
  "pricingModel": "CPC",
  "defaultBidAmount": {
    "amount": "1",
    "currency": "USD"
  },
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
    "country": null,
    "adminArea": null,
    "locality": null,
    "deviceClass": {
      "included": [
        "IPAD",
        "IPHONE"
        ]
    },
    "appDownloaders": null
  },
  "orgId": 40669820,
  "modificationTime": "2024-05-22T17:30:56.435",
  "status": "ENABLED",
  "servingStatus": "NOT_RUNNING",
  "servingStateReasons": [
    "START_DATE_IN_THE_FUTURE"
  ],
  "displayStatus": "ON_HOLD",
  "deleted": false
}
```

##### Payload Example Create an Ad Group Without Targeting

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups

{
  "name": "TripTrek ad group",
  "startTime": "2024-05-18T00:00:00.000",
  "endTime": "2024-05-22T00:00:00.000",
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
    "id": 586648342,
    "campaignId": 586640439,
    "name": "TripTrek ad group",
    "cpaGoal": null,
    "startTime": "2024-05-18T00:00:00.000",
    "endTime": "2024-05-22T00:00:00.000",
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
    "creationTime": "2024-05-11T20:22:04.405",
    "pricingModel": "CPC",
    "modificationTime": "2024-05-11T20:22:04.405",
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

##### Payload Example Create an Automated Ad Group in a Campaign with a Maximize Conversions Bid Strategy

A Maximize Conversions campaign will return an error of `AUTOMATED_KEYWORDS_REQUIRED_AD_GROUP_MISSING` and not run until an automated ad group is created.

In automated ad groups:

- Search Match can’t be turned off.
- Audience settings and keywords can’t be edited but optional ad groups can be added to the campaign and include audience settings and keywords.
- Negative keywords can be added.

A Maximize Conversions bid strategy requires the use of Search Match and an automatically created ad group. See [`AdGroup`](adgroup.md) for more details on fields and see [`Ad Groups`](ad-groups.md) for details on Search Match. See payload example in [`Create a Campaign`](create-a-campaign.md) to create a Maximize Conversions campaign.

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups

{
"name": "Automatic Ad Group",
"automatedKeywordsOptIn": true,
"pricingModel": "CPC",
"automatedKeywordsRequired": true,
"status": "ENABLED"
}
```

**Response**:

```json
{
    "data": {
        "id": 886958599,
        "campaignId": 886876955,
        "name": "Automatic Ad Group example3",
        "cpaGoal": null,
        "startTime": "2026-02-05T20:15:50.857",
        "endTime": null,
        "automatedKeywordsOptIn": true,
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
            "appDownloaders": null,
            "appCategories": null
        },
        "orgId": 19173940,
        "creationTime": "2026-02-05T20:15:50.836",
        "pricingModel": "CPC",
        "modificationTime": "2026-02-05T20:15:50.871",
        "status": "ENABLED",
        "servingStatus": "RUNNING",
        "servingStateReasons": null,
        "displayStatus": "RUNNING",
        "deleted": false,
        "defaultBidAmount": {
            "amount": "0",
            "currency": "MXN"
        },
        "biddingStrategy": "MAX_CONVERSIONS",
        "automatedKeywordsRequired": true
    },
    "pagination": null,
    "error": null
}
```

##### Payload Example Create an Ad Group with a Campaign with a Maximize Conversions Bid Strategy

In maximize conversions campaigns:

- Bid values automatically managed and returned as `0`.
- Custom ads can be created in standard ad groups in both Maximize Conversions and manual campaigns.

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups

{
  "name": "Ad Group",
  "pricingModel": "CPC",
  "status": "ENABLED",
  "startTime": "2025-12-03T15:16:03.728"
}

```

**Response**:

```json
{
    "data": {
        "id": 886958599,
        "campaignId": 886876955,
        "name": "Ad Group example3",
        "cpaGoal": null,
        "startTime": "2026-02-05T20:15:50.857",
        "endTime": null,
        "automatedKeywordsOptIn": true,
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
            "appDownloaders": null,
            "appCategories": null
        },
        "orgId": 19173940,
        "creationTime": "2026-02-05T20:15:50.836",
        "pricingModel": "CPC",
        "modificationTime": "2026-02-05T20:15:50.871",
        "status": "ENABLED",
        "servingStatus": "RUNNING",
        "servingStateReasons": null,
        "displayStatus": "RUNNING",
        "deleted": false,
        "defaultBidAmount": {
            "amount": "0",
            "currency": "MXN"
        },
        "biddingStrategy": "MAX_CONVERSIONS",
        "automatedKeywordsRequired": true
    },
    "pagination": null,
    "error": null
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes the details of the ad group and campaign.

## See Also

- [Find Ad Groups](find-ad-groups.md)
  Fetches ad groups within a campaign.
- [Find Ad Groups (org-level)](find-ad-groups-(org-level).md)
  Fetches ad groups within an organization.
- [Get an Ad Group](get-an-ad-group.md)
  Fetches a specific ad group with a campaign and ad group identifier.
- [Get all Ad Groups](get-all-ad-groups.md)
  Fetches all ad groups with a campaign identifier.
- [Update an Ad Group](update-an-ad-group.md)
  Updates an ad group with an ad group identifier.
- [Delete an Ad Group](delete-an-ad-group.md)
  Deletes an ad group with a campaign and ad group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-an-ad-group)*