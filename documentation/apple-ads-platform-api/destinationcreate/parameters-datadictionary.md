# DestinationCreate.Parameters

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Destination-specific parameters supplied when creating an ad creative.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object DestinationCreate.Parameters
```

#### Discussion

See [`DestinationParameter`](destinationparameter.md) for the full field reference.

## Properties

- `adamId` (string): The App Store app identifier. This is the `promotedObjectId` on the campaign for App Store campaigns. Required for `APP_STORE_PRODUCT_PAGE` destinations.
- `productPageId` (string): The UUID of a Custom Product Page created in App Store Connect. Omit to use the default product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destinationcreate/parameters-data.dictionary)*