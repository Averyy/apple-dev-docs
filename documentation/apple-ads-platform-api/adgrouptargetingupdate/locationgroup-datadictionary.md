# AdGroupTargetingUpdate.LocationGroup

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Location group targeting, restricting delivery to the business locations in specified groups.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingUpdate.LocationGroup
```

#### Discussion

Applies to Apple Maps campaigns. For creating and managing groups, see [`Managing Location Groups`](location-groups-overview.md). Uses the [`TargetingDataUpdate`](targetingdataupdate.md) `include`/`exclude` shape.

```json
"locationGroup": {
  "include": ["123456789"]
}
```

## Properties

- `include` ([string]): Location group IDs restricting delivery to the business locations in those groups. Mutable.
- `exclude` ([string]): Has no effect. `locationGroup` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingupdate/locationgroup-data.dictionary)*