# Update Location Group

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Update an existing location group’s name, rules, or location membership.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

The system modifies only the fields you include in the request body. Omitted fields retain their current values. See [`LocationGroupUpdate`](locationgroupupdate.md) for the request body’s accepted fields, including which ones are mutable.

`brandId` and `adAccountId` can’t change after creation, and the update request body doesn’t accept them. To move a group to a different brand or transfer ownership to another ad account, delete the group and recreate it.

`locationIds` and `rules` use full-replacement semantics: the value you send becomes the entire list, not a diff against the existing one, since the API doesn’t support partial updates within an array. To add a single location to a `STATIC` group, retrieve the current `locationIds` array, append the new ID, and send the complete list.

When you add or update rules on a `DYNAMIC` group, `systemStatus` transitions to `PENDING` while the system evaluates membership, and `groupTotal` keeps its last known value until evaluation completes. Updating only `name` or `description` leaves `systemStatus`, `groupTotal`, and membership unchanged. Because an ad group displays the place card for each location in its assigned location group, changing a group’s membership changes which place cards appear once evaluation (if triggered) completes.

#### Payload Examples

**Update Rules**:

##### Request

Replaces the rules on a dynamic group, triggering membership re-evaluation.

```json
PUT /v1/location-groups/{id}

{
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
 ]
}
```

##### Response

```json
{
 "result": {
   "id": "5764607523034238976",
   "name": "AwayFinder West Coast Stores",
   "brandId": "9151314442816847872",
   "groupType": "DYNAMIC",
   "systemStatus": "PENDING",
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
   "modificationTime": "2026-04-10T11:00:00Z",
   "eligibility": {
     "status": "PENDING"
   }
 }
}
```

**Rename Group**:

##### Request

Updates only the display name without affecting membership.

```json
PUT /v1/location-groups/{id}

{
 "name": "AwayFinder Pacific Coast Stores"
}
```

##### Response

```json
{
 "result": {
   "id": "5764607523034238976",
   "name": "AwayFinder Pacific Coast Stores",
   "brandId": "9151314442816847872",
   "groupType": "DYNAMIC",
   "systemStatus": "VALID",
   "groupTotal": 42,
   "modificationTime": "2026-04-10T12:00:00Z",
   "eligibility": {
     "status": "ELIGIBLE"
   }
 }
}
```

## Endpoint

`PUT https://api.ads.apple.com/v1/location-groups/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create Location Group](create-location-group.md)
  Create a named group of locations for geographic targeting.
- [Query Location Groups](query-location-groups.md)
  Retrieve a paginated list of location groups using filters and sorting.
- [Get Location Group](get-location-group-by-id.md)
  Retrieve a single location group by its unique identifier.
- [Delete Location Group](delete-location-group.md)
  Delete a location group by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/update-location-group)*