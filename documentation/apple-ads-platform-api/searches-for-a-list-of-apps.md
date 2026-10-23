# Search for Apps

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Search the App Store for apps matching the supplied criteria and return app details.

**Availability**:
- Apple Ads Platform API 1.0+

#### Query Parameters

#### Discussion

This endpoint searches the App Store for apps by name, content provider, or returns apps owned by the caller’s organization. It’s useful for discovering apps to target or advertise before building campaigns.

You must supply at least one of `query`, `cpids`, or `returnOwnedApps=true`. The API rejects calls that supply none of these with `INVALID_INPUT`.

The returned `adamId` is the primary identifier used in campaign `promotedObject` and creative `destination` fields.

#### Payload Examples

**Search by App Name**:

Search for apps by name, filtered to a specific App Store country or region.

##### Request

```
GET /v1/search/apps?query=AwayFinder&storeFronts=US&limit=20&offset=0
```

##### Response

```json
{
 "result": [
   {
     "adamId": 123456789,
     "appName": "AwayFinder",
     "developerName": "AwayFinder Inc.",
     "countryOrRegionCodes": [
       "US",
       "GB",
       "CA",
       "AU"
     ]
   },
   {
     "adamId": 123456790,
     "appName": "AwayFinder Pro",
     "developerName": "AwayFinder Inc.",
     "countryOrRegionCodes": [
       "US"
     ]
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 2
 }
}
```

**Return Owned Apps**:

Return all apps owned by the caller’s organization, optionally filtered to a specific App Store country or region.

##### Request

```
GET /v1/search/apps?returnOwnedApps=true&storeFronts=US&limit=50
```

##### Response

```json
{
 "result": [
   {
     "adamId": 123456789,
     "appName": "AwayFinder",
     "developerName": "AwayFinder Inc.",
     "countryOrRegionCodes": [
       "US",
       "GB",
       "CA",
       "AU"
     ]
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 1
 }
}
```

**Filter by CPID**:

Retrieve all apps for a specific content provider by CPID.

##### Request

```
GET /v1/search/apps?cpids=987654&limit=20
```

##### Response

```json
{
 "result": [
   {
     "adamId": 123456789,
     "appName": "AwayFinder",
     "developerName": "AwayFinder Inc.",
     "countryOrRegionCodes": [
       "US",
       "GB",
       "CA",
       "AU"
     ]
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 1
 }
}
```

**Multi-Storefront Search**:

Search across multiple App Store countries or regions. Repeat the `storeFronts` parameter for each country code.

##### Request

```
GET /v1/search/apps?query=AwayFinder&storeFronts=US&storeFronts=GB&storeFronts=CA&limit=20
```

##### Response

```json
{
 "result": [
   {
     "adamId": 123456789,
     "appName": "AwayFinder",
     "developerName": "AwayFinder Inc.",
     "countryOrRegionCodes": [
       "US",
       "GB",
       "CA",
       "AU"
     ]
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 1
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/search/apps`

## Parameters

### Query Parameters

- `query` (string): Free-text search matched against app name and developer name. Must contain at least one alphanumeric character and a minimum of 3 characters (2 for CJK languages).
- `returnOwnedApps` (boolean): Flag that returns apps owned by the caller’s organization when set to `true`. Can be combined with `query` and `cpids`, or used on its own. Defaults to `false`.

  **Default**: `false`
- `cpids` (string): Comma-separated list of iTunes content provider identifiers. Scopes the search to apps owned by those providers.
- `storeFronts` ([string]): One or more App Store country or region codes (ISO 3166-1 alpha-2). Repeat the parameter for multiple values. All values must be enabled App Store countries or regions, or the call returns `INVALID_COUNTRY_CODE`.
- `offset` (int32): Pagination offset for results. Defaults to `0`.

  **Default**: `0`
- `limit` (int32): Maximum number of results to return. Defaults to `20`, capped at the service-side maximum (`MAXLIMIT`).

  **Default**: `20`

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Responses

- `200` OK (`AppsSearchResponse`, `application/json`)
- `400` Bad Request (`Error`, `application/json`)
- `401` Unauthorized (`Error`, `application/json`)
- `403` Forbidden (`Error`, `application/json`)
- `404` Not Found (`Error`, `application/json`)
- `429` Too Many Requests (`Error`, `application/json`)
- `500` Internal Server Error (`Error`, `application/json`)

## See Also

- [Get App Details by Adam ID](./get-app-details-by-adam-id.md)
  Retrieve application details for a specific Adam ID.
- [Query Supported App Languages](./query-supported-app-languages.md)
  Query countries and regions to discover the ad-supported languages available in each market.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searches-for-a-list-of-apps)*