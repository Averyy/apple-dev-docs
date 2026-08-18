# AppsSearchResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Apps search response envelope.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsSearchResponse
```

#### Discussion

The search apps endpoint returns `AppsSearchResponse` as the top-level envelope. It extends the standard [`QueryResponse`](queryresponse.md) envelope. To retrieve additional pages, use `pagination`.

##### Example

```json
{
  "result": [
    {
      "adamId": 123456789,
      "appName": "AwayFinder",
      "developerName": "AwayFinder Inc.",
      "countryOrRegionCodes": [
        "US",
        "GB",
        "CA",
        "AU"
      ]
    },
    {
      "adamId": 123456790,
      "appName": "AwayFinder Pro",
      "developerName": "AwayFinder Inc.",
      "countryOrRegionCodes": [
        "US"
      ]
    }
  ],
  "pagination": {
    "totalCount": 2,
    "offset": 0,
    "pageSize": 2
  }
}
```

## Properties

- `result` ([AppInfo]) *(required)*: Array of apps matching the search criteria. See [`AppInfo`](appinfo.md).
- `pagination` (QueryPaginationResult): Pagination metadata for the current result page. See [`QueryPaginationResult`](querypaginationresult.md).
- `error` (Error): Error details if the request failed. Absent on success. See [`Error`](error.md).

## See Also

- [object AppInfo](appinfo.md)
  A single app search result.
- [object AppLocaleDetails](applocaledetails.md)
  Localized content for an app’s Default Product Page.
- [object AppLocaleDetailsQueryResponse](applocaledetailsqueryresponse.md)
  Paginated response object for app locale detail queries.
- [object AppSupportedLanguages](appsupportedlanguages.md)
  App supported and default languages for an App Store country or region.
- [object AppSupportedLanguagesQueryResponse](appsupportedlanguagesqueryresponse.md)
  Paginated response object for the supported app languages query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appssearchresponse)*