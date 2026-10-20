# Find Campaign Negative Keywords

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches negative keywords for campaigns.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

Use this endpoint to find campaign negative keywords. Use the associated `campaignId` in the URI. Find calls use [`Selector`](./selector.md) [`Condition`](./condition.md) operators to narrow results. If you don’t specify any selector conditions, all negative keywords in the campaign return in the response. See the [`NegativeKeyword`](./negativekeyword.md) object for details about selector [`Condition`](./condition.md) operators per field.

##### Payload example: Find campaign negative keywords

**Request**:

```
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

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `Selector`

The request body that includes the selector [`Condition`](./condition.md). [`Selector`](./selector.md) objects define what data the API returns when fetching resources.

## Responses

- `200` OK (`NegativeKeywordListResponse`, `application/json`): If the call succeeds, the API returns a list of [`NegativeKeyword`](./negativekeyword.md) objects in the response payload with an HTTP status code of `200` `(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Campaign Negative Keywords Endpoints
- [Create Campaign Negative Keywords](./create-campaign-negative-keywords.md)
  Creates negative keywords for a campaign.
- [Get a Campaign Negative Keyword](./get-a-campaign-negative-keyword.md)
  Fetches a specific negative keyword in a campaign.
- [Get All Campaign Negative Keywords](./get-all-campaign-negative-keywords.md)
  Fetches all negative keywords in a campaign.
- [Update Campaign Negative Keywords](./update-campaign-negative-keywords.md)
  Updates negative keywords in a campaign.
- [Delete Campaign Negative Keywords](./delete-campaign-negative-keywords.md)
  Deletes negative keywords from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-campaign-negative-keywords)*