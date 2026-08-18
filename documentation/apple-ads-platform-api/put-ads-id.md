# Update an Ad

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Updates the name or status of an existing ad by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint updates an existing ad. Only `name` and `status` are mutable. `creativeId` and `adGroupId` cannot be changed after the ad is created. The system modifies only the fields included in the request body. Omitted fields retain their current values.

To change which ad creative an ad group serves, create a new ad with the desired `creativeId` and delete the old one. This pattern ensures ad delivery history remains traceable per ad.

#### Payload Examples

**Pause Ad**:

Pause an ad by setting `status` to `PAUSED`. Send only the field you want to change.

##### Request

```json
PUT /v1/ads/777888999

{
 "status": "PAUSED"
}
```

##### Response

```json
{
 "result": {
   "id": 777888999,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "adGroupId": 555666777,
   "creativeId": 666777888,
   "name": "AwayFinder - Default Product Page",
   "status": "PAUSED",
   "systemStatus": "NOT_RUNNING",
   "systemStatusReasons": [
     "PAUSED_BY_USER"
   ],
   "systemStatusLimitingReasons": [],
   "displayStatus": "PAUSED",
   "deleted": false,
   "creationTime": "2025-09-01T08:00:00.000",
   "modificationTime": "2025-10-01T10:00:00.000"
 }
}
```

**Rename Ad**:

Rename an ad by sending only the `name` field. Status and all other fields remain unchanged.

##### Request

```json
PUT /v1/ads/777888999

{
 "name": "AwayFinder - Holiday Product Page"
}
```

##### Response

```json
{
 "result": {
   "id": 777888999,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "adGroupId": 555666777,
   "creativeId": 666777888,
   "name": "AwayFinder - Holiday Product Page",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-09-01T08:00:00.000",
   "modificationTime": "2025-10-15T14:00:00.000"
 }
}
```

## Endpoint

`PUT https://api.ads.apple.com/v1/ads/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad](post-ads.md)
  Creates a new ad that links an ad creative to an ad group for delivery.
- [Query Ads](post-ads-query.md)
  Searches and filters ads using structured query criteria including field filters, sorting, and pagination.
- [Get an Ad](get-ads-_id_.md)
  Retrieves a single ad by its unique identifier.
- [Delete an Ad](delete-ads-_id_.md)
  Soft-deletes an ad by its unique identifier, stopping delivery and removing it from active results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/put-ads-_id_)*