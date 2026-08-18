# CampaignTargetingCreate.SupplyPlacement

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The specific placement within a supply source where a new campaign’s ads are eligible to appear.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargetingCreate.SupplyPlacement
```

#### Discussion

`supplyPlacement` is **include-only**; setting `exclude` has no effect. Each placement belongs to exactly one [`CampaignTargetingCreate.SupplySource`](campaigntargetingcreate/supplysource-data.dictionary.md):

| Value | Supply source | Placement |
| --- | --- | --- |
| `APPSTORE_SEARCH_RESULTS` | `APPSTORE` | App Store Search results |
| `APPSTORE_SEARCH_TAB` | `APPSTORE` | App Store Search tab |
| `APPSTORE_TODAY_TAB` | `APPSTORE` | App Store Today tab |
| `APPSTORE_PRODUCT_PAGES` | `APPSTORE` | App Store Product pages |
| `MAPS_SEARCH_RESULTS` | `MAPS` | Apple Maps Search results |
| `MAPS_SEARCH_HOME` | `MAPS` | Apple Maps Search home |

Uses the [`TargetingDataCreate`](targetingdatacreate.md) `include`/`exclude` shape.

## Properties

- `include` ([string]): Placements to include in targeting.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingcreate/supplyplacement-data.dictionary)*