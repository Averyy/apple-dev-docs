# Bulk Delete Negative Keywords

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Soft-deletes multiple negative keywords in a single request.

**Availability**:
- Apple Ads Platform API 1.0+
- apple-ads-platform-api 1.0+

#### Discussion

Each item in `items` requires a `correlationId`, unique within the batch, and a `data` object with the `id` of the negative keyword to delete. The API processes each deletion independently.

When `allowPartialSuccess: true` is set in the request, this endpoint uses partial success semantics: if some items fail (for example, an already-deleted ID fails with `ENTITY_NOT_FOUND`), the API still processes the successful deletions. When omitted or `false`, any single item failure rejects the entire batch. The response includes a per-item result with each item’s `correlationId` and success status, with failed items reporting `success: false`. It doesn’t include the deleted negative keyword.

Deleted negative keywords are marked `deleted: true` and no longer suppress those search terms for any ad groups or campaigns that referenced them.

#### Payload Examples

##### Request

Delete two negative keywords by ID in a single request. Each item in `items` maps to a result in the response by `correlationId`.

```http
POST /v1/negative-keywords/bulk-delete

{
 "items": [
   {
     "correlationId": 0,
     "data": {
       "id": 777888999
     }
   },
   {
     "correlationId": 1,
     "data": {
       "id": 777888998
     }
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "correlationId": 0,
     "operation": "DELETE",
     "success": true
   },
   {
     "correlationId": 1,
     "operation": "DELETE",
     "success": true
   }
 ]
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/negative-keywords/bulk-delete`

## Parameters

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `NegativeKeywordDeleteBulkRequest`

## Responses

- `200` OK (`NegativeKeywordDeleteBulkResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` Too Many Requests (`ErrorResponse`, `application/json`)
- `500` Internal Server Error (`ErrorResponse`, `application/json`)

## See Also

### Negative Keywords
- [Bulk Create Negative Keywords](./post-negative-keywords-bulk-create.md)
  Create multiple negative keywords in a single request.
- [Bulk Update Negative Keywords](./post-negative-keywords-bulk-update.md)
  Update multiple negative keywords in a single request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-negative-keywords-bulk-delete)*