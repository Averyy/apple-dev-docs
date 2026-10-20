# Get Product Pages by Identifier

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches metadata for a specific product page.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to fetch metadata assigned to a specific product page using your `adamId` and `productPageId` in the resource path. Your `productPageId` is an identifier appended to your app product page. For example, `https://apps.apple.com/us/app/trip-trek/id12345678?45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.

Use your `productPageId` to create a [`Creative`](./creative.md) and obtain a `creativeId`. See [`Create a Creative`](./create-a-creative.md).

##### Payload example: Get product pages by identifier

**Request**:

```
GET https://api.searchads.apple.com/api/v5/apps/{adamId}/product-pages/{productPageId}
```

**Response**:

```json
    {
      "id”: "45812c9b-c296-43d3-c6a0-c5a02f74bf6e0",
      "name”: "Trip Trek CPP variation",
      "state": "VISIBLE",
      "adamId": 8992479644,
      "creationTime": "2024-10-25T23:59:59.000",
      "modificationTime": "2024-10-25T23:59:59.000"
    }
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/apps/{adamId}/product-pages/{productPageId}`

## Parameters

### Path Parameters

- `adamId` (int64) *(required)*: Your unique App Store app identifier.

  Your `adamId` in the resource path must match the `adamId` in your campaign. Use [`Get a Campaign`](./get-a-campaign.md) or [`Get all Campaigns`](./get-all-campaigns.md) to obtain your `adamId` and correlate it to the correct campaign.
- `productPageId` (string) *(required)*: A unique string to identify a product page on [App Store Connect](https://appstoreconnect.apple.com). For example, `45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.

## Responses

- `200` OK (`ProductPageDetailResponse`, `application/json`): If the call succeeds, the API returns the [`ProductPageDetailResponse`](./productpagedetailresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Product Page Endpoints
- [Get Product Pages](./get-product-pages.md)
  Fetches metadata of all your custom product pages.
- [Get Product Page Locales](./get-product-page-locales.md)
  Fetches product page locales by identifier.
- [Get Supported Countries or Regions](./get-supported-countries-or-regions.md)
  Fetches supported languages and language codes.
- [Get App Preview Device Sizes](./get-app-preview-device-sizes.md)
  Fetches supported app preview device-size mappings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-product-pages-by-identifier)*