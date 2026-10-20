# CreativeStateReason

**Framework**: Apple Ads  
**Kind**: typealias  
**Role**: Type

Reasons the system provides when an ad isn’t running.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
string CreativeStateReason
```

## Possible Values

- `ASSET_DELETED`: The creative asset was deleted from [App Store Connect](https://appstoreconnect.apple.com).
- `CREATIVE_SET_UNSUPPORTED`: See section 4.1 in [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md) for additional details.
- `PRODUCT_PAGE_DELETED`: The product page was deleted from [App Store Connect](https://appstoreconnect.apple.com).
- `PRODUCT_PAGE_HIDDEN`: The product page is hidden on [App Store Connect](https://appstoreconnect.apple.com).

## See Also

### Data Types
- [type CreativeType](./creativetype.md)
  The type of creative.
- [type CreativeState](./creativestate.md)
  The system state of the creative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/creativestatereason)*