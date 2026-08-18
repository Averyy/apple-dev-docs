# Delete an Ad

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Soft-deletes an ad by its unique identifier, stopping delivery and removing it from active results.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint soft-deletes an ad by its ID. The system marks the ad `deleted: true`, and it immediately stops serving. The system preserves the record and excludes it from query results by default, but a GET request still returns the ad with `deleted: true`. A subsequent PUT request to update a deleted ad returns 404 Not Found.

Deleting an ad does not affect the associated ad creative. The ad creative remains available, and new ads in any ad group can reference it. Deleting an ad does not affect delivery of other ads in the same ad group that reference the same or different ad creatives.

To change which ad creative an ad group serves, delete the existing ad and create a new ad with the desired `creativeId` in the same ad group.

Deleting an ad has the following effects:

| Constraint | Detail |
| --- | --- |
| Soft delete only | The system marks the ad `deleted: true` but does not physically remove it. It retains the record for audit purposes. |
| Delivery stops immediately | The deleted ad stops serving as soon as the system processes the delete. |
| Deleted ads return from GET | GET requests after deletion return the ad with `deleted: true`, not a 404. |
| PUT returns 404 after deletion | Attempting to update a deleted ad returns 404 Not Found. |
| Deleted ads excluded from queries | `POST /v1/ads/query` excludes deleted ads by default. Filter with `deleted EQUALS true` to confirm deletion. |
| Associated ad creative is not deleted | The ad creative record is unaffected. Other ads can use it. |
| To swap an ad creative | Delete this ad and create a new ad with the desired `creativeId` in the same ad group. |

#### Payload Examples

**Delete Ad**:

##### Request

Deletes an ad by its unique identifier. A successful delete returns HTTP 200 with an empty response body.

```None
DELETE https://api.ads.apple.com/v1/ads/777888999
```

##### Response

```json
{}
```

**Verify Deletion**:

##### Request

After deletion, confirm the ad is marked deleted by querying with `deleted EQUALS true`.

```json
POST /v1/ads/query

{
 "filters": [
   {
     "field": "adGroupId",
     "operator": "EQUALS",
     "value": 555666777
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
     "id": 777888999,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "creativeId": 666777888,
     "name": "AwayFinder - Default Product Page",
     "status": "ENABLED",
     "systemStatus": "NOT_RUNNING",
     "systemStatusReasons": [],
     "systemStatusLimitingReasons": [],
     "deleted": true,
     "creationTime": "2025-09-01T08:00:00.000",
     "modificationTime": "2025-10-15T08:00:00.000"
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

`DELETE https://api.ads.apple.com/v1/ads/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad](post-ads.md)
  Creates a new ad that links an ad creative to an ad group for delivery.
- [Query Ads](post-ads-query.md)
  Searches and filters ads using structured query criteria including field filters, sorting, and pagination.
- [Get an Ad](get-ads-_id_.md)
  Retrieves a single ad by its unique identifier.
- [Update an Ad](put-ads-_id_.md)
  Updates the name or status of an existing ad by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/delete-ads-_id_)*