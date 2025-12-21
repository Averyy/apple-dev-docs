# Get Product Pages by Identifier

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches metadata for a specific product page.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to fetch metadata assigned to a specific product page using your `adamId` and `productPageId` in the resource path. Your `productPageId` is an identifier appended to your app product page. For example, `https://apps.apple.com/us/app/trip-trek/id12345678?45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.

Use your `productPageId` to create a [`Creative`](creative.md) and obtain a `creativeId`. See [`Create a Creative`](create-a-creative.md).

##### Payload Example Get Product Pages By Identifier

## See Also

- [Get Product Pages](get-product-pages.md)
  Fetches metadata of all your custom product pages.
- [Get Product Page Locales](get-product-page-locales.md)
  Fetches product page locales by identifier.
- [Get Supported Countries or Regions](get-supported-countries-or-regions.md)
  Fetches supported languages and language codes.
- [Get App Preview Device Sizes](get-app-preview-device-sizes.md)
  Fetches supported app preview device-size mappings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-product-pages-by-identifier)*