# Query Change History

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query audit summaries grouped by transaction across a specified time range.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns one `AuditSummary` row per (`userType`, `modifiedBy`, `transactionId`, `eventType`, `entityType`) combination. The `count` field on each row indicates how many individual field changes that transaction group contains.

To fetch field-level details via `GET /v1/change-history/{detailId}`, you need a composite `detailId` in the form `EntityType.entityId.txnId`. A summary row alone doesn’t include `entityId`, so set `options.metadata` to `latest` or `snapshot` on the query request: each resulting row’s `metas` array then includes a ready-to-use `detailId` you can pass directly to the detail endpoint.

#### Request Body

##### Filters

The following fields support filtering. For non-time fields, the API supports only `EQUALS` and `IN`. It reserves `GREATER_THAN`, `LESS_THAN`, and `BETWEEN` for `eventTime`.

| Field | Operators | Notes |
| --- | --- | --- |
| `eventTime` | `BETWEEN`, `GREATER_THAN`, `LESS_THAN` | **Required.** ISO 8601 date strings. Maximum lookback is 6 months. `BETWEEN` requires two values. `GREATER_THAN` and `LESS_THAN` take one. |
| `entityType` | `IN` | Not a closed enum. A string matching the name of the API entity that changed, such as `Campaign`, `AdGroup`, `Keyword`, `NegativeKeyword`, `Ad`, `Creative`, `AdAccount`, `Org`, or `LocationGroup`. See [`Change History Endpoints`](change-history-endpoints.md) for the entity types this endpoint reports on. |
| `entityId` | `EQUALS`, `IN` | The specific entity that changed. |
| `eventType` | `IN` | `CREATE`, `UPDATE`, `DELETE` |
| `userType` | `IN` | `CUSTOMER`, `CUSTOMER_API`, `APPLE_SUPPORT` |
| `userId` | `EQUALS`, `IN` | The user who made the change. |
| `txnId` | `EQUALS`, `IN` | Transaction ID. Matches `transactionId` in response rows. |
| `adAccountId` | `EQUALS`, `IN` | Available when `entityType` is `Campaign` or `AdGroup`. |
| `campaignId` | `EQUALS`, `IN` | Available when `entityType` is `AdGroup`, `Keyword`, or `NegativeKeyword`. |
| `adGroupId` | `EQUALS`, `IN` | Available when `entityType` is `Keyword` or `NegativeKeyword`. |

##### Sorting

Sort by any filterable field using `field` and `order` (`ASC` or `DESC`). Default sort is by `eventTime` descending.

The `options` object controls response performance and metadata behavior.

| Option | Values | Default | Description |
| --- | --- | --- | --- |
| `needTotals` | `"true"`, `"false"` | `"true"` | Include total row count in the response pagination object. Set to `"false"` to skip the COUNT query for faster responses on large datasets. |
| `timeZone` | `"UTC"`, `"ORTZ"` | `"UTC"` | Timezone for `eventTime` filter values. `ORTZ` converts filter values from the org’s configured timezone to UTC server-side. |
| `metadata` | `"none"`, `"latest"`, `"snapshot"` | `"none"` | Controls entity metadata in change detail responses. `"none"` returns no metadata. `"latest"` joins current entity metadata. `"snapshot"` uses metadata captured at the time of the event. |

#### Payload Examples

**Filter by Entity Type**:

Query campaign changes within a two-week window, sorted by most recent first.

##### Request

```json
{
 "filters": [
   {
     "field": "eventTime",
     "operator": "BETWEEN",
     "value": [
       "2025-03-01",
       "2025-03-15"
     ]
   },
   {
     "field": "entityType",
     "operator": "IN",
     "value": [
       "Campaign"
     ]
   }
 ],
 "sorting": [
   {
     "field": "eventTime",
     "order": "DESC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 50
 },
 "options": {
   "needTotals": "true"
 }
}
```

##### Response

```json
{
 "dataType": "AuditSummary",
 "pagination": {
   "offset": 0,
   "pageSize": 50,
   "totalCount": 3
 },
 "result": [
   {
     "transactionId": "txn_abc123def456",
     "eventType": "UPDATE",
     "eventTime": "2025-03-15T14:30:00.000Z",
     "entityType": "Campaign",
     "count": 2,
     "metas": [],
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432"
   },
   {
     "transactionId": "txn_def789ghi012",
     "eventType": "CREATE",
     "eventTime": "2025-03-10T09:15:00.000Z",
     "entityType": "Campaign",
     "count": 1,
     "metas": [],
     "userType": "CUSTOMER",
     "modifiedBy": "12345678"
   },
   {
     "transactionId": "txn_jkl345mno678",
     "eventType": "DELETE",
     "eventTime": "2025-03-05T11:00:00.000Z",
     "entityType": "Campaign",
     "count": 1,
     "metas": [],
     "userType": "CUSTOMER",
     "modifiedBy": "11223344"
   }
 ]
}
```

**Filter by Event Type**:

Query all entity updates (no creations or deletions) over a 30-day window.

##### Request

```json
{
 "filters": [
   {
     "field": "eventTime",
     "operator": "BETWEEN",
     "value": [
       "2025-02-01",
       "2025-03-01"
     ]
   },
   {
     "field": "eventType",
     "operator": "IN",
     "value": [
       "UPDATE"
     ]
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 100
 },
 "options": {
   "needTotals": "false"
 }
}
```

