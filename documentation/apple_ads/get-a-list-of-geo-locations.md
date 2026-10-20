# Get a List of Geo Locations

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Gets geolocation details using a geoidentifier.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

Use a geo `id` in the request payload to return a corresponding `displayName` and geolocation.

##### Payload Example: Get a list of geolocations

**Request**:

```
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

### Query Parameters

- `limit` (int32): The limit on the number of geolocations in the response.

  ```console
  POST https://api.searchads.apple.com/api/v5/search/geo?limit=100
  ```

  **Default**: `20`
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number. You can apply `offset` to most API calls, but not all GET endpoints support it.

  ```console
  POST https://api.searchads.apple.com/api/v5/search/geo?offset=<OFFSET>
  ```

  **Default**: `0`

## Request Body

**Content-Type**: `application/json`  
**Type**: `[GeoRequest]`

The georequest body.

## Responses

- `200` OK (`SearchEntityListResponse`, `application/json`): If the call succeeds, the API returns a list of [`SearchEntity`](./searchentity.md) objects in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Search Geolocation Endpoints
- [Search for Geolocations](./search-for-geolocations.md)
  Fetches a list of geolocations for targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-list-of-geo-locations)*