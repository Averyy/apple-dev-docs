# CreativeLocalizationWithAssets

**Framework**: Apple Ads  
**Kind**: dictionary

The localized creative metadata with app preview.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
object CreativeLocalizationWithAssets
```

## Topics

### Objects
- [object CreativeLocalizationWithAssets.AppPreviewDeviceWithAssets](creativelocalizationwithassets/apppreviewdevicewithassets-data.dictionary.md)
  A map of app preview device assets.

## Properties

- `appName` (string): The app name on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- `appPreviewDeviceWithAssets` (CreativeLocalizationWithAssets.AppPreviewDeviceWithAssets): The map of available app preview details for a device.
- `deviceClasses` (string): The device classes assigned to a custom product page. See [`DeviceClass`](deviceclass.md) for value descriptions.
- `language` (string): The language associated with the ISO alpha-2 country code, such as `US`.
- `languageCode` (string): The ISO 639-1 language code appended to the ISO alpha-2 country code, such as `en-US`.
- `promotionalText` (string): Text that appears at the top of the main description of a product page.
- `shortDescription` (string): Concise, informative text to describe an app on a product page.
- `subTitle` (string): A summary of an app that appears below the name of an app on a product page.

## See Also

- [object AppPreviewDevicesMappingResponse](apppreviewdevicesmappingresponse.md)
  The app preview device mapping response to display name and size mapping requests.
- [object Creative](creative.md)
  The creative object.
- [object CreativeLocalization](creativelocalization.md)
  The localized creative metadata.
- [object CustomProductPageCreative](customproductpagecreative.md)
  The creative details of a product page.
- [object CreativeResponse](creativeresponse.md)
  The response details of a creative request.
- [object CreativeListResponse](creativelistresponse.md)
  A container for response details of a creative request.
- [object DefaultProductPageCreative](defaultproductpagecreative.md)
  The default product page object.
- [object MediaAppAsset](mediaappasset.md)
  The asset details of app preview or app screenshots.
- [object MediaAppAssetsDetail](mediaappassetsdetail.md)
  The app asset details of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/creativelocalizationwithassets)*