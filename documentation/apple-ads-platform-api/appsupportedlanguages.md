# AppSupportedLanguages

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

App supported and default languages for an App Store country or region.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppSupportedLanguages
```

#### Discussion

`AppSupportedLanguages` provides metadata about a supported advertising market, including the country name, its ISO 3166-1 alpha-2 `countryCode`, and the language settings relevant for ad delivery. `adsSupportedLanguages` lists all languages available for ads in that market. `adsDefaultLanguages` lists the languages the system applies automatically when you don’t set explicit language targeting.

The [`Query Supported App Languages`](query-supported-app-languages.md) endpoint returns this object, which you use to validate locale choices before setting them on creatives or ad groups.

##### Example

```json
{
  "name": "United States",
  "countryCode": "US",
  "adsSupportedLanguages": [
    {
      "language": "en",
      "languageCode": "en-US"
    },
    {
      "language": "es",
      "languageCode": "es-US"
    }
  ],
  "adsDefaultLanguages": [
    {
      "language": "en",
      "languageCode": "en-US"
    }
  ]
}
```

## Properties

- `name` (string): Country or region name. Read-only.
- `countryCode` (string): Two-letter country code. Read-only.
- `adsSupportedLanguages` ([LocaleInfo]): Supported languages for ads in this country. Read-only.
- `adsDefaultLanguages` ([LocaleInfo]): Default languages for ads in this country. Read-only.

## See Also

- [object AppInfo](appinfo.md)
  A single app search result.
- [object AppLocaleDetails](applocaledetails.md)
  Localized content for an app’s Default Product Page.
- [object AppsSearchResponse](appssearchresponse.md)
  Apps search response envelope.
- [object AppLocaleDetailsQueryResponse](applocaledetailsqueryresponse.md)
  Paginated response object for app locale detail queries.
- [object AppSupportedLanguagesQueryResponse](appsupportedlanguagesqueryresponse.md)
  Paginated response object for the supported app languages query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsupportedlanguages)*