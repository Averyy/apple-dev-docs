# Delete a Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Soft-delete a keyword by ID, setting its deleted field to true and stopping bids on that term.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Soft-deletes the keyword by setting its deleted field to true. The record remains queryable by including deleted=true in query filters. The operation returns HTTP 200 with an empty response body on success.

Deleting a keyword does not affect the parent ad group or campaign. Only the keyword itself is removed. Other keywords in the same ad group continue to serve normally. If you want to temporarily stop bidding on a term without permanently removing it, pause the keyword using `PUT /keywords/{id}` with `status: "PAUSED"` instead.

The soft delete is reflected consistently across subsequent GET and PUT requests.

| Constraint | Detail |
| --- | --- |
| Soft deletion | Deletion sets the keyword’s `deleted` field to `true`. The record remains queryable by including `deleted=true` in query filters. |
| Does not affect parent resources | Deletion doesn’t modify the parent ad group or campaign. |
| GET returns the deleted keyword | GET requests after deletion return the keyword with `deleted: true`, not a 404. |
| PUT returns 404 after deletion | PUT requests to update a deleted keyword return 404 Not Found. |
| Use PAUSED status to suspend temporarily | If you may need to reactivate the term, set `status: "PAUSED"` rather than deleting. |

#### Payload Examples

##### Request

Deletes a keyword by its unique identifier. A successful delete returns HTTP 200 with an empty response body.

```None
DELETE https://api.ads.apple.com/v1/keywords/888999000
```

##### Response

```json
{}
```

## Endpoint

`DELETE https://api.ads.apple.com/v1/keywords/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Keyword](post-keywords.md)
  Create a new keyword in an ad group, setting the match type and optional bid amount.
- [Query Keywords](post-keywords-query.md)
  Query keywords using structured filters, sorting, and pagination.
- [Get a Keyword](get-keywords-_id_.md)
  Retrieve a single keyword by its unique identifier.
- [Update a Keyword](put-keywords-_id_.md)
  Update a keyword’s bid amount or status to optimize spend and control delivery for that term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-keywords-_id_)*