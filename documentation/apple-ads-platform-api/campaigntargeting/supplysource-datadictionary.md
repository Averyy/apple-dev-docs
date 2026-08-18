# CampaignTargeting.SupplySource

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The supply source where a campaign’s ads are eligible to appear.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargeting.SupplySource
```

#### Discussion

`supplySource` is **include-only**; setting `exclude` has no effect. Valid values:

| Value | Ad channel |
| --- | --- |
| `APPSTORE` | App Store ads |
| `MAPS` | Apple Maps |

Each source has its own set of placements. See [`CampaignTargeting.SupplyPlacement`](campaigntargeting/supplyplacement-data.dictionary.md) for the full placement list, and [`TargetingData`](targetingdata.md) for the `include`/`exclude` shape.

## Properties

- `include` ([string]): Supply sources to include in targeting. Mutable.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set. Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargeting/supplysource-data.dictionary)*