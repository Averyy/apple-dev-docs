# Asset.ProviderAssetMetadata

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Provider-specific metadata attached to an asset, with keys that vary by provider.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Asset.ProviderAssetMetadata
```

#### Discussion

`providerAssetMetadata` depends on the asset’s source provider and has no fixed shape. For Apple Maps (`BUSINESS_BRAND`) assets uploaded through this API, `providerAssetMetadata` is currently empty (`{}`). The App Store Connect keys shown below (`appPreviewDevice`, `assetGenId`) illustrate the field’s shape for assets sourced from that provider and don’t apply to Maps assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/asset/providerassetmetadata-data.dictionary)*