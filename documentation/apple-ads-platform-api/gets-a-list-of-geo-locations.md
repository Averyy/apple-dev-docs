# Query Geo Locations

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Search for geographic locations by entity type and ID for use in ad group geo targeting.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns a list of geographic locations matching the specified entity criteria. To look up valid geo IDs and names before assigning geo targets to an ad group, use this endpoint.

The API sorts results alphabetically by `displayName` and paginates them using [`GeoSearchPagination`](geosearchpagination.md). Each result is a [`SearchEntity`](searchentity.md) and includes a hierarchy identifier in `legacyId`, which is a pipe-delimited string that encodes the full geographic hierarchy, such as `US|CA|San Francisco`. See [`GeoEntityType`](geoentitytype.md) for the full list of entity granularities.

The `supplySource` field controls which entity types appear in the response. Use `APPSTORE` for App Store campaigns and `MAPS` for Apple Maps campaigns. Unlike the GET endpoint, the POST endpoint does not filter by eligibility. The API always returns soft-blocked geos with their eligibility data included.

#### Payload Examples

**Query by Locality ID**:

Look up a specific locality by its numeric ID for use in an App Store ad group.

##### Request

```json
{
 "geoRequest": [
   {
     "id": "11390462",
     "entity": "Locality"
   }
 ],
 "supplySource": "APPSTORE",
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
     "id": "11390462",
     "legacyId": "US|CA|San Francisco",
     "entity": "Locality",
     "displayName": "San Francisco, California, United States",
     "countryOrRegion": "US",
     "adminArea": "CA",
     "locality": "San Francisco"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Query by AdminArea**:

Look up an admin area (state) for use in an Apple Maps ad group.

##### Request

```json
{
 "geoRequest": [
   {
     "legacyId": "US|CA",
     "entity": "AdminArea"
   }
 ],
 "supplySource": "MAPS",
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
     "id": "20039",
     "legacyId": "US|CA",
     "entity": "AdminArea",
     "displayName": "California, United States",
     "countryOrRegion": "US",
     "adminArea": "CA"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Query Multiple Entities**:

Batch-resolve multiple geo locations (a state and a postal code) in a single request.

##### Request

```json
{
 "geoRequest": [
   {
     "legacyId": "US|CA",
     "entity": "AdminArea"
   },
   {
     "legacyId": "US|TX|78238",
     "entity": "PostalCode"
   }
 ],
 "supplySource": "APPSTORE",
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
     "id": "20039",
     "legacyId": "US|CA",
     "entity": "AdminArea",
     "displayName": "California, United States",
     "countryOrRegion": "US",
     "adminArea": "CA"
   },
   {
     "id": "23041882",
     "legacyId": "US|TX|78238",
     "entity": "PostalCode",
     "displayName": "78238, Texas, United States",
     "countryOrRegion": "US",
     "adminArea": "TX",
     "postalCode": "78238"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/search/geo`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Search Geo Locations](searches-for-a-list-of-geo-locations.md)
  Search for geographic locations for use in ad group geo targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/gets-a-list-of-geo-locations)*