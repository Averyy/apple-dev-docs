# AdGroupTargeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The comprehensive audience and placement configuration for an ad group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargeting
```

#### Discussion

`AdGroupTargeting` is the comprehensive audience and placement configuration for an ad group. [`CampaignTargeting`](campaigntargeting.md) establishes campaign-level supply source, placement, and geographic markets first, and `AdGroupTargeting` then refines audience and delivery within the bounds of that campaign.

Each field uses a `TargetingData` object with `include` and `exclude` arrays. Setting `exclude` on an include-only dimension has no effect.

Not every targeting dimension is meaningful for every campaign type in practice. The API represents every dimension as the same generic `TargetingData` shape, so campaign-type pairing is usage guidance rather than a constraint the schema enforces.

Combining multiple dimensions uses AND logic: a user must match all specified criteria to be eligible.

For valid location identifier values and geographic lookup, see [`Geo Targeting Endpoints`](geo-targeting-endpoints.md). For managing location groups used in `locationGroup` targeting, see [`Managing Location Groups`](location-groups-overview.md).

For a full request that embeds `targeting` alongside the other ad group fields, see [`Create an Ad Group`](post-adgroups.md) (create) and [`Update an Ad Group`](put-adgroups-_id_.md) (update).

##### Example

> **Note**: This example shows every available targeting dimension for illustration. In practice, include only the dimensions relevant to your campaign type, with values customized to your targeting needs.

```json
{
  "country": {
    "include": ["1125", "1107"]
  },
  "adminArea": {
    "include": ["9070", "12683"]
  },
  "locality": {
    "include": ["11390462"]
  },
  "postalCode": {
    "include": ["11412181", "11412183"]
  },
  "radius": {
    "include": ["MEDIUM"]
  },
  "deviceClass": {
    "include": ["IPHONE", "IPAD"]
  },
  "minAge": {
    "include": ["25"]
  },
  "maxAge": {
    "include": ["54"]
  },
  "gender": {
    "include": ["M", "F"]
  },
  "appCategory": {
    "include": ["100"],
    "exclude": ["100"]
  },
  "appDownloader": {
    "include": ["987654321"],
    "exclude": ["555666777"]
  },
  "daypart": {
    "include": ["8", "9", "10", "32", "33", "34"]
  },
  "locationGroup": {
    "include": ["123456789"]
  }
}
```

## Topics

### Dictionaries
- [object AdGroupTargeting.AdminArea](adgrouptargeting/adminarea-data.dictionary.md)
  State or province (administrative area) targeting.
- [object AdGroupTargeting.AppCategory](adgrouptargeting/appcategory-data.dictionary.md)
  App category targeting based on App Store categories, with include and exclude support.
- [object AdGroupTargeting.AppDownloader](adgrouptargeting/appdownloader-data.dictionary.md)
  Targeting based on whether users have downloaded specific apps, identified by Adam ID.
- [object AdGroupTargeting.Country](adgrouptargeting/country-data.dictionary.md)
  Country-level geographic targeting.
- [object AdGroupTargeting.Daypart](adgrouptargeting/daypart-data.dictionary.md)
  Hour-of-day targeting, restricting delivery to specific one-hour slots in a 7-day week grid.
- [object AdGroupTargeting.DeviceClass](adgrouptargeting/deviceclass-data.dictionary.md)
  Device class targeting (for example, `IPHONE` or `IPAD`).
- [object AdGroupTargeting.Gender](adgrouptargeting/gender-data.dictionary.md)
  Gender targeting for the audience.
- [object AdGroupTargeting.Locality](adgrouptargeting/locality-data.dictionary.md)
  City or locality targeting.
- [object AdGroupTargeting.LocationGroup](adgrouptargeting/locationgroup-data.dictionary.md)
  Location group targeting, restricting delivery to the business locations in specified groups.
- [object AdGroupTargeting.MaxAge](adgrouptargeting/maxage-data.dictionary.md)
  Maximum age targeting, setting the upper bound of the target age range.
- [object AdGroupTargeting.MinAge](adgrouptargeting/minage-data.dictionary.md)
  Minimum age targeting, setting the lower bound of the target age range.
- [object AdGroupTargeting.PostalCode](adgrouptargeting/postalcode-data.dictionary.md)
  Postal code geographic targeting.
- [object AdGroupTargeting.Radius](adgrouptargeting/radius-data.dictionary.md)
  Radius targeting used with Apple Maps campaigns to restrict delivery to users within a given proximity of the brand’s locations.

## Properties

- `country` (AdGroupTargeting.Country): Country targeting. Include a country ID returned by the Geo Search API. **Include only.** Used with App Store campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `adminArea` (AdGroupTargeting.AdminArea): State or province targeting. Include admin area IDs returned by the Geo API. **Include only.** Used with App Store and Apple Maps campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `locality` (AdGroupTargeting.Locality): City targeting. Include locality IDs returned by the Geo API. **Include only.** Used with App Store and Apple Maps campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `postalCode` (AdGroupTargeting.PostalCode): Postal code targeting. Include postal code IDs returned by the Geo API. **Include only.** Used with Apple Maps campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `radius` (AdGroupTargeting.Radius): Radius targeting, used with Apple Maps campaigns to restrict delivery to users within a given proximity of the brand’s locations. Valid values: `CLOSE`, `MEDIUM`, `FAR`. **Include only.** In practice, radius targeting is applied on `MAPS_SEARCH_RESULTS` campaigns and should not be combined with geo location targeting in the same ad group, but the API does not enforce either constraint at the schema level. See [`TargetingData`](targetingdata.md). Mutable.
- `deviceClass` (AdGroupTargeting.DeviceClass): Device class targeting. Valid values: `IPHONE`, `IPAD`. **Include only.** Used with App Store campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `minAge` (AdGroupTargeting.MinAge): Minimum age targeting. Sets the lower bound of the target age range. Minimum value is 18, maximum value is 64. **Include only.** Used with App Store campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `maxAge` (AdGroupTargeting.MaxAge): Maximum age targeting. Sets the upper bound of the target age range. Minimum value is 18, maximum value is 64. To target users 65 and older, omit `maxAge` or send `include` as `null`. **Include only.** Used with App Store campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `gender` (AdGroupTargeting.Gender): Gender targeting, used with App Store campaigns. Valid values: `M`, `F`. **Include only.** See [`TargetingData`](targetingdata.md). Mutable.
- `appCategory` (AdGroupTargeting.AppCategory): App category targeting. Category ID `100` is a special value representing the same category as the promoted app. A value of `100` in `include` means you are targeting apps in the same category as your app, and a value of `100` in `exclude` means you aren’t. **Include and exclude supported.** Used with App Store campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `appDownloader` (AdGroupTargeting.AppDownloader): Reach or suppress users based on whether they’ve downloaded specific apps, identified by Adam ID. Use `include` to reach users who have downloaded those apps. Use `exclude` to suppress users who already have your app (acquisition targeting). Look up Adam IDs via [`Search for Apps`](searches-for-a-list-of-apps.md). **Include and exclude supported.** Used with App Store campaigns. See [`TargetingData`](targetingdata.md). Mutable.
- `daypart` (AdGroupTargeting.Daypart): Hour-of-day targeting. Include slot integers (0–167) to restrict delivery to those hours. **Include only.** Used with App Store and Apple Maps campaigns. Values represent one-hour windows in a 7-day week grid starting on Sunday. See [`AdGroupTargeting.Daypart`](adgrouptargeting/daypart-data.dictionary.md) for the full slot reference. See [`TargetingData`](targetingdata.md). Mutable.
- `locationGroup` (AdGroupTargeting.LocationGroup): Location group targeting. Include location group IDs to restrict delivery to the business locations in those groups. **Include only.** Used with Apple Maps campaigns. For creating and managing groups, see [`Managing Location Groups`](location-groups-overview.md). See [`TargetingData`](targetingdata.md). Mutable.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargeting)*