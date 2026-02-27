# Update Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Updates negative keywords in a campaign.

**Availability**:
- Search Ads 5.0+

#### Discussion

To update campaign negative keywords, use the associated `campaignId` in the URI. The `id` in the payload must belong to a negative keyword that exists inside the campaign in the URI. Use `PAUSED` or `ACTIVE` values to update the `status` field. Use partial updates to edit a subset of object properties without having to include all object properties in the payload. For more information, see the Use Partial Updates section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Update Campaign Negative Keywords

Negative keywords can be created in both ad groups and automated ad groups.

**Request**:

```http
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/bulk

[
  {
    "id": 542370642,
    "adGroupId": 542317095,
    "text": "Update campaign negative keyword example 1",
    "status": "PAUSED",
    "matchType": "BROAD",
    "deleted": false
  },
  {
    "id": 542370643,
    "adGroupId": 542317095,
    "text": "Update campaign negative keyword example 2",
    "status": "PAUSED",
    "matchType": "EXACT",
    "deleted": false
  }
]
```

**Response**:

```json
[
  {
    "id": 542370642,
    "campaignId": 542370539,
    "adGroupId": 542317095,
    "text": "Update campaign negative keyword example 1",
    "status": "PAUSED",
    "matchType": "BROAD",
    "modificationTime": "2025-04-08T21:15:57.643",
    "deleted": false
  },
  {
    "id": 542370643,
    "campaignId": 542370539,
    "adGroupId": 542317095,
    "text": "Update campaign negative keyword example 2",
    "status": "PAUSED",
    "matchType": "EXACT",
    "modificationTime": "2025-04-08T21:13:57.874",
    "deleted": false
  }
]
```

## Endpoint

`PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/bulk`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes negative keyword details.

## See Also

- [Create Campaign Negative Keywords](create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Find Campaign Negative Keywords](find-campaign-negative-keywords.md)
  Fetches negative keywords for campaigns.
- [Get a Campaign Negative Keyword](get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Get All Campaign Negative Keywords](get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Delete Campaign Negative Keywords](delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-campaign-negative-keywords)*