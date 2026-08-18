# CampaignTargeting.SupplyPlacement

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The specific placement within a supply source where a campaign’s ads are eligible to appear.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargeting.SupplyPlacement
```

#### Discussion

`supplyPlacement` is **include-only**; setting `exclude` has no effect. Each placement belongs to exactly one [`CampaignTargeting.SupplySource`](campaigntargeting/supplysource-data.dictionary.md):

| Value | Supply source | Placement |
| --- | --- | --- |
| `APPSTORE_SEARCH_RESULTS` | `APPSTORE` | App Store Search results |
| `APPSTORE_SEARCH_TAB` | `APPSTORE` | App Store Search tab |
| `APPSTORE_TODAY_TAB` | `APPSTORE` | App Store Today tab |
| `APPSTORE_PRODUCT_PAGES` | `APPSTORE` | App Store Product pages |
| `MAPS_SEARCH_RESULTS` | `MAPS` | Apple Maps Search results |
| `MAPS_SEARCH_HOME` | `MAPS` | Apple Maps Search home |

Uses the [`TargetingData`](targetingdata.md) `include`/`exclude` shape.

## Properties

- `include` ([string]): Placements to include in targeting. Mutable.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set. Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargeting/supplyplacement-data.dictionary)*