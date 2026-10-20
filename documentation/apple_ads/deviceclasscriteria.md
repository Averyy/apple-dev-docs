# DeviceClassCriteria

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The defined targeted audience to include by device type.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object DeviceClassCriteria
```

#### Discussion

If you don’t set the `DeviceClassCriteria`, the API targets the currently supported devices by default.

## Properties

- `included` ([string]): The dimension to include the targeting criteria values for device class targeting.

  This parameter doesn’t support the `excluded` attribute.

  ```json
  "deviceClass": {
        "included": [
          "IPAD",
          "IPHONE"
        ]
      },
  ```

  **Allowed Values**: `IPAD`, `IPHONE`

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
- [object DaypartCriteria](./daypartcriteria.md)
  The defined targeted audience to include for a specific time of day.
- [object DaypartDetail](./daypartdetail.md)
  The defined targeted audience to include by a specific time of day.
- [object GenderCriteria](./gendercriteria.md)
  The defined targeted audience to include using the gender demographic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/deviceclasscriteria)*