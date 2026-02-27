# Find Ads

**Framework**: Apple Ads  
**Kind**: httpRequest

Finds ads within a campaign by selector criteria.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find `ads` within campaigns using a [`Selector`](selector.md) [`Condition`](condition.md) to filter results. If you don’t specify selector conditions, all [`Ad`](ad.md) objects return in the response. See the [`Ad`](ad.md) object for parameter descriptions and selector condition operators.

##### Payload Example Find Ads

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/ads/find

{
  "conditions": [
    {
      "field": "creativeType",
      "operator": "EQUALS",
      "values": [
        "CUSTOM_PRODUCT_PAGE"
      ]
    },
    {
      "field": "status",
      "operator": "EQUALS",
      "values": [
        "PAUSED"
      ]
    }
  ],
  "fields": null,
  "orderBy": [
    {
      "field": "creativeType",
      "sortOrder": "ASCENDING"
    }
  ],
  "pagination": {
    "limit": 20,
    "offset": 0
  }
}
```

**Response**:

```json
{
  "data": [
    {
      "id": 573408745,
      "orgId": 39872140,
      "campaignId": 570798765,
      "adGroupId": 440797654,
      "creativeId": 94895512,
      "name": "Trip Trek custom product page variation",
      "creativeType": "CUSTOM_PRODUCT_PAGE",
      "status": "PAUSED",
      "servingStatus": "NOT_RUNNING",
      "servingStateReasons": [
        "PAUSED_BY_USER"
      ],
      "deleted": false,
      "creationTime": "2024-10-08T00:03:47.889Z",
      "modificationTime": "2024-10-09T00:03:47.889Z"
    }
  ],
  "pagination": {
    "totalResults": 1,
    "startIndex": 1,
    "itemsPerPage": 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/ads/find`

## Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create an Ad](create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads (org-level)](find-ads-(org-level).md)
  Fetches ads within an organization by selector criteria.
- [Get an Ad](get-an-ad.md)
  Fetches an ad assigned to an ad group by identifier.
- [Get All Ads](get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Update an Ad](update-an-ad.md)
  Updates an ad in an ad group.
- [Delete an Ad](delete-an-ad.md)
  Deletes an ad from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-ads)*