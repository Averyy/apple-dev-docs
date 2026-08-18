# AdGroupTargetingCreate.LocationGroup

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Location group targeting, restricting delivery to the business locations in specified groups.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingCreate.LocationGroup
```

#### Discussion

Used with Apple Maps campaigns. For creating and managing groups, see [`Managing Location Groups`](location-groups-overview.md). Uses the [`TargetingDataCreate`](targetingdatacreate.md) `include`/`exclude` shape.

## Properties

- `include` ([string]): Location group IDs restricting delivery to the business locations in those groups. Mutable.
- `exclude` ([string]): Has no effect. `locationGroup` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingcreate/locationgroup-data.dictionary)*