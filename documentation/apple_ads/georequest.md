# GeoRequest

**Framework**: Apple Ads  
**Kind**: dictionary

The geosearch request object.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object GeoRequest
```

## Properties

- `entity` (string) *(required)*: The type of geography for targeting locations. Search results are in the preferred language according to your organization.
- `id` (string) *(required)*: The geographic location in the format of [`CountryOrRegion`](countryorregion.md)|`adminArea`|`locality`. A `countryCode` is an ISO alpha-2 country code string. An `adminArea` is a state or the equivalent according to its associated `country`. A `locality` is a city or the equivalent according to its associated `adminArea`. Use the `id` that returns in the response in the [`TargetingDimensions`](targetingdimensions.md) object.

## See Also

- [object SearchEntity](searchentity.md)
  The list of geolocations that includes the geoidentifier and entity type.
- [object SearchEntityListResponse](searchentitylistresponse.md)
  The response details of geosearch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/georequest)*