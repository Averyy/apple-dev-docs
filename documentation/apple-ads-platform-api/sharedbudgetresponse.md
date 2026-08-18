# SharedBudgetResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a single budget order operation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudgetResponse
```

#### Discussion

Create, update, and get-by-ID budget order operations return `SharedBudgetResponse` as the single-item response envelope.

##### Example

```json
{
  "result": {
    "id": 777888999,
    "orgId": 100456789,
    "name": "AwayFinder - Q1 2025 Budget",
    "startTime": "2025-01-01T00:00:00.000",
    "endTime": "2025-03-31T23:59:59.000",
    "value": {
      "amount": "10000.00",
      "currency": "USD"
    },
    "adAccountIds": [
      123456789
    ],
    "systemStatus": "ACTIVE",
    "systemStatusReasons": [],
    "invoiceDetail": {
      "primaryBuyerName": "Jane Smith",
      "primaryBuyerEmail": "jane.smith@awayfinder.com",
      "billingEmail": "billing@awayfinder.com"
    },
    "deleted": false,
    "creationTime": "2025-01-01T00:00:00.000",
    "modificationTime": "2025-01-01T00:00:00.000"
  }
}
```

## Properties

- `result` (SharedBudget): The `SharedBudget` object returned by the operation, reflecting its post-operation state. Absent if an error occurred. See [`SharedBudget`](sharedbudget.md). Read-only.
- `error` (Error): Error details if the operation failed. Absent on success. Read-only.

## See Also

- [object SharedBudget](sharedbudget.md)
  A budget order.
- [object SharedBudgetCreate](sharedbudgetcreate.md)
  The request body for creating a new budget order.
- [object SharedBudgetUpdate](sharedbudgetupdate.md)
  Request body for updating an existing budget order.
- [object SharedBudgetQueryResponse](sharedbudgetqueryresponse.md)
  The response object for a budget order query.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudgetresponse)*