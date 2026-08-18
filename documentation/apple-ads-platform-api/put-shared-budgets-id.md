# Update a Budget Order

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Updates mutable fields of an existing budget order by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint updates one or more mutable fields on an existing budget order. Only include the fields you want to change. Fields you don’t include remain unchanged. Pass the budget order `id` as a URL path parameter. You don’t need to include it in the request body. End date changes on active budget orders can only shorten the period, not extend it, except that you can set `endTime` to `null` to remove the expiration date entirely and make the budget open-ended.

#### Payload Examples

**Increase Budget**:

##### Request

Increase the total budget order amount on an active budget order.

```json
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

```json
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

- `X-Ap-Context` (string) *(required)*

## See Also

- [Get a Budget Order by ID](get-shared-budgets-_id_.md)
  Retrieves a single budget order by its ID.
- [Create a Budget Order](post-shared-budgets.md)
  Creates a budget order that can be assigned to campaigns within an ad account.
- [Query Budget Orders](post-shared-budgets-query.md)
  Returns a filtered, sorted, and paginated list of budget orders.
- [Delete a Budget Order](delete-shared-budgets-_id_.md)
  Soft-deletes a budget order by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/put-shared-budgets-_id_)*