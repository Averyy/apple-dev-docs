# DaypartCriteria

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The defined targeted audience to include for a specific time of day.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object DaypartCriteria
```

## Properties

- `userTime` (DaypartDetail): The dimension to target criteria for a specific time of day. Numbers ranging from `0` to `167` represent the hours of a week beginning at Sunday 12:00 midnight. For example, the hour beginning Monday at 1:00 a.m. is `25`.

  ```json
  "daypart": {
        "userTime": {
          "included": [
            1,
            3,
            22
          ]
        }
      }

  ```

## See Also

### Audience Refinement
- [object TargetingDimensions](./targetingdimensions.md)
  The optional criteria to use with ad groups to narrow the audience that views your ads.
- [object AppCategoryCriteria](./appcategorycriteria.md)
  The defined target audience by app category.
- [object AppDownloaderCriteria](./appdownloadercriteria.md)
  The defined targeted audience according to app downloads.
- [object AdminAreaCriteria](./adminareacriteria.md)
  The defined targeted audience by administrative area.
- [object CountryCriteria](./countrycriteria.md)
  The defined targeted audience by country or region.
- [object LocalityCriteria](./localitycriteria.md)
  The defined targeted audience by locality.
- [object AgeCriteria](./agecriteria.md)
  The defined targeted audience to include using the age demographic.
- [object AgeRange](./agerange.md)
  The defined target audience to include using the age-range demographic.
- [object DaypartDetail](./daypartdetail.md)
  The defined targeted audience to include by a specific time of day.
- [object DeviceClassCriteria](./deviceclasscriteria.md)
  The defined targeted audience to include by device type.
- [object GenderCriteria](./gendercriteria.md)
  The defined targeted audience to include using the gender demographic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/daypartcriteria)*