# MediaAppVideoAsset

**Framework**: Apple Ads  
**Kind**: dictionary

The app preview or screenshot asset detail.

**Availability**:
- Search Ads 4.8+

## Declaration

```swift
object MediaAppVideoAsset
```

## Properties

- `assetGenId` (string): The unique identifier for an app preview or screenshot. Your `adamId` is the first numerical grouping in `assetGenId`. For example, in `1408851466;en-US;5;0;f8c9add6280c781e6f701c506be5a921`, `1408851466` is your `adamId`. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with `Find App Assets`. This field is sortable.
- `assetType` (string): The type of creative asset. `APP_PREVIEW` is a video still image of video assets that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). Note, the playable URL isn’t in the API response. `SCREENSHOT` is a standard image  of the app that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `assetURL` (string): The resolved URL for the screenshot. For a video asset, the image is the first frame.
- `assetVideoURL` (string): The fully resolved URL for the asset video. The field is non-null for preview assets; otherwise, it’s null.
- `orientation` (string): The orientation of the asset that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `sortPosition` (int64): The position in the sort order to show the asset of app preview.
- `sourceHeight` (int32): The height of the asset that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `sourceWidth` (int32): The width of the asset that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).

## See Also

- [object LocaleInfo](localeinfo.md)
  The supported languages and language codes.
- [object CountryOrRegion](countryorregion.md)
  The supported locales of a product page.
- [object CountriesOrRegionsListResponse](countriesorregionslistresponse.md)
  A container for product page responses.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/mediaappvideoasset)*