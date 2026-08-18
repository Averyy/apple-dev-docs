# Bulk Create Keywords

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Creates multiple keywords in a single request.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint creates multiple keywords in a single request. Each item in the `items` array contains a `correlationId` and a `data` object with the keyword fields. The `adGroupId` and `text` fields are required per item. You can optionally set `bid` to override the ad group’s default bid.

A single request can create keywords across different ad groups. This makes the endpoint well-suited for seeding a new campaign structure with a full keyword list in one call, rather than creating keywords one ad group at a time.

#### Payload Examples

##### Request

Create three keywords with different match types.

```json
{
 "items": [
   {
     "correlationId": 0,
     "data": {
       "adGroupId": 555666777,
       "text": "photo editor",
       "matchType": "EXACT",
       "bid": {
         "amount": "2.50",
         "currency": "USD"
       }
     }
   },
   {
     "correlationId": 1,
     "data": {
       "adGroupId": 555666777,
       "text": "photo editing app",
       "matchType": "BROAD",
       "bid": {
         "amount": "1.75",
         "currency": "USD"
       }
     }
   },
   {
     "correlationId": 2,
     "data": {
       "adGroupId": 555666777,
       "text": "best photo editor",
       "matchType": "EXACT",
       "bid": {
         "amount": "3.00",
         "currency": "USD"
       }
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
     "operation": "CREATE",
     "success": true,
     "result": {
       "id": 888999000,
       "adAccountId": 123456789,
       "campaignId": 444555666,
       "adGroupId": 555666777,
       "text": "photo editor",
       "matchType": "EXACT",
       "bid": {
         "amount": "2.50",
         "currency": "USD"
       },
       "status": "ENABLED",
       "deleted": false,
       "creationTime": "2025-06-01T10:00:00.000",
       "modificationTime": "2025-06-01T10:00:00.000"
     }
   },
   {
     "correlationId": 1,
     "operation": "CREATE",
     "success": true,
     "result": {
       "id": 888999001,
       "adAccountId": 123456789,
       "campaignId": 444555666,
       "adGroupId": 555666777,
       "text": "photo editing app",
       "matchType": "BROAD",
       "bid": {
         "amount": "1.75",
         "currency": "USD"
       },
       "status": "ENABLED",
       "deleted": false,
       "creationTime": "2025-06-01T10:00:00.000",
       "modificationTime": "2025-06-01T10:00:00.000"
     }
   },
   {
     "correlationId": 2,
     "operation": "CREATE",
     "success": true,
     "result": {
       "id": 888999002,
       "adAccountId": 123456789,
       "campaignId": 444555666,
       "adGroupId": 555666777,
       "text": "best photo editor",
       "matchType": "EXACT",
       "bid": {
         "amount": "3.00",
         "currency": "USD"
       },
       "status": "ENABLED",
       "deleted": false,
       "creationTime": "2025-06-01T10:00:00.000",
       "modificationTime": "2025-06-01T10:00:00.000"
     }
   }
 ]
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/keywords/bulk-create`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Bulk Update Keywords](post-keywords-bulk-update.md)
  Updates multiple keywords in a single request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-keywords-bulk-create)*