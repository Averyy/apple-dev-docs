# MediaAppAssetsDetail

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The app asset details of a device.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object MediaAppAssetsDetail
```

## Properties

- `appPreviewDeviceFallBackDevices` ([string]): Devices that don’t have uploaded assets use fallback device mapping.
- `appPreviews` ([MediaAppVideoAsset]): Still images of video assets to use for [app previews](https://developer.apple.com/app-store/app-previews/).
- `screenshots` ([MediaAppAsset]): Standard images of your app to use for [app previews](https://developer.apple.com/app-store/app-previews/).

## See Also

### Creative Request and Response Objects
- [object AppPreviewDevicesMappingResponse](./apppreviewdevicesmappingresponse.md)
  The app preview device mapping response to display name and size mapping requests.
- [object Creative](./creative.md)
  The creative object.
- [object CreativeLocalization](./creativelocalization.md)
  The localized creative metadata.
- [object CreativeLocalizationWithAssets](./creativelocalizationwithassets.md)
  The localized creative metadata with app preview.
- [object CustomProductPageCreative](./customproductpagecreative.md)
  The creative details of a product page.
- [object CreativeResponse](./creativeresponse.md)
  The response details of a creative request.
- [object CreativeListResponse](./creativelistresponse.md)
  A container for response details of a creative request.
- [object DefaultProductPageCreative](./defaultproductpagecreative.md)
  The default product page object.
- [object MediaAppAsset](./mediaappasset.md)
  The asset details of app preview or app screenshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/mediaappassetsdetail)*