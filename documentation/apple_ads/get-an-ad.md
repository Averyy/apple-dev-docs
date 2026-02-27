# Get an Ad

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches an ad assigned to an ad group by identifier.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to fetch an [`Ad`](ad.md) assigned to an ad group. Use your `adId` in the resource path.

##### Payload Example Get an Ad

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/ads/{adId}
```

**Response**:

```json
{
    "id": 573408745,
    "orgId": 39872140,
    "campaignId": 570798765,
    "adGroupId": 570798765,
    "creativeId": 94895512,
    "name": "Trip Trek custom product page variation",
    "creativeType": "CUSTOM_PRODUCT_PAGE",
    "status": "PAUSED",
    "servingStatus": "NOT_RUNNING",
    "servingStateReasons": [
      "PAUSED_BY_USER"
      ],
    "deleted": false,
    "creationTime": "2024-10-08T00:18:37.606Z",
    "modificationTime": "2024-10-09T00:18:37.606Z"
}

```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/ads/{adId}`

## Parameters

- `adId` (int64) *(required)*: A unique identifier representing the assignment relationship between an ad group and an [`Ad`](ad.md).
- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## See Also

- [Create an Ad](create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads](find-ads.md)
  Finds ads within a campaign by selector criteria.
- [Find Ads (org-level)](find-ads-(org-level).md)
  Fetches ads within an organization by selector criteria.
- [Get All Ads](get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Update an Ad](update-an-ad.md)
  Updates an ad in an ad group.
- [Delete an Ad](delete-an-ad.md)
  Deletes an ad from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-an-ad)*