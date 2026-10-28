# Find Ads

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Finds ads within a campaign by selector criteria.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

Use this endpoint to find `ads` within campaigns using a [`Selector`](./selector.md) [`Condition`](./condition.md) to filter results. If you don’t specify selector conditions, all [`Ad`](./ad.md) objects return in the response. See the [`Ad`](./ad.md) object for parameter descriptions and selector condition operators.

### Payload example: Find ads

**Request**:

```
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

### Path Parameters

- `campaignId` (int64) *(required)*: The unique identifier for the campaign.

## Request Body

**Content-Type**: `application/json`  
**Type**: `Selector`

The request body that includes the selector [`Condition`](./condition.md). [`Selector`](./selector.md) objects define what data the API returns when fetching resources.

## Responses

- `200` OK (`AdListResponse`, `application/json`): If the call succeeds, the API returns the [`AdListResponse`](./adlistresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Ad Endpoints
- [Create an Ad](./create-an-ad.md)
  Creates an ad in an ad group with a creative.
- [Find Ads (org-level)](./find-ads-%28org-level%29.md)
  Fetches ads within an organization by selector criteria.
- [Get an Ad](./get-an-ad.md)
  Fetches an ad assigned to an ad group by identifier.
- [Get All Ads](./get-all-ads.md)
  Fetches all ads assigned to an ad group.
- [Update an Ad](./update-an-ad.md)
  Updates an ad in an ad group.
- [Delete an Ad](./delete-an-ad.md)
  Deletes an ad from an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-ads)*