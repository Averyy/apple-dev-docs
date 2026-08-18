# Asset

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Unified asset entity containing product-agnostic asset metadata and references.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Asset
```

#### Discussion

An `Asset` is the unified media entity used across ad placements in the Apple Ads Platform API. Different providers supply assets: App Store Connect images for Apple Ads campaigns, and Maps media for Apple Maps. The `assetType` field determines which sub-object is present in `assetDetails`.

Query endpoint requests support fields marked **Filterable** in the properties as filter criteria. See [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md) for details on constructing queries.

##### Example

```json
{
  "id": "770e8400-e29b-41d4-a716-446655440002",
  "name": "awayfinder_hero.png",
  "assetType": "IMAGE",
  "providerAssetId": "abc123-provider-id",
  "promotedObjectId": "987654321",
  "promotedObjectType": "BUSINESS_BRAND",
  "providerAssetMetadata": {
    "appPreviewDevice": "iphone_6_7",
    "assetGenId": "123456789;en-US;iphone_6_7;1;abc123def"
  },
  "assetDetails": {
    "width": 1920,
    "height": 1080,
    "format": "PNG",
    "sizeBytes": 2097152,
    "orientation": "LANDSCAPE",
    "providerAssetUrl": "https://is5-ssl.mzstatic.com/image/thumb/Purple123/v4/9b/7a/a4/awayfinder_hero.png/2048x2732.png",
    "providerToken": "Purple123/v4/9b/7a/a4/awayfinder_hero.png",
    "checkSum": "a3c2e1d4b5f6",
    "sortPosition": 1,
    "adAccountId": "123456789"
  },
  "parentAssetId": null,
  "variantIds": [],
  "creationTime": "2026-03-01T12:00:00.000",
  "modificationTime": "2026-03-01T12:00:00.000",
  "deleted": false,
  "eligibility": {
    "status": "ELIGIBLE",
    "blockedGroups": [],
    "allowedGroups": []
  }
}
```

## Topics

### Dictionaries
- [object Asset.ProviderAssetMetadata](asset/providerassetmetadata-data.dictionary.md)
  Provider-specific metadata attached to an asset, with keys that vary by provider.

## Properties

- `id` (uuid): Internal asset identifier (UUID). Filterable with `EQUALS`, `IN`.
- `name` (string): User-facing asset name or description. Filterable with `EQUALS`, `IN`, `LIKE`, `LIKE_IGNORE_CASE`, `STARTS_WITH`, `ENDS_WITH`.
- `assetType` (AssetType): The media type of the asset. See [`AssetType`](assettype.md) for details. Filterable with `EQUALS`, `IN`.
- `providerAssetId` (string): Asset identifier assigned by the provider system (e.g., App Store Connect asset ID). Filterable with `EQUALS`, `IN`.
- `promotedObjectId` (string): Identifier of the promoted object (e.g., `adamId` for apps, `brandId` for Maps). Filterable with `EQUALS`.
- `promotedObjectType` (PromotedObjectType): The type of the promoted object. See [`PromotedObjectType`](promotedobjecttype.md) for details. Filterable with `EQUALS`.
- `providerAssetMetadata` (Asset.ProviderAssetMetadata): Provider-specific metadata. Structure varies by provider type. For example, an App Store Connect asset returns keys such as `appPreviewDevice` and `assetGenId`.
- `assetDetails` (AssetImage): Type-specific asset details. When `assetType` is `IMAGE`, contains `AssetImage` properties: `width`, `height`, `format`, `sizeBytes`, `orientation`, `providerAssetUrl` (provider URL for accessing the image), `providerToken` (provider token for referencing the image in provider-specific APIs), `checkSum` (file checksum), `sortPosition` (display order for UI sorting), and `adAccountId` (ad account identifier, present for custom assets). See [`AssetImage`](assetimage.md) for details.
- `parentAssetId` (string): Identifier of the parent asset if this asset is a variant (crop, resize). Null for original assets.
- `variantIds` ([string]): Asset variant identifiers (e.g., different sizes, formats, or localizations).
- `creationTime` (date-time): Asset creation timestamp (ISO-8601 format). Read-only.
- `modificationTime` (date-time): Last modification timestamp (ISO-8601 format). Read-only.
- `deleted` (boolean): Soft delete flag indicating whether the asset has been deleted. Deleted assets are excluded from query results unless an explicit `deleted` filter is supplied. Default: `false`. Read-only.
- `eligibility` (AssetEligibility): Eligibility data. Always returned unless excluded via a `fields` projection parameter. See [`AssetEligibility`](asseteligibility.md) for details. Read-only.

## See Also

- [object AssetResponse](assetresponse.md)
  The Get Asset and Upload Asset endpoints return this response object.
- [object AssetQueryResponse](assetqueryresponse.md)
  Paginated response object for asset queries.
- [object AssetEligibility](asseteligibility.md)
  Eligibility status and constraint details for an asset.
- [object AssetConstraintGroup](assetconstraintgroup.md)
  A constraint group defining the supply placements and countries or regions where an asset is blocked or allowed to serve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/asset)*