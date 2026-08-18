# ProductPageDetailsResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Response object for a single product page retrieval.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ProductPageDetailsResponse
```

#### Discussion

The [`Get Product Page by ID`](get-product-page-by-id.md) endpoint returns `ProductPageDetailsResponse` as the top-level envelope.

##### Example

```json
{
  "result": {
    "id": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
    "adamId": 123456789,
    "name": "AwayFinder - Holiday Season CPP",
    "state": "PUBLISHED",
    "deepLink": "https://apps.apple.com/us/app/awayfinder/id123456789?ppid=133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
    "creationTime": "2025-04-10T08:00:00.000",
    "modificationTime": "2025-05-01T14:30:00.000"
  }
}
```

## Properties

- `result` (ProductPageDetails): On success, the [`ProductPageDetails`](productpagedetails.md) object for the requested product page. Read-only.
- `error` (Error): Populated only when the request fails. Omitted entirely on success. See [`Error`](error.md).

## See Also

- [object ProductPageDetails](productpagedetails.md)
  Product page metadata for a Default Product Page, Custom Product Page, or Product Page Optimization (PPO) variant.
- [object ProductPageDetailsQueryResponse](productpagedetailsqueryresponse.md)
  Paginated response object for the product page details query.
- [object ProductPageLocaleDetails](productpagelocaledetails.md)
  Locale-specific metadata for an App Store product page.
- [object ProductPageLocaleDetailsQueryResponse](productpagelocaledetailsqueryresponse.md)
  Paginated response object for the product page locale details query.
- [object DeviceAssetGroup](deviceassetgroup.md)
  Represents assets organized by device type with fallback device information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/productpagedetailsresponse)*