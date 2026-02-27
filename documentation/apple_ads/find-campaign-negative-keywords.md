# Find Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches negative keywords for campaigns.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find campaign negative keywords. Use the associated `campaignId` in the URI. Find calls use [`Selector`](selector.md) [`Condition`](condition.md) operators to narrow results. If you don’t specify any selector conditions, all negative keywords in the campaign return in the response. See the [`NegativeKeyword`](negativekeyword.md) object for details about selector [`Condition`](condition.md) operators per field.

##### Payload Example Find Campaign Negative Keywords

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/find

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
      "adGroupId": 542317095,
      "text": "Find campaign negative keywords example 1",
      "status": "ACTIVE",
      "matchType": "BROAD",
      "modificationTime": "2023-04-08T17:48:31.979",
      "deleted": false
    },
    {
      "id": 542370643,
      "campaignId": 542370539,
      "adGroupId": 542317095,
      "text": "Find campaign negative keywords example 2",
      "status": "ACTIVE",
      "matchType": "EXACT",
      "modificationTime": "2023-04-08T17:48:31.984",
      "deleted": false
    },
    {
      "id": 542370644,
      "campaignId": 542370539,
      "adGroupId": 542317095,
      "text": "Find campaign negative keywords example 3",
      "status": "ACTIVE",
      "matchType": "EXACT",
      "modificationTime": "2023-04-08T20:52:59.050",
      "deleted": false
    },
    {
      "id": 542370645,
      "campaignId": 542370539,
      "adGroupId": 542317095,
      "text": "Find campaign negative keywords example 4",
      "status": "ACTIVE",
      "matchType": "BROAD",
      "modificationTime": "2023-04-08T20:52:59.054",
      "deleted": false
    }
  ],
  "pagination": {
    "totalResults": 4,
    "startIndex": 1,
    "itemsPerPage": 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/negativekeywords/find`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create Campaign Negative Keywords](create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Get a Campaign Negative Keyword](get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Get All Campaign Negative Keywords](get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Update Campaign Negative Keywords](update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.
- [Delete Campaign Negative Keywords](delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-campaign-negative-keywords)*