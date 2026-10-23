# Update a Budget Order

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Updates mutable fields of an existing budget order by its unique identifier.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint updates one or more mutable fields on an existing budget order. Only include the fields you want to change. Fields you don’t include remain unchanged. Pass the budget order `id` as a URL path parameter. You don’t need to include it in the request body. End date changes on active budget orders can only shorten the period, not extend it, except that you can set `endTime` to `null` to remove the expiration date entirely and make the budget open-ended.

Omit the `X-AP-Context` header. This endpoint requires organization-level permissions, and the API returns `403 Forbidden` if you send an ad account header. See [Budget Orders Endpoints](./budget-orders-endpoints.md).

#### Payload Examples

**Increase Budget**:

##### Request

Increase the total budget order amount on an active budget order.

```http
PUT /v1/shared-budgets/{id}

{
 "value": {
   "amount": "25000.00",
   "currency": "USD"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 777890001,
   "name": "AwayFinder Q3 2025 Budget",
   "startTime": "2025-07-01T00:00:00.000",
   "endTime": "2025-09-30T23:59:59.000",
   "value": {
     "amount": "25000.00",
     "currency": "USD"
   },
   "adAccountIds": [
     123456789
   ],
   "systemStatus": "ACTIVE",
   "systemStatusReasons": [],
   "deleted": false,
   "creationTime": "2025-06-01T10:00:00.000",
   "modificationTime": "2025-07-15T09:30:00.000"
 }
}
```

**Rename and Update Invoice**:

##### Request

Rename the budget order and update the invoice order number.

```http
PUT /v1/shared-budgets/{id}

{
 "name": "AwayFinder Q3+Q4 2025 Budget",
 "invoiceDetail": {
   "orderNumber": "PO-2025-Q3Q4"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 777890001,
   "name": "AwayFinder Q3+Q4 2025 Budget",
   "startTime": "2025-07-01T00:00:00.000",
   "endTime": "2025-09-30T23:59:59.000",
   "value": {
     "amount": "25000.00",
     "currency": "USD"
   },
   "adAccountIds": [
     123456789
   ],
   "systemStatus": "ACTIVE",
   "systemStatusReasons": [],
   "deleted": false,
   "creationTime": "2025-06-01T10:00:00.000",
   "modificationTime": "2025-07-15T09:30:00.000"
 }
}
```

## Endpoint

`PUT https://api.ads.apple.com/v1/shared-budgets/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SharedBudgetUpdate`

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
- [Create a Budget Order](./post-shared-budgets.md)
  Creates a budget order that can be assigned to campaigns within an ad account.
- [Query Budget Orders](./post-shared-budgets-query.md)
  Returns a filtered, sorted, and paginated list of budget orders.
- [Delete a Budget Order](./delete-shared-budgets-_id_.md)
  Soft-deletes a budget order by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/put-shared-budgets-_id_)*