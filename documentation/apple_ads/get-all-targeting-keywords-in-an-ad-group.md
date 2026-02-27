# Get All Targeting Keywords in an Ad Group

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches all targeting keywords in ad groups.

**Availability**:
- Search Ads 5.0+

#### Discussion

To return all targeting keywords for a campaign, use the associated `campaignId` and `adgroupId` as a resource. You can also use a partial fetch. For more information, see the Use a Partial Fetch section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Get All Targeting Keywords

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords
```

**Response**:

```json
[
        {
            "id": 542370642,
            "adGroupId": 542317095,
            "text": "targeting keyword example 1",
            "status": "ACTIVE",
            "matchType": "BROAD",
            "bidAmount": {
                "amount": "100",
                "currency": "USD"
            },
            "modificationTime": "2024-04-08T16:53:17.457",
            "deleted": false
        },
        {
            "id": 542370643,
            "adGroupId": 542317095,
            "text": "targeting keyword example 2",
            "status": "ACTIVE",
            "matchType": "BROAD",
            "bidAmount": {
                "amount": "100",
                "currency": "USD"
            },
            "modificationTime": "2024-04-08T20:48:28.206",
            "deleted": false
        },
        {
            "id": 542370644,
            "adGroupId": 542317095,
            "text": "targeting keyword example 3",
            "status": "PAUSED",
            "matchType": "BROAD",
            "bidAmount": {
                "amount": "2",
                "currency": "USD"
            },
            "modificationTime": "2023-04-08T21:02:24.257",
            "deleted": false
        },
        {
            "id": 542370645,
            "adGroupId": 542317095,
            "text": "targeting keyword example 4",
            "status": "ACTIVE",
            "matchType": "EXACT",
            "bidAmount": {
                "amount": "100",
                "currency": "USD"
            },
            "modificationTime": "2024-04-08T16:53:17.468",
            "deleted": false
        },
        {
            "id": 542370646,
            "adGroupId": 542317095,
            "text": "targeting keyword example 5",
            "status": "ACTIVE",
            "matchType": "EXACT",
            "bidAmount": {
                "amount": "100",
                "currency": "USD"
            },
            "modificationTime": "2023-04-08T17:53:10.899",
            "deleted": false
        },
        {
            "id": 542370647,
            "adGroupId": 542317095,
            "text": "targeting keyword example 6",
            "status": "PAUSED",
            "matchType": "EXACT",
            "bidAmount": {
                "amount": "100",
                "currency": "USD"
            },
            "modificationTime": "2024-04-08T21:02:24.267",
            "deleted": false
        }
    ]
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/targetingkeywords`

## Parameters

- `limit` (int32): The number of items to return per request. The maximum is 1000 for most objects.
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.

## See Also

- [Create Targeting Keywords](create-targeting-keywords.md)
  Creates targeting keywords in ad groups.
- [Find Targeting Keywords in a Campaign](find-targeting-keywords-in-a-campaign.md)
  Fetches targeting keywords in a campaign’s ad groups.
- [Get a Targeting Keyword in an Ad Group](get-a-targeting-keyword-in-an-ad-group.md)
  Fetches a specific targeting keyword in an ad group.
- [Update Targeting Keywords](update-targeting-keywords.md)
  Updates targeting keywords in ad groups.
- [Delete Targeting Keywords](delete-targeting-keywords.md)
  Deletes targeting keywords from ad groups.
- [Delete a Targeting Keyword](delete-a-targeting-keyword.md)
  Deletes a targeting keyword in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-targeting-keywords-in-an-ad-group)*