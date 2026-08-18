# Bulk Update Negative Keywords

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Update multiple negative keywords in a single request.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Updates multiple negative keywords in a single API call. The request body contains an `items` array where each item wraps a `BulkNegativeKeywordUpdate` object with a `correlationId`. Each item must include the `id` of the negative keyword to update along with only the fields being changed. Unset fields retain their current values.

When `allowPartialSuccess: true` is set in the request, this endpoint uses partial success semantics: if some items fail validation (for example, an ID that does not exist), the API still applies the successful updates. When omitted or `false`, any single item failure rejects the entire batch. The response includes a per-item result array with each item’s `correlationId`, success status, the updated object, and any error details for failures.

#### Payload Examples

##### Request

Update the status of two negative keywords in a single request.

```json
POST /v1/negative-keywords/bulk-update

{
 "items": [
   {
     "correlationId": 0,
     "data": {
       "id": 777888999,
       "status": "PAUSED"
     }
   },
   {
     "correlationId": 1,
     "data": {
       "id": 777888998,
       "status": "ENABLED"
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
     "operation": "UPDATE",
     "success": true,
     "result": {
       "id": 777888999,
       "adAccountId": 123456789,
       "campaignId": 444555666,
       "text": "free app",
       "matchType": "BROAD",
       "status": "PAUSED",
       "deleted": false,
       "creationTime": "2025-01-10T08:00:00.000",
       "modificationTime": "2025-01-10T09:00:00.000"
     }
   },
   {
     "correlationId": 1,
     "operation": "UPDATE",
     "success": true,
     "result": {
       "id": 777888998,
       "adAccountId": 123456789,
       "campaignId": 444555666,
       "adGroupId": 555666777,
       "text": "cheap downloads",
       "matchType": "EXACT",
       "status": "ENABLED",
       "deleted": false,
       "creationTime": "2025-01-10T08:00:00.000",
       "modificationTime": "2025-01-10T09:00:00.000"
     }
   }
 ]
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/negative-keywords/bulk-update`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Bulk Create Negative Keywords](post-negative-keywords-bulk-create.md)
  Create multiple negative keywords in a single request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-negative-keywords-bulk-update)*