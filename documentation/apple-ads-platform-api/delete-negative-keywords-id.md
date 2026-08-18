# Delete a Negative Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Soft-delete a negative keyword by ID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint soft-deletes the specified negative keyword by setting its `deleted` field to `true`. The record remains queryable by including `deleted=true` in query filters. The operation returns HTTP 200 with an empty response body on success.

Once soft-deleted, the previously blocked search terms are no longer suppressed. If the deleted negative keyword was campaign-level, ads across all ad groups in the campaign may begin appearing for those queries again. If it was ad-group-level, only that ad group is affected. To temporarily stop suppression without deleting the negative keyword, use `PUT /negative-keywords/{id}` with `status: "PAUSED"`. To have the negative keyword start suppressing search terms again, set `status: "ENABLED"` instead of deleting.

The soft delete is reflected consistently across subsequent GET and PUT requests, and reversible by re-enabling the record.

| Constraint | Detail |
| --- | --- |
| Soft deletion | Deletion sets `deleted=true` on the negative keyword record instead of removing it. The record remains queryable with the appropriate filter. |
| Exclusion is lifted immediately | Previously blocked search terms are no longer suppressed after deletion. |
| GET returns the deleted negative keyword | GET requests after deletion return the negative keyword with `deleted: true`, not a 404. |
| PUT returns 404 after deletion | PUT requests to update a deleted negative keyword return 404 Not Found. |
| Use ENABLED status to resume suppression | To have the negative keyword start suppressing search terms again, set `status: "ENABLED"` rather than deleting. |

#### Payload Examples

##### Request

Deletes a negative keyword by its unique identifier. A successful delete returns HTTP 200 with an empty response body.

```None
DELETE https://api.ads.apple.com/v1/negative-keywords/777888999
```

##### Response

```json
{}
```

## Endpoint

`DELETE https://api.ads.apple.com/v1/negative-keywords/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Negative Keyword](post-negative-keywords.md)
  Create a negative keyword at the campaign or ad group level to prevent ads from showing for unwanted search terms.
- [Query Negative Keywords](post-negative-keywords-query.md)
  Query negative keywords using structured filters, sorting, and pagination.
- [Get a Negative Keyword](get-negative-keywords-_id_.md)
  Retrieve a single negative keyword by its unique identifier.
- [Update a Negative Keyword](put-negative-keywords-_id_.md)
  Update a negative keyword’s status to enable or pause its search term exclusion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-negative-keywords-_id_)*