# DeviceAssetGroup

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Represents assets organized by device type with fallback device information.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object DeviceAssetGroup
```

#### Discussion

`DeviceAssetGroup` is a value type within the `assetsByDevice` map on `ProductPageLocaleDetails` and `AppLocaleDetails`, keyed by specific device type string (e.g., `iphone_6_5`, `iphone_6_7`, `ipadPro`).

##### Example

```json
{
  "assets": [
    {
      "assetId": "550e8400-e29b-41d4-a716-446655440000"
    },
    {
      "assetId": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
    }
  ],
  "appPreviewDeviceFallBackDevices": [
    "iphone6",
    "iphone5"
  ]
}
```

## Properties

- `assets` ([AssetReference]): Ordered list of asset references for this device type. Each item is an `AssetReference` containing an `assetId` UUID. Read-only.
- `appPreviewDeviceFallBackDevices` ([string]): List of fallback device type strings to use if assets are not available for this device (e.g., `["iphone6", "iphone5"]`). Empty array when no fallback applies. Read-only.

## See Also

- [object ProductPageDetails](productpagedetails.md)
  Product page metadata for a Default Product Page, Custom Product Page, or Product Page Optimization (PPO) variant.
- [object ProductPageDetailsResponse](productpagedetailsresponse.md)
  Response object for a single product page retrieval.
- [object ProductPageDetailsQueryResponse](productpagedetailsqueryresponse.md)
  Paginated response object for the product page details query.
- [object ProductPageLocaleDetails](productpagelocaledetails.md)
  Locale-specific metadata for an App Store product page.
- [object ProductPageLocaleDetailsQueryResponse](productpagelocaledetailsqueryresponse.md)
  Paginated response object for the product page locale details query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/deviceassetgroup)*