# Get Change History Detail

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve field-level before and after values for a single entity change by its detail ID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns the complete field-level change record for a single entity within a transaction. The response contains a `details` array of [`ActivityDetail`](activitydetail.md) objects, each holding a `changes` array of field change objects. Each change object captures the `field` name, `oldValues`, and `newValues` as string arrays. To page through a large `changes` array, use `limit` and `offset`.

What populates `oldValues` and `newValues` depends on the event type that produced the change.

| Event Type | `oldValues` | `newValues` |
| --- | --- | --- |
| `CREATE` | Empty array | Set to values at creation |
| `UPDATE` | Previous field value | Updated field value |
| `DELETE` | Last known value | Typically empty [], but may contain system-managed values (e.g., deletion flag, status, transaction ID) set at delete time. |

#### Payload Examples

**Campaign Update**:

##### Request

Retrieve field-level details for a campaign update that changed two fields in the same transaction: it re-enables `status` and increases `dailyBudget`.

```None
GET https://api.ads.apple.com/v1/change-history/Campaign.444555666.txn_abc123def456
```

##### Response

```json
{
 "dataType": "ChangeDetail",
 "pagination": {
   "offset": 0,
   "pageSize": 1,
   "totalCount": 1
 },
 "result": [
   {
     "transactionId": "txn_abc123def456",
     "detailId": "Campaign.444555666.txn_abc123def456",
     "eventType": "UPDATE",
     "entityType": "Campaign",
     "entityId": "444555666",
     "eventTime": "2025-03-15T14:30:00.000Z",
     "userType": "CUSTOMER_API",
     "modifiedBy": "555666777",
     "entityMetaData": {
       "name": "AwayFinder - Summer App Promo"
     },
     "details": [
       {
         "transactionId": "txn_abc123def456",
         "changes": [
           {
             "field": "status",
             "oldValues": [
               "PAUSED"
             ],
             "newValues": [
               "ENABLED"
             ]
           },
           {
             "field": "dailyBudget",
             "oldValues": [
               "50.00"
             ],
             "newValues": [
               "100.00"
             ]
           }
         ]
       }
     ]
   }
 ]
}
```

**Ad Group Create**:

##### Request

Retrieve field-level details for a new ad group creation. `oldValues` is empty for all fields on `CREATE` events.

```None
GET https://api.ads.apple.com/v1/change-history/AdGroup.888999333.txn_def789ghi012
```

##### Response

```json
{
 "dataType": "ChangeDetail",
 "pagination": {
   "offset": 0,
   "pageSize": 1,
   "totalCount": 1
 },
 "result": [
   {
     "transactionId": "txn_def789ghi012",
     "detailId": "AdGroup.888999333.txn_def789ghi012",
     "eventType": "CREATE",
     "entityType": "AdGroup",
     "entityId": "888999333",
     "eventTime": "2025-03-10T09:15:00.000Z",
     "userType": "CUSTOMER",
     "modifiedBy": "12345678",
     "entityMetaData": {
       "name": "AwayFinder — Broad Match — US",
       "campaignId": "444555777"
     },
     "details": [
       {
         "transactionId": "txn_def789ghi012",
         "changes": [
           {
             "field": "name",
             "oldValues": [],
             "newValues": [
               "AwayFinder — Broad Match — US"
             ]
           },
           {
             "field": "status",
             "oldValues": [],
             "newValues": [
               "ENABLED"
             ]
           },
           {
             "field": "defaultBidAmount",
             "oldValues": [],
             "newValues": [
               "2.50"
             ]
           },
           {
             "field": "campaignId",
             "oldValues": [],
             "newValues": [
               "444555777"
             ]
           }
         ]
       }
     ]
   }
 ]
}
```

**Keyword Delete**:

##### Request

Retrieve field-level details for a deleted keyword. `newValues` is empty for all fields on `DELETE` events.

```None
GET https://api.ads.apple.com/v1/change-history/Keyword.777888999.txn_jkl345mno678
```

##### Response

```json
{
 "dataType": "ChangeDetail",
 "pagination": {
   "offset": 0,
   "pageSize": 1,
   "totalCount": 1
 },
 "result": [
   {
     "transactionId": "txn_jkl345mno678",
     "detailId": "Keyword.777888999.txn_jkl345mno678",
     "eventType": "DELETE",
     "entityType": "Keyword",
     "entityId": "777888999",
     "eventTime": "2025-03-05T11:00:00.000Z",
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432",
     "entityMetaData": {
       "adGroupId": "888999111",
       "campaignId": "444555666"
     },
     "details": [
       {
         "transactionId": "txn_jkl345mno678",
         "changes": [
           {
             "field": "text",
             "oldValues": [
               "fitness tracker"
             ],
             "newValues": []
           },
           {
             "field": "matchType",
             "oldValues": [
               "BROAD"
             ],
             "newValues": []
           },
           {
             "field": "status",
             "oldValues": [
               "ENABLED"
             ],
             "newValues": []
           }
         ]
       }
     ]
   }
 ]
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/change-history/{detailId}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Change History](query-audit-summary-_-grouped-by-transaction.md)
  Query audit summaries grouped by transaction across a specified time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-change-details-by-detailid)*