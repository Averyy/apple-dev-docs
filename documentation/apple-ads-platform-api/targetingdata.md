# TargetingData

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The shared include and exclude pattern for all ad group and campaign targeting dimensions.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object TargetingData
```

#### Discussion

`TargetingData` is the shared include/exclude pattern for all ad group targeting dimensions. The `include` array restricts delivery to the specified values. The `exclude` array blocks delivery to those values. When you set both arrays, `include` takes precedence over `exclude` for overlapping values.

- **Not all dimensions support both arrays.** For `AdGroupTargeting`, only `appCategory` and `appDownloader` support both `include` and `exclude`. All other ad group targeting dimensions are include-only.
- For `CampaignTargeting`, all three dimensions (`supplySource`, `supplyPlacement`, `countryOrRegion`) are include-only. See the per-dimension support table in [`AdGroupTargeting`](adgrouptargeting.md).

This object is embedded within [`CampaignTargeting`](campaigntargeting.md) fields `supplySource`, `supplyPlacement`, and `countryOrRegion`, which control the ad channel, placement, and geographic markets for a campaign.

[`AdGroupTargeting`](adgrouptargeting.md) also embeds `TargetingData` within fields such as `country`, `deviceClass`, `gender`, `minAge`, and others, which refine audience and delivery within that campaign. The valid values for each field depend on the targeting dimension: `supplySource` accepts `APPSTORE` and `MAPS`, while `deviceClass` accepts `IPHONE` and `IPAD`.

##### Example

```json
{
  "include": [
    "APPSTORE"
  ],
  "exclude": [
    "MAPS"
  ]
}
```

## Properties

- `include` ([string]): Criteria to include in targeting. Mutable.
- `exclude` ([string]): Criteria to exclude from targeting. Mutable.

## See Also

- [object AdGroup](adgroup.md)
  Primary unit governing targeting, bid strategy, pricing model, and scheduling within a campaign.
- [object AdGroupCreate](adgroupcreate.md)
  The request body for creating a new ad group.
- [object AdGroupUpdate](adgroupupdate.md)
  The request body for updating an existing ad group.
- [object AdGroupResponse](adgroupresponse.md)
  The response object for an ad group operation.
- [object AdGroupQueryResponse](adgroupqueryresponse.md)
  The response object for an ad group query, containing matched results and pagination metadata.
- [object AdGroupTargeting](adgrouptargeting.md)
  The comprehensive audience and placement configuration for an ad group.
- [object AdGroupTargetingCreate](adgrouptargetingcreate.md)
  The targeting configuration for creating a new ad group, specifying audience dimensions to include or exclude.
- [object AdGroupTargetingUpdate](adgrouptargetingupdate.md)
  The targeting configuration for updating an existing ad group, specifying audience dimensions to include or exclude.
- [object BidStrategy](bidstrategy.md)
  Defines how an ad group or campaign competes in auctions, including bid type, optimization goal, and bid amount.
- [object BidStrategyCreate](bidstrategycreate.md)
  The creation payload for configuring a bid strategy on an ad group or campaign.
- [object BidStrategyUpdate](bidstrategyupdate.md)
  The request body for updating a bid strategy on an ad group or campaign.
- [object CPAGoal](cpagoal.md)
  A deprecated cost-per-acquisition goal value. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object CPAGoalCreate](cpagoalcreate.md)
  The deprecated request payload for setting a cost-per-acquisition goal. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object CPAGoalUpdate](cpagoalupdate.md)
  The deprecated request payload for updating a cost-per-acquisition goal. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object TargetingDataCreate](targetingdatacreate.md)
  A targeting dimension value set for creating ad group or campaign targeting, specifying values to include or exclude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/targetingdata)*