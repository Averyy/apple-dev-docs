# AdGroupResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for an ad group operation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupResponse
```

#### Discussion

`AdGroupResponse` is the single-item response envelope returned by create, update, and delete ad group operations.

##### Example

```json
{
  "result": {
    "id": 555666777,
    "name": "AwayFinder iOS — New Users 18-34",
    "adAccountId": 123456789,
    "campaignId": 444555666,
    "pricingModel": "CPT",
    "status": "ENABLED",
    "systemStatus": "RUNNING",
    "displayStatus": "RUNNING",
    "startTime": "2025-09-01T00:00:00.000",
    "endTime": "2025-12-31T23:59:59.000",
    "automatedKeywordsOptIn": false,
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
    },
    "deleted": false,
    "creationTime": "2025-01-10T08:00:00.000",
    "modificationTime": "2025-06-01T10:00:00.000"
  }
}
```

## Properties

- `result` (AdGroup): The affected `AdGroup` object in its post-operation state. Present on success. See [`AdGroup`](adgroup.md).
- `error` (Error): Structured details about what went wrong, of type `Error`. Present on failure, in place of `result`, for operational errors specific to the ad group request. HTTP-level errors (400, 401, 403, etc.) return a separate `ErrorResponse` body as the top-level response instead. See [`Error`](error.md).

## See Also

- [object AdGroup](adgroup.md)
  Primary unit governing targeting, bid strategy, pricing model, and scheduling within a campaign.
- [object AdGroupCreate](adgroupcreate.md)
  The request body for creating a new ad group.
- [object AdGroupUpdate](adgroupupdate.md)
  The request body for updating an existing ad group.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupresponse)*