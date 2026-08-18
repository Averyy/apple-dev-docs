# Search Geo Locations

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Search for geographic locations for use in ad group geo targeting.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns a list of geographic locations matching the search criteria. To discover valid geo location identifiers by name before assigning targets to an ad group, use this endpoint. For ID-based lookup of known locations, use the POST endpoint `POST /v1/search/geo` instead.

The API sorts results alphabetically by `displayName` and paginates them. Each result includes a `legacyId`, which is a pipe-delimited string encoding the full geographic hierarchy (such as `US|CA|San Francisco`), and an `eligibility` object scoped to the requested `supplySource`.

Every request requires `supplySource`, which determines which `entity` types are available. See the `supplySource` parameter below for details.

#### Payload Examples

**Search by Name**:

##### Request

Search for localities matching “San Francisco” in the US for App Store campaigns.

```None
GET https://api.ads.apple.com/v1/search/geo?query=San%20Francisco&entity=Locality&countrycode=US&supplySource=APPSTORE
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

```None
GET https://api.ads.apple.com/v1/search/geo?entity=AdminArea&countrycode=US&supplySource=MAPS
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

```None
GET https://api.ads.apple.com/v1/search/geo?query=New%20York&entity=Locality&countrycode=US&supplySource=APPSTORE&eligible=true
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

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Geo Locations](gets-a-list-of-geo-locations.md)
  Search for geographic locations by entity type and ID for use in ad group geo targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searches-for-a-list-of-geo-locations)*