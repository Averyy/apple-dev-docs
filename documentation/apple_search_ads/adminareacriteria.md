# AdminAreaCriteria

**Framework**: Apple Search Ads  
**Kind**: dictionary

The defined targeted audience by administrative area.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object AdminAreaCriteria
```

#### Discussion

An `adminArea` is a state or the equivalent according to its associated `country`.

Use [`Search for Geolocations`](search-for-geolocations.md) with `entity` to search for and retrieve geolocations. Then use geotargeting dimensions `country`, `adminArea`, and `locality` in the [`TargetingDimensions`](targetingdimensions.md) payload with the [`Update an Ad Group`](update-an-ad-group.md) endpoint.

## See Also

- [object TargetingDimensions](targetingdimensions.md)
  The optional criteria to use with ad groups to narrow the audience that views your ads.
- [object AppCategoryCriteria](appcategorycriteria.md)
  The defined target audience by app category.
- [object AppDownloaderCriteria](appdownloadercriteria.md)
  The defined targeted audience according to app downloads.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/adminareacriteria)*