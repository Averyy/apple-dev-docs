# AdGroupCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for creating a new ad group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupCreate
```

#### Discussion

`AdGroupCreate` is the request payload for creating a new ad group via `POST /v1/adgroups`.

You can’t create keywords or negative keywords inline. Create the ad group first, then add keywords and negative keywords with separate calls.

##### Example

```json
{
  "name": "AwayFinder iOS — New Users 18-34",
  "campaignId": 444555666,
  "startTime": "2025-09-01T00:00:00.000",
  "endTime": "2025-12-31T23:59:59.000",
  "pricingModel": "CPT",
  "automatedKeywordsOptIn": false,
  "status": "ENABLED",
  "automatedKeywordsRequired": false,
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bidStrategyGoal": "TAP",
    "bid": {
      "amount": "2.50",
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
  }
}
```

## Topics

### Dictionaries
- [object AdGroupCreate.BidStrategy](adgroupcreate/bidstrategy-data.dictionary.md)
  The creation payload for configuring a bid strategy on an ad group or campaign.
- [object AdGroupCreate.CpaCap](adgroupcreate/cpacap-data.dictionary.md)
  The deprecated request payload for setting a cost-per-acquisition goal. Use `bidStrategy` with `MAX_CONVERSIONS` instead.
- [object AdGroupCreate.Targeting](adgroupcreate/targeting-data.dictionary.md)
  The targeting configuration for creating a new ad group, specifying audience dimensions to include or exclude.
### Type Aliases
- [type AdGroupCreate.PricingModel](adgroupcreate/pricingmodel-data.typealias.md)
  The unit of ad delivery an ad group is charged for, independent of how the account funds spend.
- [type AdGroupCreate.Status](adgroupcreate/status-data.typealias.md)
  Advertiser-configurable serving status for an ad group.

## Properties

- `name` (string) *(required)*: The advertiser-given name of this ad group.
- `campaignId` (int64) *(required)*: The campaign this ad group belongs to. Immutable after creation.
- `startTime` (date-time): The scheduled start date and time of this ad group in ISO 8601 format.
- `endTime` (date-time): The scheduled end date and time. Omit to inherit the campaign end date.
- `pricingModel` (AdGroupCreate.PricingModel) *(required)*: The pricing model for this ad group (`CPA`, `CPM`, or `CPT`). Must match the campaign’s billing event: `CPT` pairs with `billingEvent: TAPS`, `CPM` pairs with `billingEvent: IMPRESSIONS`. See [`AdGroupCreate.PricingModel`](adgroupcreate/pricingmodel-data.typealias.md). Immutable after creation.
- `automatedKeywordsOptIn` (boolean): Auto opt-in for Search Match. When enabled, the system automatically targets additional relevant search terms beyond the explicit keyword list.
- `status` (AdGroupCreate.Status): Advertiser-configurable serving status. No default is applied when this field is omitted. See [`AdGroupStatus`](adgroupstatus.md).
- `automatedKeywordsRequired` (boolean): Whether automated keyword generation is required for this ad group.
- `bidStrategy` (AdGroupCreate.BidStrategy): The bid strategy for this ad group. If omitted, the campaign-level bid strategy applies. See [`BidStrategyCreate`](bidstrategycreate.md).
- `targeting` (AdGroupCreate.Targeting): Audience and placement targeting for this ad group (device class, age, gender, location, etc.). See [`AdGroupTargetingCreate`](adgrouptargetingcreate.md).
- `cpaCap` (AdGroupCreate.CpaCap): Deprecated. Use `bidStrategy` with `MAX_CONVERSIONS` instead. See [`CPAGoalCreate`](cpagoalcreate.md).

## See Also

- [object AdGroup](adgroup.md)
  Primary unit governing targeting, bid strategy, pricing model, and scheduling within a campaign.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupcreate)*