# Query Location Groups

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a paginated list of location groups using filters and sorting.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns a paginated list of location groups accessible to the authenticated ad account. An empty request body returns all non-deleted groups with default pagination applied.

#### Request Body

See [`QueryRequest`](queryrequest.md).

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filters` | array | No | Filter conditions to narrow results. |
| `sorting` | array | No | Sort order for results (field + ASC/DESC). |
| `pagination` | object | No | Offset and page size. Defaults apply if omitted. |

##### Filtering

The system combines multiple filters with AND logic. The `id` filter matches the group’s system-assigned identifier, the same `id` value returned in create and get responses. Filtering by `brandId` is the most common way to scope results to a single brand’s groups.

The system excludes soft-deleted groups from results by default. To include them, add a filter with `field: "deleted"`, `operator: "EQUALS"`, `value: true`.

##### Sorting and Pagination

You can sort results by any filterable field using the `sorting` array. The response includes a `pagination` object with `totalCount`, `offset`, and `pageSize`. Page through large result sets by incrementing `offset`.

Two behaviors are worth noting when filtering by ID or excluding deleted groups:

| Constraint | Detail |
| --- | --- |
| `id` filter | Matches the group’s system-assigned identifier, not the provider object ID. |
| Deleted groups excluded | Use a `deleted EQUALS true` filter to surface soft-deleted groups. |

##### Find Groups for a Location

There is no dedicated filter for looking up location groups by location membership. To determine which groups contain a specific location, query location groups scoped to the location’s brand with a `brandId` filter, then inspect each returned group’s membership client-side. For `STATIC` groups, check whether the location’s `id` appears in the group’s `locationIds` array. For `DYNAMIC` groups, check whether the location satisfies the group’s `rules` criteria.

Narrow results using any of the following fields and operators:

| Field | Type | Operators | Notes |
| --- | --- | --- | --- |
| `id` | string | EQUALS, IN | Matches the group’s system-assigned identifier. |
| `name` | string | EQUALS, CONTAINS | Group display name. |
| `brandId` | string | EQUALS | Parent brand. |
| `groupType` | string | EQUALS, IN | `STATIC` or `DYNAMIC`. |
| `deleted` | boolean | EQUALS | Soft-delete flag. Defaults to excluding deleted groups. |
| `isAllLocationsGroup` | boolean | EQUALS | All-locations group flag. |
| `eligibility.status` | string | EQUALS, IN | Eligibility status. |
| `eligibility.blockedGroups.supplyPlacement` | string | CONTAINS_ANY | Blocked placement. |
| `eligibility.blockedGroups.countryOrRegion` | string | CONTAINS_ANY | Blocked country. |
| `eligibility.allowedGroups.supplyPlacement` | string | CONTAINS_ANY | Allowed placement. |
| `eligibility.allowedGroups.countryOrRegion` | string | CONTAINS_ANY | Allowed country. |

#### Payload Examples

**Filter by Brand**:

##### Request

Returns all location groups belonging to a specific brand.

```json
{
 "filters": [
   {
     "field": "brandId",
     "operator": "EQUALS",
     "value": "9151314442816847872"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 100
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": "5764607523034238976",
     "name": "AwayFinder West Coast Stores",
     "brandId": "9151314442816847872",
     "groupType": "DYNAMIC",
     "systemStatus": "VALID",
     "groupTotal": 42,
     "isAllLocationsGroup": false,
     "eligibility": {
       "status": "ELIGIBLE"
     },
     "creationTime": "2025-02-01T09:00:00Z",
     "modificationTime": "2025-03-25T16:00:00Z"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 100
 }
}
```

**Filter Dynamic Groups**:

##### Request

Returns only `DYNAMIC` location groups.

```json
{
 "filters": [
   {
     "field": "groupType",
     "operator": "EQUALS",
     "value": "DYNAMIC"
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "id": "5764607523034238976",
     "name": "AwayFinder West Coast Stores",
     "brandId": "9151314442816847872",
     "groupType": "DYNAMIC",
     "systemStatus": "VALID",
     "groupTotal": 42,
     "isAllLocationsGroup": false,
     "eligibility": {
       "status": "ELIGIBLE"
     },
     "creationTime": "2025-02-01T09:00:00Z",
     "modificationTime": "2025-03-25T16:00:00Z"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 100
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/location-groups/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create Location Group](create-location-group.md)
  Create a named group of locations for geographic targeting.
- [Get Location Group](get-location-group-by-id.md)
  Retrieve a single location group by its unique identifier.
- [Update Location Group](update-location-group.md)
  Update an existing location group’s name, rules, or location membership.
- [Delete Location Group](delete-location-group.md)
  Delete a location group by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-location-groups)*