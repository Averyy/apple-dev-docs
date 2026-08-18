# AdGroupTargeting.Locality

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

City or locality targeting.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargeting.Locality
```

#### Discussion

Locality IDs are returned by [`Search Geo Locations`](searches-for-a-list-of-geo-locations.md) or [`Query Geo Locations`](gets-a-list-of-geo-locations.md). Used with App Store and Apple Maps campaigns. Uses the [`TargetingData`](targetingdata.md) `include`/`exclude` shape.

```json
"locality": {
  "include": ["155356"]
}
```

## Properties

- `include` ([string]): Locality IDs restricting delivery to those cities. Mutable.
- `exclude` ([string]): Has no effect. `locality` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargeting/locality-data.dictionary)*