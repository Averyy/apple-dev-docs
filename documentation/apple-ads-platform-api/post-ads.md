# Create an Ad

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Creates a new ad that links an ad creative to an ad group for delivery.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint creates an ad that links an ad creative to an ad group.

- `adGroupId` and `creativeId` are required at creation and are **immutable**: you cannot change them after creating the ad.
- The ad creative defines the visual content (product page or Apple Maps ad creative).
- The ad controls the `name` and `status`.
- An ad group can contain multiple ads, but only one ad per ad group can be `ENABLED` at a time.

The ad’s `displayStatus` is an aggregate of campaign-level, ad group-level, and ad-level state, combined with ad creative eligibility.

The `systemStatus` will be `NOT_RUNNING` if the ad creative is in `PENDING` state (awaiting system validation, policy determination, or asset CDN availability), or if Apple has rejected the ad creative (`INVALID`).

#### Payload Examples

**App Store Ad**:

An ad linking an App Store ad creative to an ad group in an App Store campaign.

##### Request

```json
POST /v1/ads

{
 "name": "AwayFinder - Default Product Page",
 "adGroupId": 555666777,
 "creativeId": 666777888,
 "status": "ENABLED"
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
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-09-01T08:00:00.000",
   "modificationTime": "2025-09-01T08:00:00.000"
 }
}
```

**Apple Maps Ad**:

An ad linking an Apple Maps ad creative to an ad group in an Apple Maps campaign.

##### Request

```json
POST /v1/ads

{
 "name": "AwayFinder - Maps Creative",
 "adGroupId": 555666777,
 "creativeId": 666777888,
 "status": "ENABLED"
}
```

##### Response

```json
{
 "result": {
   "id": 777888998,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "adGroupId": 555666777,
   "creativeId": 666777888,
   "name": "AwayFinder - Maps Creative",
   "status": "ENABLED",
   "systemStatus": "NOT_RUNNING",
   "systemStatusReasons": [
     "AD_APPROVAL_PENDING"
   ],
   "systemStatusLimitingReasons": [],
   "displayStatus": "PROCESSING",
   "deleted": false,
   "creationTime": "2025-09-01T09:00:00.000",
   "modificationTime": "2025-09-01T09:00:00.000"
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/ads`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Ads](post-ads-query.md)
  Searches and filters ads using structured query criteria including field filters, sorting, and pagination.
- [Get an Ad](get-ads-_id_.md)
  Retrieves a single ad by its unique identifier.
- [Update an Ad](put-ads-_id_.md)
  Updates the name or status of an existing ad by its unique identifier.
- [Delete an Ad](delete-ads-_id_.md)
  Soft-deletes an ad by its unique identifier, stopping delivery and removing it from active results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-ads)*