# Bulk Delete Negative Keywords

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Delete multiple negative keywords in a single request.

**Availability**:
- Apple Ads Platform API 1.0+
- apple-ads-platform-api 1.0+

#### Discussion

Deletes multiple negative keywords in a single API call. The request body contains an `items` array where each item specifies the `correlationId` and a `data` object with the `id` of the negative keyword to delete. The API processes each deletion independently.

When `allowPartialSuccess: true` is set in the request, this endpoint uses partial success semantics: if some items fail (for example, an ID that does not exist), the API still processes the successful deletions. When omitted or `false`, any single item failure rejects the entire batch. The response includes a per-item result with each item’s `correlationId`, success status, and any error details for failures; it doesn’t include the deleted negative keyword.

Once deleted, the negative keyword no longer suppresses those search terms for any ad groups or campaigns that referenced it.

#### Payload Examples

##### Request

Delete two negative keywords by ID in a single request. Each item in `items` maps to a result in the response by `correlationId`.

```json
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

- `X-Ap-Context` (string) *(required)*

## See Also

- [Bulk Create Negative Keywords](post-negative-keywords-bulk-create.md)
  Create multiple negative keywords in a single request.
- [Bulk Update Negative Keywords](post-negative-keywords-bulk-update.md)
  Update multiple negative keywords in a single request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-negative-keywords-bulk-delete)*