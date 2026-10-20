# Create a Budget Order

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Creates a budget order that can be assigned to campaigns within an ad account.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint creates a budget order that campaigns can draw from via `SharedBudgetAssignment`. With a budget order, total spend across all assigned campaigns can’t exceed the budget order’s `value`, providing centralized cost control across a campaign group.

Omit the `X-AP-Context` header. This endpoint requires organization-level permissions, and the API returns `403 Forbidden` if you send an ad account header. See [Budget Orders Endpoints](./budget-orders-endpoints.md).

#### Payload Examples

##### Request

Creates a $20,000 budget order for Q3 2026, active from July through September.

```json
{
 "name": "AwayFinder - Q3 2026 Budget",
 "startTime": "2026-07-01T00:00:00.000",
 "endTime": "2026-09-30T23:59:59.000",
 "value": {
   "amount": "20000.00",
   "currency": "USD"
 },
 "adAccountIds": [
   123456789
 ],
 "invoiceDetail": {
   "name": "AwayFinder Q3 2026 Invoice",
   "primaryBuyerName": "Jane Smith",
   "primaryBuyerEmail": "jane.smith@awayfinder.com",
   "billingEmail": "billing@awayfinder.com"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 777890001,
   "name": "AwayFinder - Q3 2026 Budget",
   "startTime": "2026-07-01T00:00:00.000",
   "endTime": "2026-09-30T23:59:59.000",
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
     "primaryBuyerName": "Jane Smith",
     "primaryBuyerEmail": "jane.smith@awayfinder.com",
     "billingEmail": "billing@awayfinder.com"
   },
   "deleted": false,
   "creationTime": "2026-06-06T10:00:00.000",
   "modificationTime": "2026-06-06T10:00:00.000"
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/shared-budgets`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SharedBudgetCreate`

## Responses

- `200` OK (`SharedBudgetResponse`, `application/json`): Successful operation. Returns [`SharedBudgetResponse`](./sharedbudgetresponse.md) (`result`: [`SharedBudget`](./sharedbudget.md)).
- `400` Bad Request (`ErrorResponse`, `application/json`): Bad Request. Returns [`ErrorResponse`](./errorresponse.md).
- `401` Unauthorized (`ErrorResponse`, `application/json`): Unauthorized.
- `403` Forbidden (`ErrorResponse`, `application/json`): Forbidden. See [Budget Orders Endpoints](./budget-orders-endpoints.md) for `X-AP-Context` requirements.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found. Returns [`ErrorResponse`](./errorresponse.md).
- `429` Too Many Requests (`ErrorResponse`, `application/json`): Rate Limit Exceeded. See [Applying Rate Limits](./rate-limits.md).
- `500` Internal Server Error (`ErrorResponse`, `application/json`): Internal Server Error. Returns [`ErrorResponse`](./errorresponse.md).

## See Also

- [Get a Budget Order by ID](./get-shared-budgets-_id_.md)
  Retrieves a single budget order by its ID.
- [Query Budget Orders](./post-shared-budgets-query.md)
  Returns a filtered, sorted, and paginated list of budget orders.
- [Update a Budget Order](./put-shared-budgets-_id_.md)
  Updates mutable fields of an existing budget order by its unique identifier.
- [Delete a Budget Order](./delete-shared-budgets-_id_.md)
  Soft-deletes a budget order by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-shared-budgets)*