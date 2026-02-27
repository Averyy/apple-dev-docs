# AppAsset

**Framework**: Apple Ads  
**Kind**: dictionary

The app assets associated with an adam ID.

**Availability**:
- Search Ads 4.8+

## Declaration

```swift
object AppAsset
```

## Properties

- `adamId` (string): Your unique App Store app identifier. Use [`Get a Campaign`](get-a-campaign.md) or [`Get all Campaigns`](get-all-campaigns.md) to obtain your `adamId`. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find App Assets`](find-app-assets.md). This field is sortable.
- `appPreviewDevice` (string): Indicates the device model and corresponding display size. See [`AppPreviewDevicesMappingResponse.Data`](apppreviewdevicesmappingresponse/data-data.dictionary.md). This field is sortable.
- `assetGenId` (string): The unique identifier for an app preview or screenshot. Your `adamId` is the first numerical grouping in `assetGenId`. For example, in `1408851466;en-US;5;0;f8c9add6280c781e6f701c506be5a921`, `1408851466` is your `adamId`. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find App Assets`](find-app-assets.md). This field is sortable.
- `assetType` (string): The type of creative asset. `APP_PREVIEW` is a video still image of video assets that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). Note, the playable URL isn’t in the API response. `SCREENSHOT` is a standard image  of the app that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `assetURL` (string): The resolved URL for the screenshot that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). For a video asset, the image is the first frame.
- `assetVideoUrl` (string): The fully resolved URL for the asset video. The field is non-null for preview assets; otherwise, it’s null.
- `deleted` (boolean): Indicates whether the asset was deleted from [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). This field is sortable.
- `orientation` (string): The orientation of the asset that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `sourceHeight` (int32): The height of the asset that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). This field is sortable.
- `sourceWidth` (int32): The width of the asset that you upload to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). This field is sortable.

## See Also

- [object AppAssetListResponse](appassetlistresponse.md)
  The response to a request that returns a list of app assets.
- [object ProductPageReason](productpagereason.md)
  The ad creative rejection reason based on a product page.
- [object ProductPageReasonListResponse](productpagereasonlistresponse.md)
  The response to a request that returns a list of product page rejection reasons.
- [object ProductPageReasonResponse](productpagereasonresponse.md)
  A container for product page reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/appasset)*