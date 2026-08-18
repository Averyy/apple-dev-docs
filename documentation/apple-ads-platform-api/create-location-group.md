# Create Location Group

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Create a named group of locations for geographic targeting.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Location groups define which physical locations are in scope for an ad group. All other settings, including schedule, creatives, and bids, live on the ad group or ad itself. Each group belongs to a single brand and ad account. You set both at creation, and neither can change afterward. Once created, reference the group’s `id` in an ad group’s targeting configuration to restrict delivery to those locations.

#### Request Body

See [`LocationGroupCreate`](locationgroupcreate.md).

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Display name for the group. |
| `brandId` | string | Yes | The brand this group belongs to. |
| `adAccountId` | string | Yes | The ad account that owns the group. |
| `groupType` | string | Yes | `STATIC` or `DYNAMIC`. |
| `locationIds` | array of strings | No | Location IDs. Required for `STATIC` groups. |
| `rules` | array | No | Filter rules for automatic membership. Required for `DYNAMIC` groups. |
| `description` | string | No | Optional description of the group. |

The `groupType` you choose determines how membership is defined and maintained:

| Type | How Membership Is Defined |
| --- | --- |
| `STATIC` | An explicit list of `locationIds` associated with the brand. Membership changes only when you update the `locationIds` array. |
| `DYNAMIC` | A set of `rules` evaluated against the brand’s full location catalog. Membership updates automatically as locations are added to or removed from the brand. |

`STATIC` groups give precise control over which locations are targeted. `DYNAMIC` groups reduce maintenance when the brand’s footprint changes frequently, for example always including every location in a given city without manually updating the group.

##### System Status After Creation

A newly created `STATIC` group has `systemStatus: VALID` immediately. A `DYNAMIC` group starts with `systemStatus: PENDING` while the system evaluates the rules against the brand’s locations. Once evaluation completes, `systemStatus` transitions to `VALID` and `groupTotal` reflects the number of matched locations.

Two fields set at creation are locked in permanently:

| Field | Notes |
| --- | --- |
| `brandId` | Scopes the group to a single brand. Cannot be changed after creation. |
| `adAccountId` | Determines which ad account owns and can access the group. |

Creating a group also requires satisfying the following constraints:

| Constraint | Detail |
| --- | --- |
| `locationIds` required for `STATIC` | At least one location ID must be provided when `groupType` is `STATIC`. |
| `rules` required for `DYNAMIC` | At least one rule must be provided when `groupType` is `DYNAMIC`. |
| `groupTotal` on creation | For `STATIC` groups, `groupTotal` equals the number of IDs supplied. For `DYNAMIC` groups, `groupTotal` is `0` until evaluation completes. |
| `locality` value format | A `rules` entry with `field: locality` must use the pipe-delimited format `countryOrRegion|adminArea|locality`, for example `"US|New York|Brooklyn"`, not a bare city name. |

##### Dynamic Rule Field Values

When `field` is `adminArea`, the `value` must be the full English name of the administrative area, such as `"Illinois"` rather than `"IL"` or `"California"` rather than `"CA"`.

> **Note**: **Important:** The API accepts abbreviated codes without returning an error, but the system creates the location group with `groupTotal: 0` because no locations match. There is no validation error to indicate the mismatch. Use the full name exactly as it appears in a location’s `adminArea` field (returned by [`Query for Locations`](query-locations.md) or [`Get a Location`](get-location-by-id.md)) to ensure rules evaluate correctly.

#### Payload Examples

**Static Group**:

##### Request

Creates a static group with an explicit list of location IDs.

```json
{
 "name": "AwayFinder Downtown Stores",
 "brandId": "9151314442816847872",
 "adAccountId": "293897290",
 "groupType": "STATIC",
 "locationIds": [
   "7205759403792794",
   "7205759403792795"
 ]
}
```

##### Response

```json
{
 "result": {
   "id": "5764607523034238976",
   "name": "AwayFinder Downtown Stores",
   "brandId": "9151314442816847872",
   "adAccountId": "293897290",
   "groupType": "STATIC",
   "systemStatus": "VALID",
   "locationIds": [
     "7205759403792794",
     "7205759403792795"
   ],
   "groupTotal": 2,
   "isAllLocationsGroup": false,
   "creationTime": "2026-02-01T09:00:00Z",
   "modificationTime": "2026-02-01T09:00:00Z",
   "eligibility": {
     "status": "ELIGIBLE"
   }
 }
}
```

**Dynamic Group**:

##### Request

Creates a dynamic group that automatically includes all locations in the specified states.

```json
{
 "name": "AwayFinder West Coast Stores",
 "brandId": "9151314442816847872",
 "adAccountId": "293897290",
 "groupType": "DYNAMIC",
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
 "description": "All AwayFinder locations on the West Coast"
}
```

##### Response

```json
{
 "result": {
   "id": "5764607523034238977",
   "name": "AwayFinder West Coast Stores",
   "brandId": "9151314442816847872",
   "adAccountId": "293897290",
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
   "groupTotal": 0,
   "isAllLocationsGroup": false,
   "description": "All AwayFinder locations on the West Coast",
   "creationTime": "2026-02-01T09:00:00Z",
   "modificationTime": "2026-02-01T09:00:00Z",
   "eligibility": {
     "status": "PENDING"
   }
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/location-groups`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Location Groups](query-location-groups.md)
  Retrieve a paginated list of location groups using filters and sorting.
- [Get Location Group](get-location-group-by-id.md)
  Retrieve a single location group by its unique identifier.
- [Update Location Group](update-location-group.md)
  Update an existing location group’s name, rules, or location membership.
- [Delete Location Group](delete-location-group.md)
  Delete a location group by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/create-location-group)*