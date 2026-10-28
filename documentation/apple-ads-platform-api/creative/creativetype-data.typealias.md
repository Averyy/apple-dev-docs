# Creative.CreativeType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Type of ad creative, determining which ad placements it can serve on.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Creative.CreativeType
```

## Possible Values

- `CUSTOM_PRODUCT_PAGE`: Uses a custom App Store Connect product page as the pre-tap experience. Requires `productPageId` in the destination.
- `DEFAULT_PRODUCT_PAGE`: Uses the app’s default App Store listing as the pre-tap experience. No `productPageId` required.
- `LOCAL_ADS_SEARCH_CREATIVE`: Ad creative for Ads on Apple Maps.

## Discussion

The `CUSTOM_PRODUCT_PAGE` and `DEFAULT_PRODUCT_PAGE` values are App Store ad creative types. The `LOCAL_ADS_SEARCH_CREATIVE` value is for Ads on Apple Maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creative/creativetype-data.typealias)*