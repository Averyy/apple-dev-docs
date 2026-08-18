# Delete a Budget Order

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Soft-deletes a budget order by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint soft-deletes the specified budget order. The system marks the record `deleted: true`, and it’s no longer available for assignment to campaigns. You must remove all campaign assignments before you can delete a budget order.

##### Check Deletion Restrictions

Deletion returns a `400 Bad Request` in the following cases:

- The budget order has been canceled (status reason `CANCELED`).
- The budget order has completed or expired (status reason `SCHEDULE_EXPIRED`).
- The budget order is exhausted (status reason `EXHAUSTED`).
- The budget order has already started (start time is in the past).
- The budget order has campaigns currently assigned to it. Remove all campaign assignments first.

Deleting an already-deleted budget order returns a `404 Not Found`.

Deletion has different implications depending on what you’re trying to do next:

| Scenario | Behavior |
| --- | --- |
| Campaign assignments | You must remove them before deletion is allowed. A budget order with active campaign assignments cannot be deleted. |
| Querying deleted budget orders | Include `deleted: EQUALS: true` in query filters to return deleted budget orders. |
| Restoration | The API cannot restore soft-deleted budget orders. |
| Re-creation | Create a new budget order with the same name and parameters if needed. |

#### Payload Examples

##### Request

Deletes a budget order by its unique identifier. Remove all campaign assignments before issuing this request. A successful delete returns HTTP 200 with an empty response body.

```None
DELETE https://api.ads.apple.com/v1/shared-budgets/777890001
```

##### Response

```json
{}
```

## Endpoint

`DELETE https://api.ads.apple.com/v1/shared-budgets/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Get a Budget Order by ID](get-shared-budgets-_id_.md)
  Retrieves a single budget order by its ID.
- [Create a Budget Order](post-shared-budgets.md)
  Creates a budget order that can be assigned to campaigns within an ad account.
- [Query Budget Orders](post-shared-budgets-query.md)
  Returns a filtered, sorted, and paginated list of budget orders.
- [Update a Budget Order](put-shared-budgets-_id_.md)
  Updates mutable fields of an existing budget order by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-shared-budgets-_id_)*