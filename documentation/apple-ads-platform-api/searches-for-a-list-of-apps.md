# Search for Apps

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Search the App Store for apps matching the supplied criteria and return app details.

**Availability**:
- apple-ads-platform-api 1.0+

#### Query Parameters

#### Discussion

This endpoint searches the App Store for apps by name, content provider, or returns apps owned by the caller’s organization. It’s useful for discovering apps to target or advertise before building campaigns.

You must supply at least one of `query`, `cpids`, or `returnOwnedApps=true`. The API rejects calls that supply none of these with `INVALID_INPUT`.

The returned `adamId` is the primary identifier used in campaign `promotedObject` and creative `destination` fields.

#### Payload Examples

**Search by App Name**:

Search for apps by name, filtered to a specific App Store country or region.

##### Request

```None
GET https://api.ads.apple.com/v1/search/apps?query=AwayFinder&storeFronts=US&limit=20&offset=0
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

```None
GET https://api.ads.apple.com/v1/search/apps?returnOwnedApps=true&storeFronts=US&limit=50
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

```None
GET https://api.ads.apple.com/v1/search/apps?cpids=987654&limit=20
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

```None
GET https://api.ads.apple.com/v1/search/apps?query=AwayFinder&storeFronts=US&storeFronts=GB&storeFronts=CA&limit=20
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

- `X-Ap-Context` (string) *(required)*

## See Also

- [Get App Details by Adam ID](get-app-details-by-adam-id.md)
  Retrieve application details for a specific Adam ID.
- [Query Supported App Languages](query-supported-app-languages.md)
  Query countries and regions to discover the ad-supported languages available in each market.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searches-for-a-list-of-apps)*