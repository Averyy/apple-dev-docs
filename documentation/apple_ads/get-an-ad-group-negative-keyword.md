# Get an Ad Group Negative Keyword

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches a specific negative keyword in an ad group.

**Availability**:
- Search Ads 5.0+

#### Discussion

To return a specific negative keyword, use the associated `campaignId`, `adgroupId`, and `keywordId` as a resource. You can also use a partial fetch. For more information, see the Use a Partial Fetch section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Get an Ad Group Negative Keyword

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/{keywordId}
```

**Response**:

```json
{
  "id": 542370642,
  "campaignId": 542370539,
  "adGroupId": 427916203,
  "text": "ad group negative keyword example 1",
  "status": "ACTIVE",
  "matchType": "EXACT",
  "modificationTime": "2024-04-08T17:49:30.399",
  "deleted": false
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords/{keywordId}`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.
- `keywordId` (int64) *(required)*: The unique identifier for the keyword.

## See Also

- [Create Ad Group Negative Keywords](create-ad-group-negative-keywords.md)
  Creates negative keywords in a specific ad group.
- [Find Ad Group Negative Keywords](find-ad-group-negative-keywords.md)
  Fetches negative keywords in a campaign’s ad groups.
- [Get All Ad Group Negative Keywords](get-all-ad-group-negative-keywords.md)
  Fetches all negative keywords in ad groups.
- [Update Ad Group Negative Keywords](update-ad-group-negative-keywords.md)
  Updates negative keywords in an ad group.
- [Delete Ad Group Negative Keywords](delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-an-ad-group-negative-keyword)*