# ProductPageDetails

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Product page metadata for a Default Product Page, Custom Product Page, or Product Page Optimization (PPO) variant.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ProductPageDetails
```

#### Discussion

`ProductPageDetails` describes a product page associated with an app. The product page query and get-by-ID endpoints return it. Creative and ad group objects that use a product page destination reference the page by its `productPageId` only, not this full object.

##### Example

```json
{
  "id": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
  "adamId": 324684580,
  "name": "AwayFinder Premium Campaign Landing",
  "state": "PUBLISHED",
  "deepLink": "awayfinder://campaign/premium",
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-12T09:30:00.000"
}
```

## Properties

- `id` (string): Product page identifier. This is the App Store Connect product page UUID. Read-only.
- `adamId` (int64): The App Store app identifier (Adam ID) this product page belongs to.
- `name` (string): The product page name as configured in App Store Connect.
- `state` (string): Product page state. Nullable string with no fixed enum, e.g. `PUBLISHED`. App Store Connect may also surface states such as `READY_FOR_DISTRIBUTION` before a page finishes propagating.
- `deepLink` (uri): Deep link URL for this product page. Only present for product pages with a configured deep link destination.
- `creationTime` (date-time): Timestamp when the product page was created, in ISO 8601 format. Read-only.
- `modificationTime` (date-time): Timestamp when the product page was last modified, in ISO 8601 format. Read-only.

## See Also

- [object ProductPageDetailsResponse](productpagedetailsresponse.md)
  Response object for a single product page retrieval.
- [object ProductPageDetailsQueryResponse](productpagedetailsqueryresponse.md)
  Paginated response object for the product page details query.
- [object ProductPageLocaleDetails](productpagelocaledetails.md)
  Locale-specific metadata for an App Store product page.
- [object ProductPageLocaleDetailsQueryResponse](productpagelocaledetailsqueryresponse.md)
  Paginated response object for the product page locale details query.
- [object DeviceAssetGroup](deviceassetgroup.md)
  Represents assets organized by device type with fallback device information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/productpagedetails)*