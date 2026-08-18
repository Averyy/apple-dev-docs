# ProductPageDetailsQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Paginated response object for the product page details query.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ProductPageDetailsQueryResponse
```

#### Discussion

`ProductPageDetailsQueryResponse` is the top-level envelope returned by [`Query Product Pages`](query-product-pages.md). The `pagination` object describes the current page position.

##### Example

```json
{
  "result": [
    {
      "id": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
      "adamId": 324684580,
      "name": "AwayFinder Premium Landing",
      "state": "PUBLISHED",
      "deepLink": "awayfinder://campaign/premium",
      "creationTime": "2025-01-10T08:00:00.000",
      "modificationTime": "2025-01-10T08:00:00.000"
    }
  ],
  "pagination": {
    "totalCount": 1,
    "offset": 0,
    "pageSize": 20
  }
}
```

## Properties

- `result` ([ProductPageDetails]): Array of product page details objects. See [`ProductPageDetails`](productpagedetails.md). Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the result set, including `pageSize` (number of results per page), `offset` (zero-based offset of the first result), and `totalCount` (total number of matching records, only populated when the request sends `fetchTotalCount: true`). Read-only.
- `error` (Error): Error details if the request failed. Omitted entirely on success. See [`Error`](error.md). Read-only.

## See Also

- [object ProductPageDetails](productpagedetails.md)
  Product page metadata for a Default Product Page, Custom Product Page, or Product Page Optimization (PPO) variant.
- [object ProductPageDetailsResponse](productpagedetailsresponse.md)
  Response object for a single product page retrieval.
- [object ProductPageLocaleDetails](productpagelocaledetails.md)
  Locale-specific metadata for an App Store product page.
- [object ProductPageLocaleDetailsQueryResponse](productpagelocaledetailsqueryresponse.md)
  Paginated response object for the product page locale details query.
- [object DeviceAssetGroup](deviceassetgroup.md)
  Represents assets organized by device type with fallback device information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/productpagedetailsqueryresponse)*