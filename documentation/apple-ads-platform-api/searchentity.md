# SearchEntity

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single geographic location result returned by the geo search endpoints.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SearchEntity
```

#### Discussion

`SearchEntity` is a single geographic location result returned by the geo search endpoints. It provides multiple identifiers for the same location: `id` (numeric) for use as a targeting value in `AdGroupTargeting`, and `legacyId` (pipe-delimited) for human-readable reference. The `entity` field classifies the geographic granularity from `Country` down to `PostalCode`.

The `eligibility` field indicates whether you can use the location for ads on the requested supply source.

- If `eligibility` is absent from the response, no restrictions apply.
- If it contains `blockedGroups`, the location has one or more blocking reasons for that supply source (e.g., low search volume, sparse coverage, or a hard-block condition), but the API still returns it with this data so the client can decide how to present it.
- The API scopes eligibility to the single `supplySource` specified in the request.
- The response includes only `blockedGroups` matching that supply source.

##### Example

```json
{
  "id": "555666777",
  "legacyId": "US|CA|San Francisco|94103",
  "entity": "PostalCode",
  "displayName": "94103, San Francisco, California, United States",
  "countryOrRegion": "US",
  "adminArea": "CA",
  "postalCode": "94103",
  "eligibility": {
    "blockedGroups": [
      {
        "supplySource": ["MAPS"],
        "reasons": ["POSTAL_CODE_SPARSE"]
      }
    ]
  }
}
```

## Topics

### Dictionaries
- [object SearchEntity.Eligibility](searchentity/eligibility-data.dictionary.md)
  Supply source eligibility restrictions for this search entity.

## Properties

- `id` (string): Numeric geo location identifier. Example: `"11390462"`. Read-only.
- `legacyId` (string): Pipe-delimited geo identifier encoding the hierarchy. Examples: `US`, `US|CA`, `US|CA|San Francisco`, `US|TX|78238`. Read-only.
- `entity` (GeoEntityType): Geo entity type. Values: `Country`, `AdminArea`, `Locality`, `PostalCode`. Read-only.
- `displayName` (string): Localized display name with full hierarchy. Example: `"San Francisco, California, United States"`. Read-only.
- `countryOrRegion` (string): ISO 3166-1 alpha-2 country code. Read-only.
- `adminArea` (string): State or province identifier. Present for `AdminArea`, `Locality`, and `PostalCode` entities. Read-only.
- `locality` (string): City or locality name. Present for `Locality` entities only. Read-only.
- `postalCode` (string): Postal code value. Present for `PostalCode` entities only. Read-only.
- `eligibility` (SearchEntity.Eligibility): Supply source eligibility restrictions scoped to the `supplySource` specified in the request. See [`GeoEligibility`](geoeligibility.md). Absent from the response when no restrictions apply. Read-only.

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
- [object GeoBlockedGroup](geoblockedgroup.md)
  A blocking rule that names the supply source(s) and reason code(s) restricting a geo location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searchentity)*