# AdGroupUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating an existing ad group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupUpdate
```

#### Discussion

`AdGroupUpdate` is the request payload for modifying an existing ad group. Include only the fields you want to change. The `pricingModel` and `automatedKeywordsRequired` fields are immutable.

To manage keywords and negative keywords, use the dedicated keyword endpoints.

##### Example

```json
{
  "name": "AwayFinder iOS — New Users 18-34",
  "startTime": "2025-09-01T00:00:00.000",
  "endTime": "2025-12-31T23:59:59.000",
  "automatedKeywordsOptIn": false,
  "status": "ENABLED",
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bidStrategyGoal": "TAP",
    "bid": {
      "amount": "7.50",
      "currency": "USD"
    }
  },
  "targeting": {
    "deviceClass": {
      "include": [
        "IPHONE"
      ]
    },
    "minAge": {
      "include": [
        "18"
      ]
    },
    "maxAge": {
      "include": [
        "34"
      ]
    }
  }
}
```

## Topics

### Dictionaries
- [object AdGroupUpdate.BidStrategy](adgroupupdate/bidstrategy-data.dictionary.md)
  The request body for updating a bid strategy on an ad group or campaign.
- [object AdGroupUpdate.CpaCap](adgroupupdate/cpacap-data.dictionary.md)
  The deprecated request payload for updating a cost-per-acquisition goal. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object AdGroupUpdate.Targeting](adgroupupdate/targeting-data.dictionary.md)
  The targeting configuration for updating an existing ad group, specifying audience dimensions to include or exclude.
### Type Aliases
- [type AdGroupUpdate.Status](adgroupupdate/status-data.typealias.md)
  Advertiser-configurable serving status for an ad group.

## Properties

- `name` (string): The advertiser-given name of this ad group. Mutable.
- `startTime` (date-time): The scheduled start date and time of this ad group in ISO 8601 format. Mutable.
- `endTime` (date-time): The scheduled end date and time. Omit to inherit the campaign end date. Mutable.
- `automatedKeywordsOptIn` (boolean): Opt in to Search Match, which automatically matches search terms without requiring explicit keywords. Mutable.
- `status` (AdGroupUpdate.Status): Advertiser-configurable serving status. Use to pause (`PAUSED`) or resume (`ENABLED`) this ad group. See [`AdGroupStatus`](adgroupstatus.md). Mutable.
- `automatedKeywordsRequired` (boolean): Immutable. Set at creation via `AdGroupCreate`. Any value sent here is ignored.
- `bidStrategy` (AdGroupUpdate.BidStrategy): The bid strategy for this ad group. `bidStrategyType` and `bidStrategyGoal` must be sent together and matched per the pairings in [`AdGroupUpdate.BidStrategy`](adgroupupdate/bidstrategy-data.dictionary.md). See [`AdGroupUpdate.BidStrategy`](adgroupupdate/bidstrategy-data.dictionary.md) and [`BidStrategyUpdate`](bidstrategyupdate.md). Mutable.
- `targeting` (AdGroupUpdate.Targeting): Audience and placement targeting configuration for this ad group. See [`AdGroupTargetingUpdate`](adgrouptargetingupdate.md). Mutable.
- `cpaCap` (AdGroupUpdate.CpaCap): Deprecated. Still accepted on update for backward compatibility, but use `bidStrategy` with `MAX_CONVERSIONS` instead. See [`CPAGoalUpdate`](cpagoalupdate.md).

## See Also

- [object AdGroup](adgroup.md)
  Primary unit governing targeting, bid strategy, pricing model, and scheduling within a campaign.
- [object AdGroupCreate](adgroupcreate.md)
  The request body for creating a new ad group.
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
- [object TargetingData](targetingdata.md)
  The shared include and exclude pattern for all ad group and campaign targeting dimensions.
- [object TargetingDataCreate](targetingdatacreate.md)
  A targeting dimension value set for creating ad group or campaign targeting, specifying values to include or exclude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupupdate)*