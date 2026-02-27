# Delete a Targeting Keyword

**Framework**: Apple Ads  
**Kind**: httpRequest

Deletes a targeting keyword in an ad group.

**Availability**:
- Search Ads 5.0+

#### Discussion

To delete targeting keywords, include the associated `campaignId` and `adgroupId` in the URI with the `keywordId`. This is a soft deletion.

##### Payload Example Delete a Targeting Keyword

**Request**:

```None
DELETE https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/{keywordId}
```

**Response**:

```json
{
    "data": 1,
    "pagination": null,
    "error": null
}

```

## Endpoint

`DELETE https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords/{keywordId}`

## Parameters

- `adgroupId` (int64) *(required)*: The unique identifier for the ad group.
- `campaignId` (int64) *(required)*: The unique identifier for the campaign.
- `keywordId` (int64) *(required)*: The unique identifier for the keyword.

## See Also

- [Create Targeting Keywords](create-targeting-keywords.md)
  Creates targeting keywords in ad groups.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/delete-a-targeting-keyword)*