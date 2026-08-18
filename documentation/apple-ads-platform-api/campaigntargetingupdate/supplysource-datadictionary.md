# CampaignTargetingUpdate.SupplySource

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The supply source where an existing campaign’s ads are eligible to appear.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargetingUpdate.SupplySource
```

#### Discussion

`supplySource` is **include-only**; setting `exclude` has no effect. Omit to leave unchanged. Valid values:

| Value | Ad channel |
| --- | --- |
| `APPSTORE` | App Store ads |
| `MAPS` | Apple Maps |

Each source has its own set of placements. See [`CampaignTargetingUpdate.SupplyPlacement`](campaigntargetingupdate/supplyplacement-data.dictionary.md) for the full placement list, and [`TargetingDataUpdate`](targetingdataupdate.md) for the `include`/`exclude` shape.

## Properties

- `include` ([string]): Supply sources to include in targeting. Omit to leave unchanged. Mutable.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set. Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingupdate/supplysource-data.dictionary)*