# Get a Creative

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches a creative by identifier.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

Use this endpoint to fetch details of a [`Creative`](./creative.md) using your `creativeId` in the resource path.

##### Payload example: Get a creative

**Request**:

```
GET https://api.searchads.apple.com/api/v5/creatives/{creativeId}
```

**Response**:

```json
 {
      "id": 94790778,
      "orgId": 42173330,
      "adamId": 918469737,
      "name": "Trip Trek CPP variation 1",
      "type": "CUSTOM_PRODUCT_PAGE",
      "state": "VALID",
      "stateReasons": [],
      "creationTime": "2024-11-08T21:53:35.036",
      "modificationTime": "2024-09-04T21:53:35.036",
      "productPageId": "00d99d1e-ee93-48fc-973e-7ffc0ddfced6"
 }
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/creatives/{creativeId}`

## Parameters

### Path Parameters

- `creativeId` (int64) *(required)*: The unique identifier for a [`Creative`](./creative.md).

### Query Parameters

- `includeDeletedCreativeSetAssets` (boolean): Include deleted assets in the response. By default deleted assets don’t return.

## Responses

- `200` OK (`CreativeResponse`, `application/json`): If the call succeeds, the API returns the [`CreativeResponse`](./creativeresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Creative Endpoints
- [Create a Creative](./create-a-creative.md)
  Creates a creative object within an organization.
- [Find Creatives](./find-creatives.md)
  Finds creatives within an organization.
- [Get All Creatives](./get-all-creatives.md)
  Fetches all creatives within an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-creative)*