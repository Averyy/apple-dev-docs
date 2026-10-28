# Find Creatives

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Finds creatives within an organization.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

Use this endpoint to find creatives using a [`Selector`](./selector.md) [`Condition`](./condition.md) to filter results. If you don’t specify selector conditions, all creatives return in the response. See [`Creative`](./creative.md) for field descriptions and selector condition operators.

Values are case-sensitive strings. The `orderBy` selector supports the `Id` and `name` fields.

### Payload example: Find creatives

**Request**:

```
POST https://api.searchads.apple.com/api/v5/creatives/find

{
  "conditions": [
    {
      "field": "name",
      "operator": "CONTAINS",
      "values": [
        "Trip"
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
      "id": 573408745,
      "orgId": 39872140,
      "adamId": 899247664,
      "name": "Trip Trek custom product page variation 1",
      "type": "CUSTOM_PRODUCT_PAGE",
      "state": "VALID",
      "stateReasons": [],
      "creationTime": "2024-10-09T20:07:19.506Z",
      "modificationTime": "2024-10-18T20:07:19.506Z",
      "productPageId": "76659d7a-d146-43d3-b6b8-b7a12f74bf6b"
    },
    {
      "id": 75606108,
      "orgId": 39879640,
      "adamId": 1004806037,
      "name": "Trip Trek Creative Set variation 2",
      "type": "CREATIVE_SET",
      "state": "INVALID",
      "stateReasons": [],
      "creationTime": "2024-03-04T02:44:14.775",
      "modificationTime": "2024-08-17T01:16:37.827",
      "languageCode": "en_US"
    }
  ],
  “pagination”: {
    “totalResults”: 2,
    “startIndex”: 1,
    “itemsPerPage”: 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/creatives/find`

## Request Body

**Content-Type**: `application/json`  
**Type**: `Selector`

The request body that includes the selector [`Condition`](./condition.md). [`Selector`](./selector.md) objects define what data the API returns when fetching resources.

## Responses

- `200` OK (`CreativeListResponse`, `application/json`): If the call succeeds, the API returns the [`CreativeListResponse`](./creativelistresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Creative Endpoints
- [Create a Creative](./create-a-creative.md)
  Creates a creative object within an organization.
- [Get a Creative](./get-a-creative.md)
  Fetches a creative by identifier.
- [Get All Creatives](./get-all-creatives.md)
  Fetches all creatives within an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-creatives)*