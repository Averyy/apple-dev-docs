# Find Targeting Keywords in a Campaign

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches targeting keywords in a campaign’s ad groups.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to find targeting keywords in different ad groups within the same campaign. Use the associated `campaignId` in the URI. Find calls use [`Selector`](./selector.md) [`Condition`](./condition.md) operators to narrow results. If you don’t specify any selector conditions in the payload, the API returns all keywords across all ad groups of the campaign. For more information about available selection condition operators to use, see the [`Keyword`](./keyword.md) object.

##### Payload example: Find targeting keywords in a campaign

**Request**:

```
POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/targetingkeywords/find

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
      "adGroupId": 427916203,
      "text": "targeting keyword example 1",
      "status": "PAUSED",
      "matchType": "BROAD",
      "bidAmount": {
        "amount": "100",
        "currency": "USD"
      },
      "modificationTime": "2024-04-08T21:03:02.216",
      "deleted": false
    },
    {
      "id": 542370642,
      "adGroupId": 427916203,
      "text": "targeting keyword example 2",
      "status": "ACTIVE",
      "matchType": "EXACT",
      "bidAmount": {
        "amount": "100",
        "currency": "USD"
      },
      "modificationTime": "2024-04-08T17:53:10.899",
      "deleted": false
    }
  ],
  "pagination": {
    "totalResults": 2,
    "startIndex": 1,
    "itemsPerPage": 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/campaigns/{campaignId}/adgroups/targetingkeywords/find`

## Parameters

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `Selector`

The request body that includes the selector [`Condition`](./condition.md). [`Selector`](./selector.md) objects define what data the API returns when fetching resources.

## Responses

- `200` OK (`KeywordListResponse`, `application/json`): If the call succeeds, the API returns a list of [`Keyword`](./keyword.md) objects in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Ad Group Targeting Keywords Endpoints
- [Create Targeting Keywords](./create-targeting-keywords.md)
  Creates targeting keywords in ad groups.
- [Get a Targeting Keyword in an Ad Group](./get-a-targeting-keyword-in-an-ad-group.md)
  Fetches a specific targeting keyword in an ad group.
- [Get All Targeting Keywords in an Ad Group](./get-all-targeting-keywords-in-an-ad-group.md)
  Fetches all targeting keywords in ad groups.
- [Update Targeting Keywords](./update-targeting-keywords.md)
  Updates targeting keywords in ad groups.
- [Delete Targeting Keywords](./delete-targeting-keywords.md)
  Deletes targeting keywords from ad groups.
- [Delete a Targeting Keyword](./delete-a-targeting-keyword.md)
  Deletes a targeting keyword in an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-targeting-keywords-in-a-campaign)*