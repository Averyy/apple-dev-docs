# CampaignTargetingCreate.CountryOrRegion

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The countries or regions where a new campaign’s ads are eligible to serve.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignTargetingCreate.CountryOrRegion
```

#### Discussion

`countryOrRegion` uses ISO 3166-1 alpha-2 country codes (for example, `US`, `CA`, `GB`). It’s include-only: the `exclude` array is not supported at the campaign level. See [`TargetingDataCreate`](targetingdatacreate.md) for the `include`/`exclude` shape.

Only include markets where the promoted app or brand is available. See [`CampaignTargetingCreate.SupplySource`](campaigntargetingcreate/supplysource-data.dictionary.md) and [`CampaignTargetingCreate.SupplyPlacement`](campaigntargetingcreate/supplyplacement-data.dictionary.md) for the other targeting dimensions.

## Properties

- `include` ([string]): Countries or regions to include in targeting.
- `exclude` ([string]): Not supported at the campaign level. Has no effect if set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigntargetingcreate/countryorregion-data.dictionary)*