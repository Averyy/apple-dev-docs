# AdGroupQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for an ad group query, containing matched results and pagination metadata.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupQueryResponse
```

#### Discussion

`AdGroupQueryResponse` is returned by the ad group query endpoint.

Use the `QueryRequest` body with `filters` to scope results to a specific campaign, status, or set of ad group IDs.

##### Example

```json
{
  "result": [
    {
      "id": 555666777,
      "name": "AwayFinder - Broad Match",
      "adAccountId": 123456789,
      "campaignId": 444555666,
      "startTime": "2025-09-01T08:00:00.000",
      "endTime": null,
      "pricingModel": "CPT",
      "automatedKeywordsOptIn": true,
      "status": "ENABLED",
      "systemStatus": "RUNNING",
      "systemStatusReasons": [],
      "systemStatusLimitingReasons": [],
      "automatedKeywordsRequired": false,
      "displayStatus": "RUNNING",
      "bidStrategy": {
        "bidStrategyType": "MANUAL_CPT",
        "bidStrategyGoal": "TAP",
        "bid": {
          "amount": "5.00",
          "currency": "USD"
        }
      },
      "targeting": null,
      "creationTime": "2025-09-01T08:00:00.000",
      "modificationTime": "2025-09-01T08:00:00.000",
      "deleted": false,
      "cpaCap": null
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20,
    "totalCount": 1
  }
}
```

## Properties

- `result` ([AdGroup]): The filtered, sorted, and paginated set of matching `AdGroup` objects. See [`AdGroup`](adgroup.md). Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the response, including `offset`, `pageSize`, and `totalCount`, to support offset-based navigation through large result sets. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error information if the request encountered an error. See [`Error`](error.md). Read-only.

## See Also

- [object AdGroup](adgroup.md)
  Primary unit governing targeting, bid strategy, pricing model, and scheduling within a campaign.
- [object AdGroupCreate](adgroupcreate.md)
  The request body for creating a new ad group.
- [object AdGroupUpdate](adgroupupdate.md)
  The request body for updating an existing ad group.
- [object AdGroupResponse](adgroupresponse.md)
  The response object for an ad group operation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupqueryresponse)*