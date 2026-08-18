# Create a Budget Order

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Creates a budget order that can be assigned to campaigns within an ad account.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint creates a budget order that campaigns can draw from via `SharedBudgetAssignment`. With a budget order, total spend across all assigned campaigns cannot exceed the budget order’s `value`, providing centralized cost control across a campaign group.

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

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Get a Budget Order by ID](get-shared-budgets-_id_.md)
  Retrieves a single budget order by its ID.
- [Query Budget Orders](post-shared-budgets-query.md)
  Returns a filtered, sorted, and paginated list of budget orders.
- [Update a Budget Order](put-shared-budgets-_id_.md)
  Updates mutable fields of an existing budget order by its unique identifier.
- [Delete a Budget Order](delete-shared-budgets-_id_.md)
  Soft-deletes a budget order by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-shared-budgets)*