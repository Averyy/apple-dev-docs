# CustomProductPageCreative

**Framework**: Apple Ads  
**Kind**: dictionary

The creative details of a product page.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
object CustomProductPageCreative
```

## Properties

- `productPageId` (string) *(required)*: A unique string to identify a product page on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com), such as `45812c9b-c296-43d3-c6a0-c5a02f74bf6e`.
- `adamId` (int64) *(required)*: Your unique App Store app identifier. You can obtain your `adamId` through [`Get a Campaign`](get-a-campaign.md) or [`Get all Campaigns`](get-all-campaigns.md).
- `creationTime` (date-time): The date and time of the creation of the [`Creative`](creative.md) object.
- `id` (int64): The `creativeId` is a unique identifier for a creative.
- `modificationTime` (date-time): The date and time of the most recent modification of the object.
- `name` (string) *(required)*: The name of a creative.
- `orgId` (int64): The identifier of the organization that owns a campaign. Your `orgId` is the same as your account in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/).
- `state` (string): The system state of the custom product page that indicates whether the page is visible. See [`CreativeState`](creativestate.md) for value descriptions.
- `stateReasons` ([string]): The detailed explanation of the system state. See [`CreativeStateReason`](creativestatereason.md) for value descriptions.
- `type` (string) *(required)*: The type of creative. See [`CreativeType`](creativetype.md) for value descriptions.

## See Also

- [object AppPreviewDevicesMappingResponse](apppreviewdevicesmappingresponse.md)
  The app preview device mapping response to display name and size mapping requests.
- [object Creative](creative.md)
  The creative object.
- [object CreativeLocalization](creativelocalization.md)
  The localized creative metadata.
- [object CreativeLocalizationWithAssets](creativelocalizationwithassets.md)
  The localized creative metadata with app preview.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/customproductpagecreative)*