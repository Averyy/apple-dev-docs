# Get an Ad Group

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a single ad group by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a single ad group by its ID. The response includes all fields set at creation and any values modified since, including the full `targeting` and `bidStrategy` nested objects.

The response includes the following status fields:

| Field | Type | Description |
| --- | --- | --- |
| `status` | string | Advertiser-managed state: `ENABLED` or `PAUSED`. |
| `systemStatus` | string | System-computed: `RUNNING` or `NOT_RUNNING`. When `NOT_RUNNING`, inspect `systemStatusReasons`. |
| `displayStatus` | string | System-computed, rolled-up delivery state. See [`AdGroupDisplayStatus`](adgroupdisplaystatus.md). |

Keep the following constraints in mind when reading a GET response:

| Constraint | Detail |
| --- | --- |
| Deleted ad groups are returned | The API returns a deleted ad group with `deleted: true` and does not remove the record from GET by ID responses. |
| `campaignId` is always returned | The parent campaign ID is always present in the response. |
| Use query endpoint for listing | `GET /adgroups/{id}` returns a single record. Use `POST /adgroups/query` to filter and list multiple ad groups. |

#### Payload Examples

**App Store Ad Group**:

##### Request

Retrieves an App Store ad group by its unique identifier. This example shows a standard targeting ad group with device and age targeting.

```None
GET https://api.ads.apple.com/v1/adgroups/555666777
```

##### Response

```json
{
 "result": {
   "id": 555666777,
   "name": "AwayFinder iOS — New Users 18-34",
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "targeting": {
     "deviceClass": {
       "include": [
         "IPHONE"
       ]
     },
     "minAge": {
       "include": [
         "18"
       ]
     },
     "maxAge": {
       "include": [
         "34"
       ]
     },
     "appDownloader": {
       "include": [
         "123456789"
       ]
     }
   },
   "automatedKeywordsOptIn": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**Apple Maps Ad Group**:

##### Request

Retrieves an Apple Maps ad group by its unique identifier. This example shows an ad group targeting Apple Maps.

```None
GET https://api.ads.apple.com/v1/adgroups/555666779
```

##### Response

```json
{
 "result": {
   "id": 555666779,
   "name": "AwayFinder Maps — Nearby Search",
   "adAccountId": 123456789,
   "campaignId": 444555668,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP",
     "bid": {
       "amount": "5.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "radius": {
       "include": [
         "MEDIUM"
       ]
     }
   },
   "automatedKeywordsOptIn": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/adgroups/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad Group](post-adgroups.md)
  Create a new ad group within a campaign, defining targeting, bid strategy, and scheduling for a set of ads.
- [Query Ad Groups](post-adgroups-query.md)
  Query ad groups using filters, sorting, and pagination.
- [Update an Ad Group](put-adgroups-_id_.md)
  Update an existing ad group’s name, status, bid strategy, targeting, or scheduling.
- [Delete an Ad Group](delete-adgroups-_id_.md)
  Soft-delete an ad group by its unique identifier, along with all ads and keywords associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-adgroups-_id_)*