# Search for Geolocations

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches a list of geolocations for targeting.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to obtain App Store locations you can use to refine your target audience. Specify the criteria for a geolocation search using the geotargeting criteria [`CountryCriteria`](countrycriteria.md), [`AdminAreaCriteria`](adminareacriteria.md), and [`LocalityCriteria`](localitycriteria.md), and then apply them to ad groups using [`Create an Ad Group`](create-an-ad-group.md) and [`Update an Ad Group`](update-an-ad-group.md) endpoints.

![A graphic depicting the search for geolocations workflow. First, run a get call for geo locations. Next, specify targeting criteria followed by applying the geo targeting in an ad group.](https://docs-assets.developer.apple.com/published/cfbf26de925c930d1bac7724045eb908/media-4465064%402x.png)

##### Payload Example Search for Geolocations

**Request**:

```None
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

- `countrycode` (string): The country or region to serve ads in. Campaigns that serve multiple countries or regions can’t use geotargeting. The query uses a `countrycode` value in an ISO alpha-2 country code format. ```console
GET https://api.searchads.apple.com/api/v5/search/geo?countrycode=US
```
- `entity` (string): The `country`, `AdminArea`, or L`ocality` locations available for targeting. An `AdminArea` is the state or the equivalent according to its associated country. A `Locality` is the city or the equivalent according to its associated `AdminArea`. A `countrycode` is a mandatory parameter. ```console
GET https://api.searchads.apple.com/api/v5/search/geo?entity=AdminArea&countrycode=US
``` ```console
GET https://api.searchads.apple.com/api/v5/search/geo?entity=Locality&countrycode=US
``` The `entity` query parameter searches the `displayNames` for `country`, `adminArea`, and `Locality` in all languages. Search results in the response payload are in the preferred language according to your organization. If you don’t input a query parameter, all applicable values return in the response payload as a default.
- `limit` (int32): The limit on the number of geolocations in the response. ```console
GET https://api.searchads.apple.com/api/v5/search/geo?limit=1000
```
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number. You can apply `offset` to most API calls, but not all GET endpoints support it.
- `query` (string): The `query` search pattern uses a prefix-matching algorithm. You can use spaces in search patterns. Prefixes require a minimum of three characters. If you’re sending a quoted search string, use HTML encoding. ```console
GET https://api.searchads.apple.com/api/v5/search/geo?query=%22New%20H%22
```

## See Also

- [Get a List of Geo Locations](get-a-list-of-geo-locations.md)
  Gets geolocation details using a geoidentifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/search-for-geolocations)*