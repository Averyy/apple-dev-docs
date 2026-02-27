# Delete Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Deletes negative keywords from a campaign.

**Availability**:
- Search Ads 5.0+

#### Discussion

To delete campaign negative keywords, use the associated `campaignId` in the URI. Include each `keywordId` in the payload.

##### Payload Example Delete Campaign Negative Keywords

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/delete/bulk

[
    578054687,
    578054686,
    578054685
]

```

**Response**:

```json
{
    "data": 3,
    "pagination": null,
    "error": null
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/delete/bulk`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body.

## See Also

- [Create Campaign Negative Keywords](create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Find Campaign Negative Keywords](find-campaign-negative-keywords.md)
  Fetches negative keywords for campaigns.
- [Get a Campaign Negative Keyword](get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Get All Campaign Negative Keywords](get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Update Campaign Negative Keywords](update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/delete-campaign-negative-keywords)*