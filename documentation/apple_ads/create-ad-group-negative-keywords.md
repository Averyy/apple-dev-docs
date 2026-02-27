# Create Ad Group Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Creates negative keywords in a specific ad group.

**Availability**:
- Search Ads 5.0+

#### Discussion

Negative keywords prevent your ad from showing up in App Store searches. Negative keywords can belong to a campaign or an ad group.

To create ad group negative keywords, use the associated `campaignId` and `adgroupId` in the URI.

##### Payload Example Create Ad Group Negative Keywords

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/bulk

[  
 {
    "text": "ad group negative keyword 1",
    "matchType": "BROAD"
  },
  {
    "text": "ad group negative keyword 2",
    "matchType": "EXACT"
  }
]

```

**Response**:

```json
[
  {
    "id": 542370642,
    "campaignId": 542370539,
    "adGroupId": 427916203,
    "text": "ad group negative keyword example 1",
    "status": "ACTIVE",
    "matchType": "BROAD",
    "modificationTime": "2024-04-08T22:02:07.514",
    "deleted": false
  },
  {
    "id": 542370643,
    "campaignId": 542370539,
    "adGroupId": 427916203,
    "text": "Update campaign negative keyword example 2",
    "status": "ACTIVE",
    "matchType": "EXACT",
    "modificationTime": "2024-04-08T22:02:07.523",
    "deleted": false
  }
]
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/bulk`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes negative keyword details.

## See Also

- [Find Ad Group Negative Keywords](find-ad-group-negative-keywords.md)
  Fetches negative keywords in a campaign’s ad groups.
- [Get an Ad Group Negative Keyword](get-an-ad-group-negative-keyword.md)
  Fetches a specific negative keyword in an ad group.
- [Get All Ad Group Negative Keywords](get-all-ad-group-negative-keywords.md)
  Fetches all negative keywords in ad groups.
- [Update Ad Group Negative Keywords](update-ad-group-negative-keywords.md)
  Updates negative keywords in an ad group.
- [Delete Ad Group Negative Keywords](delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-ad-group-negative-keywords)*