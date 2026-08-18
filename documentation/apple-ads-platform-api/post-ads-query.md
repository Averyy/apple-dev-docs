# Query Ads

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Searches and filters ads using structured query criteria including field filters, sorting, and pagination.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint queries ads using a standard `QueryRequest` body. Filter by `adGroupId` to scope results to a specific ad group, or by `campaignId` to retrieve all ads across an entire campaign. An empty request body returns all ads for the ad account with default pagination.

The system excludes deleted ads from results by default. To retrieve deleted ads, include a `deleted EQUALS true` filter.

#### Payload Examples

**Query by Ad Group**:

Retrieve all active ads in a specific ad group, sorted by creation time descending.

##### Request

```json
POST /v1/ads/query

{
 "filters": [
   {
     "field": "adGroupId",
     "operator": "EQUALS",
     "value": 555666777
   }
 ],
 "sorting": [
   {
     "field": "creationTime",
     "order": "DESC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": 777888999,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "creativeId": 666777888,
     "name": "AwayFinder - Default Product Page",
     "status": "ENABLED",
     "systemStatus": "RUNNING",
     "systemStatusReasons": [],
     "systemStatusLimitingReasons": [],
     "deleted": false,
     "creationTime": "2025-09-01T08:00:00.000",
     "modificationTime": "2025-09-01T08:00:00.000"
   },
   {
     "id": 777888998,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "creativeId": 666777889,
     "name": "AwayFinder - Holiday Product Page",
     "status": "ENABLED",
     "systemStatus": "RUNNING",
     "systemStatusReasons": [],
     "systemStatusLimitingReasons": [],
     "deleted": false,
     "creationTime": "2025-10-01T08:00:00.000",
     "modificationTime": "2025-10-01T08:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Filter by Status**:

Retrieve only paused ads within a campaign to identify ads that may need to be re-enabled.

##### Request

```json
POST /v1/ads/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555666
   },
   {
     "field": "status",
     "operator": "EQUALS",
     "value": "PAUSED"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": 777888998,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "creativeId": 666777888,
     "name": "AwayFinder - Maps Creative",
     "status": "PAUSED",
     "systemStatus": "NOT_RUNNING",
     "systemStatusReasons": [
       "PAUSED_BY_USER"
     ],
     "systemStatusLimitingReasons": [],
     "deleted": false,
     "creationTime": "2025-09-01T09:00:00.000",
     "modificationTime": "2025-10-01T10:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/ads/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad](post-ads.md)
  Creates a new ad that links an ad creative to an ad group for delivery.
- [Get an Ad](get-ads-_id_.md)
  Retrieves a single ad by its unique identifier.
- [Update an Ad](put-ads-_id_.md)
  Updates the name or status of an existing ad by its unique identifier.
- [Delete an Ad](delete-ads-_id_.md)
  Soft-deletes an ad by its unique identifier, stopping delivery and removing it from active results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-ads-query)*