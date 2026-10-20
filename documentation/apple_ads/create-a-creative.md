# Create a Creative

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Creates a creative object within an organization.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to create a [`Creative`](./creative.md) object within your organization using your `productPageId`.

##### Payload example: Create a creative

**Request**:

```
POST https://api.searchads.apple.com/api/v5/creatives

{
  "adamId": 899247964,
  "name": "Trip Trek CPP variation",
  "type”: "CUSTOM_PRODUCT_PAGE",
  "productPageId": "45812c9b-c296-43d3-c6a0-c5a02f74bf6e"
}
```

**Response**:

```json
{
    "id": 94895512,
    "orgId": 39872140,
    "adamId": 899247964,
    "name": "Trip Trek CPP variation",
    "type": "CUSTOM_PRODUCT_PAGE",
    "state": "VALID",
    "stateReasons": [],
    "creationTime": "2024-10-09T06:48:22.812Z",
    "modificationTime": "2024-107-09T06:48:22.812Z",
    "productPageId": "45812c9b-c296-43d3-c6a0-c5a02f74bf6e"
  }

```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/creatives`

## Request Body

**Content-Type**: `application/json`  
**Type**: `(CustomProductPageCreative | DefaultProductPageCreative)`

The request body that includes details of the [`Creative`](./creative.md).

## Responses

- `200` OK (`CreativeResponse`, `application/json`): If the call succeeds, the API returns the `CreativeResponse` object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Creative Endpoints
- [Find Creatives](./find-creatives.md)
  Finds creatives within an organization.
- [Get a Creative](./get-a-creative.md)
  Fetches a creative by identifier.
- [Get All Creatives](./get-all-creatives.md)
  Fetches all creatives within an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-a-creative)*