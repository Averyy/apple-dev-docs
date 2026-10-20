# MediaDetail

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The media detail object.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object MediaDetail
```

## Properties

- `adamId` (int64): Your unique App Store app identifier.
- `appName` (string): The name of an app.
- `artistName` (string): The name of the app author.
- `availableStorefronts` ([string]): Countries or regions where the app is available.
- `deviceClasses` ([string]): Device classes supported.
- `iconPictureUrl` (string): The URL of the image asset.
- `id` (string): A unique ID.
- `isPreOrder` (boolean): Indicates if the app is a pre-order.
- `primaryGenre` (string): The genre of the app.
- `primaryLanguage` (string)
- `secondaryGenre` (string)

## Relationships

### Inherited By
- [MediaDetailResponse](./mediadetailresponse.md)

## See Also

### Response Objects
- [object MediaDetailResponse](./mediadetailresponse.md)
- [object MediaLocaleDetail](./medialocaledetail.md)
  The media locale detail object.
- [object MediaLocaleDetailResponse](./medialocaledetailresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/mediadetail)*