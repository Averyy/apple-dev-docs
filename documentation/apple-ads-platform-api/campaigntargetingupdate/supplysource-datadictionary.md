# CampaignTargetingUpdate.SupplySource

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The supply source where an existing campaign’s ads are eligible to appear.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object CampaignTargetingUpdate.SupplySource
```

#### Discussion

The `supplySource` field is fixed at creation and can’t be changed by update. Including this field in an update request is unsupported, even when the value matches the campaign’s current `supplySource`. Valid values:

| Value | Ad channel |
| --- | --- |
| `APPSTORE` | App Store ads |
| `MAPS` | Apple Maps |

Each source has its own set of placements. See [`CampaignTargetingUpdate.SupplyPlacement`](campaigntargetingupdate/supplyplacement-data.dictionary.md) for the full placement list, and [`TargetingDataUpdate`](targetingdataupdate.md) for the `include`/`exclude` shape.

## Properties

- `include` ([string]): Supply sources to include in targeting. Don’t set on update; the campaign’s `supplySource` can’t be changed after creation.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingupdate/supplysource-data.dictionary)*