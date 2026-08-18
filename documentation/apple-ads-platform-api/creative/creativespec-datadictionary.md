# Creative.CreativeSpec

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Pre-tap ad experience specification with customizable attributes and assets.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Creative.CreativeSpec
```

#### Discussion

Empty for Product Page ad creatives (`CUSTOM_PRODUCT_PAGE`, `DEFAULT_PRODUCT_PAGE`) since pre-tap content isn’t customizable for these types. For `LOCAL_ADS_SEARCH_CREATIVE`, `creativeSpec` carries the Apple Maps ad creative spec:

| Property | Type | Description |
| --- | --- | --- |
| `brandId` | String | Brand identifier for the ad creative on Apple Maps. |
| `creativeSubtype` | Enum (`BUSINESS_LOGO`, `BUSINESS_ASSET`) | Sub-type classification for the creative. |
| `creativeAssets` | Array of asset references | Ordered list of asset references for this creative, each identified by `assetId`. |
| `localizedText` | Map of locale to map of text key to string | Localized ad copy by locale key, then by text key (e.g., `headline`, `body`). |
| `defaultLocale` | String | Default locale used alongside `localizedText`. |

See [`CreativeCreate.CreativeSpec`](creativecreate/creativespec-data.dictionary.md) for a create-time example.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creative/creativespec-data.dictionary)*