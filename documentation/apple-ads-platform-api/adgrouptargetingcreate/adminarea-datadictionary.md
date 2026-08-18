# AdGroupTargetingCreate.AdminArea

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

State or province (administrative area) targeting.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingCreate.AdminArea
```

#### Discussion

Admin area IDs are returned by [`Search Geo Locations`](searches-for-a-list-of-geo-locations.md) or [`Query Geo Locations`](gets-a-list-of-geo-locations.md). Used with App Store and Apple Maps campaigns. Uses the [`TargetingDataCreate`](targetingdatacreate.md) `include`/`exclude` shape.

```json
"adminArea": {
  "include": ["2068"]
}
```

## Properties

- `include` ([string]): Admin area IDs to restrict delivery to those states or provinces. Mutable.
- `exclude` ([string]): Has no effect. `adminArea` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingcreate/adminarea-data.dictionary)*