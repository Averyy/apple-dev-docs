# Create Location Group

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Create a named group of locations for geographic targeting.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

Location groups define which physical locations are in scope for an ad group. All other settings, including schedule, creatives, and bids, live on the ad group or ad itself. Each group belongs to a single brand and ad account. You set both at creation, and neither can change afterward. Once created, reference the group’s `id` in an ad group’s targeting configuration to restrict delivery to those locations.

#### Request Body

See [`LocationGroupCreate`](locationgroupcreate.md).

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