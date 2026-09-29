# Bulk Delete Keywords

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Soft-deletes multiple keywords in a single request.

**Availability**:
- Apple Ads Platform API 1.0+
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint soft-deletes multiple keywords in a single request. Each item in the `items` array specifies the `id` of a keyword to delete. The system marks deleted keywords `deleted: true`, and they stop serving. The response doesn’t include the deleted keyword, just each item’s success status.

To stop a keyword from serving temporarily, set `status: PAUSED` with the bulk update endpoint instead.

#### Payload Examples

##### Request

Soft-delete two keywords.

```json
{
 "items": [
   {
     "correlationId": 0,
     "data": {
       "id": 888999000
     }
   },
   {
     "correlationId": 1,
     "data": {
       "id": 888999001
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

`POST https://api.ads.apple.com/v1/keywords/bulk-delete`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Bulk Create Keywords](post-keywords-bulk-create.md)
  Creates multiple keywords in a single request.
- [Bulk Update Keywords](post-keywords-bulk-update.md)
  Updates multiple keywords in a single request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-keywords-bulk-delete)*