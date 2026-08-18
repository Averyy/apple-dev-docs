# SharedBudgetQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a budget order query.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudgetQueryResponse
```

#### Discussion

The budget order query endpoint returns `SharedBudgetQueryResponse`, which contains the filtered, sorted, and paginated set of `SharedBudget` objects matching the request. The `result` array holds the matching records. To scope results by ad account ID, status, or specific budget IDs, use the `QueryRequest` body with `filters`.

> **Note**: The underlying implementation is the generic `QueryResponse<SharedBudget>` envelope. This documentation uses the type name `SharedBudgetQueryResponse` for clarity.

##### Example

```json
{
  "result": [
    {
      "id": 777890001,
      "name": "AwayFinder - Q3 2025 Budget",
      "startTime": "2025-07-01T00:00:00.000",
      "endTime": "2025-09-30T23:59:59.000",
      "value": {
        "amount": "20000.00",
        "currency": "USD"
      },
      "adAccountIds": [
        123456789
      ],
      "orgId": 555666777,
      "systemStatus": "ACTIVE",
      "systemStatusReasons": [],
      "invoiceDetail": {
        "primaryBuyerName": "Jordan Lee",
        "primaryBuyerEmail": "jordan.lee@awayfinder.com",
        "billingEmail": "billing@awayfinder.com",
        "clientName": "AwayFinder Inc.",
        "orderNumber": "PO-2025-Q3"
      },
      "creationTime": "2025-06-01T10:00:00.000",
      "modificationTime": "2025-06-01T10:00:00.000",
      "deleted": false
    }
  ],
  "pagination": {
    "pageSize": 20,
    "offset": 0,
    "totalCount": 1
  }
}
```

## Properties

- `result` ([SharedBudget]): Array of `SharedBudget` objects matching the query filters. Omitted entirely on failure rather than returned as `null`. Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the result set, including `pageSize` (number of results per page), `offset` (zero-based offset of the first result), and `totalCount` (total number of matching records, only populated when the request sends `fetchTotalCount: true`). Read-only.
- `error` (Error): Error details if the request failed. Omitted entirely on success and never returned as `"error": null`. Only appears when the operation fails. See [`Error`](error.md). Read-only.

## See Also

- [object SharedBudget](sharedbudget.md)
  A budget order.
- [object SharedBudgetCreate](sharedbudgetcreate.md)
  The request body for creating a new budget order.
- [object SharedBudgetUpdate](sharedbudgetupdate.md)
  Request body for updating an existing budget order.
- [object SharedBudgetResponse](sharedbudgetresponse.md)
  The response object for a single budget order operation.
- [object SharedBudgetAssignment](sharedbudgetassignment.md)
  Represents a single budget order assignment within a campaign’s `sharedBudgets` array.
- [object SharedBudgetAssignmentCreate](sharedbudgetassignmentcreate.md)
  Request payload for assigning a campaign to a budget order at campaign creation time.
- [object SharedBudgetAssignmentUpdate](sharedbudgetassignmentupdate.md)
  Request payload for changing or removing a campaign’s budget order assignment.
- [object InvoiceDetail](invoicedetail.md)
  Invoice billing details for accounts on the Line of Credit (LOC) payment model.
- [object InvoiceDetailUpdate](invoicedetailupdate.md)
  The request body for updating the invoice details of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudgetqueryresponse)*