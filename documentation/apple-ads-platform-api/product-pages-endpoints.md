# Product Pages Endpoints

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Retrieve product pages and their localized details.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Product pages are the App Store listings that users land on after tapping an ad. You create and manage them in App Store Connect. The Apple Ads Platform API provides read-only endpoints to discover, retrieve, and inspect them. Product pages serve as the post-tap destination in a [`Creative`](./creative.md) object and determine which app experience users see after they tap your ad.

Use [Search Apps Endpoints](./search-apps-endpoints.md) to find an app’s `adamId` before looking up its product pages, and confirm the app is eligible to advertise with [App Eligibility Endpoints](./app-eligibility-endpoints.md) before building a creative around one of its product pages.

#### Call the Product Pages Endpoints

Use these endpoints to discover, retrieve, and inspect product pages:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/product-pages/query` | [`Query Product Pages`](./query-product-pages.md) retrieves custom product pages (CPPs) available to the authenticated ad account. |
| `GET` | `/v1/product-pages/{productPageId}` | [`Get Product Page by ID`](./get-product-page-by-id.md) retrieves a single custom product page (CPP) by its ID. |
| `POST` | `/v1/product-pages/locale-details/query` | [`Query Product Page Locale Details`](./query-product-page-locale-details.md) retrieves localized metadata for custom product pages. |
| `POST` | `/v1/apps/{adamId}/locale-details/query` | [`Query App Locale Details`](./query-default-product-page-locale-details-by-adam-id.md) retrieves the Default Product Page’s localized metadata for an app by its Adam ID. |

##### Compare the Default with Custom Product Pages

The endpoint you call depends on whether you need the app’s default listing or a specific custom product page:

| Type | How to Fetch |
| --- | --- |
| Default product page (main listing) | Use [`Query App Locale Details`](./query-default-product-page-locale-details-by-adam-id.md) with `adamId` in the path. |
| Custom product pages (CPPs) | Use [`Query Product Page Locale Details`](./query-product-page-locale-details.md) with a `productPageId` filter. |

##### Use the Default Product Page

Every app has exactly one Default Product Page (DPP). It reflects the app’s standard App Store listing: the same screenshots, preview videos, app name, and description that all users see by default. You don’t need any additional setup to use it for advertising.

When creating a creative for a default product page, set `creativeType` to `DEFAULT_PRODUCT_PAGE` and reference the app by its `adamId` in the creative’s `destination` field. To retrieve the DPP’s localized assets for a given app without needing a `productPageId`, use [`Query App Locale Details`](./query-default-product-page-locale-details-by-adam-id.md).

##### Use Custom Product Pages

Custom Product Pages (CPPs) are alternate product pages you configure in App Store Connect with tailored screenshots, preview videos, and promotional text. You design each CPP for a specific audience or campaign goal, showing a different app experience to different users without changing your default listing.

A custom product page has its own `productPageId`, which you use in the creative’s `destination` field alongside the app’s `adamId`. Set `creativeType` to `CUSTOM_PRODUCT_PAGE` when creating a creative for a CPP.

To retrieve product pages available to the authenticated ad account, use [`Query Product Pages`](./query-product-pages.md). This endpoint returns custom product pages only. For the default product page, use [`Query App Locale Details`](./query-default-product-page-locale-details-by-adam-id.md). To fetch a specific page by its `productPageId`, use [`Get Product Page by ID`](./get-product-page-by-id.md).

##### Reference a Product Page in a Creative

Product page creatives use the `destination` field to define the post-tap App Store listing. The `adamId` and `productPageId` belong in `destination.parameters`, not directly on `destination`.

##### Retrieve Locale Details

Each product page has per-locale metadata describing how the app appears for a given App Store country or region and language. Locale details include:

- **`appName`**: The localized app display name as it appears on the App Store.
- **`subTitle`**: The app subtitle for the locale.
- **`promotionalText`**: Up to 170 characters of promotional copy.
- **`deviceClasses`**: Supported device classes (`IPHONE`, `IPAD`) for the locale.
- **`assetsByDevice`**: Screenshots and preview videos organized by device type via [`DeviceAssetGroup`](./deviceassetgroup.md), with fallback devices when assets aren’t available for a given class.

To retrieve locale details for any combination of product pages, App Store countries or regions, and languages in a single request, use [`Query Product Page Locale Details`](./query-product-page-locale-details.md).

## Topics

- [Query Product Pages](./query-product-pages.md)
  Queries App Store product pages available to your account.
- [Get Product Page by ID](./get-product-page-by-id.md)
  Retrieves a specific Custom Product Page (CPP) by its unique UUID.
- [Query Product Page Locale Details](./query-product-page-locale-details.md)
  Queries the localized content of custom product pages (CPPs).
- [Query App Locale Details](./query-default-product-page-locale-details-by-adam-id.md)
  Returns the default product page locale details for an app identified by its adamId.

## See Also

### Related Documentation
- [Search Apps Endpoints](./search-apps-endpoints.md)
  Browse the endpoints for searching apps and retrieving app details.
- [App Eligibility Endpoints](./app-eligibility-endpoints.md)
  Check whether apps qualify to run ads and look up rejection reasons for creatives.
### Product Pages
- [Product Pages Data Objects](./product-pages-data-objects.md)
  Reference the response objects returned by product page endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/product-pages-endpoints)*