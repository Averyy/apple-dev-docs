# Destination.Parameters

**Framework**: Apple Ads Platform API  
**Kind**: dictionary  
**Role**: Object

Destination-specific parameters for the post-tap experience.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
object Destination.Parameters
```

## Discussion

See [`DestinationParameter`](../destinationparameter.md) for the full field reference.

## Properties

- `adamId` (string): The App Store app identifier. This is the `promotedObjectId` on the campaign for App Store campaigns. Required for `APP_STORE_PRODUCT_PAGE` destinations.
- `productPageId` (string): The UUID of a Custom Product Page created in App Store Connect. Omit to use the default product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destination/parameters-data.dictionary)*