# CampaignTargetingCreate.SupplyPlacement

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The specific placement within a supply source where a new campaign’s ads are eligible to appear.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object CampaignTargetingCreate.SupplyPlacement
```

#### Discussion

The `supplyPlacement` field is **include-only**; setting `exclude` has no effect. Each placement belongs to exactly one [`CampaignTargetingCreate.SupplySource`](campaigntargetingcreate/supplysource-data.dictionary.md):

| Value | Supply source | Placement |
| --- | --- | --- |
| `APPSTORE_SEARCH_RESULTS` | `APPSTORE` | App Store Search results |
| `APPSTORE_SEARCH_TAB` | `APPSTORE` | App Store Search tab |
| `APPSTORE_TODAY_TAB` | `APPSTORE` | App Store Today tab |
| `APPSTORE_PRODUCT_PAGES` | `APPSTORE` | App Store Product pages |
| `MAPS_SEARCH_RESULTS` | `MAPS` | Apple Maps Search results |
| `MAPS_SEARCH_HOME` | `MAPS` | Apple Maps Search home |

Uses the [`TargetingDataCreate`](targetingdatacreate.md) `include`/`exclude` shape.

> **Note**: To target both `MAPS_SEARCH_RESULTS` and `MAPS_SEARCH_HOME`, omit `supplyPlacement` from `targeting` entirely rather than listing both values in `include`. Listing multiple `MAPS` placement values together is rejected. Choose this at create time. A campaign created with a single placement can’t be widened to target both placements later through [`CampaignTargetingUpdate.SupplyPlacement`](campaigntargetingupdate/supplyplacement-data.dictionary.md), since omitting the field on update leaves the current placement unchanged instead of expanding it. Widening to both placements requires creating a new campaign.

## Properties

- `include` ([string]): Placements to include in targeting.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingcreate/supplyplacement-data.dictionary)*