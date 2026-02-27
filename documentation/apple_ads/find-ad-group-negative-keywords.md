# Find Ad Group Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches negative keywords in a campaign’s ad groups.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find negative keywords in different ad groups within the same campaign. Use the associated `campaignId` in the URI. Find calls use [`Selector`](selector.md) [`Condition`](condition.md) operators to narrow results. If you don’t specify any selector conditions, the API returns all negative keywords across all ad groups of the campaign. See the [`NegativeKeyword`](negativekeyword.md) object for details about [`Selector`](selector.md) `condition` operators per field.

##### Payload Example Find Ad Group Negative Neywords

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/negativekeywords/find

{
  "pagination": {
    "offset": 0,
    "limit": 100
  },
  "orderBy": [
    {
      "field": "id",
      "sortOrder": "ASCENDING"
    }
  ],
  "conditions": [
    {
      "field": "deleted",
      "operator": "EQUALS",
      "values": [
        "false"
      ]
    }
  ]
}
```

**Response**:

```json
{
  "data": [
    {
      "id": 542370642,
      "campaignId": 542370539,
      "adGroupId": 427916203,
      "text": "ad group negative keyword example 1",
      "status": "ACTIVE",
      "matchType": "BROAD",
      "modificationTime": "2024-04-08T17:49:30.393",
      "deleted": false
    },
    {
      "id": 542370643,
      "campaignId": 542370539,
      "adGroupId": 427916203,
      "text": "ad group negative keyword example 2",
      "status": "ACTIVE",
      "matchType": "EXACT",
      "modificationTime": "2024-04-08T17:49:30.399",
      "deleted": false
    },
    {
      "id": 542370644,
      "campaignId": 542370539,
      "adGroupId": 427916203,
      "text": "ad group negative keyword example 3",
      "status”: "ACTIVE",
      "matchType": "BROAD",
      "modificationTime": "2024-04-08T01:55:00.017",
      "deleted": false
    },
    {
      "id": 542370645,
      "campaignId": 542370539,
      "adGroupId": 427916203,
      "text": "ad group negative keyword example 4",
      "status": "ACTIVE",
      "matchType": "EXACT",
      "modificationTime": "2024-04-08T01:55:00.025",
      "deleted": false
    },
    {
      "id": 542370646,
      "campaignId": 542370539,
      "adGroupId": 427916203,
      "text": "ad group negative keyword example 5",
      "status": "ACTIVE",
      "matchType": "BROAD",
      "modificationTime": "2024-04-08T20:34:19.129",
      "deleted": false
    },
    {
      "id": 542370647,
      "campaignId": 542370539,
      "adGroupId": 427916203,
      "text": "ad group negative keyword example 6",
      "status": "ACTIVE",
      "matchType": "EXACT",
      "modificationTime": "2024-04-08T20:34:19.131",
      "deleted": false
    }
  ],
  "pagination": {
    "totalResults": 6,
    "startIndex": 1,
    "itemsPerPage": 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/negativekeywords/find`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

[`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create Ad Group Negative Keywords](create-ad-group-negative-keywords.md)
  Creates negative keywords in a specific ad group.
- [Get an Ad Group Negative Keyword](get-an-ad-group-negative-keyword.md)
  Fetches a specific negative keyword in an ad group.
- [Get All Ad Group Negative Keywords](get-all-ad-group-negative-keywords.md)
  Fetches all negative keywords in ad groups.
- [Update Ad Group Negative Keywords](update-ad-group-negative-keywords.md)
  Updates negative keywords in an ad group.
- [Delete Ad Group Negative Keywords](delete-ad-group-negative-keywords.md)
  Deletes negative keywords from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-ad-group-negative-keywords)*