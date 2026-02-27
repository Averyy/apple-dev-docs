# ProductPageDetail

**Framework**: Apple Ads  
**Kind**: dictionary

The product page metadata.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
object ProductPageDetail
```

## Mentions

- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

## Properties

- `adamId` (int64): Your unique App Store app identifier. Use [`Get a Campaign`](get-a-campaign.md) or [`Get all Campaigns`](get-all-campaigns.md) to obtain your `adamId` used in your campaign.
- `creationTime` (date-time): The date and time the object was created. This field is not modifiable.
- `deepLink` (string): The deep link set up in your custom product page metadata on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). Deep links are available on iOS 18 and later for Today tab and search results ad variations, and iPadOS 18 and later for search results ad variations. Note that deep links are not available for ads with demographic targeting (age or gender). This field is not modifiable.
- `id` (string): A unique string to identify a product page on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). For example, `45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.
- `modificationTime` (date-time): The date and time of the most recent modification of the object. This field is not modifiable.
- `name` (string): The name of your custom product page on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `state` (string): The system state of the custom product page that indicates whether the page is visible or not.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/productpagedetail)*