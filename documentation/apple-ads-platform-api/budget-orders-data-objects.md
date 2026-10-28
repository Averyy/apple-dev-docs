# Budget Order Data Objects

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Build budget order and campaign assignment requests, and read budget order and invoice detail responses.

**Availability**:
- Apple Ads Platform API 1.0+

## Overview

A budget order, represented by [`SharedBudget`](./sharedbudget.md), sets a spending cap and an active window. Manage it with [`SharedBudgetCreate`](./sharedbudgetcreate.md) and [`SharedBudgetUpdate`](./sharedbudgetupdate.md), and read it back through [`SharedBudgetResponse`](./sharedbudgetresponse.md) or [`SharedBudgetQueryResponse`](./sharedbudgetqueryresponse.md). Campaigns draw from a budget order through [`SharedBudgetAssignment`](./sharedbudgetassignment.md) entries. Accounts on the Line of Credit payment model also carry billing contacts in [`InvoiceDetail`](./invoicedetail.md).

For the calls that use these objects, see [Budget Orders Endpoints](./budget-orders-endpoints.md).

## Topics

- [object SharedBudget](./sharedbudget.md)
  A budget order.
- [object SharedBudgetCreate](./sharedbudgetcreate.md)
  The request body for creating a new budget order.
- [object SharedBudgetUpdate](./sharedbudgetupdate.md)
  Request body for updating an existing budget order.
- [object SharedBudgetResponse](./sharedbudgetresponse.md)
  The response object for a single budget order operation.
- [object SharedBudgetQueryResponse](./sharedbudgetqueryresponse.md)
  The response object for a budget order query.
- [object SharedBudgetAssignment](./sharedbudgetassignment.md)
  Represents a single budget order assignment within a campaign’s `sharedBudgets` array.
- [object SharedBudgetAssignmentCreate](./sharedbudgetassignmentcreate.md)
  Request payload for assigning a campaign to a budget order at campaign creation time.
- [object SharedBudgetAssignmentUpdate](./sharedbudgetassignmentupdate.md)
  Request payload for changing or removing a campaign’s budget order assignment.
- [object InvoiceDetail](./invoicedetail.md)
  Invoice billing details for accounts on the Line of Credit (LOC) payment model.
- [object InvoiceDetailUpdate](./invoicedetailupdate.md)
  The request body for updating the invoice details of a budget order.

## See Also

### Budget Orders
- [Budget Orders Endpoints](./budget-orders-endpoints.md)
  Create, retrieve, update, and delete budget orders through these endpoints.
- [Budget Order Data Types](./budget-orders-data-types.md)
  Track budget order status, status reasons, and payment model with these enumerated types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/budget-orders-data-objects)*