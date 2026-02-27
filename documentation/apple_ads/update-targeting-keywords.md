# Update Targeting Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Updates targeting keywords in ad groups.

**Availability**:
- Search Ads 5.0+

#### Discussion

To update targeting keywords, use the associated `campaignId` and `adgroupId` in the URI. The `id` in the payload must belong to a keyword that exists inside the ad group in the URI. The `status` and `bidAmount` fields are modifiable in the payload. Use partial updates to edit a subset of object properties without having to include all object properties in the payload. For more information, see the Use Partial Updates section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Update Ad Group Targeting Keywords

When updating keywords in a campaign with a Maximize Conversions bidding strategy, `bidAmount` cannot be changed to a non-zero/non-null value.

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/bulk

[  
  {
    "id": "542370642",
    "status": "PAUSED",
    "bidAmount": {
      "amount”: "100",
      "currency": "USD"
    }
  },
  {
    "id": "542370643",
    "status": "PAUSED",
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
    "status": "PAUSED",
    "matchType": "BROAD",
    "bidAmount": {
      "amount": "100",
      "currency": "USD"
    },
    "modificationTime": "2025-04-08T21:02:24.257",
    "deleted": false
  },
  {
    "id": 542370643,
    "adGroupId": 427916203,
    "text": "targeting keyword example 2",
    "status": "PAUSED",
    "matchType": "EXACT",
    "modificationTime": "2025-04-08T21:02:24.267",
    "deleted": false
  }
]
```

## Endpoint

`PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/bulk`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes keyword targeting details.

## See Also

- [Create Targeting Keywords](create-targeting-keywords.md)
  Creates targeting keywords in ad groups.
- [Find Targeting Keywords in a Campaign](find-targeting-keywords-in-a-campaign.md)
  Fetches targeting keywords in a campaign’s ad groups.
- [Get a Targeting Keyword in an Ad Group](get-a-targeting-keyword-in-an-ad-group.md)
  Fetches a specific targeting keyword in an ad group.
- [Get All Targeting Keywords in an Ad Group](get-all-targeting-keywords-in-an-ad-group.md)
  Fetches all targeting keywords in ad groups.
- [Delete Targeting Keywords](delete-targeting-keywords.md)
  Deletes targeting keywords from ad groups.
- [Delete a Targeting Keyword](delete-a-targeting-keyword.md)
  Deletes a targeting keyword in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-targeting-keywords)*