# SearchEntity

**Framework**: Apple Search Ads  
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

## See Also

- [object GeoRequest](georequest.md)
  The geosearch request object.
- [object SearchEntityListResponse](searchentitylistresponse.md)
  The response details of geosearch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/searchentity)*