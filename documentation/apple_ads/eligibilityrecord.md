# EligibilityRecord

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

App eligibility parameters that an API response returns.

**Availability**:
- Search Ads 4.10+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object EligibilityRecord
```

## Properties

- `adamId` (int64): Your unique App Store app identifier.
- `countryOrRegion` (string): The App Store geoterritories where you’re promoting your app. The value is an ISO 3166-1 alpha-2 country code.

  The `EQUALS` and `IN` selector [`Condition`](./condition.md) operators are available to use with [`Find App Eligibility Records`](./find-app-eligibility-records.md).
- `deviceClass` (string): The eligible devices you can use for targeting. See [`DeviceClass`](./deviceclass.md).

  You can use the `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find App Eligibility Records`](./find-app-eligibility-records.md).

  **Allowed Values**: `IPHONE`, `IPAD`
- `minAge` (int32): The minimum age you can use to create an ad group. See [`AgeRange`](./agerange.md).

  **Maximum**: `65`
- `state` (string): The system state of the app eligibility review process.

  You can use the  `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find App Eligibility Records`](./find-app-eligibility-records.md).

  **Allowed Values**: `ELIGIBLE`, `INELIGIBLE`
- `supplySource` (string): The ad placements eligible for a campaign.

  You can use the  `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find App Eligibility Records`](./find-app-eligibility-records.md).

  See [`SupplySource`](./supplysource.md).

  **Allowed Values**: `APPSTORE_SEARCH_RESULTS`, `APPSTORE_SEARCH_TAB`, `APPSTORE_PRODUCT_PAGES_BROWSE`, `APPSTORE_TODAY_TAB`

## See Also

### App Eligibility Request and Response Objects
- [object EligibilityRecordListResponse](./eligibilityrecordlistresponse.md)
  The response details to an app eligibility request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/eligibilityrecord)*