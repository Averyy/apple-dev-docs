# AppSupportedLanguagesQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Paginated response object for the supported app languages query.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppSupportedLanguagesQueryResponse
```

#### Discussion

`AppSupportedLanguagesQueryResponse` is the top-level envelope returned by [`Query Supported App Languages`](query-supported-app-languages.md).

##### Example

```json
{
  "result": [
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
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 100,
    "totalCount": 91
  }
}
```

The `pagination` object contains the following fields:

| Field | Description |
| --- | --- |
| `pageSize` | Number of results per page. |
| `offset` | Zero-based offset of the first result. |
| `totalCount` | Total number of matching records. Only populated when the request sends `fetchTotalCount: true`. |

## Properties

- `result` ([AppSupportedLanguages]): Array of `AppSupportedLanguages` objects, one per market. Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the result set. See fields below. Read-only.
- `error` (Error): Error details if the request failed. Omitted entirely on success. See [`Error`](error.md). Read-only.

## See Also

- [object AppInfo](appinfo.md)
  A single app search result.
- [object AppLocaleDetails](applocaledetails.md)
  Localized content for an app’s Default Product Page.
- [object AppsSearchResponse](appssearchresponse.md)
  Apps search response envelope.
- [object AppLocaleDetailsQueryResponse](applocaledetailsqueryresponse.md)
  Paginated response object for app locale detail queries.
- [object AppSupportedLanguages](appsupportedlanguages.md)
  App supported and default languages for an App Store country or region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsupportedlanguagesqueryresponse)*