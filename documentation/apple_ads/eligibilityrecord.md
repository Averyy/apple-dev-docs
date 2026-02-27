# EligibilityRecord

**Framework**: Apple Ads  
**Kind**: dictionary

App eligibility parameters that an API response returns.

**Availability**:
- Search Ads 4.10+

## Declaration

```swift
object EligibilityRecord
```

## Properties

- `adamId` (int64): Your unique App Store app identifier.
- `countryOrRegion` (string): The App Store geoterritories where you’re promoting your app. The value is an ISO 3166-1 alpha-2 country code. The `EQUALS` and `IN` selector [`Condition`](condition.md) operators are available to use with [`Find App Eligibility Records`](find-app-eligibility-records.md).
- `deviceClass` (string): The eligible devices you can use for targeting. See [`DeviceClass`](deviceclass.md). You can use the `EQUALS` and `IN` selector [`Condition`](condition.md) operators with [`Find App Eligibility Records`](find-app-eligibility-records.md).
- `minAge` (int32): The minimum age you can use to create an ad group. See [`AgeRange`](agerange.md).
- `state` (string): The system state of the app eligibility review process. You can use the  `EQUALS` and `IN` selector [`Condition`](condition.md) operators with [`Find App Eligibility Records`](find-app-eligibility-records.md).
- `supplySource` (string): The ad placements eligible for a campaign. You can use the  `EQUALS` and `IN` selector [`Condition`](condition.md) operators with [`Find App Eligibility Records`](find-app-eligibility-records.md). See [`SupplySource`](supplysource.md).

## See Also

- [object EligibilityRecordListResponse](eligibilityrecordlistresponse.md)
  The response details to an app eligibility request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/eligibilityrecord)*