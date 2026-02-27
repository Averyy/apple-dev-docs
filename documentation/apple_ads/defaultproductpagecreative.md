# DefaultProductPageCreative

**Framework**: Apple Ads  
**Kind**: dictionary

The default product page object.

## Declaration

```swift
object DefaultProductPageCreative
```

## Properties

- `adamId` (int64) *(required)*: Your unique App Store app identifier.
- `creationTime` (date-time): The timestamp for the creation of the report in the format of `YYYY-MM-DD’T’HH:mm:ss.SSS`.
- `id` (int64): The unique identifier for a creative.
- `modificationTime` (date-time): The date and time of the most recent modification of the object.
- `name` (string) *(required)*: The unique name of the creative.
- `orgId` (int64): The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in the [`Apple Ads UI`](https://developer.apple.comhttps://ads.apple.com/advanced).
- `productPageId` (string): The product page identifier.
- `state` (string): The system state of the process.
- `stateReasons` ([string]): A list of reasons that displays when an ad isn’t running.
- `type` (string) *(required)*: The type of creative.

## See Also

- [object AppPreviewDevicesMappingResponse](apppreviewdevicesmappingresponse.md)
  The app preview device mapping response to display name and size mapping requests.
- [object Creative](creative.md)
  The creative object.
- [object CreativeLocalization](creativelocalization.md)
  The localized creative metadata.
- [object CreativeLocalizationWithAssets](creativelocalizationwithassets.md)
  The localized creative metadata with app preview.
- [object CustomProductPageCreative](customproductpagecreative.md)
  The creative details of a product page.
- [object CreativeResponse](creativeresponse.md)
  The response details of a creative request.
- [object CreativeListResponse](creativelistresponse.md)
  A container for response details of a creative request.
- [object MediaAppAsset](mediaappasset.md)
  The asset details of app preview or app screenshots.
- [object MediaAppAssetsDetail](mediaappassetsdetail.md)
  The app asset details of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/defaultproductpagecreative)*