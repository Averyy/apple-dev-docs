# Get Asset

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a single asset by its UUID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a single asset by its UUID. Use it after uploading an asset to check its `eligibility` status before referencing it in a creative.

This endpoint still returns deleted assets, with `deleted: true`. Responses always include the `eligibility` field unless excluded via a `fields` projection parameter.

#### Payload Examples

##### Request

Retrieves a single asset by its UUID.

```None
GET https://api.ads.apple.com/v1/assets/770e8400-e29b-41d4-a716-446655440002
```

##### Response

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

## Endpoint

`GET https://api.ads.apple.com/v1/assets/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Upload Asset](upload-asset.md)
  Upload a binary image file to create a new asset.
- [Query Assets](query-assets.md)
  Retrieve a paginated list of creative assets using filters and sorting.
- [Delete Asset](delete-asset-by-id.md)
  Soft-delete an asset by its UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-asset-by-id)*