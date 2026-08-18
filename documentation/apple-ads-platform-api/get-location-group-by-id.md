# Get Location Group

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a single location group by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns the full state of a location group, including its membership definition, current `systemStatus`, `groupTotal`, and `eligibility`. To confirm a group was created correctly, or to inspect its current membership before attaching it to an ad group’s targeting configuration, use this endpoint.

The response’s `systemStatus` field can take any of the following values:

| Status | Meaning |
| --- | --- |
| `VALID` | The group is fully evaluated and eligible for use in targeting. `groupTotal` reflects the current matched-location count. |
| `PENDING` | The system is evaluating the group’s dynamic rules. `groupTotal` may be `0`. Check again after a short interval. |
| `INVALID` | One or more issues prevent the group from serving. Inspect `eligibility` for details. |
| `DELETED` | The group has been soft-deleted and is no longer available for targeting. |

`PENDING` appears immediately after a `DYNAMIC` group is created or after its `rules` are updated. `STATIC` groups transition directly to `VALID` because membership is explicit and requires no evaluation.

Fetching a group by ID differs from a bulk query in a couple of ways:

| Constraint | Detail |
| --- | --- |
| Single group only | Retrieves one group by ID. Use [`Query Location Groups`](query-location-groups.md) to retrieve multiple groups with filters. |
| Deleted groups | Soft-deleted groups are still retrievable by ID. They appear in the response with `systemStatus: DELETED`. |

#### Payload Examples

##### Request

Retrieves a single location group by its unique identifier.

```None
GET https://api.ads.apple.com/v1/location-groups/5764607523034238976
```

##### Response

```json
{
 "result": {
   "id": "5764607523034238976",
   "name": "AwayFinder West Coast Stores",
   "brandId": "9151314442816847872",
   "adAccountId": "293897290",
   "groupType": "DYNAMIC",
   "systemStatus": "VALID",
   "rules": [
     {
       "field": "adminArea",
       "operator": "IN",
       "value": [
         "California",
         "Oregon",
         "Washington"
       ]
     }
   ],
   "groupTotal": 42,
   "isAllLocationsGroup": false,
   "description": "All AwayFinder locations on the West Coast",
   "creationTime": "2026-02-01T09:00:00Z",
   "modificationTime": "2026-03-25T16:00:00Z",
   "eligibility": {
     "status": "ELIGIBLE"
   }
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/location-groups/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create Location Group](create-location-group.md)
  Create a named group of locations for geographic targeting.
- [Query Location Groups](query-location-groups.md)
  Retrieve a paginated list of location groups using filters and sorting.
- [Update Location Group](update-location-group.md)
  Update an existing location group’s name, rules, or location membership.
- [Delete Location Group](delete-location-group.md)
  Delete a location group by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-location-group-by-id)*