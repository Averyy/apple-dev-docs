# CreativeType

**Framework**: Apple Ads  
**Kind**: typealias  
**Role**: Type

The type of creative.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
string CreativeType
```

## Possible Values

- `CUSTOM_PRODUCT_PAGE`: You can assign only one custom product page to an [`AdGroup`](./adgroup.md).
- `DEFAULT_PRODUCT_PAGE`: Default product page ads are automatically created for APPSTORE_SEARCH_TAB campaigns when using the Campaign Management API version 5.2 or later.
- `CREATIVE_SET`: See section 4.1 in [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md) for additional details on Creative Sets deprecation.

## Mentions

- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

## See Also

### Data Types
- [type CreativeState](./creativestate.md)
  The system state of the creative.
- [type CreativeStateReason](./creativestatereason.md)
  Reasons the system provides when an ad isn’t running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/creativetype)*