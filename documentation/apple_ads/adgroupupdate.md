# AdGroupUpdate

**Framework**: Apple Ads  
**Kind**: dictionary

The list of ad group fields that are updatable.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object AdGroupUpdate
```

## Properties

- `automatedKeywordsOptIn` (boolean): The parameter for enabling and disabling Search Match. If `true`, the system automatically adds optimized keywords in addition to those you explicitly add to the ad group. See the Enable and Disable Search Match section of [`Ad Groups`](ad-groups.md).
- `cpaGoal` (Money): The cost-per-acquisition goal. Cannot be set for ad groups in `MAX_CONVERSIONS` campaigns. Returned as `null` for Max Conversions ad groups. > ❗ **Important**:  You can update the `cpaGoal` only in campaigns that use the `APPSTORE_SEARCH_RESULTS` supply source. This field is updatable.
- `defaultBidAmount` (Money): The default maximum cost-per-tap or cost-per-impression bid for the ad group. This field is updatable.
- `endTime` (date-time): The scheduled end date and time for the ad group, which the system determines from the ad group with the latest end time. - The `endTime` is updatable until you reach the designated time.
- The `endTime` must be after the `startTime`.
- The `endTime` must be in UTC.
- `name` (string): The unique name of the ad group. Responses don’t include deleted ad groups. This field is updatable.
- `startTime` (date-time): The scheduled start date and time for the ad group with the earliest start time in the campaign. - The `startTime` must be greater than the current time, and before the campaign `endTime`, if you set it.
- If you don’t set a `startTime`, the campaign defaults to the campaign request timestamp and the `startTime` is updatable until you reach the designated time.
- The `startTime` must be in UTC.
- `status` (string): The user-controlled status to enable or pause the ad group. This field is updatable.
- `targetingDimensions` (TargetingDimensions): The targeting criteria to narrow the audience. Targeting options include age, gender, geolocation, daypart, device, and app downloaders. This field is updatable.

## See Also

- [object AdGroup](adgroup.md)
  The response to ad group requests.
- [object AdGroupResponse](adgroupresponse.md)
  A container for the ad group response body.
- [object AdGroupListResponse](adgrouplistresponse.md)
  The response details of ad group requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/adgroupupdate)*