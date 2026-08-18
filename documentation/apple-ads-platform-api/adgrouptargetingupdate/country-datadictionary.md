# AdGroupTargetingUpdate.Country

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Country-level geographic targeting.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingUpdate.Country
```

#### Discussion

Country IDs are returned by [`Search Geo Locations`](searches-for-a-list-of-geo-locations.md) or [`Query Geo Locations`](gets-a-list-of-geo-locations.md) (`supplySource=APPSTORE`). Used with App Store campaigns. Uses the [`TargetingDataUpdate`](targetingdataupdate.md) `include`/`exclude` shape.

```json
"country": {
  "include": ["1125"]
}
```

## Properties

- `include` ([string]): A country ID to restrict delivery to that market. Mutable.
- `exclude` ([string]): Has no effect. `country` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingupdate/country-data.dictionary)*