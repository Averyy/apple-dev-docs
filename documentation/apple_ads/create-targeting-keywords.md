# Create Targeting Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Creates targeting keywords in ad groups.

**Availability**:
- Search Ads 5.0+

#### Overview

> **Note**:  If you create duplicate keywords, the payload response indicates an error, but the call returns with a 200 status code.

- 400: An invalid query or missing required parameters.
- 401: An unauthenticated call fails to get the requested response.
- 403: Insufficient rights to the resource.
- 404: The API can’t locate the resource.
- 429: The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [`Calling the Apple Ads API`](calling-the-apple-search-ads-api.md).
- 500: The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

#### Discussion

Keywords must belong to a specific ad group, unlike negative keywords, which can belong to a campaign or an ad group.

To create targeting keywords, use the associated `campaignId` and `adgroupId` in the URI.

> **Note**:  The limit is 5000 targeting keywords per campaign and per ad group.

##### Payload Example Create Ad Group Targeting Keywords

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/bulk

[  
  {
    "text": "targeting keyword example 1",
    "matchType": "BROAD",
    "bidAmount": {
      "amount": "100",
      "currency": "USD"
    }
  },
  {
    "text": "targeting keyword example 2",
    "matchType": "EXACT",
    "bidAmount": {
      "amount": "100",
      "currency": "USD"
    }
  }
]

```

**Response**:

```json
[
  {
    "id": 542370642,
    "adGroupId": 427916203,
    "text": "targeting keyword example 1",
    "status": "ACTIVE",
    "matchType": "BROAD",
    "bidAmount": {
      "amount": "1.5",
      "currency": "USD"
    },
    "modificationTime": "2023-04-08T16:53:17.457",
    "deleted”: false
  },
  {
    "id": 542370642,
    "adGroupId": 427916203,
    "text": “targeting keyword example 2”,
    "status": “ACTIVE",
    "matchType": "EXACT",
    "bidAmount": {
      "amount": "2",
      "currency": "USD"
    },
    "modificationTime": "2024-04-08T16:53:17.468",
    "deleted": false
  }
]
```

##### Payload Example Create Ad Group Targeting Keywords in a Maximize Conversions Campaign

- `bidAmount` must be omitted, `null`, or `0`.
- Keywords cannot be created in automated ad groups.

**Request**:

```http
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/bulk

[
  {
    "text": "travel",
    "matchType": "BROAD"
  },
  {
    "text": "flight",
    "matchType": "EXACT"
  }
]

```

**Response**:

```json
[
  {
    "id": 542370642,
    "adGroupId": 427916203,
    "text": "targeting keyword TripTrek 1",
    "status": "ACTIVE",
    "matchType": "BROAD",
    "bidAmount": {
      "amount": "0",
      "currency": "USD"
    },
    "modificationTime": "2025-04-08T16:53:17.457",
    "deleted”: false
  },
  {
    "id": 542370642,
    "adGroupId": 427916203,
    "text": “targeting keyword TripTrek 2”,
    "status": “ACTIVE",
    "matchType": "EXACT",
    "bidAmount": {
      "amount": "0",
      "currency": "USD"
    },
    "modificationTime": "2025-04-08T16:53:17.468",
    "deleted": false
  }
]
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/bulk`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes keyword targeting details.

## See Also

- [Find Targeting Keywords in a Campaign](find-targeting-keywords-in-a-campaign.md)
  Fetches targeting keywords in a campaign’s ad groups.
- [Get a Targeting Keyword in an Ad Group](get-a-targeting-keyword-in-an-ad-group.md)
  Fetches a specific targeting keyword in an ad group.
- [Get All Targeting Keywords in an Ad Group](get-all-targeting-keywords-in-an-ad-group.md)
  Fetches all targeting keywords in ad groups.
- [Update Targeting Keywords](update-targeting-keywords.md)
  Updates targeting keywords in ad groups.
- [Delete Targeting Keywords](delete-targeting-keywords.md)
  Deletes targeting keywords from ad groups.
- [Delete a Targeting Keyword](delete-a-targeting-keyword.md)
  Deletes a targeting keyword in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-targeting-keywords)*