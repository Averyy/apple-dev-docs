# Delete Asset

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Soft-delete an asset by its UUID.

**Availability**:
- Apple Ads Platform API 1.0+

## Discussion

This endpoint soft-deletes an asset. You can delete only assets that have been uploaded. The [`Query Assets`](./query-assets.md) excludes deleted assets from results by default, but [`Get Asset`](./get-asset-by-id.md) can still retrieve them with `deleted: true`. Attempting to delete an asset that’s already deleted returns 404.

## Payload Examples

### Request

Soft-deletes an asset. Query results exclude the asset by default, but Get Asset by ID can still retrieve it.

```
DELETE /v1/assets/770e8400-e29b-41d4-a716-446655440002
```

### Response

```json
{
 "result": {}
}
```

## Endpoint

`DELETE https://api.ads.apple.com/v1/assets/{id}`

## Parameters

### Path Parameters

- `id` (uuid) *(required)*

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Responses

- `200` OK (`Response`, `application/json`)
- `400` Bad Request (`Error`, `application/json`)
- `401` Unauthorized (`Error`, `application/json`)
- `403` Forbidden (`Error`, `application/json`)
- `404` Not Found (`Response`, `application/json`)
- `429` Too Many Requests (`Error`, `application/json`)
- `500` Internal Server Error (`Error`, `application/json`)

## See Also

- [Upload Asset](./upload-asset.md)
  Upload a binary image file to create a new asset.
- [Query Assets](./query-assets.md)
  Retrieve a paginated list of creative assets using filters and sorting.
- [Get Asset](./get-asset-by-id.md)
  Retrieve a single asset by its UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-asset-by-id)*