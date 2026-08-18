# AppLocaleDetailsQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Paginated response object for app locale detail queries.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppLocaleDetailsQueryResponse
```

#### Discussion

The [`Query App Locale Details`](query-default-product-page-locale-details-by-adam-id.md) endpoint returns `AppLocaleDetailsQueryResponse` as the top-level envelope.

##### Example

```json
{
  "result": [
    {
      "adamId": 123456789,
      "language": "en",
      "languageCode": "en-US",
      "isPrimaryLocale": true,
      "appName": "AwayFinder - Trip Planner",
      "subTitle": "Plan your next getaway",
      "promotionalText": "Get 3 months of Premium free",
      "shortDescription": "Plan, book, and track every trip in one place",
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
            }
          ]
        }
      }
    }
  ],
  "pagination": {
    "pageSize": 20,
    "offset": 0,
    "totalCount": 1
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

- `result` ([AppLocaleDetails]): Array of `AppLocaleDetails` objects, one per supported locale. Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the result set. See fields below. Read-only.
- `error` (Error): Error details if the request failed. Omitted entirely on success. See [`Error`](error.md). Read-only.

## See Also

- [object AppInfo](appinfo.md)
  A single app search result.
- [object AppLocaleDetails](applocaledetails.md)
  Localized content for an app’s Default Product Page.
- [object AppsSearchResponse](appssearchresponse.md)
  Apps search response envelope.
- [object AppSupportedLanguages](appsupportedlanguages.md)
  App supported and default languages for an App Store country or region.
- [object AppSupportedLanguagesQueryResponse](appsupportedlanguagesqueryresponse.md)
  Paginated response object for the supported app languages query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/applocaledetailsqueryresponse)*