# AdGroup

**Framework**: Apple Ads  
**Kind**: dictionary

The response to ad group requests.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object AdGroup
```

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

## Properties

- `automatedKeywordsOptIn` (boolean): The parameter for enabling and disabling Search Match. If `true`, the system automatically adds optimized keywords in addition to those you explicitly add to the ad group. Can be toggled `true` or `false` for standard ad groups in `MAX_CONVERSIONS` campaigns. Required to be `true` for automated ad groups. See [`Create an Ad Group`](create-an-ad-group.md). See [`Ad Groups`](ad-groups.md). You can use the `EQUALS` selector [`Condition`](condition.md) operator with [`Find Ad Groups`](find-ad-groups.md).
- `automatedKeywordsRequired` (boolean): A read-only field indicating if this is the automated ad group. Defaults to `false`. An automated ad group must exist for Maximize Conversions campaigns to run. See [`Create an Ad Group`](create-an-ad-group.md).
- `biddingStrategy` (string): The bid strategy for the campaign. See [`Campaigns`](campaigns.md)
- `campaignId` (int64): The unique identifier for a campaign. You can use the `EQUALS`, `IN`, and `STARTSWITH` selector [`Condition`](condition.md) operators with [`Find Ad Groups`](find-ad-groups.md).
- `cpaGoal` (Money): Optional. The cost-per-acquisition goal. Cannot be set for ad groups in `MAX_CONVERSIONS` campaigns. Returned as `null` for Max Conversions ad groups. > ❗ **Important**:  You can update the `cpaGoal` only in campaigns that use the `APPSTORE_SEARCH_RESULTS` supply source.
- `defaultBidAmount` (Money) *(required)*: The default maximum cost-per-tap or cost-per-impression bid for the ad group. You can use the `EQUALS, GREATER_THAN, and LESS_THAN` selector [`Condition`](condition.md) operators with [`Find Ad Groups`](find-ad-groups.md).
- `deleted` (boolean): The indicator of whether the ad group is soft-deleted. This includes keywords that belong to an ad group. You can use the `EQUALS` and `IN` selector [`Condition`](condition.md) operators with [`Find Ad Groups`](find-ad-groups.md).
- `displayStatus` (string): The status of the ad group. The status resolves according to `servingStatus` and additional criteria.
- `endTime` (date-time): The scheduled end time and date for the ad group, which the system determines from the ad group with the latest end time. - The `endTime` must be after the `startTime`.
- The `endTime` is updatable until you reach the designated time.
- The `endTime` must be in UTC.
- `id` (int64): The unique identifier for the ad group that you can use as `adGroupId` in endpoint resources. You can use the `EQUALS`, `IN`, and `STARTSWITH` selector [`Condition`](condition.md) operators with [`Find Ad Groups`](find-ad-groups.md).
- `modificationTime` (date-time): The date and time of the most recent modification of the object.
- `name` (string) *(required)*: The unique name of the ad group. Responses don’t include deleted ad groups. You can use the `EQUALS`, `IN`, and `STARTSWITH` selector [`Condition`](condition.md) operators with [`Find Ad Groups`](find-ad-groups.md).
- `orgId` (int64): The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/).
- `paymentModel` (string): The payment model that you set through [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/). If you don’t set a payment model, campaigns can’t run. See [`PaymentModel`](paymentmodel.md) for value descriptions. If you don’t select a payment model, you can still create campaigns. You must select a payment model before a campaign is eligible to run. See [`BudgetOrder`](budgetorder.md) for details about setting a payment model.
- `pricingModel` (string) *(required)*: The type of pricing model for a bid. See [`PricingModel`](pricingmodel.md) for value descriptions.
- `servingStateReasons` ([string]): A list of reasons that displays when an ad group isn’t running.
- `servingStatus` (string): The status of whether the ad group is serving.
- `startTime` (date-time) *(required)*: The scheduled start date and time for the ad group with the earliest start time in the campaign. - The `startTime` must be greater than the current time, and before the campaign `endTime`, if you set it.
- If you don’t set a `startTime`, the campaign defaults to the campaign request timestamp and the `startTime` is updatable until you reach the designated time.
- The `startTime` must be in UTC.
- `status` (string): The user-controlled status to enable or pause the ad group. This field is updatable. You can use the `EQUALS` selector [`Condition`](condition.md) operator with [`Find Ad Groups`](find-ad-groups.md).
- `targetingDimensions` (TargetingDimensions): The targeting criteria to narrow the audience.

## See Also

- [object AdGroupUpdate](adgroupupdate.md)
  The list of ad group fields that are updatable.
- [object AdGroupResponse](adgroupresponse.md)
  A container for the ad group response body.
- [object AdGroupListResponse](adgrouplistresponse.md)
  The response details of ad group requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/adgroup)*