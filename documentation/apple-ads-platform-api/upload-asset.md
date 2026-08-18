# Upload Asset

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Upload a binary image file to create a new asset.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint uploads a raw image file and associates it with a promoted object (Brand). The multipart request body must include the binary image file alongside `promotedObjectId` and `promotedObjectType` fields that identify the brand the asset belongs to.

After upload, the asset begins processing. Poll using [`Get Asset`](get-asset-by-id.md) until the `eligibility.status` indicates the asset is ready before referencing it in a creative.

The returned asset has `assetType: IMAGE` and a `providerAssetId` that the provider system assigns.

#### Request Body

Multipart form data (`multipart/form-data`) containing the binary image file and promoted-object metadata.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | binary | Yes | The image file to upload. Accepted formats: PNG, JPG, HEIC. |
| `promotedObjectId` | string | Yes | The identifier of the promoted object (e.g., the brand ID for a `BUSINESS_BRAND`). |
| `promotedObjectType` | string | Yes | The type of the promoted object. Only `BUSINESS_BRAND` is supported. |

##### Post Upload Workflow

1. Poll `GET /v1/assets/{id}` until `eligibility.status` indicates the asset is ready to use.
2. Reference the asset UUID in a `creativeAssets` array when creating a `LOCAL_ADS_SEARCH_CREATIVE`.

#### Payload Examples

##### Request

POST a multipart form including the image file, `promotedObjectId`, and `promotedObjectType`.

```console
curl -X POST https://api.ads.apple.com/v1/assets/upload \
-H "Authorization: Bearer {access_token}" \
-H "X-AP-Context: adAccountId={adAccountId}" \
-F "file=@hero.png;type=image/png" \
-F "promotedObjectId=123456789" \
-F "promotedObjectType=BUSINESS_BRAND"
```

##### Response

```json
{
 "result": {
   "id": "770e8400-e29b-41d4-a716-446655440002",
   "name": "hero.png",
   "assetType": "IMAGE",
   "providerAssetId": "abc123provider001",
   "promotedObjectId": "123456789",
   "promotedObjectType": "BUSINESS_BRAND",
   "providerAssetMetadata": {},
   "assetDetails": {
     "width": 1920,
     "height": 1080,
     "format": "PNG",
     "sizeBytes": 2097152
   },
   "parentAssetId": null,
   "variantIds": [],
   "eligibility": {
     "status": "PENDING",
     "blockedGroups": [],
     "allowedGroups": []
   },
   "creationTime": "2026-06-06T10:00:00.000",
   "modificationTime": "2026-06-06T10:00:00.000"
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/assets/upload`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Assets](query-assets.md)
  Retrieve a paginated list of creative assets using filters and sorting.
- [Get Asset](get-asset-by-id.md)
  Retrieve a single asset by its UUID.
- [Delete Asset](delete-asset-by-id.md)
  Soft-delete an asset by its UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/upload-asset)*