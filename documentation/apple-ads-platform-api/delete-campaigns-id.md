# Delete a Campaign

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Soft-delete a campaign by its unique identifier, cascading to its ad groups, keywords, and ads.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint deletes a campaign by its ID. The campaign is soft-deleted: it is marked with `deleted: true` and excluded from query results by default, but the record and all its fields are preserved.

After deletion, the query API will no longer include the deleted campaign by default. To retrieve deleted campaigns via the query API, pass an explicit filter with `deleted IN [true, false]`. To confirm deletion, use `GET /v1/campaigns/{id}` and verify that `Campaign.deleted` is `true`. You can also check that `systemStatus` is `NOT_RUNNING` and that `systemStatusReasons` contains `DELETED_BY_USER`.

Keep the following in mind when relying on this endpoint’s soft-delete behavior:

| Constraint | Detail |
| --- | --- |
| Soft delete only | The campaign is marked `deleted: true` but not physically removed. The record is retained. |
| Deleted campaigns excluded from queries by default | `POST /v1/campaigns/query` results automatically exclude campaigns with `deleted: true` unless explicitly filtered. |
| Active ad groups are also deleted | Deleting a campaign cascades to its associated ad groups, keywords, and ads. |

#### Payload Examples

**Delete Campaign**:

##### Request

Deletes a campaign by its unique identifier. A successful delete returns HTTP 200 with an empty result.

```None
DELETE https://api.ads.apple.com/v1/campaigns/111222333
```

##### Response

```json
{}
```

**Verify Deletion**:

##### Request

After deletion, confirm the campaign is marked deleted by retrieving it directly by ID.

```None
GET https://api.ads.apple.com/v1/campaigns/111222333
```

##### Response

```json
{
 "result": {
   "id": 111222333,
   "deleted": true,
   "systemStatus": "NOT_RUNNING",
   "systemStatusReasons": [
     "DELETED_BY_USER"
   ],
   "displayStatus": "DELETED"
 }
}
```

## Endpoint

`DELETE https://api.ads.apple.com/v1/campaigns/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Campaign](post-campaigns.md)
  Create a new advertising campaign with a promoted object, budget, targeting, and bid strategy configuration.
- [Query Campaigns](post-campaigns-query.md)
  Query campaigns using filters, sorting, and pagination.
- [Get a Campaign](get-campaigns-_id_.md)
  Retrieve a single campaign by its unique identifier.
- [Update a Campaign](put-campaigns-_id_.md)
  Update a campaign’s name, status, budget, targeting, or bid strategy.
- [Get Legacy App Limited Status Reason Details](get-campaigns-_id_-legacy-app-limited-status-reason-details.md)
  Return a map of country or region codes to their associated limited-status reason for legacy app campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-campaigns-_id_)*