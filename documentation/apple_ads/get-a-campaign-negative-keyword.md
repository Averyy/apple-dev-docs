# Get a Campaign Negative Keyword

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches a specific negative keyword in a campaign.

**Availability**:
- Search Ads 5.0+

#### Discussion

To return a specific campaign negative keyword, use the associated `campaignId` and `keywordId` in the URI. You can also use a partial fetch. For more information, see the Use a Partial Fetch section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Get a Campaign Negative Keyword

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/{keywordId}
```

**Response**:

```json
{  
  "id": 542370642,
  "campaignId": 542370539,
  "adGroupId": 542317095,
  "text": "Get campaign negative keywords example",
  "status": "ACTIVE",
  "matchType": "BROAD",
  "modificationTime": "2024-04-08T17:48:31.979",
  "deleted": false
}

```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/{keywordId}`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.
- `keywordId` (int64) *(required)*: The unique identifier for the keyword.

## See Also

- [Create Campaign Negative Keywords](create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Find Campaign Negative Keywords](find-campaign-negative-keywords.md)
  Fetches negative keywords for campaigns.
- [Get All Campaign Negative Keywords](get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Update Campaign Negative Keywords](update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.
- [Delete Campaign Negative Keywords](delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-campaign-negative-keyword)*