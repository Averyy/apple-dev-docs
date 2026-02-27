# Get All Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches all negative keywords in a campaign.

**Availability**:
- Search Ads 5.0+

#### Discussion

To return all campaign negative keywords, use the associated `campaignId` in the URI. You can also use a partial fetch. For more information, see the Use a Partial Fetch section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Get All Campaign Negative Keywords

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords
```

**Response**:

```json
[
        {
            "id": 542370642,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get campaign negative keyword example 1",
            "status": "ACTIVE",
            "matchType": "BROAD",
            "modificationTime": "2024-04-08T17:48:31.979",
            "deleted": false
        },
        {
            "id": 542370643,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get campaign negative keyword example 2",
            "status": "ACTIVE",
            "matchType": "EXACT",
            "modificationTime": "2024-04-08T17:48:31.984",
            "deleted": false
        },
        {
            "id": 542370644,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get campaign negative keyword example 3",
            "status": "ACTIVE",
            "matchType": "EXACT",
            "modificationTime": "2024-04-08T20:52:59.050",
            "deleted": false
        },
        {
            "id": 542370645,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get campaign negative keyword example 4",
            "status": "ACTIVE",
            "matchType": "BROAD",
            "modificationTime": "2024-04-08T20:52:59.054",
            "deleted": false
        }
    ]
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords`

## Parameters

- `limit` (int32): The number of items to return per request. The maximum is 1000 for most objects.
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.

## See Also

- [Create Campaign Negative Keywords](create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Find Campaign Negative Keywords](find-campaign-negative-keywords.md)
  Fetches negative keywords for campaigns.
- [Get a Campaign Negative Keyword](get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Update Campaign Negative Keywords](update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.
- [Delete Campaign Negative Keywords](delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-campaign-negative-keywords)*