# Query for Locations

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a paginated list of business locations using filters and sorting.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a paginated list of physical business locations associated with a brand. Locations are the physical stores or venues that `BUSINESS_BRAND` campaigns advertise. When creating ad groups for these campaigns, use location `id` values from this endpoint to scope delivery to specific stores or venues.

Locations are registered entities that represent physical places of business, such as retail stores, restaurants, and service centers. An empty request body returns all locations with default pagination. Filter by `brandId` to retrieve locations for a specific brand.

#### Request Body

See [`QueryRequest`](queryrequest.md).

Each location record returned by this endpoint includes the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for the location. Used in ad group targeting. |
| `name` | string | Display name of the location. |
| `address.countryOrRegion` | string | ISO 3166-1 alpha-2 country code. |
| `address.adminArea` | string | State or province name. |
| `address.locality` | string | City or town name. |
| `address.postalCode` | string | Postal or ZIP code. |
| `status` | string | Operational status: `OPEN`, `OPENING_SOON`, `CLOSED`, `MOVED`, `TEMPORARILY_CLOSED`. |
| `eligibility` | object | System-managed eligibility for ad targeting. |

Narrow results using any of these fields and their supported operators:

| Field | Operators | Description |
| --- | --- | --- |
| `brandId` | `EQUALS` | Filter by the brand the location belongs to. |
| `address.countryOrRegion` | `EQUALS`, `IN` | Filter by country or region code. |
| `address.adminArea` | `EQUALS`, `IN` | Filter by state or province name. |
| `address.locality` | `EQUALS`, `STARTS_WITH` | Filter by city or town name. |
| `address.postalCode` | `EQUALS`, `IN` | Filter by postal or ZIP code. |
| `eligibility.status` | `EQUALS`, `IN` | Filter by eligibility status: `ELIGIBLE`, `INELIGIBLE`, `LIMITED`, `PENDING`, `UNDEFINED`. |
| `status` | `EQUALS`, `IN` | Filter by operational status. |
| `name` | `EQUALS`, `STARTS_WITH` | Filter by location display name or prefix. |

A few limitations apply to querying locations and using the results for targeting:

| Constraint | Detail |
| --- | --- |
| Filter by `brandId` | Omitting this returns locations across all brands, which may be a large result set. |
| Location IDs in targeting | Add location `id` values to a `LocationGroup`, then reference the group via `targeting.locationGroup` in ad group targeting. |
| Open locations only | Only locations with `status: OPEN` are typically eligible for ad group targeting. |

#### Payload Examples

**Query by Brand**:

##### Request

Retrieve all open locations for a specific brand.

```json
{
 "filters": [
   {
     "field": "brandId",
     "operator": "EQUALS",
     "value": "9151314442816847872"
   },
   {
     "field": "status",
     "operator": "EQUALS",
     "value": "OPEN"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": "902134",
     "name": "AwayFinder - Downtown SF",
     "brandId": "9151314442816847872",
     "address": {
       "countryOrRegion": "US",
       "adminArea": "California",
       "locality": "San Francisco"
     },
     "categories": [
       "shopping.retail"
     ],
     "displayPoint": {
       "latitude": "37.7749",
       "longitude": "-122.4194"
     },
     "status": "OPEN",
     "eligibility": {
       "status": "ELIGIBLE",
       "blockedGroups": [],
       "allowedGroups": []
     },
     "creationTime": "2025-01-10T08:00:00Z",
     "modificationTime": "2025-01-10T08:00:00Z"
   },
   {
     "id": "830123",
     "name": "AwayFinder - Palo Alto",
     "brandId": "9151314442816847872",
     "address": {
       "countryOrRegion": "US",
       "adminArea": "California",
       "locality": "Palo Alto"
     },
     "categories": [
       "shopping.retail"
     ],
     "displayPoint": {
       "latitude": "37.4419",
       "longitude": "-122.1430"
     },
     "status": "OPEN",
     "eligibility": {
       "status": "ELIGIBLE",
       "blockedGroups": [],
       "allowedGroups": []
     },
     "creationTime": "2025-01-10T08:00:00Z",
     "modificationTime": "2025-01-10T08:00:00Z"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Filter by Country**:

##### Request

Retrieve all locations in a specific country to build a country-scoped targeting set.

```json
{
 "filters": [
   {
     "field": "brandId",
     "operator": "EQUALS",
     "value": "9151314442816847872"
   },
   {
     "field": "address.countryOrRegion",
     "operator": "EQUALS",
     "value": "GB"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": "812456",
     "name": "AwayFinder - London Oxford Street",
     "brandId": "9151314442816847872",
     "address": {
       "countryOrRegion": "GB",
       "adminArea": "England",
       "locality": "London"
     },
     "categories": [
       "shopping.retail"
     ],
     "displayPoint": {
       "latitude": "51.5074",
       "longitude": "-0.1278"
     },
     "status": "OPEN",
     "eligibility": {
       "status": "ELIGIBLE",
       "blockedGroups": [],
       "allowedGroups": []
     },
     "creationTime": "2025-02-01T09:00:00Z",
     "modificationTime": "2025-02-01T09:00:00Z"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Query by Name**:

##### Request

Search for locations by name prefix, sorted alphabetically.

```json
{
 "filters": [
   {
     "field": "brandId",
     "operator": "EQUALS",
     "value": "9151314442816847872"
   },
   {
     "field": "name",
     "operator": "STARTS_WITH",
     "value": "AwayFinder"
   }
 ],
 "sorting": [
   {
     "field": "name",
     "order": "ASC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 50
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": "902134",
     "name": "AwayFinder - Downtown SF",
     "brandId": "9151314442816847872",
     "address": {
       "countryOrRegion": "US",
       "adminArea": "California",
       "locality": "San Francisco"
     },
     "categories": [
       "shopping.retail"
     ],
     "displayPoint": {
       "latitude": "37.7749",
       "longitude": "-122.4194"
     },
     "status": "OPEN",
     "eligibility": {
       "status": "ELIGIBLE",
       "blockedGroups": [],
       "allowedGroups": []
     },
     "creationTime": "2025-01-10T08:00:00Z",
     "modificationTime": "2025-01-10T08:00:00Z"
   },
   {
     "id": "812456",
     "name": "AwayFinder - London Oxford Street",
     "brandId": "9151314442816847872",
     "address": {
       "countryOrRegion": "GB",
       "adminArea": "England",
       "locality": "London"
     },
     "categories": [
       "shopping.retail"
     ],
     "displayPoint": {
       "latitude": "51.5074",
       "longitude": "-0.1278"
     },
     "status": "OPEN",
     "eligibility": {
       "status": "ELIGIBLE",
       "blockedGroups": [],
       "allowedGroups": []
     },
     "creationTime": "2025-02-01T09:00:00Z",
     "modificationTime": "2025-02-01T09:00:00Z"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 50
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/locations/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Get a Location](get-location-by-id.md)
  Retrieve a single business location by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-locations)*