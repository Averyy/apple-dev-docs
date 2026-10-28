# Search for Geolocations

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches a list of geolocations for targeting.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Discussion

Use this endpoint to obtain App Store locations you can use to refine your target audience. Specify the criteria for a geolocation search using the geotargeting criteria [`CountryCriteria`](./countrycriteria.md), [`AdminAreaCriteria`](./adminareacriteria.md), and [`LocalityCriteria`](./localitycriteria.md), and then apply them to ad groups using [`Create an Ad Group`](./create-an-ad-group.md) and [`Update an Ad Group`](./update-an-ad-group.md) endpoints.

![A graphic depicting the search for geolocations workflow. First, run a get call for geo locations. Next, specify targeting criteria followed by applying the geo targeting in an ad group.](https://developer.apple.com/tutorials/images/com.apple.appleads/media-4465064@2x.png)

### Payload Example: Search for Geolocations

**Request**:

```
GET https://api.searchads.apple.com/api/v5/search/geo?entity=adminArea&countrycode=US
```

**Response**:

```json
{
  "id": "US|CA",
  "entity": "AdminArea",
  "displayName": "California, United States",
  "countryOrRegion": "US",
  "adminArea": "CA",
  "locality": null
}

```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/search/geo`

## Parameters

### Query Parameters

- `countrycode` (string): The country or region to serve ads in. Campaigns that serve multiple countries or regions can’t use geotargeting.

  The query uses a `countrycode` value in an ISO alpha-2 country code format.

  ```console
  GET https://api.searchads.apple.com/api/v5/search/geo?countrycode=US
  ```

  **Default**: `US`
- `entity` (string): The `country`, `AdminArea`, or L`ocality` locations available for targeting.

  An `AdminArea` is the state or the equivalent according to its associated country. A `Locality` is the city or the equivalent according to its associated `AdminArea`.

  A `countrycode` is a mandatory parameter.

  ```console
  GET https://api.searchads.apple.com/api/v5/search/geo?entity=AdminArea&countrycode=US
  ```

  ```console
  GET https://api.searchads.apple.com/api/v5/search/geo?entity=Locality&countrycode=US
  ```

  The `entity` query parameter searches the `displayNames` for `country`, `adminArea`, and `Locality` in all languages.

  Search results in the response payload are in the preferred language according to your organization.

  If you don’t input a query parameter, all applicable values return in the response payload as a default.
- `limit` (int32): The limit on the number of geolocations in the response.

  ```console
  GET https://api.searchads.apple.com/api/v5/search/geo?limit=1000
  ```

  **Default**: `20`
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number. You can apply `offset` to most API calls, but not all GET endpoints support it.

  **Default**: `0`
- `query` (string): The `query` search pattern uses a prefix-matching algorithm. You can use spaces in search patterns. Prefixes require a minimum of three characters. If you’re sending a quoted search string, use HTML encoding.

  ```console
  GET https://api.searchads.apple.com/api/v5/search/geo?query=%22New%20H%22
  ```

  **Default**: `*:*`

## Responses

- `200` OK (`SearchEntityListResponse`, `application/json`): If the call succeeds, the API returns the [`SearchEntity`](./searchentity.md) object in the response payload with an HTTP status code of `200` `(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `404` Not Found (`ApiErrorResponse`, `application/json`): The API can’t locate the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Search Geolocation Endpoints
- [Get a List of Geo Locations](./get-a-list-of-geo-locations.md)
  Gets geolocation details using a geoidentifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/search-for-geolocations)*