# GeoEligibility

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Eligibility restrictions for a geographic location, scoped to the supply source specified in the request.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object GeoEligibility
```

#### Discussion

`SearchEntity` responses embed `GeoEligibility`, which summarizes the serving eligibility for a geographic location relative to the supply source specified in the request. When present, `blockedGroups` is always non-empty. The API omits `GeoEligibility` entirely from the response when no restrictions apply. Each `GeoBlockedGroup` entry in `blockedGroups` identifies the supply source and the reason the geo is blocked.

To pre-validate geo targeting choices before applying them to an ad group and avoid campaign configuration errors, use `GeoEligibility` data.

##### Example

```json
{
  "blockedGroups": [
    {
      "supplySource": [
        "MAPS"
      ],
      "reasons": [
        "COUNTRY_NOT_SUPPORTED"
      ]
    }
  ]
}
```

## Properties

- `blockedGroups` ([GeoBlockedGroup]): Array of [`GeoBlockedGroup`](geoblockedgroup.md) objects. Each entry specifies the supply source and the reason the geo is blocked. Always non-empty when present. `GeoEligibility` is omitted from the response entirely when no restrictions apply. Read-only.

## See Also

- [object GeoRequest](georequest.md)
  A single geo entity lookup criterion used in a geo location search request.
- [object GeoSearchPostRequest](geosearchpostrequest.md)
  Request body for querying geo locations.
- [object GeoSearchResponse](geosearchresponse.md)
  Response envelope for the geo location search endpoints.
- [object GeoSearchPagination](geosearchpagination.md)
  Pagination parameters for geo location search requests and responses.
- [object GeoBlockedGroup](geoblockedgroup.md)
  A blocking rule that names the supply source(s) and reason code(s) restricting a geo location.
- [object SearchEntity](searchentity.md)
  A single geographic location result returned by the geo search endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/geoeligibility)*