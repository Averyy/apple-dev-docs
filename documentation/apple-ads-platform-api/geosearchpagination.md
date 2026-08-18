# GeoSearchPagination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Pagination parameters for geo location search requests and responses.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object GeoSearchPagination
```

#### Discussion

`GeoSearchPagination` controls and reports offset-based pagination through geo location search results.

When used in a [`GeoSearchPostRequest`](geosearchpostrequest.md) body, set `offset` and `pageSize` to retrieve a specific page of results. The GET endpoint (`GET /v1/search/geo`) accepts `offset` and `pageSize` as query parameters instead of a request body. In both cases the response `pagination` object includes `totalCount`, enabling callers to calculate the total number of pages available.

The default `pageSize` of 20 is sufficient for most targeted lookups. Increase it for searches expected to return many matching locations. To retrieve the next page, increment `offset` by `pageSize`.

##### Example

```json
{
  "totalCount": 87,
  "offset": 20,
  "pageSize": 20
}
```

## Properties

- `totalCount` (int64): Total number of results matching the search criteria. Present in the response only. Read-only.
- `offset` (int32): Zero-based index of the first result to return. Defaults to `0`.
- `pageSize` (int32): Maximum number of results to return per page. Defaults to `20`.

## See Also

- [object GeoRequest](georequest.md)
  A single geo entity lookup criterion used in a geo location search request.
- [object GeoSearchPostRequest](geosearchpostrequest.md)
  Request body for querying geo locations.
- [object GeoSearchResponse](geosearchresponse.md)
  Response envelope for the geo location search endpoints.
- [object GeoEligibility](geoeligibility.md)
  Eligibility restrictions for a geographic location, scoped to the supply source specified in the request.
- [object GeoBlockedGroup](geoblockedgroup.md)
  A blocking rule that names the supply source(s) and reason code(s) restricting a geo location.
- [object SearchEntity](searchentity.md)
  A single geographic location result returned by the geo search endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/geosearchpagination)*