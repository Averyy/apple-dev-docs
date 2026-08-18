# CreativeCreate.CreativeSpec

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The ad creative spec object matching the ad creative type being created.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CreativeCreate.CreativeSpec
```

#### Discussion

- For `CUSTOM_PRODUCT_PAGE` and `DEFAULT_PRODUCT_PAGE`, pass an empty object (`{}`). Pre-tap content is not customizable for these types.
- For `LOCAL_ADS_SEARCH_CREATIVE`, `creativeSpec` is required and must carry the Apple Maps ad creative spec: - `brandId`: The brand this ad creative belongs to.
- `creativeSubtype`: Asset format, either `BUSINESS_LOGO` or `BUSINESS_ASSET`.
- `creativeAssets`: Array of asset references, each identified by `assetId`, pointing to the image or video content to display.
- `localizedText`: Promotional copy keyed by locale, for example `"en-US": {"promoText": "Visit us today for special offers!"}`.
- `defaultLocale`: The locale whose promo text is used as the fallback when a viewer’s locale isn’t present in `localizedText`.

##### Example

This example shows a `LOCAL_ADS_SEARCH_CREATIVE` creativeSpec using the `BUSINESS_ASSET` subtype with multiple creative assets.

```json
"creativeSpec": {
  "brandId": "1558132598865909760",
  "creativeSubtype": "BUSINESS_ASSET",
  "defaultLocale": "en",
  "localizedText": {
    "en": {
      "promoText": "Visit AwayFinder!"
    }
  },
  "creativeAssets": [
    {
      "assetId": "6442f87b-8956-480f-899d-e825d95cdd46",
      "sortOrder": 0
    },
    {
      "assetId": "23f9ff8f-fdfe-402f-8bef-6a4a73168954",
      "sortOrder": 1
    },
    {
      "assetId": "df9cd75c-a894-4411-85ae-20a06343d09c",
      "sortOrder": 2
    }
  ]
}
```

See [`CreativeCreate.CreativeType`](creativecreate/creativetype-data.typealias.md) for the values that determine which shape applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativecreate/creativespec-data.dictionary)*