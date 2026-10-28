# Get App Preview Device Sizes

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches supported app preview device-size mappings.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Creative Sets](./creative-sets.md)

## Discussion

Use this endpoint to return a complete list of supported app preview device-size mappings.

### Payload example: Get app preview device sizes

**Request**:

```
GET https://api.searchads.apple.com/api/v5/creativeappmappings/devices
```

**Response**:

```json
{
    "ipadPro": "iPad 12.9",
    "iphone6+": "iPhone 5.5",
    "iphone_5_8": "iPhone 5.8",
    "iphone5": "iPhone 4",
    "iphone6": "iPhone 4.7",
    "ipadPro_2018": "iPad 11",
    "ipad": "iPad 9.7",
    "iphone_6_5": "iPhone 6.5",
    "ipad_10_5": "iPad 10.5"
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/creativeappmappings/devices`

## Responses

- `200` OK (`AppPreviewDevicesMappingResponse`, `application/json`): If the call succeeds, the API returns the [`AppPreviewDevicesMappingResponse`](./apppreviewdevicesmappingresponse.md) object in the response payload with an HTTP status code of `200(OK)`.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Product Page Endpoints
- [Get Product Pages](./get-product-pages.md)
  Fetches metadata of all your custom product pages.
- [Get Product Pages by Identifier](./get-product-pages-by-identifier.md)
  Fetches metadata for a specific product page.
- [Get Product Page Locales](./get-product-page-locales.md)
  Fetches product page locales by identifier.
- [Get Supported Countries or Regions](./get-supported-countries-or-regions.md)
  Fetches supported languages and language codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-app-preview-device-sizes)*