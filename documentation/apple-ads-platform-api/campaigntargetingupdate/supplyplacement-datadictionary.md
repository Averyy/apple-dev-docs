# CampaignTargetingUpdate.SupplyPlacement

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The specific placement within a supply source where an existing campaign’s ads are eligible to appear.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargetingUpdate.SupplyPlacement
```

#### Discussion

`supplyPlacement` is **include-only**; setting `exclude` has no effect. Omit to leave unchanged. Each placement belongs to exactly one [`CampaignTargetingUpdate.SupplySource`](campaigntargetingupdate/supplysource-data.dictionary.md):

| Value | Supply source | Placement |
| --- | --- | --- |
| `APPSTORE_SEARCH_RESULTS` | `APPSTORE` | App Store Search results |
| `APPSTORE_SEARCH_TAB` | `APPSTORE` | App Store Search tab |
| `APPSTORE_TODAY_TAB` | `APPSTORE` | App Store Today tab |
| `APPSTORE_PRODUCT_PAGES` | `APPSTORE` | App Store Product pages |
| `MAPS_SEARCH_RESULTS` | `MAPS` | Apple Maps Search results |
| `MAPS_SEARCH_HOME` | `MAPS` | Apple Maps Search home |

Uses the [`TargetingDataUpdate`](targetingdataupdate.md) `include`/`exclude` shape.

## Properties

- `include` ([string]): Placements to include in targeting. Omit to leave unchanged. Mutable.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set. Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingupdate/supplyplacement-data.dictionary)*