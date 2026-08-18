# SearchEntity.Eligibility

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Supply source eligibility restrictions for this search entity.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SearchEntity.Eligibility
```

#### Discussion

The API scopes `eligibility` to the supply source specified in the request and omits it from the response entirely when no restrictions apply to that location.

See [`GeoEligibility`](geoeligibility.md) for the full field reference.

## Properties

- `blockedGroups` ([GeoBlockedGroup]): Array of [`GeoBlockedGroup`](geoblockedgroup.md) objects. Each entry specifies the supply source and the reason the geo is blocked. Always non-empty when present. `GeoEligibility` is omitted from the response entirely when no restrictions apply. Read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searchentity/eligibility-data.dictionary)*