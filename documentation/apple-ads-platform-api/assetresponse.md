# AssetResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The Get Asset and Upload Asset endpoints return this response object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AssetResponse
```

#### Discussion

[`Get Asset`](get-asset-by-id.md) and [`Upload Asset`](upload-asset.md) return `AssetResponse` as the top-level envelope. On success, `result` contains the [`Asset`](asset.md) object. On failure, `result` is absent and `error` describes the problem.

##### Example

```json
{
  "result": {
    "id": "770e8400-e29b-41d4-a716-446655440002",
    "name": "awayfinder_hero.png",
    "assetType": "IMAGE",
    "providerAssetId": "abc123-provider-id",
    "promotedObjectId": "987654321",
    "promotedObjectType": "BUSINESS_BRAND",
    "providerAssetMetadata": {},
    "assetDetails": {
      "width": 1920,
      "height": 1080,
      "format": "PNG",
      "sizeBytes": 2097152,
      "orientation": "LANDSCAPE"
    },
    "parentAssetId": null,
    "variantIds": [],
    "creationTime": "2026-03-01T12:00:00.000",
    "modificationTime": "2026-03-01T12:00:00.000",
    "eligibility": {
      "status": "ELIGIBLE",
      "blockedGroups": [],
      "allowedGroups": []
    }
  }
}
```

## Properties

- `result` (Asset): The retrieved asset. Absent if no asset was found. See [`Asset`](asset.md). Read-only.
- `error` (Error): Error details if the request failed. Absent on success. See [`Error`](error.md). Read-only.

## See Also

- [object Asset](asset.md)
  Unified asset entity containing product-agnostic asset metadata and references.
- [object AssetQueryResponse](assetqueryresponse.md)
  Paginated response object for asset queries.
- [object AssetEligibility](asseteligibility.md)
  Eligibility status and constraint details for an asset.
- [object AssetConstraintGroup](assetconstraintgroup.md)
  A constraint group defining the supply placements and countries or regions where an asset is blocked or allowed to serve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/assetresponse)*