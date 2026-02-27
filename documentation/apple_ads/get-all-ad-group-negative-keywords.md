# Get All Ad Group Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches all negative keywords in ad groups.

**Availability**:
- Search Ads 5.0+

#### Discussion

To return all ad group negative keywords, use the associated `campaignId` and `adgroupId` as a resource. You can also use a partial fetch. For more information, see the Use a Partial Fetch section of [`Using Apple Ads API Functionality`](using-apple-search-ads-api-functionality.md).

##### Payload Example Get All Ad Group Negative Keywords

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords
```

**Response**:

```json
[
        {
            "id": 542370642,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get ad group negative keyword example 1",
            "status": "ACTIVE",
            "matchType": "BROAD",
            "modificationTime": "2023-04-08T17:49:30.393",
            "deleted": false
        },
        {
            "id": 542370643,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get ad group negative keyword example 2",
            "status": "ACTIVE",
            "matchType": "EXACT",
            "modificationTime": "2023-04-08T17:49:30.399",
            "deleted": false
        },
        {
            "id": 542370644,
            "campaignId": 542370539,
            "adGroupId": 427916203,
            "text": "Get ad group negative keyword example 3",
            "status": "ACTIVE",
            "matchType": "EXACT",
            "modificationTime": "2024-04-08T22:02:07.523",
            "deleted": false
        }
    ]
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/{adgroupId}/negativekeywords`

## Parameters

- `limit` (int32): The number of items to return per request. The maximum is 1000 for most objects.
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.

## See Also

- [Create Ad Group Negative Keywords](create-ad-group-negative-keywords.md)
  Creates negative keywords in a specific ad group.
- [Find Ad Group Negative Keywords](find-ad-group-negative-keywords.md)
  Fetches negative keywords in a campaign’s ad groups.
- [Get an Ad Group Negative Keyword](get-an-ad-group-negative-keyword.md)
  Fetches a specific negative keyword in an ad group.
- [Update Ad Group Negative Keywords](update-ad-group-negative-keywords.md)
  Updates negative keywords in an ad group.
- [Delete Ad Group Negative Keywords](delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-ad-group-negative-keywords)*