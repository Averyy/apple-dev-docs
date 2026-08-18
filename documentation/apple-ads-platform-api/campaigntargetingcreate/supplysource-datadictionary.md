# CampaignTargetingCreate.SupplySource

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The supply source where a new campaign’s ads are eligible to appear.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargetingCreate.SupplySource
```

#### Discussion

`supplySource` is **include-only**; setting `exclude` has no effect. Valid values:

| Value | Ad channel |
| --- | --- |
| `APPSTORE` | App Store ads |
| `MAPS` | Apple Maps |

Each source has its own set of placements. See [`CampaignTargetingCreate.SupplyPlacement`](campaigntargetingcreate/supplyplacement-data.dictionary.md) for the full placement list, and [`TargetingDataCreate`](targetingdatacreate.md) for the `include`/`exclude` shape.

## Properties

- `include` ([string]): Supply sources to include in targeting.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingcreate/supplysource-data.dictionary)*