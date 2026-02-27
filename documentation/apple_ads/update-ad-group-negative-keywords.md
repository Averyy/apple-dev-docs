# Update Ad Group Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Updates negative keywords in an ad group.

**Availability**:
- Search Ads 5.0+

#### Discussion

To update negative keywords, use the associated `campaignId` and `adgroupId` in the URI. The `id` in the payload must belong to a negative keyword that exists inside the ad group in the URI. Use `PAUSED` or `ACTIVE` values to update the `status` field. Use partial updates to edit a subset of object properties without having to include all object properties in the payload. For more information, see the Use Partial Updates section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Update Ad Group Negative Keywords

**Request**:

```None
PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/bulk

[
  {
    "id": "12345678",
    "status": "PAUSED"
  },
  {
    "id": "12345679",
    "status": "PAUSED"
  }
]

```

**Response**:

```json
[
  {
    "id": 12345678,
    "campaignId": 542370539,
    "adGroupId": 427916203,
    "text": "Update ad group negative keyword example 1",
    "status": "PAUSED",
    "matchType": "BROAD",
    "modificationTime": "2024-04-08T22:08:42.618",
    "deleted": false
  },
  {
    "id": 12345679,
    "campaignId": 542370539,
    "adGroupId": 427916203,
    "text": "Update ad group negative keyword example 2",
    "status": "PAUSED",
    "matchType": "EXACT",
    "modificationTime": "2024-04-08T22:08:42.618",
    "deleted": false
  }
]
```

## Endpoint

`PUT https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/bulk`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes negative keyword details.

## See Also

- [Create Ad Group Negative Keywords](create-ad-group-negative-keywords.md)
  Creates negative keywords in a specific ad group.
- [Find Ad Group Negative Keywords](find-ad-group-negative-keywords.md)
  Fetches negative keywords in a campaign’s ad groups.
- [Get an Ad Group Negative Keyword](get-an-ad-group-negative-keyword.md)
  Fetches a specific negative keyword in an ad group.
- [Get All Ad Group Negative Keywords](get-all-ad-group-negative-keywords.md)
  Fetches all negative keywords in ad groups.
- [Delete Ad Group Negative Keywords](delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/update-ad-group-negative-keywords)*