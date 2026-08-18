# AdGroup.Targeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The comprehensive audience and placement configuration for an ad group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroup.Targeting
```

#### Discussion

Defines the audience dimensions, such as geography, demographics, device, and behavior, that this ad group targets. Each dimension supports `include` and/or `exclude` lists depending on the field.

##### Example

```json
{
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

See [`AdGroupTargeting`](adgrouptargeting.md) for the full field reference.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/targeting-data.dictionary)*