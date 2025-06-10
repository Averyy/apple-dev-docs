# Custom Product Pages

**Framework**: Apple Search Ads

View Custom Product Page details.

#### Overview

In iOS 15 and later, you can use [`custom product pages`](https://developer.apple.comhttps://developer.apple.com/app-store/product-page/) that you build in [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) to create ad variations in the Apple Search Ads Campaign Management API to promote your apps.

To create a custom product page ad, use the following workflow:

![A diagram showing the five-step workflow for creating a custom product page ad.](https://docs-assets.developer.apple.com/published/56d06d39dc5e190bae2f397206d352ea/media-3921834%402x.png)

1. Use [`Get Product Pages`](get-product-pages.md) to fetch your `productPageId`.
2. Use [`Get Product Page Locales`](get-product-page-locales.md) to fetch locale metadata and supported languages. Verify that your custom product page locale and asset data match the language and device types in your campaign [`AdGroup`](adgroup.md).
3. Use [`Create a Creative`](create-a-creative.md) with your `productPageId` to obtain a `creativeId`.
4. Use [`Create an Ad`](create-an-ad.md) with a `creativeId` to assign a custom product page to an [`AdGroup`](adgroup.md). Each ad group can have one custom product page. For information about how to update a custom product page ad group assignment, see [`Update an Ad`](update-an-ad.md).
5. Use [`Get Ad-Level Reports`](get-ad-level-reports.md) to track the performance of ads in your campaigns. These details help you optimize your Apple Search Ads campaigns to deliver a contextualized customer experience.

> **Note**:  If you’ve been using Creative Sets with the API, see section 4.1 in  [`Apple Search Ads Campaign Management API 4`](apple-search-ads-campaign-management-api-4.md) for Creative Sets deprecation details.

## Topics

### Product Page Endpoints
- [Get Product Pages](get-product-pages.md)
  Fetches metadata of all your custom product pages.
- [Get Product Pages by Identifier](get-product-pages-by-identifier.md)
  Fetches metadata for a specific product page.
- [Get Product Page Locales](get-product-page-locales.md)
  Fetches product page locales by identifier.
- [Get Supported Countries or Regions](get-supported-countries-or-regions.md)
  Fetches supported languages and language codes.
- [Get App Preview Device Sizes](get-app-preview-device-sizes.md)
  Fetches supported app preview device-size mappings.
### Product Page Request and Response Objects
- [object LocaleInfo](localeinfo.md)
  The supported languages and language codes.
- [object CountryOrRegion](countryorregion.md)
  The supported locales of a product page.
- [object CountriesOrRegionsListResponse](countriesorregionslistresponse.md)
  A container for product page responses.
- [object MediaAppVideoAsset](mediaappvideoasset.md)
  The app preview or screenshot asset detail.
- [object ProductPageLocaleDetail](productpagelocaledetail.md)
  The product page locale metadata on App Store Connect.
- [object ProductPageDetail](productpagedetail.md)
  The product page metadata.
- [object ProductPageDetailWithAssets](productpagedetailwithassets.md)
  The product page asset metadata.
- [object ProductPageLocaleDetailListResponse](productpagelocaledetaillistresponse.md)
  A container for product page responses.
- [object ProductPageDetailResponse](productpagedetailresponse.md)
  A container for product page responses.
- [object ProductPageDetailWithAssetInfoResponse](productpagedetailwithassetinforesponse.md)
  A container for product page responses.
- [object ProductPageDetailListResponse](productpagedetaillistresponse.md)
  A container for product page responses.
- [object ProductPageReasonCreate](productpagereasoncreate.md)
  The ad creative rejection reason based on a product page.

## See Also

- [Ads](ads.md)
  Assign an ad creative to an ad group.
- [Ad Rejection Reasons](ad-rejection-reasons.md)
  Review reasons for an ad rejection.
- [Creatives](creatives.md)
  Create and manage ad creatives within your organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/custom-product-pages)*