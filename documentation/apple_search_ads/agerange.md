# AgeRange

**Framework**: Apple Search Ads  
**Kind**: dictionary

The defined target audience to include using the age-range demographic.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object AgeRange
```

#### Discussion

Use this dimension to limit the age group to target your ad to.

```json
    "age": {
      "included": [
        {
          "minAge": 20,
          "maxAge": 25
        }

```

## See Also

- [object TargetingDimensions](targetingdimensions.md)
  The optional criteria to use with ad groups to narrow the audience that views your ads.
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
- [object DaypartCriteria](daypartcriteria.md)
  The defined targeted audience to include for a specific time of day.
- [object DaypartDetail](daypartdetail.md)
  The defined targeted audience to include by a specific time of day.
- [object DeviceClassCriteria](deviceclasscriteria.md)
  The defined targeted audience to include by device type.
- [object GenderCriteria](gendercriteria.md)
  The defined targeted audience to include using the gender demographic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/agerange)*