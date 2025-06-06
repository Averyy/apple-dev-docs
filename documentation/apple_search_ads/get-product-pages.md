# Get Product Pages

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches metadata of all your custom product pages.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Search Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to fetch your product page metadata using your `adamId` in the resource path. Use your `productPageId` to [`Create a Creative`](create-a-creative.md) obtain a `creativeId`.

##### Payload Example Get Product Pages

The `id` in the response is your `productPageId`, an identifier for your app product page. For example, `45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.

## See Also

- [Get Product Pages by Identifier](get-product-pages-by-identifier.md)
  Fetches metadata for a specific product page.
- [Get Product Page Locales](get-product-page-locales.md)
  Fetches product page locales by identifier.
- [Get Supported Countries or Regions](get-supported-countries-or-regions.md)
  Fetches supported languages and language codes.
- [Get App Preview Device Sizes](get-app-preview-device-sizes.md)
  Fetches supported app preview device-size mappings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/get-product-pages)*