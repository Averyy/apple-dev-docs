# Query Budget Orders

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Returns a filtered, sorted, and paginated list of budget orders.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint finds budget orders by name, status, or date range, or retrieves them across an ad account. Narrow and order the result set with `filters`, `sorting`, and `pagination`.

See [`QueryFilterOperator`](queryfilteroperator.md) for the full set of supported comparison operators.

##### Filterable Fields

| Field | Type | Operators | Sortable | Description |
| --- | --- | --- | --- | --- |
| `deleted` | boolean | `EQUALS`, `IN` |  | Whether the budget order has been soft-deleted. |
| `id` | integer | `EQUALS`, `IN` |  | System-assigned unique identifier for the budget order. |
| `name` | string | `EQUALS`, `IN`, `LIKE`, `STARTS_WITH`, `ENDS_WITH` | Yes | The budget order’s display name. |
| `orgId` | integer | `EQUALS` |  | The organization that owns the budget order. |
| `adAccountIds` | array of integers | `EQUALS`, `IN` |  | The ad accounts the budget order is assigned to. |
| `systemStatus` | string (enum) | `EQUALS`, `IN` |  | The budget order’s current status. See [`BudgetSystemStatus`](budgetsystemstatus.md). |
| `systemStatusReasons` | array of strings (enum) | `CONTAINS_ANY`, `CONTAINS_ALL`, `NOT_CONTAINS_ANY`, `NOT_CONTAINS_ALL`, `IS_NULL`, `IS_NOT_NULL` |  | Reasons contributing to the current `systemStatus`. See [`BudgetSystemStatusReason`](budgetsystemstatusreason.md). |
| `startTime` | string (date-time) | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` |  | The budget order’s scheduled start date and time. |
| `endTime` | string (date-time) | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` |  | The budget order’s scheduled end date and time. |
| `creationTime` | string (date-time) | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` |  | Timestamp when the budget order was created. |
| `modificationTime` | string (date-time) | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` |  | Timestamp of the last modification to the budget order. |

The `value` and `invoiceDetail` fields aren’t filterable. The request body is a [`QueryRequest`](queryrequest.md) composed of [`QueryFilter`](queryfilter.md) conditions and [`QuerySort`](querysort.md) directives ([`QuerySortOrder`](querysortorder.md)), controlled by [`QueryPagination`](querypagination.md).

#### Payload Examples

##### Request

Query all active budget orders for an ad account, sorted by name.

```json
{
 "filters": [
   {
     "field": "deleted",
     "operator": "EQUALS",
     "value": false
   }
 ],
 "sorting": [
   {
     "field": "name",
     "order": "ASC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": 777890001,
     "name": "AwayFinder - Q3 2025 Budget",
     "orgId": 555666777,
     "startTime": "2025-07-01T00:00:00.000",
     "endTime": "2025-09-30T23:59:59.000",
     "value": {
       "amount": "20000.00",
       "currency": "USD"
     },
     "adAccountIds": [
       123456789
     ],
     "systemStatus": "ACTIVE",
     "systemStatusReasons": [],
     "invoiceDetail": {
       "orderNumber": "PO-2025-Q3",
       "clientName": "AwayFinder Inc.",
       "billingEmail": "billing@awayfinder.com"
     },
     "deleted": false,
     "creationTime": "2025-06-01T10:00:00.000",
     "modificationTime": "2025-06-01T10:00:00.000"
   },
   {
     "id": 777890002,
     "name": "AwayFinder - Q4 2025 Budget",
     "orgId": 555666777,
     "startTime": "2025-10-01T00:00:00.000",
     "endTime": "2025-12-31T23:59:59.000",
     "value": {
       "amount": "25000.00",
       "currency": "USD"
     },
     "adAccountIds": [
       123456789
     ],
     "systemStatus": "INACTIVE",
     "systemStatusReasons": [
       "SCHEDULE_PENDING"
     ],
     "invoiceDetail": {
       "orderNumber": "PO-2025-Q4",
       "clientName": "AwayFinder Inc.",
       "billingEmail": "billing@awayfinder.com"
     },
     "deleted": false,
     "creationTime": "2025-06-01T10:30:00.000",
     "modificationTime": "2025-06-01T10:30:00.000"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/shared-budgets/query`

## Parameters

- `X-Ap-Context` (string)

## See Also

- [Get a Budget Order by ID](get-shared-budgets-_id_.md)
  Retrieves a single budget order by its ID.
- [Create a Budget Order](post-shared-budgets.md)
  Creates a budget order that can be assigned to campaigns within an ad account.
- [Update a Budget Order](put-shared-budgets-_id_.md)
  Updates mutable fields of an existing budget order by its unique identifier.
- [Delete a Budget Order](delete-shared-budgets-_id_.md)
  Soft-deletes a budget order by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-shared-budgets-query)*