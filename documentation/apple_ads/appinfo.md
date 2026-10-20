# AppInfo

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The response to an app search request.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object AppInfo
```

## Properties

- `adamId` (int64): Your unique [App Store Connect](https://appstoreconnect.apple.com) app identifier.
- `appName` (string): The name of the app.
- `countryOrRegionCodes` ([string]): A list of ISO alpha-2 country code strings.
- `developerName` (string): The developer name for the app.

## See Also

### Search Apps Request and Response Objects
- [object AppInfoListResponse](./appinfolistresponse.md)
  The response details of app search requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/appinfo)*