# Get a Location

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a single business location by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves the full details of a specific business location registered in Apple Ads. The response includes the location’s address, geographic coordinates, business categories, and current status.

To verify location details before adding a location to a group, or to inspect the current status of a known location, use this endpoint.

The location’s `status` field can be one of the following:

| Status | Description |
| --- | --- |
| `OPEN` | The location is open and eligible for targeting in Apple Maps campaigns. |
| `CLOSED` | The location has permanently closed. |
| `MOVED` | The location has relocated. A new location record reflects the current address. |
| `TEMPORARILY_CLOSED` | The location is temporarily unavailable. |
| `OPENING_SOON` | The location is not yet open but will open soon. |

Retrieving a location’s details is subject to brand ownership and status limitations:

| Constraint | Detail |
| --- | --- |
| Brand ownership | You can only retrieve locations belonging to brands accessible to your ad account. |
| Open locations only | Only locations with `status: OPEN` can be added to location groups and targeted in campaigns. |

#### Payload Examples

##### Request

Retrieves a single location by its unique identifier. The response includes the full location object with address, coordinates, and eligibility status.

```None
GET https://api.ads.apple.com/v1/locations/7205759403792794
```

##### Response

```json
{
 "result": {
   "id": "7205759403792794",
   "name": "AwayFinder - Downtown SF",
   "brandId": "9151314442816847872",
   "status": "OPEN",
   "countryOrRegion": "US",
   "categories": [
     "travel",
     "tourism"
   ],
   "address": {
     "subThoroughfare": "123",
     "thoroughfare": "Market Street",
     "locality": "San Francisco",
     "adminArea": "California",
     "postalCode": "94105",
     "countryOrRegion": "US",
     "fullThoroughfare": "123 Market Street",
     "fullAddress": "123 Market Street, San Francisco, California 94105, US"
   },
   "displayPoint": {
     "latitude": "37.7749",
     "longitude": "-122.4194"
   },
   "creationTime": "2025-01-15T10:00:00Z",
   "modificationTime": "2026-03-20T14:45:00Z",
   "eligibility": {
     "status": "ELIGIBLE"
   }
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/locations/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query for Locations](query-locations.md)
  Retrieve a paginated list of business locations using filters and sorting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-location-by-id)*