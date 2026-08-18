# AuditSummaryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response envelope returned by the Query Change History endpoint, wrapping an array of audit summary rows with pagination metadata.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AuditSummaryResponse
```

#### Discussion

`AuditSummaryResponse` is the response envelope returned by `POST /v1/change-history/query`. The `result` array contains one `AuditSummary` row per unique (`userType`, `modifiedBy`, `transactionId`, `eventType`, `entityType`) combination matching the query filters.

Use `pagination` to navigate large result sets.

##### Example

```json
{
  "dataType": "AuditSummary",
  "result": [
    {
      "transactionId": "txn_abc123def456",
      "eventType": "UPDATE",
      "eventTime": "2025-03-15T14:30:00.000Z",
      "entityType": "Campaign",
      "count": 2,
      "metas": [],
      "userType": "CUSTOMER_API",
      "modifiedBy": "555666777"
    },
    {
      "transactionId": "txn_def789ghi012",
      "eventType": "CREATE",
      "eventTime": "2025-03-10T09:15:00.000Z",
      "entityType": "AdGroup",
      "count": 1,
      "metas": [],
      "userType": "CUSTOMER",
      "modifiedBy": "123456789"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 50,
    "totalCount": 2
  }
}
```

## Properties

- `result` ([AuditSummary]): The array of [`AuditSummary`](auditsummary.md) rows matching the query. Each row represents one transaction grouping. Read-only.
- `pagination` (Pagination): Pagination state for the response. See [`Pagination`](pagination.md). Contains `offset`, `pageSize`, and `totalCount`. `totalCount` is `0` when you set `needTotals` to `"false"` in the request options, which avoids a costly COUNT query. Read-only.
- `error` (ErrorMessage): Present when the request failed. See [`ErrorMessage`](errormessage.md). Contains error details. Read-only.

## See Also

- [object ActivityDetail](activitydetail.md)
  A group of field-level changes that occurred within a single activity context in a change details record.
- [object AuditSummary](auditsummary.md)
  One row in the query change history response, grouping a single actor’s entity changes in one transaction by entity type and event type.
- [object BaseAuditResponse](baseauditresponse.md)
  Common response envelope fields shared by all change history response objects.
- [object ChangeDetails](changedetails.md)
  Field-level change record for a single API entity within a transaction.
- [object ChangeDetailsResponse](changedetailsresponse.md)
  The response envelope returned by the Get Change History Detail endpoint, wrapping an array of change detail records with pagination metadata.
- [object ErrorMessage](errormessage.md)
  Error information returned in a change history response when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditsummaryresponse)*