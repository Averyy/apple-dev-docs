# SearchEntity

**Framework**: Apple Ads  
**Kind**: dictionary

The list of geolocations that includes the geoidentifier and entity type.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object SearchEntity
```

#### Discussion

Use the [`Search for Geolocations`](search-for-geolocations.md) endpoint to fetch a `displayName` for a geolocation.

##### Example Search Entity Object

```json
{
  "id": "US|CA|Cupertino",
  "entity": "locality",
  "displayName": "Cupertino, California, United States",
  "countryOrRegion": "US",
  "adminArea": "CA",
  "locality": "Cupertino"
}
```

## Properties

- `adminArea` (string): A state or the equivalent according to its associated country.
- `countryOrRegion` (string): The geoterritory where you’re promoting your app in ISO alpha-2 country code format.
- `displayName` (string): The geographic targeting location in the format of `locality`,`adminArea,countryOrRegion`.
- `entity` (string): The type of geography for targeting locations. Search results are in the preferred language according to your organization.
- `id` (string): The geographic location in the format of [`CountryOrRegion`](countryorregion.md)|`adminArea`|`locality`.
- `locality` (string): A city or the equivalent according to its associated `adminArea`.

## See Also

- [object GeoRequest](georequest.md)
  The geosearch request object.
- [object SearchEntityListResponse](searchentitylistresponse.md)
  The response details of geosearch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/searchentity)*