# AppDownloaderCriteria

**Framework**: Apple Search Ads  
**Kind**: dictionary

The defined targeted audience according to app downloads.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object AppDownloaderCriteria
```

#### Discussion

To target all users, don’t include the `AppDownloaderCriteria` dimension in the request payload.

Use the `adamId` of the app you’re promoting in your campaign as an `included`  or `excluded` value. You can obtain your app `adamId` through [`Get a Campaign`](get-a-campaign.md), [`Get all Campaigns`](get-all-campaigns.md), or [`Search for iOS apps`](search-for-ios-apps.md) using the `returnOwnedApps` query.

## See Also

- [object TargetingDimensions](targetingdimensions.md)
  The optional criteria to use with ad groups to narrow the audience that views your ads.
- [object AppCategoryCriteria](appcategorycriteria.md)
  The defined target audience by app category.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/appdownloadercriteria)*