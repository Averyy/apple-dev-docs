# AdGroupTargetingCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The targeting configuration for creating a new ad group, specifying audience dimensions to include or exclude.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingCreate
```

#### Overview

For valid location identifier values and geographic lookup, see [`Geo Targeting Endpoints`](geo-targeting-endpoints.md).

## Topics

### Dictionaries
- [object AdGroupTargetingCreate.AdminArea](adgrouptargetingcreate/adminarea-data.dictionary.md)
  State or province (administrative area) targeting.
- [object AdGroupTargetingCreate.AppCategory](adgrouptargetingcreate/appcategory-data.dictionary.md)
  App category targeting based on App Store categories, with include and exclude support.
- [object AdGroupTargetingCreate.AppDownloader](adgrouptargetingcreate/appdownloader-data.dictionary.md)
  Targeting based on whether users have downloaded specific apps, identified by Adam ID.
- [object AdGroupTargetingCreate.Country](adgrouptargetingcreate/country-data.dictionary.md)
  Country-level geographic targeting.
- [object AdGroupTargetingCreate.Daypart](adgrouptargetingcreate/daypart-data.dictionary.md)
  Hour-of-day targeting, restricting delivery to specific one-hour slots in a 7-day week grid.
- [object AdGroupTargetingCreate.DeviceClass](adgrouptargetingcreate/deviceclass-data.dictionary.md)
  Device class targeting (for example, `IPHONE` or `IPAD`).
- [object AdGroupTargetingCreate.Gender](adgrouptargetingcreate/gender-data.dictionary.md)
  Gender targeting for the audience.
- [object AdGroupTargetingCreate.Locality](adgrouptargetingcreate/locality-data.dictionary.md)
  City or locality targeting.
- [object AdGroupTargetingCreate.LocationGroup](adgrouptargetingcreate/locationgroup-data.dictionary.md)
  Location group targeting, restricting delivery to the business locations in specified groups.
- [object AdGroupTargetingCreate.MaxAge](adgrouptargetingcreate/maxage-data.dictionary.md)
  Maximum age targeting, setting the upper bound of the target age range.
- [object AdGroupTargetingCreate.MinAge](adgrouptargetingcreate/minage-data.dictionary.md)
  Minimum age targeting, setting the lower bound of the target age range.
- [object AdGroupTargetingCreate.PostalCode](adgrouptargetingcreate/postalcode-data.dictionary.md)
  Postal code geographic targeting.
- [object AdGroupTargetingCreate.Radius](adgrouptargetingcreate/radius-data.dictionary.md)
  Radius targeting used with Apple Maps campaigns to restrict delivery to users within a given proximity of the brand’s locations.

## Properties

- `country` (AdGroupTargetingCreate.Country): Country-level geographic targeting. Include a country ID returned by the Geo Search API. See [`TargetingDataCreate`](targetingdatacreate.md).
- `adminArea` (AdGroupTargetingCreate.AdminArea): Administrative area (state or province) targeting. Include admin area IDs returned by the Geo API. See [`TargetingDataCreate`](targetingdatacreate.md).
- `locality` (AdGroupTargetingCreate.Locality): City or locality targeting. Include locality IDs returned by the Geo API. See [`TargetingDataCreate`](targetingdatacreate.md).
- `postalCode` (AdGroupTargetingCreate.PostalCode): Postal code geographic targeting. Include postal code IDs returned by the Geo API. See [`TargetingDataCreate`](targetingdatacreate.md).
- `radius` (AdGroupTargetingCreate.Radius): Radius targeting, used with Apple Maps campaigns. Valid values: `CLOSE`, `MEDIUM`, `FAR`. In practice, radius targeting is applied on `MAPS_SEARCH_RESULTS` campaigns and should not be combined with geo location targeting, but the API does not enforce this constraint at the schema level. See [`TargetingDataCreate`](targetingdatacreate.md).
- `deviceClass` (AdGroupTargetingCreate.DeviceClass): Device class targeting (e.g., `IPHONE`, `IPAD`). See [`TargetingDataCreate`](targetingdatacreate.md).
- `minAge` (AdGroupTargetingCreate.MinAge): Minimum age targeting for the audience. Minimum value is 18, maximum value is 64. See [`TargetingDataCreate`](targetingdatacreate.md).
- `maxAge` (AdGroupTargetingCreate.MaxAge): Maximum age targeting for the audience. Minimum value is 18, maximum value is 64. To target users 65 and older, omit `maxAge`, or send `include` as `null`. See [`TargetingDataCreate`](targetingdatacreate.md).
- `gender` (AdGroupTargetingCreate.Gender): Gender targeting for the audience. Valid values: `M`, `F`. See [`TargetingDataCreate`](targetingdatacreate.md).
- `appCategory` (AdGroupTargetingCreate.AppCategory): App category targeting based on App Store categories. Category ID `100` is a special value representing the same category as the promoted app. A value of `100` in `include` means you are targeting apps in the same category as your app, and a value of `100` in `exclude` means you aren’t. See [`TargetingDataCreate`](targetingdatacreate.md).
- `appDownloader` (AdGroupTargetingCreate.AppDownloader): Reach or suppress users based on whether they’ve downloaded specific apps, identified by Adam ID. Use `include` to reach users who have downloaded those apps. Use `exclude` to suppress users who already have your app (acquisition targeting). Look up Adam IDs via [`Search for Apps`](searches-for-a-list-of-apps.md). See [`TargetingDataCreate`](targetingdatacreate.md).
- `daypart` (AdGroupTargetingCreate.Daypart): Time-of-day targeting (dayparting). Include-only. The `exclude` array is not supported for this dimension. Values are slot integers (0–167). For the full slot reference, see [`AdGroupTargeting`](adgrouptargeting.md). See [`TargetingDataCreate`](targetingdatacreate.md).
- `locationGroup` (AdGroupTargetingCreate.LocationGroup): Location group targeting for Apple Maps campaigns. See [`TargetingDataCreate`](targetingdatacreate.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingcreate)*