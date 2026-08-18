# Query Assets

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a paginated list of creative assets using filters and sorting.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint queries assets using a standard `QueryRequest` body. Filter by `promotedObjectId` to retrieve all assets for a specific brand. An empty request body returns all assets with default pagination.

After uploading an asset, use this endpoint to check `eligibility` status in bulk rather than polling each asset individually.

#### Request Body

See [`QueryRequest`](queryrequest.md).

Narrow results using any of the following fields and operators:

| Field | Operators | Description |
| --- | --- | --- |
| `promotedObjectId` | `EQUALS` | Scope to a specific brand or app. |
| `promotedObjectType` | `EQUALS` | Filter by type: `BUSINESS_BRAND` or `APPSTORE_APP`. |
| `providerAssetId` | `EQUALS`, `IN` | Filter by the provider-assigned asset identifier. |
| `assetType` | `EQUALS`, `IN` | Filter by asset type: `IMAGE`. |

Querying assets carries a couple of caveats around scope and variants:

| Constraint | Detail |
| --- | --- |
| Always filter by `promotedObjectId` | Omitting this returns assets across all brands, which may be a large result set. |
| Asset crops not included in query results | Variant assets (crops) are omitted from query responses. To retrieve a specific variant, use Get Asset by ID. |

#### Payload Examples

**Query by Brand**:

Retrieve all assets for a specific brand.

##### Request

```json
{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": "9151314442816847872"
   },
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": "BUSINESS_BRAND"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": "770e8400-e29b-41d4-a716-446655440002",
     "name": "awayfinder_hero.png",
     "assetType": "IMAGE",
     "providerAssetId": "abc123-provider-id",
     "promotedObjectId": "9151314442816847872",
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
     "creationTime": "2026-01-10T08:00:00.000",
     "modificationTime": "2026-01-10T08:00:00.000",
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

**Query App Ads Assets**:

Retrieve assets for a specific App Store app by its Adam ID.

##### Request

```json
{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": "123456789"
   },
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": "APPSTORE_APP"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": "990e8400-e29b-41d4-a716-446655440004",
     "name": "AwayFinder Screenshot 1",
     "assetType": "IMAGE",
     "providerAssetId": "987654321-screenshot-1",
     "promotedObjectId": "123456789",
     "promotedObjectType": "APPSTORE_APP",
     "providerAssetMetadata": {
       "appPreviewDevice": "iphone_6_7",
       "assetGenId": "123456789;en-US;iphone_6_7;1;abc123def"
     },
     "assetDetails": {
       "width": 1284,
       "height": 2778,
       "format": "PNG",
       "sizeBytes": 2456789,
       "orientation": "PORTRAIT"
     },
     "parentAssetId": null,
     "variantIds": [],
     "creationTime": "2026-03-01T08:00:00.000",
     "modificationTime": "2026-03-01T08:00:00.000",
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

## Endpoint

`POST https://api.ads.apple.com/v1/assets/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Upload Asset](upload-asset.md)
  Upload a binary image file to create a new asset.
- [Get Asset](get-asset-by-id.md)
  Retrieve a single asset by its UUID.
- [Delete Asset](delete-asset-by-id.md)
  Soft-delete an asset by its UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-assets)*