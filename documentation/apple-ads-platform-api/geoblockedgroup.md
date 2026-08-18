# GeoBlockedGroup

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A blocking rule that names the supply source(s) and reason code(s) restricting a geo location.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object GeoBlockedGroup
```

#### Discussion

`GeoEligibility` responses embed `GeoBlockedGroup`. It describes why a geographic location is blocked for the given supply source. The `reasons` array mixes two categories of codes with different behavior:

- The API always filters hard-block reasons (`NO_MUID`, `NOT_SUPPORTED`, `SOURCE_REMOVED`, `COUNTRY_NOT_SUPPORTED`, `COUNTRY_NOT_SEARCHABLE`, `MAPS_SOURCE_NOT_MATCHED`) out of search results, regardless of request parameters.
- The API includes soft-block reasons (`LOCALITY_LOW_SEARCH_VOLUME`, `POSTAL_CODE_SPARSE`) in search results by default so clients can decide how to handle them. Pass `eligible=true` to the GET endpoint to exclude these geos from results entirely as well.

##### Example

```json
{
  "supplySource": [
    "MAPS"
  ],
  "reasons": [
    "COUNTRY_NOT_SUPPORTED",
    "LOCALITY_LOW_SEARCH_VOLUME"
  ]
}
```

###### Reasons Accepted Values

Hard-block (always filtered from results):

- `NO_MUID`: No Maps ID. The geo cannot serve in MAPS.
- `NOT_SUPPORTED`: The geo is not supported for this supply source.
- `SOURCE_REMOVED`: The geo has been removed from the Maps source table.
- `COUNTRY_NOT_SUPPORTED`: The country is not in the MAPS program.
- `COUNTRY_NOT_SEARCHABLE`: Country-level geos are not searchable in MAPS.
- `MAPS_SOURCE_NOT_MATCHED`: The geo is not present in Maps data.

Soft-block (included by default, filtered only when `eligible=true`):

- `LOCALITY_LOW_SEARCH_VOLUME`: The locality has insufficient Maps search volume.
- `POSTAL_CODE_SPARSE`: The postal code has sparse Maps coverage.

## Properties

- `supplySource` ([SearchSupplySourceType]): Array of supply source strings this restriction applies to. Values: `APPSTORE`, `MAPS`. Read-only.
- `reasons` ([string]): Array of reason codes for the eligibility restriction. See reason codes below. Read-only.

## See Also

- [object GeoRequest](georequest.md)
  A single geo entity lookup criterion used in a geo location search request.
- [object GeoSearchPostRequest](geosearchpostrequest.md)
  Request body for querying geo locations.
- [object GeoSearchResponse](geosearchresponse.md)
  Response envelope for the geo location search endpoints.
- [object GeoSearchPagination](geosearchpagination.md)
  Pagination parameters for geo location search requests and responses.
- [object GeoEligibility](geoeligibility.md)
  Eligibility restrictions for a geographic location, scoped to the supply source specified in the request.
- [object SearchEntity](searchentity.md)
  A single geographic location result returned by the geo search endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/geoblockedgroup)*