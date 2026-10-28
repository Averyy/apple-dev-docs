# Get a Budget Order by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieves a single budget order by its ID.

**Availability**:
- Apple Ads Platform API 1.0+

## Discussion

This endpoint retrieves the full details of a specific budget order by its ID. The response includes the budget order’s value, active date range, assigned ad accounts, and invoice details.

Users with organization-level permissions don’t need the `X-AP-Context` header. Users limited to specific ad accounts must send it. See [Budget Orders Endpoints](./budget-orders-endpoints.md).

## Payload Examples

### Request

Retrieves the full details of a specific budget order by its ID.

```
GET /v1/shared-budgets/777888999
```

### Response

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

## Endpoint

`GET https://api.ads.apple.com/v1/shared-budgets/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Header Parameters

- `X-AP-Context` (string)

## Responses

- `200` OK (`SharedBudgetResponse`, `application/json`): Successful operation. Returns [`SharedBudgetResponse`](./sharedbudgetresponse.md) (`result`: [`SharedBudget`](./sharedbudget.md)).
- `400` Bad Request (`ErrorResponse`, `application/json`): Bad Request. Returns [`ErrorResponse`](./errorresponse.md).
- `401` Unauthorized (`ErrorResponse`, `application/json`): Unauthorized.
- `403` Forbidden (`ErrorResponse`, `application/json`): Forbidden. See [Budget Orders Endpoints](./budget-orders-endpoints.md) for `X-AP-Context` requirements.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found. Returns [`ErrorResponse`](./errorresponse.md).
- `429` Too Many Requests (`ErrorResponse`, `application/json`): Rate Limit Exceeded. See [Applying Rate Limits](./rate-limits.md).
- `500` Internal Server Error (`ErrorResponse`, `application/json`): Internal Server Error. Returns [`ErrorResponse`](./errorresponse.md).

## See Also

- [Create a Budget Order](./post-shared-budgets.md)
  Creates a budget order that can be assigned to campaigns within an ad account.
- [Query Budget Orders](./post-shared-budgets-query.md)
  Returns a filtered, sorted, and paginated list of budget orders.
- [Update a Budget Order](./put-shared-budgets-_id_.md)
  Updates mutable fields of an existing budget order by its unique identifier.
- [Delete a Budget Order](./delete-shared-budgets-_id_.md)
  Soft-deletes a budget order by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-shared-budgets-_id_)*