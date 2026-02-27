# TargetingDimensions

**Framework**: Apple Ads  
**Kind**: dictionary

The optional criteria to use with ad groups to narrow the audience that views your ads.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object TargetingDimensions
```

#### Discussion

Specify targeting criteria in the [`TargetingDimensions`](targetingdimensions.md) object and apply it to ad groups using [`Create an Ad Group`](create-an-ad-group.md)  and [`Update an Ad Group`](update-an-ad-group.md) endpoints.

## Properties

- `adminArea` (AdminAreaCriteria): The dimension to target users by `adminArea.` An `adminArea` is a state or the equivalent according to its associated `country`. Use [`Search for Geolocations`](search-for-geolocations.md) with `entity` to search for and retrieve geolocations. Then use geotargeting dimensions `country`, `adminArea`, and `locality` in the `TargetingDimensions` payload with the [`Create an Ad Group`](create-an-ad-group.md)  and [`Update an Ad Group`](update-an-ad-group.md) endpoints.
- `age` (AgeCriteria): The dimension to target users by age demographic. Limit the age group you want to show your ad to. You must set a minimum age. To include multiple ranges, input them as a list.****
- `appCategories` (AppCategoryCriteria): The dimension to include target audience by app category. Only applicable to campaigns using a [`SupplySource`](supplysource.md) of `APPSTORE_PRODUCT_PAGES_BROWSE`. See the [`App Store`](https://developer.apple.comhttps://developer.apple.com/app-store/categories/) for more details about categories.
- `appDownloaders` (AppDownloaderCriteria): The dimension to include users who have downloaded your app or to exclude users who haven’t downloaded your app. Each campaign can promote only one app per `adamId`.
- `country` (CountryCriteria): The dimension to target users by country or region. Use [`Search for Geolocations`](search-for-geolocations.md) with `entity` to search for and retrieve geolocations. Then use geotargeting dimensions `country`, `adminArea`, and `locality` in the `TargetingDimensions` payload with the [`Create an Ad Group`](create-an-ad-group.md)  and [`Update an Ad Group`](update-an-ad-group.md) endpoints. For the country dimension, use a single country code in an ISO alpha-2 country code format. Campaigns that serve multiple countries or regions can’t use geotargeting. Use [`UpdateCampaignRequest`](updatecampaignrequest.md) to clear geotargeting from a campaign.
- `daypart` (DaypartCriteria): The dimension to target users by a specific time of day. Numbers ranging from `0` to `167` represent the hours of a week beginning at Sunday 12:00 midnight. For example, the hour beginning Monday at 1:00 a.m. is `25`.
- `deviceClass` (DeviceClassCriteria): The dimension to target users by device class. This defaults to the device classes that the promoted app supports.
- `gender` (GenderCriteria): The dimension to target users by gender demographic. Specify the gender you want to show your ad to. To specify all genders, set the value to `null`.
- `locality` (LocalityCriteria): The dimension to target users by `locality`. A `locality` is a city or the equivalent according to its associated `adminArea`. See [`Search for Geolocations`](search-for-geolocations.md) to retrieve geolocations.

## See Also

- [object AppCategoryCriteria](appcategorycriteria.md)
  The defined target audience by app category.
- [object AppDownloaderCriteria](appdownloadercriteria.md)
  The defined targeted audience according to app downloads.
- [object AdminAreaCriteria](adminareacriteria.md)
  The defined targeted audience by administrative area.
- [object CountryCriteria](countrycriteria.md)
  The defined targeted audience by country or region.
- [object LocalityCriteria](localitycriteria.md)
  The defined targeted audience by locality.
- [object AgeCriteria](agecriteria.md)
  The defined targeted audience to include using the age demographic.
- [object AgeRange](agerange.md)
  The defined target audience to include using the age-range demographic.
- [object DaypartCriteria](daypartcriteria.md)
  The defined targeted audience to include for a specific time of day.
- [object DaypartDetail](daypartdetail.md)
  The defined targeted audience to include by a specific time of day.
- [object DeviceClassCriteria](deviceclasscriteria.md)
  The defined targeted audience to include by device type.
- [object GenderCriteria](gendercriteria.md)
  The defined targeted audience to include using the gender demographic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/targetingdimensions)*