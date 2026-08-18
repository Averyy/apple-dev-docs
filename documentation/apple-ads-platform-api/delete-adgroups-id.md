# Delete an Ad Group

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Soft-delete an ad group by its unique identifier, along with all ads and keywords associated with it.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint deletes an ad group by its ID, using a soft delete: the system marks it `deleted: true` and preserves the record. By default, `POST /adgroups/query` results exclude it unless you filter with `deleted EQUALS true`.

Deletion cascades to all resources nested under the ad group: it also marks ads, keywords, and negative keywords as deleted. This operation cannot be undone.

Deleting an ad group has the following effects:

| Constraint | Detail |
| --- | --- |
| Soft delete only | The system marks the ad group `deleted: true` but retains the record. |
| Cascade deletion | Deletion also marks all ads, keywords, and negative keywords belonging to the ad group as deleted. |
| Excluded from query results by default | `POST /adgroups/query` results exclude deleted ad groups unless you filter with `deleted EQUALS true`. |
| Parent campaign deletion also deletes ad groups | Deleting a campaign cascades to all of its ad groups and their nested resources. |

#### Payload Examples

**Delete Ad Group**:

##### Request

Deletes an ad group by its unique identifier. A successful delete returns HTTP 200 with an empty response body.

```None
DELETE https://api.ads.apple.com/v1/adgroups/555666777
```

##### Response

```json
{}
```

**Verify Deletion**:

##### Request

Query with `deleted EQUALS true` to confirm the ad group shows as deleted.

```json
POST /v1/adgroups/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555666
   },
   {
     "field": "deleted",
     "operator": "EQUALS",
     "value": true
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "id": 555666777,
     "name": "AwayFinder iOS — New Users 18-34",
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "pricingModel": "CPT",
     "status": "ENABLED",
     "systemStatus": "NOT_RUNNING",
     "deleted": true,
     "creationTime": "2025-01-10T08:00:00.000",
     "modificationTime": "2025-06-15T14:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`DELETE https://api.ads.apple.com/v1/adgroups/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad Group](post-adgroups.md)
  Create a new ad group within a campaign, defining targeting, bid strategy, and scheduling for a set of ads.
- [Query Ad Groups](post-adgroups-query.md)
  Query ad groups using filters, sorting, and pagination.
- [Get an Ad Group](get-adgroups-_id_.md)
  Retrieve a single ad group by its unique identifier.
- [Update an Ad Group](put-adgroups-_id_.md)
  Update an existing ad group’s name, status, bid strategy, targeting, or scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-adgroups-_id_)*