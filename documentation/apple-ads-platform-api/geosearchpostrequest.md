# GeoSearchPostRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request body for querying geo locations.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object GeoSearchPostRequest
```

#### Discussion

`GeoSearchPostRequest` is the request body for the `POST /v1/search/geo` endpoint. It accepts an array of [`GeoRequest`](georequest.md) objects, each specifying a geo entity, and returns eligibility data for all of them in a single call scoped to the specified `supplySource`. Use this for batch-validating a list of location IDs before setting them as ad group targeting values.

Each `GeoRequest` must supply exactly one of `id` (numeric `geo_location_id`) or `legacyId` (pipe-delimited string such as `US|CA|San Francisco`) plus the required `entity` field. The response is a [`GeoSearchResponse`](geosearchresponse.md) containing a `result` array of matching entities.

Available results and entity restrictions differ by `supplySource`, as shown below:

| `supplySource` | Behavior |
| --- | --- |
| `APPSTORE` | Returns results for App Store campaigns. `PostalCode` entities are excluded. |
| `MAPS` | Returns results for Apple Maps campaigns. Restricted to US and CA. `Country` entity type excluded. `PostalCode` entities are available. |

##### Example

```json
{
  "geoRequest": [
    {
      "id": "123456789",
      "entity": "AdminArea"
    },
    {
      "legacyId": "US|CA|San Francisco",
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

## Topics

### Type Aliases
- [type GeoSearchPostRequest.SupplySource](geosearchpostrequest/supplysource-data.typealias.md)
  The supply source context that scopes a geo location search to App Store or Apple Maps eligibility rules.

## Properties

- `geoRequest` ([GeoRequest]) *(required)*: Array of [`GeoRequest`](georequest.md) objects. Each entry specifies a geo entity to look up. Supports (`entity ID`, `type`) or (`legacyID`, `type`) pairs. Supply exactly one of `id` (numeric) or `legacyId` (pipe-delimited) per entry along with the required `entity` type.
- `supplySource` (GeoSearchPostRequest.SupplySource) *(required)*: Supply source context for eligibility scoping. Case-insensitive. Values: `APPSTORE`, `MAPS`.
- `pagination` (GeoSearchPagination): Optional pagination parameters controlling page size and offset. See [`GeoSearchPagination`](geosearchpagination.md). Defaults to `offset: 0`, `pageSize: 20` if omitted.

## See Also

- [object GeoRequest](georequest.md)
  A single geo entity lookup criterion used in a geo location search request.
- [object GeoSearchResponse](geosearchresponse.md)
  Response envelope for the geo location search endpoints.
- [object GeoSearchPagination](geosearchpagination.md)
  Pagination parameters for geo location search requests and responses.
- [object GeoEligibility](geoeligibility.md)
  Eligibility restrictions for a geographic location, scoped to the supply source specified in the request.
- [object GeoBlockedGroup](geoblockedgroup.md)
  A blocking rule that names the supply source(s) and reason code(s) restricting a geo location.
- [object SearchEntity](searchentity.md)
  A single geographic location result returned by the geo search endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/geosearchpostrequest)*