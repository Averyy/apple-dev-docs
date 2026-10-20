# Get Product Pages

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches metadata of all your custom product pages.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to fetch your product page metadata using your `adamId` in the resource path. Use your `productPageId` to [`Create a Creative`](./create-a-creative.md) obtain a `creativeId`.

##### Payload example: Get product pages

The `id` in the response is your `productPageId`, an identifier for your app product page. For example, `45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.

**Request**:

```
GET https://api.searchads.apple.com/api/v5/apps/{adamId}/product-pages
```

**Response**:

```json

    {
      "id": "45812c9b-c296-43d3-c6a0-c5a02f74bf6e",
      "name": "Trip Trek CPP variation 1",
      "state": "VISIBLE",
      "adamId": 899247964,
      "creationTime": "2024-10-25T23:59:59.000",
      "modificationTime": "2024-10-08T17:44:49.718Z"
   }
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/apps/{adamId}/product-pages`

## Parameters

### Path Parameters

- `adamId` (int64) *(required)*: The unique identifier for the ad group.

### Query Parameters

- `name` (string): Filters by `name` field. For example, the name of your custom product page on [App Store Connect](https://appstoreconnect.apple.com).
- `states` (string): Filters by `states`, which indicates whether the product page is visible or not.

  **Allowed Values**: `HIDDEN`, `VISIBLE`

## Responses

- `200` OK (`ProductPageDetailListResponse`, `application/json`): If the call succeeds, the API returns the [`ProductPageDetailListResponse`](./productpagedetaillistresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Product Page Endpoints
- [Get Product Pages by Identifier](./get-product-pages-by-identifier.md)
  Fetches metadata for a specific product page.
- [Get Product Page Locales](./get-product-page-locales.md)
  Fetches product page locales by identifier.
- [Get Supported Countries or Regions](./get-supported-countries-or-regions.md)
  Fetches supported languages and language codes.
- [Get App Preview Device Sizes](./get-app-preview-device-sizes.md)
  Fetches supported app preview device-size mappings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-product-pages)*