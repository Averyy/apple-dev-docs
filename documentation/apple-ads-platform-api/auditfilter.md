# AuditFilter

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single filter condition in an audit query request, specifying the field to filter on, the comparison operator, and one or more values to match against.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AuditFilter
```

#### Discussion

`AuditFilter` is the building block for narrowing change history query results. Each filter targets a single field and applies the specified operator against the provided values. The system combines multiple filters in the same request with logical AND.

Every `AuditQuery` request requires an `eventTime` filter:

```json
{ "field": "eventTime", "operator": "BETWEEN", "value": ["2025-03-01", "2025-03-31"] }
{ "field": "eventTime", "operator": "GREATER_THAN", "value": "2025-03-01T00:00:00.000Z" }
{ "field": "eventTime", "operator": "LESS_THAN", "value": "2025-03-31T23:59:59.999Z" }
```

Use `IN` for categorical filters:

```json
{ "field": "entityType", "operator": "IN", "value": ["Campaign", "AdGroup"] }
{ "field": "eventType", "operator": "IN", "value": ["UPDATE"] }
{ "field": "userType", "operator": "IN", "value": ["CUSTOMER_API"] }
```

Each field accepts only certain operators and value formats, summarized below.

| Field | Operator | Accepted Values |
| --- | --- | --- |
| `eventTime` | `BETWEEN`, `GREATER_THAN`, `LESS_THAN` | ISO 8601 timestamps. Maximum lookback is 6 months. `BETWEEN` requires two values. `GREATER_THAN` and `LESS_THAN` each take a single timestamp. |
| `entityType` | `IN` | Not a closed enum. A string matching the name of the API entity that changed, such as `Campaign`, `AdGroup`, `Keyword`, `NegativeKeyword`, `Ad`, `Creative`, `AdAccount`, `Org`, or `LocationGroup`. See [`Change History Endpoints`](change-history-endpoints.md) for the entity types this endpoint reports on. |
| `entityId` | `EQUALS`, `IN` | Entity ID string(s). Identifies the specific entity that changed. |
| `eventType` | `IN` | `CREATE`, `UPDATE`, `DELETE` |
| `userType` | `IN` | `CUSTOMER`, `CUSTOMER_API`, `APPLE_SUPPORT` |
| `userId` | `EQUALS`, `IN` | User ID string(s). |
| `txnId` | `EQUALS`, `IN` | Transaction ID string(s). Matches `transactionId` in `AuditSummary` response rows. |
| `adAccountId` | `EQUALS`, `IN` | Ad account ID string(s). Available when `entityType` is `Campaign` or `AdGroup`. |
| `campaignId` | `EQUALS`, `IN` | Campaign ID string(s). Available when `entityType` is `AdGroup`, `Keyword`, or `NegativeKeyword`. |
| `adGroupId` | `EQUALS`, `IN` | Ad group ID string(s). Available when `entityType` is `Keyword` or `NegativeKeyword`. |

##### Example

```json
{
  "field": "campaignId",
  "operator": "IN",
  "value": ["123456789", "987654321"]
}
```

## Topics

### Dictionaries
- [object AuditFilter.Value](auditfilter/value-data.dictionary.md)
  One or more filter values, provided as a string or array of strings.

## Properties

- `field` (string): The name of the field to filter on. Standard event fields always available: `eventTime`, `entityType`, `entityId`, `userId`, `userType`, `txnId`. Parent identifier fields vary by `entityType`: `adAccountId` (for `Campaign`, `AdGroup`), `campaignId` (for `AdGroup`, `Keyword`, `NegativeKeyword`), `adGroupId` (for `Keyword`, `NegativeKeyword`). For non-time fields, the API supports only `EQUALS` and `IN`. It reserves `GREATER_THAN`, `LESS_THAN`, and `BETWEEN` for `eventTime`.
- `operator` (AuditOperator): The comparison operator to apply. See [`AuditOperator`](auditoperator.md). For most fields use `IN`. For `eventTime` use `BETWEEN` for a bounded range, or `GREATER_THAN`/`LESS_THAN` for an open-ended range.
- `value` (AuditFilter.Value): One or more filter values as strings. See [`AuditFilter.Value`](auditfilter/value-data.dictionary.md). For `BETWEEN`, provide exactly two values representing the inclusive lower and upper bounds.

## See Also

- [object AuditQuery](auditquery.md)
  Request body for the Query Change History endpoint.
- [object AuditSorting](auditsorting.md)
  A sort directive in an audit query request, specifying a field to sort by and the direction.
- [object Pagination](pagination.md)
  Pagination state in change history list responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditfilter)*