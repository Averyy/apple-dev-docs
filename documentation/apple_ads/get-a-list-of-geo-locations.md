# Get a List of Geo Locations

**Framework**: Apple Ads  
**Kind**: httpRequest

Gets geolocation details using a geoidentifier.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use a geo `id` in the request payload to return a corresponding `displayName` and geolocation.

##### Payload Example Get a List of Geolocations

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/search/geo

[
  {
    "id": "US|CA|Cupertino",
    "entity": "locality"
  }
]
```

**Response**:

```json
{
  "id": "US||CA|Cupertino",
  "entity": "locality",
  "displayName": "Cupertino, California, United States",
  "countryOrRegion”: "US",
  "adminArea”: "CA",
  "locality": "Cupertino"
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/search/geo`

## Parameters

- `limit` (int32): The limit on the number of geolocations in the response. ```console
POST https://api.searchads.apple.com/api/v5/search/geo?limit=100
```
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number. You can apply `offset` to most API calls, but not all GET endpoints support it. ```console
POST https://api.searchads.apple.com/api/v5/search/geo?offset=<OFFSET>
```

## Request Body

The georequest body.

## See Also

- [Search for Geolocations](search-for-geolocations.md)
  Fetches a list of geolocations for targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-list-of-geo-locations)*