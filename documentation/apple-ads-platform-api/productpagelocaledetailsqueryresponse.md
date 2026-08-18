# ProductPageLocaleDetailsQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Paginated response object for the product page locale details query.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ProductPageLocaleDetailsQueryResponse
```

#### Discussion

`ProductPageLocaleDetailsQueryResponse` is the top-level envelope returned by [`Query Product Page Locale Details`](query-product-page-locale-details.md). The `pagination` object describes the current page position.

##### Example

```json
{
  "result": [
    {
      "productPageId": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
      "adamId": 123456789,
      "language": "en",
      "languageCode": "en-US",
      "appName": "AwayFinder",
      "subTitle": "Get more done every day",
      "promotionalText": "Now with AI-powered scheduling",
      "shortDescription": "The all-in-one task manager for busy professionals.",
      "deviceClasses": [
        "IPHONE",
        "IPAD"
      ],
      "assetsByDevice": {
        "iphone_6_5": {
          "assets": [
            {
              "assetId": "41a91e19-e021-45bb-ac5a-5faec02f9445"
            },
            {
              "assetId": "52b02f2a-f132-56cc-bd6b-6cbfd13c0556"
            }
          ],
          "appPreviewDeviceFallBackDevices": []
        }
      }
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

- `result` ([ProductPageLocaleDetails]): Array of product page locale details objects, one per product page and locale combination. See [`ProductPageLocaleDetails`](productpagelocaledetails.md). Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the result set, including `pageSize` (number of results per page), `offset` (zero-based offset of the first result), and `totalCount` (total number of matching records, only populated when the request sends `fetchTotalCount: true`). Read-only.
- `error` (Error): Error details if the request failed. Omitted entirely on success. See [`Error`](error.md). Read-only.

## See Also

- [object ProductPageDetails](productpagedetails.md)
  Product page metadata for a Default Product Page, Custom Product Page, or Product Page Optimization (PPO) variant.
- [object ProductPageDetailsResponse](productpagedetailsresponse.md)
  Response object for a single product page retrieval.
- [object ProductPageDetailsQueryResponse](productpagedetailsqueryresponse.md)
  Paginated response object for the product page details query.
- [object ProductPageLocaleDetails](productpagelocaledetails.md)
  Locale-specific metadata for an App Store product page.
- [object DeviceAssetGroup](deviceassetgroup.md)
  Represents assets organized by device type with fallback device information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/productpagelocaledetailsqueryresponse)*