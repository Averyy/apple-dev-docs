# Delete Asset

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Soft-delete an asset by its UUID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint soft-deletes an asset. You can delete only assets that have been uploaded. [`Query Assets`](query-assets.md) excludes deleted assets from results by default, but [`Get Asset`](get-asset-by-id.md) can still retrieve them with `deleted: true`. Attempting to delete an asset that is already deleted returns 404.

#### Payload Examples

##### Request

Soft-deletes an asset. Query results exclude the asset by default, but Get Asset by ID can still retrieve it.

```None
DELETE https://api.ads.apple.com/v1/assets/770e8400-e29b-41d4-a716-446655440002
```

##### Response

```json
{
 "result": {}
}
```

## Endpoint

`DELETE https://api.ads.apple.com/v1/assets/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Upload Asset](upload-asset.md)
  Upload a binary image file to create a new asset.
- [Query Assets](query-assets.md)
  Retrieve a paginated list of creative assets using filters and sorting.
- [Get Asset](get-asset-by-id.md)
  Retrieve a single asset by its UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-asset-by-id)*