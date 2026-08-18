# AssetQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Paginated response object for asset queries.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AssetQueryResponse
```

#### Discussion

`AssetQueryResponse` is the top-level envelope returned by [`Query Assets`](query-assets.md). The `pagination` object describes the current page position.

##### Example

```json
{
  "result": [
    {
      "id": "770e8400-e29b-41d4-a716-446655440002",
      "name": "awayfinder_hero.png",
      "assetType": "IMAGE",
      "providerAssetId": "abc123-provider-id",
      "promotedObjectId": "123456789",
      "promotedObjectType": "APPSTORE_APP",
      "providerAssetMetadata": {
        "appPreviewDevice": "iphone_6_7",
        "assetGenId": "123456789;en-US;iphone_6_7;1;abc123def"
      },
      "assetDetails": {
        "width": 1920,
        "height": 1080,
        "format": "PNG",
        "sizeBytes": 2097152,
        "orientation": "LANDSCAPE"
      },
      "parentAssetId": null,
      "variantIds": [],
      "creationTime": "2025-01-10T08:00:00.000",
      "modificationTime": "2025-01-10T08:00:00.000",
      "eligibility": {
        "status": "ELIGIBLE",
        "blockedGroups": [],
        "allowedGroups": []
      }
    }
  ],
  "pagination": {
    "totalCount": 1,
    "offset": 0,
    "pageSize": 20
  }
}
```

## Properties

- `result` ([Asset]): Array of `Asset` objects matching the query filters. See [`Asset`](asset.md). Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the result set, including `pageSize` (number of results per page), `offset` (zero-based offset of the first result), and `totalCount` (total number of matching records, only populated when the request sends `fetchTotalCount: true`). Read-only.
- `error` (Error): Error details if the request failed. Omitted entirely on success. See [`Error`](error.md). Read-only.

## See Also

- [object Asset](asset.md)
  Unified asset entity containing product-agnostic asset metadata and references.
- [object AssetResponse](assetresponse.md)
  The Get Asset and Upload Asset endpoints return this response object.
- [object AssetEligibility](asseteligibility.md)
  Eligibility status and constraint details for an asset.
- [object AssetConstraintGroup](assetconstraintgroup.md)
  A constraint group defining the supply placements and countries or regions where an asset is blocked or allowed to serve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/assetqueryresponse)*