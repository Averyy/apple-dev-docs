# GeoSearchResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Response envelope for the geo location search endpoints.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object GeoSearchResponse
```

#### Discussion

`GeoSearchResponse` is the response envelope for both `GET /v1/search/geo` and `POST /v1/search/geo`. The `result` array contains [`SearchEntity`](searchentity.md) objects sorted alphabetically by `displayName`. To determine how many pages of results are available and iterate using `offset`, use the `pagination.totalCount` value.

Each `SearchEntity` in the array includes `id` (numeric string, use as targeting value in ad group `targetingDimensions`), `legacyId` (pipe-delimited hierarchy for human reference), `entity` type, localized `displayName`, `countryOrRegion`, `adminArea`, `locality`, `postalCode`, and an `eligibility` object scoped to the `supplySource` specified in the request. If `eligibility` is absent from the response, no restrictions apply for that supply source.

If the request is invalid, for example an unknown supply source or a query string shorter than two characters, the API returns an HTTP error status with a structured error body rather than this response.

##### Example

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

## Properties

- `result` ([SearchEntity]): Array of [`SearchEntity`](searchentity.md) objects matching the request criteria. Results are sorted alphabetically by `displayName` and deduplicated across the requested geo entities. Read-only.
- `pagination` (GeoSearchPagination): Pagination metadata including `totalCount`, `offset`, and `pageSize`. See [`GeoSearchPagination`](geosearchpagination.md). Read-only.

## See Also

- [object GeoRequest](georequest.md)
  A single geo entity lookup criterion used in a geo location search request.
- [object GeoSearchPostRequest](geosearchpostrequest.md)
  Request body for querying geo locations.
- [object GeoSearchPagination](geosearchpagination.md)
  Pagination parameters for geo location search requests and responses.
- [object GeoEligibility](geoeligibility.md)
  Eligibility restrictions for a geographic location, scoped to the supply source specified in the request.
- [object GeoBlockedGroup](geoblockedgroup.md)
  A blocking rule that names the supply source(s) and reason code(s) restricting a geo location.
- [object SearchEntity](searchentity.md)
  A single geographic location result returned by the geo search endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/geosearchresponse)*