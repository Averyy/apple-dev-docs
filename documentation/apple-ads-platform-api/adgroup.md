# AdGroup

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Primary unit governing targeting, bid strategy, pricing model, and scheduling within a campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroup
```

#### Discussion

An `AdGroup` is the primary unit for governing ad delivery within a campaign. Multiple ad groups within a campaign allow different targeting strategies, bids, and schedules to compete and optimize within the same promoted app or brand.

Fields marked **Filterable** in the dictionary keys work as filter criteria in query endpoint requests. See [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md) for details on constructing queries.

##### Example

```json
{
  "id": 555666777,
  "name": "AwayFinder iOS — New Users 18-34",
  "adAccountId": 123456789,
  "campaignId": 444555666,
  "startTime": "2025-09-01T00:00:00.000",
  "endTime": "2025-12-31T23:59:59.000",
  "pricingModel": "CPT",
  "automatedKeywordsOptIn": false,
  "automatedKeywordsRequired": false,
  "status": "ENABLED",
  "systemStatus": "RUNNING",
  "systemStatusReasons": [],
  "systemStatusLimitingReasons": [],
  "displayStatus": "RUNNING",
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bidStrategyGoal": "TAP",
    "bid": {
      "amount": "5.00",
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
    },
    "appDownloader": {
      "include": [
        "123456789"
      ]
    }
  },
  "cpaCap": null,
  "deleted": false,
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000"
}
```

## Topics

### Dictionaries
- [object AdGroup.BidStrategy](adgroup/bidstrategy-data.dictionary.md)
  Defines how this ad group competes in auctions, including bid type, optimization goal, and bid amount.
- [object AdGroup.CpaCap](adgroup/cpacap-data.dictionary.md)
  A deprecated cost-per-acquisition goal value. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object AdGroup.Targeting](adgroup/targeting-data.dictionary.md)
  The comprehensive audience and placement configuration for an ad group.
### Type Aliases
- [type AdGroup.DisplayStatus](adgroup/displaystatus-data.typealias.md)
  Derived display status for an ad group, combining advertiser-set status with system status.
- [type AdGroup.PricingModel](adgroup/pricingmodel-data.typealias.md)
  The unit of ad delivery an ad group is charged for, independent of how the account funds spend.
- [type AdGroup.Status](adgroup/status-data.typealias.md)
  Advertiser-configurable serving status for an ad group.
- [type AdGroup.SystemStatus](adgroup/systemstatus-data.typealias.md)
  System-derived operational status reflecting whether an ad group is actively serving.
- [type AdGroup.SystemStatusLimitingReasons](adgroup/systemstatuslimitingreasons-data.typealias.md)
  Reasons that limit delivery for an ad group without fully stopping it.
- [type AdGroup.SystemStatusReasons](adgroup/systemstatusreasons-data.typealias.md)
  Reasons that can cause an ad group’s system status to be `NOT_RUNNING`.

## Properties

- `name` (string): The advertiser-given name of this ad group. Mutable. Filterable: EQUALS, STARTS_WITH.
- `adAccountId` (int64): The ad account this ad group belongs to. Read-only.
- `campaignId` (int64): The campaign this ad group belongs to. Immutable after creation. Filterable: EQUALS.
- `startTime` (date-time): Ad group schedule start time. ISO 8601 format, for example `2025-09-01T00:00:00.000`. Mutable. Filterable: LESS_THAN, GREATER_THAN.
- `endTime` (date-time): Ad group schedule end time. ISO 8601 format, for example `2025-12-31T23:59:59.000`. Mutable. Filterable: LESS_THAN, GREATER_THAN.
- `pricingModel` (AdGroup.PricingModel): The pricing model for this ad group. Values: `CPA`, `CPM`, `CPT`. See [`AdGroup.PricingModel`](adgroup/pricingmodel-data.typealias.md). Immutable after creation. Must match the parent campaign’s billing event.
- `automatedKeywordsOptIn` (boolean): Opt in to Search Match, which automatically matches search terms without requiring explicit keywords. Mutable.
- `status` (AdGroup.Status): Advertiser-configurable status for this ad group. See [`AdGroupStatus`](adgroupstatus.md). Mutable. Filterable: EQUALS, IN.
- `systemStatus` (AdGroup.SystemStatus): System-computed operational status reflecting the ad group’s current serving state. See [`AdGroupSystemStatus`](adgroupsystemstatus.md). Read-only.
- `systemStatusReasons` ([AdGroup.SystemStatusReasons]): System-applied reasons that contribute to the current `systemStatus`. See [`AdGroupSystemStatusReason`](adgroupsystemstatusreason.md) for all values. Read-only.
- `systemStatusLimitingReasons` ([AdGroup.SystemStatusLimitingReasons]): System-applied reasons that limit delivery below maximum potential. See [`AdGroupSystemLimitedStatusReason`](adgroupsystemlimitedstatusreason.md) for details. Read-only.
- `automatedKeywordsRequired` (boolean): Auto keyword generation required. Immutable after creation.
- `displayStatus` (AdGroup.DisplayStatus): System-computed, rolled-up delivery state combining `status` and `systemStatus` into a single delivery label, more intuitive than a binary running/not-running signal. See [`AdGroupDisplayStatus`](adgroupdisplaystatus.md). Read-only.
- `bidStrategy` (AdGroup.BidStrategy): The bid strategy for this ad group. If omitted, the campaign-level bid strategy applies. See [`AdGroup.BidStrategy`](adgroup/bidstrategy-data.dictionary.md). Mutable.
- `targeting` (AdGroup.Targeting): Targeting configuration for this ad group. See [`AdGroupTargeting`](adgrouptargeting.md). Mutable.
- `id` (int64): The unique identifier for this ad group. Read-only. Filterable: EQUALS, IN.
- `creationTime` (date-time): Timestamp when the ad group was created. Read-only.
- `modificationTime` (date-time): Timestamp of the last modification to the ad group. Read-only.
- `deleted` (boolean): Indicates if the ad group has been deleted. Read-only. Filterable: EQUALS.
- `cpaCap` (AdGroup.CpaCap): Deprecated. Use `bidStrategy` with `MAX_CONVERSIONS` instead. See [`CPAGoal`](cpagoal.md).

## See Also

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
- [object TargetingData](targetingdata.md)
  The shared include and exclude pattern for all ad group and campaign targeting dimensions.
- [object TargetingDataCreate](targetingdatacreate.md)
  A targeting dimension value set for creating ad group or campaign targeting, specifying values to include or exclude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup)*