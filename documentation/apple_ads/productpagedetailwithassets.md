# ProductPageDetailWithAssets

**Framework**: Apple Ads  
**Kind**: dictionary

The product page asset metadata.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
object ProductPageDetailWithAssets
```

## Properties

- `adamId` (int64): Your unique App Store app identifier. Use [`Get a Campaign`](get-a-campaign.md) or [`Get all Campaigns`](get-all-campaigns.md) to obtain your `adamId` used in your campaign.
- `contentProviderId` (int64): A unique identifier of the registered content owner.
- `creationTime` (date-time): The date and time the object was created. This field is not modifiable.
- `id` (int64): A unique string to identify a product page on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). For example, `45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.
- `isDefault` (boolean): Indicates if the custom product page is the default on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `localization` ([CreativeLocalizationWithAssets]): Localized metadata used on a product page with app preview.
- `modificationTime` (date-time): The date and time of the most recent modification of the object. This field is not modifiable.
- `name` (string): The name of your custom product page, as input through [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).

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
- [object ProductPageDetail](productpagedetail.md)
  The product page metadata.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/productpagedetailwithassets)*