# Get a Budget Order by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieves a single budget order by its ID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves the full details of a specific budget order by its ID. The response includes the budget order’s value, active date range, assigned ad accounts, and invoice details.

#### Payload Examples

##### Request

Retrieves the full details of a specific budget order by its ID.

```None
GET https://api.ads.apple.com/v1/shared-budgets/777888999
```

##### Response

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

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Budget Order](post-shared-budgets.md)
  Creates a budget order that can be assigned to campaigns within an ad account.
- [Query Budget Orders](post-shared-budgets-query.md)
  Returns a filtered, sorted, and paginated list of budget orders.
- [Update a Budget Order](put-shared-budgets-_id_.md)
  Updates mutable fields of an existing budget order by its unique identifier.
- [Delete a Budget Order](delete-shared-budgets-_id_.md)
  Soft-deletes a budget order by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-shared-budgets-_id_)*