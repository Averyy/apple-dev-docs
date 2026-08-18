# AppLocaleDetails

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Localized content for an app’s Default Product Page.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppLocaleDetails
```

#### Discussion

`AppLocaleDetails` represents the localized metadata and asset groupings for a single locale of an app’s Default Product Page (DPP). `language` (e.g., `"en"`) and `languageCode` (e.g., `"en-US"`) identify each locale entry.

##### Example

```json
{
  "adamId": 324684580,
  "language": "en",
  "languageCode": "en-US",
  "isPrimaryLocale": true,
  "appName": "AwayFinder - Travel Planner",
  "subTitle": "Discover new destinations",
  "promotionalText": "Get 3 months of Premium free",
  "shortDescription": "Plan trips and discover destinations with AwayFinder",
  "deviceClasses": [
    "IPHONE",
    "IPAD"
  ],
  "assetsByDevice": {
    "iphone_6_5": {
      "appPreviewDeviceFallBackDevices": [
        "iphone6",
        "iphone5"
      ],
      "assets": [
        {
          "assetId": "550e8400-e29b-41d4-a716-446655440000"
        },
        {
          "assetId": "660f9511-f3ac-52e5-b827-557766551111"
        }
      ]
    }
  }
}
```

## Topics

### Dictionaries
- [object AppLocaleDetails.AssetsByDevice](applocaledetails/assetsbydevice-data.dictionary.md)
  Map of device type to a `DeviceAssetGroup` containing the ordered list of asset IDs and any fallback device references.

## Properties

- `adamId` (int64): App Store identifier for the app.
- `language` (string): Language identifier (e.g., `"en"`).
- `languageCode` (string): BCP-47 language code (e.g., `"en-US"`).
- `isPrimaryLocale` (boolean): True if this locale’s `languageCode` matches the app’s primary language.
- `appName` (string): Localized app name.
- `subTitle` (string): Localized app subtitle.
- `promotionalText` (string): Promotional text for this locale (max 170 characters).
- `shortDescription` (string): Short description for this locale (max 4000 characters).
- `deviceClasses` ([string]): Device families with available assets for this locale.
- `assetsByDevice` (AppLocaleDetails.AssetsByDevice): Map of device type (e.g., `"iphone_6_5"`) to a `DeviceAssetGroup` containing the ordered list of asset IDs and any fallback device references.

## See Also

- [object AppInfo](appinfo.md)
  A single app search result.
- [object AppsSearchResponse](appssearchresponse.md)
  Apps search response envelope.
- [object AppLocaleDetailsQueryResponse](applocaledetailsqueryresponse.md)
  Paginated response object for app locale detail queries.
- [object AppSupportedLanguages](appsupportedlanguages.md)
  App supported and default languages for an App Store country or region.
- [object AppSupportedLanguagesQueryResponse](appsupportedlanguagesqueryresponse.md)
  Paginated response object for the supported app languages query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/applocaledetails)*