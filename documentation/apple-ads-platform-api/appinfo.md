# AppInfo

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single app search result.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppInfo
```

#### Discussion

`AppInfo` represents one app returned from the search apps endpoint. It includes the app’s Adam ID, display name, developer name, and the country or region codes where the app is available.

##### Example

```json
{
  "adamId": 123456789,
  "appName": "AwayFinder",
  "developerName": "AwayFinder Inc.",
  "countryOrRegionCodes": [
    "US",
    "CA",
    "GB"
  ]
}
```

## Properties

- `adamId` (int64) *(required)*: The Adam ID of the app. Use this value when creating campaigns targeting this app.
- `appName` (string) *(required)*: The app display name as shown in the App Store.
- `developerName` (string) *(required)*: The developer or publisher name.
- `countryOrRegionCodes` ([string]) *(required)*: ISO 3166-1 alpha-2 codes for all App Store countries or regions where this app is available.

## See Also

- [object AppLocaleDetails](applocaledetails.md)
  Localized content for an app’s Default Product Page.
- [object AppsSearchResponse](appssearchresponse.md)
  Apps search response envelope.
- [object AppLocaleDetailsQueryResponse](applocaledetailsqueryresponse.md)
  Paginated response object for app locale detail queries.
- [object AppSupportedLanguages](appsupportedlanguages.md)
  App supported and default languages for an App Store country or region.
- [object AppSupportedLanguagesQueryResponse](appsupportedlanguagesqueryresponse.md)
  Paginated response object for the supported app languages query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appinfo)*