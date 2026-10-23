# Search Geo Locations

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Search for geographic locations for use in ad group geo targeting.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint returns a list of geographic locations matching the search criteria. To discover valid geo location identifiers by name before assigning targets to an ad group, use this endpoint. For ID-based lookup of known locations, use the POST endpoint `POST /v1/search/geo` ([`Query Geo Locations`](./gets-a-list-of-geo-locations.md)) instead.

The API sorts results alphabetically by `displayName` and paginates them. Each result includes a `legacyId`, which is a pipe-delimited string encoding the full geographic hierarchy (such as `US|CA|San Francisco`), and an `eligibility` object scoped to the requested `supplySource`.

Every request requires `supplySource`, which determines which `entity` types are available. See the `supplySource` parameter below for details.

#### Payload Examples

**Search by Name**:

##### Request

Search for localities matching “San Francisco” in the US for App Store campaigns.

```
GET /v1/search/geo?query=San%20Francisco&entity=Locality&countrycode=US&supplySource=APPSTORE
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
   },
   {
     "id": "11390475",
     "legacyId": "US|CA|South San Francisco",
     "entity": "Locality",
     "displayName": "South San Francisco, California, United States",
     "countryOrRegion": "US",
     "adminArea": "CA",
     "locality": "South San Francisco"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**All States**:

##### Request

Return all admin areas (states) in the US for Maps campaigns. Omit `query` to return every match.

```
GET /v1/search/geo?entity=AdminArea&countrycode=US&supplySource=MAPS
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
     "id": "20048",
     "legacyId": "US|TX",
     "entity": "AdminArea",
     "displayName": "Texas, United States",
     "countryOrRegion": "US",
     "adminArea": "TX"
   }
 ],
 "pagination": {
   "totalCount": 51,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Eligible Only**:

##### Request

Search for localities in New York, excluding soft-blocked geos.

```
GET /v1/search/geo?query=New%20York&entity=Locality&countrycode=US&supplySource=APPSTORE&eligible=true
```

##### Response

```json
{
 "result": [
   {
     "id": "11390500",
     "legacyId": "US|NY|New York City",
     "entity": "Locality",
     "displayName": "New York City, New York, United States",
     "countryOrRegion": "US",
     "adminArea": "NY",
     "locality": "New York City"
   },
   {
     "id": "11390512",
     "legacyId": "US|NY|Buffalo",
     "entity": "Locality",
     "displayName": "Buffalo, New York, United States",
     "countryOrRegion": "US",
     "adminArea": "NY",
     "locality": "Buffalo"
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

`GET https://api.ads.apple.com/v1/search/geo`

## Parameters

### Query Parameters

- `supplySource` (SearchSupplySourceType) *(required)*: Supply source context for eligibility evaluation. Case-insensitive. Values: `APPSTORE`, `MAPS`. Controls which `entity` types are available. `APPSTORE` excludes the `PostalCode` entity, which is a `MAPS`-level geo. `MAPS` excludes the `Country` entity and restricts results to the US and Canada. Example: `supplySource=APPSTORE`. Omitting it returns a 400 error.
- `query` (string): Search string. Minimum 2 characters. The API rejects shorter values with error code `MIN_QUERY_LENGTH`. Use `\*` to return all matching geos, or omit the parameter for the same result. Example: `query=San Francisco`.

  **Default**: `*:*`
- `entity` (GeoEntityType): Geo entity type to filter results. Values: `Country`, `AdminArea`, `Locality`, `PostalCode`. Example: `entity=Locality`.
- `countrycode` (string): ISO 3166-1 alpha-2 country code to scope results. When `entity` is `AdminArea`, `Locality`, or `PostalCode` and `countrycode` is omitted, defaults to `US`. Example: `countrycode=US`.

  **Default**: `US`
- `eligible` (boolean): Controls soft-block filtering. When `false` (default), the API includes soft-blocked geos (low search volume, sparse coverage) with eligibility data. When `true`, the API excludes them from results entirely. Example: `eligible=true`.

  **Default**: `false`
- `offset` (int32): Zero-based index of the first result to return. Defaults to `0`. Example: `offset=20`.

  **Default**: `0`
- `pageSize` (int32): Maximum number of results per page. Defaults to `20`. Example: `pageSize=50`.

  **Default**: `20`

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Responses

- `200` OK (`GeoSearchResponse`, `application/json`)
- `400` Bad Request (`Error`, `application/json`)
- `401` Unauthorized (`Error`, `application/json`)
- `403` Forbidden (`Error`, `application/json`)
- `404` Not Found (`Error`, `application/json`)
- `429` Too Many Requests (`Error`, `application/json`)
- `500` Internal Server Error (`Error`, `application/json`)

## See Also

- [Query Geo Locations](./gets-a-list-of-geo-locations.md)
  Search for geographic locations by entity type and ID for use in ad group geo targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searches-for-a-list-of-geo-locations)*