# ProductPageLocaleDetail

**Framework**: Apple Ads  
**Kind**: dictionary

The product page locale metadata on App Store Connect.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
object ProductPageLocaleDetail
```

## Topics

### Objects
- [object ProductPageLocaleDetail.AppPreviewDeviceWithAssets](productpagelocaledetail/apppreviewdevicewithassets-data.dictionary.md)
  A map of app preview device assets.

## Properties

- `adamId` (int64): Your unique App Store app identifier. Use [`Get a Campaign`](get-a-campaign.md) or [`Get all Campaigns`](get-all-campaigns.md) to obtain your `adamId` used in your campaign.
- `appName` (string): The app name on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `appPreviewDeviceWithAssets` (ProductPageLocaleDetail.AppPreviewDeviceWithAssets): A map between the device and available app preview details for that device.
- `deviceClasses` (string): The device classes assigned to a custom product page on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `language` (string): The language associated with the ISO alpha-2 country code, such as `US`.
- `languageCode` (string): The ISO 639-1 language code appended to the ISO 3166-1 alpha-2 country code, such as `en-US`.
- `productPageId` (string): A unique string to identify a product page on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). For example, `45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.
- `promotionalText` (string): Text that appears at the top of the main description of a product page.
- `shortDescription` (string): Concise, informative text used on a product page to describe an app.
- `subTitle` (string): A summary of an app on a product page that appears below the name of an app.

## See Also

- [object LocaleInfo](localeinfo.md)
  The supported languages and language codes.
- [object CountryOrRegion](countryorregion.md)
  The supported locales of a product page.
- [object CountriesOrRegionsListResponse](countriesorregionslistresponse.md)
  A container for product page responses.
- [object MediaAppVideoAsset](mediaappvideoasset.md)
  The app preview or screenshot asset detail.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/productpagelocaledetail)*