##### Response

```json
{
 "dataType": "AuditSummary",
 "pagination": {
   "offset": 0,
   "pageSize": 100,
   "totalCount": 0
 },
 "result": [
   {
     "transactionId": "txn_pqr901stu234",
     "eventType": "UPDATE",
     "eventTime": "2025-02-20T16:45:00.000Z",
     "entityType": "AdGroup",
     "count": 3,
     "metas": [],
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432"
   },
   {
     "transactionId": "txn_vwx567yza890",
     "eventType": "UPDATE",
     "eventTime": "2025-02-14T10:20:00.000Z",
     "entityType": "Keyword",
     "count": 5,
     "metas": [],
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432"
   }
 ]
}
```

**Filter by User Type**:

Audit all changes made via the API (`CUSTOMER_API`) across all entity types for a single day.

##### Request

```json
{
 "filters": [
   {
     "field": "eventTime",
     "operator": "BETWEEN",
     "value": [
       "2025-03-15",
       "2025-03-16"
     ]
   },
   {
     "field": "userType",
     "operator": "IN",
     "value": [
       "CUSTOMER_API"
     ]
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 100
 },
 "options": {
   "needTotals": "true",
   "timeZone": "ORTZ"
 }
}
```

##### Response

```json
{
 "dataType": "AuditSummary",
 "pagination": {
   "offset": 0,
   "pageSize": 100,
   "totalCount": 4
 },
 "result": [
   {
     "transactionId": "txn_abc123def456",
     "eventType": "UPDATE",
     "eventTime": "2025-03-15T22:30:00.000Z",
     "entityType": "Campaign",
     "count": 2,
     "metas": [],
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432"
   },
   {
     "transactionId": "txn_bcd234efg567",
     "eventType": "CREATE",
     "eventTime": "2025-03-15T18:10:00.000Z",
     "entityType": "Keyword",
     "count": 12,
     "metas": [],
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432"
   },
   {
     "transactionId": "txn_cde345fgh678",
     "eventType": "UPDATE",
     "eventTime": "2025-03-15T14:05:00.000Z",
     "entityType": "AdGroup",
     "count": 1,
     "metas": [],
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432"
   },
   {
     "transactionId": "txn_def456ghi789",
     "eventType": "DELETE",
     "eventTime": "2025-03-15T09:00:00.000Z",
     "entityType": "Ad",
     "count": 1,
     "metas": [],
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432"
   }
 ]
}
```

**With Metadata**:

Query keyword changes with `options.metadata` set to `latest`, returning per-entity metadata entries in `metas`.

##### Request

```json
{
 "filters": [
   {
     "field": "eventTime",
     "operator": "BETWEEN",
     "value": [
       "2025-03-15",
       "2025-03-16"
     ]
   },
   {
     "field": "entityType",
     "operator": "IN",
     "value": [
       "Keyword"
     ]
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 50
 },
 "options": {
   "needTotals": "true",
   "metadata": "latest"
 }
}
```

##### Response

```json
{
 "dataType": "AuditSummary",
 "pagination": {
   "offset": 0,
   "pageSize": 50,
   "totalCount": 1
 },
 "result": [
   {
     "transactionId": "0eee6ae3-69c8-4162-bad6-1d9ee5a3f29b",
     "eventType": "CREATE",
     "eventTime": "2025-03-15T18:10:00.000Z",
     "entityType": "Keyword",
     "count": 2,
     "metas": [
       {
         "Keyword": "2278500001",
         "detailId": "Keyword.2278500001.0eee6ae3-69c8-4162-bad6-1d9ee5a3f29b",
         "meta": {
           "text": "investment app",
           "status": "ENABLED",
           "deleted": false,
           "adGroupId": "2147067585",
           "bidAmount": 5.0,
           "keywordId": "2278500001",
           "matchType": "BROAD",
           "campaignId": "2143534060",
           "adAccountId": "7719420",
           "normalizedText": "INVESTMENT APP"
         }
       },
       {
         "Keyword": "2278502253",
         "detailId": "Keyword.2278502253.0eee6ae3-69c8-4162-bad6-1d9ee5a3f29b",
         "meta": {
           "text": "ai investing",
           "status": "ENABLED",
           "deleted": false,
           "adGroupId": "2147067585",
           "bidAmount": 5.0,
           "keywordId": "2278502253",
           "matchType": "BROAD",
           "campaignId": "2143534060",
           "adAccountId": "7719420",
           "normalizedText": "AI INVESTING"
         }
       }
     ],
     "userType": "CUSTOMER_API",
     "modifiedBy": "98765432"
   }
 ]
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/change-history/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

An [`AuditQuery`](auditquery.md) object specifying filter fields, sorting, pagination, and options. Every request requires a time-range filter on `eventTime`. Use `BETWEEN` for a bounded range or `GREATER_THAN`/`LESS_THAN` for an open-ended range.

## See Also

- [Get Change History Detail](get-change-details-by-detailid.md)
  Retrieve field-level before and after values for a single entity change by its detail ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-audit-summary-_-grouped-by-transaction)*