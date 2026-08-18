# Search Apps Endpoints

**Framework**: Apple Ads Platform API

Browse the endpoints for searching apps and retrieving app details.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Use the Search Apps API to query localized app metadata, find the `adamId` that becomes the `promotedObjectId` on your campaign, and verify `availableStorefronts` before setting campaign target App Store countries or regions.

You can only create campaigns for apps that you own in your ad account. Searching the App Store catalog returns metadata for any public app, but the `adamId` you use as `promotedObjectId` must belong to an app you own. To search only the apps your organization owns, use the `returnOwnedApps` parameter on [`Search for Apps`](searches-for-a-list-of-apps.md).

Confirm an app is eligible to advertise with [`App Eligibility Endpoints`](app-eligibility-endpoints.md) before building a campaign around it, and use [`Product Pages Endpoints`](product-pages-endpoints.md) to discover its product pages for a creative once it’s eligible.

#### Explore the Available Endpoints

The Search Apps API provides three endpoints for finding, validating, and describing apps:

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/v1/search/apps` | Searches the App Store for apps by name, content provider, or returns apps owned by your organization. See [`Search for Apps`](searches-for-a-list-of-apps.md). |
| `GET` | `/v1/apps/{adamId}` | Retrieves details for a single app by its Adam ID. See [`Get App Details by Adam ID`](get-app-details-by-adam-id.md). |
| `POST` | `/v1/metadata/apps/supported-languages/query` | Returns the languages supported for app advertising in each country or region. See [`Query Supported App Languages`](query-supported-app-languages.md). |

To retrieve the default product page’s localized metadata for an Adam ID, see [`Query App Locale Details`](query-default-product-page-locale-details-by-adam-id.md) under [`Product Pages Endpoints`](product-pages-endpoints.md).

#### Review the Fields for App Search Results

Each app returned by the search endpoint includes an `AppInfo` object with the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `adamId` | integer | The app’s Adam ID. Use as `promotedObjectId` when creating a campaign. |
| `appName` | string | The application display name as it appears on the App Store. |
| `developerName` | string | The developer or company name. |
| `countryOrRegionCodes` | array[string] | Country or region codes where the app is available. |

#### Review the Fields for a Single Apps Details

Retrieving a single app by Adam ID returns an `AppDetails` object with the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | The app’s Adam ID. Use as `promotedObjectId` when creating a campaign. |
| `appName` | string | The application display name as it appears on the App Store. |
| `artistName` | string | The developer or company name associated with the app in App Store Connect. |
| `primaryLanguage` | string | The primary language of the app. |
| `primaryGenre` | string | The primary App Store genre category. |
| `secondaryGenre` | string | The secondary App Store genre category, if assigned. |
| `deviceClasses` | array[string] | Supported device classes: `IPHONE`, `IPAD`. |
| `iconPictureUrl` | string (URI) | URL of the app’s icon image. |
| `isPreorder` | boolean | Whether the app is currently available as a pre-order. |
| `availableStorefronts` | array[string] | ISO 3166-1 alpha-2 country codes where the app is available. Use to validate that a campaign’s `countryOrRegion` is a subset of this list. |

## Topics

- [Search for Apps](searches-for-a-list-of-apps.md)
  Search the App Store for apps matching the supplied criteria and return app details.
- [Get App Details by Adam ID](get-app-details-by-adam-id.md)
  Retrieve application details for a specific Adam ID.
- [Query Supported App Languages](query-supported-app-languages.md)
  Query countries and regions to discover the ad-supported languages available in each market.

## See Also

- [App Eligibility Endpoints](app-eligibility-endpoints.md)
  Check whether apps qualify to run ads and look up rejection reasons for creatives.
- [Product Pages Endpoints](product-pages-endpoints.md)
  Retrieve product pages and their localized details.
- [Search Apps Data Objects](search-apps-data-objects.md)
  Browse the response objects returned by the search apps and app details endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/search-apps-endpoints)*