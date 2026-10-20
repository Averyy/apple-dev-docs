# MediaLocaleDetail

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The media locale detail object.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object MediaLocaleDetail
```

## Topics

### Dictionaries
- [object MediaLocaleDetail.AppPreviewDeviceWithAssets](./medialocaledetail/apppreviewdevicewithassets-data.dictionary.md)

## Properties

- `appName` (string): The name of the app.
- `appPreviewDeviceWithAssets` (MediaLocaleDetail.AppPreviewDeviceWithAssets): The device display name, fallback device display names, and associated assets.
- `isPrimaryLocale` (boolean): The language of the primary locale for the app.
- `language` (string): The app language.
- `shortDescription` (string): An abbreviated description of the app.
- `subTitle` (string): The subtitle for the app.

## Relationships

### Inherited By
- [MediaLocaleDetailResponse](./medialocaledetailresponse.md)

## See Also

### Response Objects
- [object MediaDetail](./mediadetail.md)
  The media detail object.
- [object MediaDetailResponse](./mediadetailresponse.md)
- [object MediaLocaleDetailResponse](./medialocaledetailresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/medialocaledetail)*