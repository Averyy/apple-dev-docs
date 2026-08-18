# CampaignTargetingUpdate.CountryOrRegion

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The countries or regions where an existing campaign’s ads are eligible to serve.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargetingUpdate.CountryOrRegion
```

#### Discussion

`countryOrRegion` uses ISO 3166-1 alpha-2 country codes (for example, `US`, `CA`, `GB`). It’s include-only: the `exclude` array is not supported at the campaign level. Omit to leave unchanged. See [`TargetingDataUpdate`](targetingdataupdate.md) for the `include`/`exclude` shape.

Only include markets where the promoted app or brand is available. See [`CampaignTargetingUpdate.SupplySource`](campaigntargetingupdate/supplysource-data.dictionary.md) and [`CampaignTargetingUpdate.SupplyPlacement`](campaigntargetingupdate/supplyplacement-data.dictionary.md) for the other targeting dimensions.

## Properties

- `include` ([string]): Countries or regions to include in targeting. Omit to leave unchanged. Mutable.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set. Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingupdate/countryorregion-data.dictionary)*