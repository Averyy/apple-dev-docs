# AdGroupUpdate.Targeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The targeting configuration for updating an existing ad group, specifying audience dimensions to include or exclude.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupUpdate.Targeting
```

#### Discussion

Defines the audience dimensions, such as geography, demographics, device, and behavior, to include or exclude when updating this ad group. The `daypart` dimension is include-only and does not support `exclude`.

See [`AdGroupTargetingUpdate`](adgrouptargetingupdate.md) for the full field reference.

## Properties

- `country` (AdGroupTargetingUpdate.Country): Country-level geographic targeting. Include a country ID returned by the Geo Search API. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `adminArea` (AdGroupTargetingUpdate.AdminArea): Administrative area (state or province) targeting. Include admin area IDs returned by the Geo API. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `locality` (AdGroupTargetingUpdate.Locality): City or locality targeting. Include locality IDs returned by the Geo API. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `postalCode` (AdGroupTargetingUpdate.PostalCode): Postal code geographic targeting. Include postal code IDs returned by the Geo API. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `radius` (AdGroupTargetingUpdate.Radius): Radius targeting for Apple Maps campaigns. Valid values: `CLOSE`, `MEDIUM`, `FAR`. In practice, radius targeting applies only to `MAPS_SEARCH_RESULTS` campaigns. Avoid combining it with geo location targeting, though the API does not enforce this constraint at the schema level. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `deviceClass` (AdGroupTargetingUpdate.DeviceClass): Device class targeting (e.g., `IPHONE`, `IPAD`). See [`TargetingDataUpdate`](targetingdataupdate.md).
- `minAge` (AdGroupTargetingUpdate.MinAge): Minimum age targeting for the audience. Minimum value is 18, maximum value is 64. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `maxAge` (AdGroupTargetingUpdate.MaxAge): Maximum age targeting for the audience. Minimum value is 18, maximum value is 64. To target users 65 and older, omit `maxAge` or send `include` as `null`. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `gender` (AdGroupTargetingUpdate.Gender): Gender targeting for the audience. Valid values: `M`, `F`. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `appCategory` (AdGroupTargetingUpdate.AppCategory): App category targeting based on App Store categories. Category ID `100` is a special value representing the same category as the promoted app. A value of `100` in `include` means you are targeting apps in the same category as your app, and a value of `100` in `exclude` means you aren’t. See [`TargetingDataUpdate`](targetingdataupdate.md).
- `appDownloader` (AdGroupTargetingUpdate.AppDownloader): Reach users who have downloaded specific apps (by Adam ID). Look up Adam IDs via [`Search for Apps`](searches-for-a-list-of-apps.md). See [`TargetingDataUpdate`](targetingdataupdate.md).
- `daypart` (AdGroupTargetingUpdate.Daypart): Time-of-day targeting (dayparting). Include-only. The API does not support the `exclude` array for this dimension. Values are slot integers (0–167). For the full slot reference, see [`AdGroupTargeting`](adgrouptargeting.md). See [`TargetingDataUpdate`](targetingdataupdate.md).
- `locationGroup` (AdGroupTargetingUpdate.LocationGroup): Location group targeting for Apple Maps campaigns. See [`TargetingDataUpdate`](targetingdataupdate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupupdate/targeting-data.dictionary)*