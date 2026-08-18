# AdGroupCreate.Targeting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The targeting configuration for creating a new ad group, specifying audience dimensions to include or exclude.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupCreate.Targeting
```

#### Discussion

Defines the audience dimensions, such as geography, demographics, device, and behavior, to include or exclude when creating this ad group. The `daypart` dimension is include-only and does not support `exclude`.

See [`AdGroupTargetingCreate`](adgrouptargetingcreate.md) for the full field reference.

## Properties

- `country` (AdGroupTargetingCreate.Country): Country-level geographic targeting. Include a country ID returned by the Geo Search API. See [`TargetingDataCreate`](targetingdatacreate.md).
- `adminArea` (AdGroupTargetingCreate.AdminArea): Administrative area (state or province) targeting. Include admin area IDs returned by the Geo API. See [`TargetingDataCreate`](targetingdatacreate.md).
- `locality` (AdGroupTargetingCreate.Locality): City or locality targeting. Include locality IDs returned by the Geo API. See [`TargetingDataCreate`](targetingdatacreate.md).
- `postalCode` (AdGroupTargetingCreate.PostalCode): Postal code geographic targeting. Include postal code IDs returned by the Geo API. See [`TargetingDataCreate`](targetingdatacreate.md).
- `radius` (AdGroupTargetingCreate.Radius): Radius targeting, used with Apple Maps campaigns. Valid values: `CLOSE`, `MEDIUM`, `FAR`. In practice, radius targeting is applied on `MAPS_SEARCH_RESULTS` campaigns and should not be combined with geo location targeting, but the API does not enforce this constraint at the schema level. See [`TargetingDataCreate`](targetingdatacreate.md).
- `deviceClass` (AdGroupTargetingCreate.DeviceClass): Device class targeting (e.g., `IPHONE`, `IPAD`). See [`TargetingDataCreate`](targetingdatacreate.md).
- `minAge` (AdGroupTargetingCreate.MinAge): Minimum age targeting for the audience. Minimum value is 18, maximum value is 64. See [`TargetingDataCreate`](targetingdatacreate.md).
- `maxAge` (AdGroupTargetingCreate.MaxAge): Maximum age targeting for the audience. Minimum value is 18, maximum value is 64. To target users 65 and older, omit `maxAge`, or send `include` as `null` or as an empty array (`[]`). See [`TargetingDataCreate`](targetingdatacreate.md).
- `gender` (AdGroupTargetingCreate.Gender): Gender targeting for the audience. Valid values: `M`, `F`. See [`TargetingDataCreate`](targetingdatacreate.md).
- `appCategory` (AdGroupTargetingCreate.AppCategory): App category targeting based on App Store categories. Category ID `100` is a special value representing the same category as the promoted app. A value of `100` in `include` means you are targeting apps in the same category as your app, and a value of `100` in `exclude` means you aren’t. See [`TargetingDataCreate`](targetingdatacreate.md).
- `appDownloader` (AdGroupTargetingCreate.AppDownloader): Reach users who have downloaded specific apps (by Adam ID). Look up Adam IDs via [`Search for Apps`](searches-for-a-list-of-apps.md). See [`TargetingDataCreate`](targetingdatacreate.md).
- `daypart` (AdGroupTargetingCreate.Daypart): Time-of-day targeting (dayparting). Include-only. The `exclude` array is not supported for this dimension. Values are slot integers (0–167). For the full slot reference, see [`AdGroupTargeting`](adgrouptargeting.md). See [`TargetingDataCreate`](targetingdatacreate.md).
- `locationGroup` (AdGroupTargetingCreate.LocationGroup): Location group targeting for Apple Maps campaigns. See [`TargetingDataCreate`](targetingdatacreate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupcreate/targeting-data.dictionary)*