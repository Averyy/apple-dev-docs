# Delete a Negative Keyword

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Soft-delete a negative keyword by ID.

**Availability**:
- Apple Ads Platform API 1.0+

## Discussion

This endpoint soft-deletes the specified negative keyword by setting its `deleted` field to `true`. The record is no longer returned by the query endpoint or by ID. The operation returns HTTP 200 with an empty response body on success.

Once soft-deleted, the previously blocked search terms are no longer suppressed. If the deleted negative keyword was campaign-level, ads across all ad groups in the campaign may begin appearing for those queries again. If it was ad-group-level, only that ad group is affected. To temporarily stop suppression without deleting the negative keyword, use `PUT /negative-keywords/{id}` with `status: "PAUSED"`. To have the negative keyword start suppressing search terms again, set `status: "ENABLED"` instead of deleting.

Deletion is permanent. A deleted negative keyword can’t be retrieved, updated, or re-enabled. To suppress those search terms again, create a new negative keyword.

| Constraint | Detail |
| --- | --- |
| Soft deletion | Deletion sets `deleted=true` on the negative keyword record instead of removing it. The record never appears in query results. |
| Exclusion is lifted immediately | Previously blocked search terms are no longer suppressed after deletion. |
| GET returns 404 after deletion | GET requests for a deleted negative keyword return 404 Not Found. |
| PUT returns 404 after deletion | PUT requests to update a deleted negative keyword return 404 Not Found. |
| Use ENABLED status to resume suppression | To have the negative keyword start suppressing search terms again, set `status: "ENABLED"` rather than deleting. |

## Payload Examples

### Request

Deletes a negative keyword by its unique identifier. A successful delete returns HTTP 200 with an empty response body.

```
DELETE /v1/negative-keywords/777888999
```

### Response

```json
{}
```

## Endpoint

`DELETE https://api.ads.apple.com/v1/negative-keywords/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Responses

- `200` OK (`Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` Too Many Requests (`ErrorResponse`, `application/json`)
- `500` Internal Server Error (`ErrorResponse`, `application/json`)

## See Also

- [Create a Negative Keyword](./post-negative-keywords.md)
  Create a negative keyword at the campaign or ad group level to prevent ads from showing for unwanted search terms.
- [Query Negative Keywords](./post-negative-keywords-query.md)
  Query negative keywords using structured filters, sorting, and pagination.
- [Get a Negative Keyword](./get-negative-keywords-_id_.md)
  Retrieve a single negative keyword by its unique identifier.
- [Update a Negative Keyword](./put-negative-keywords-_id_.md)
  Update a negative keyword’s status to enable or pause its search term exclusion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-negative-keywords-_id_)*