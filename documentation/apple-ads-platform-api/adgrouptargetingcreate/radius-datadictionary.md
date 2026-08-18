# AdGroupTargetingCreate.Radius

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Radius targeting used with Apple Maps campaigns to restrict delivery to users within a given proximity of the brand’s locations.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingCreate.Radius
```

#### Discussion

In practice, radius targeting is applied on `MAPS_SEARCH_RESULTS` campaigns and should not be combined with geo location targeting in the same ad group, but the API does not enforce either constraint at the schema level. Uses the [`TargetingDataCreate`](targetingdatacreate.md) `include`/`exclude` shape.

```json
"radius": {
  "include": ["CLOSE"]
}
```

## Properties

- `include` ([string]): Radius values (`CLOSE`, `MEDIUM`, or `FAR`) restricting delivery to that proximity. Mutable.
- `exclude` ([string]): Has no effect. `radius` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingcreate/radius-data.dictionary)*