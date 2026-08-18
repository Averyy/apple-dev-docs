# Query Ad Groups

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query ad groups using filters, sorting, and pagination.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint queries ad groups using a standard `QueryRequest` body. Filter by `campaignId` to scope results to a specific campaign. An empty request body returns all non-deleted ad groups across all campaigns in the ad account with default pagination.

Each result in the response includes the full `targeting` and `bidStrategy` nested objects, making this the primary endpoint for auditing ad group configuration at scale.

#### Payload Examples

**Query by Campaign**:

Query all ad groups for a specific campaign, sorted by creation time descending.

##### Request

```json
POST /v1/adgroups/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555666
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
     "id": 555666777,
     "name": "AwayFinder iOS — New Users 18-34",
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "pricingModel": "CPT",
     "status": "ENABLED",
     "systemStatus": "RUNNING",
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
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Filter by Status**:

Return only enabled ad groups for a specific campaign.

##### Request

```json
POST /v1/adgroups/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555668
   },
   {
     "field": "status",
     "operator": "EQUALS",
     "value": "ENABLED"
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
     "id": 555666779,
     "name": "AwayFinder Maps — Nearby Search",
     "adAccountId": 123456789,
     "campaignId": 444555668,
     "pricingModel": "CPT",
     "status": "ENABLED",
     "systemStatus": "RUNNING",
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
   },
   {
     "id": 555666780,
     "name": "AwayFinder Maps — SF Bay Area",
     "adAccountId": 123456789,
     "campaignId": 444555668,
     "pricingModel": "CPT",
     "status": "ENABLED",
     "systemStatus": "RUNNING",
     "startTime": "2025-09-01T00:00:00.000",
     "endTime": "2025-12-31T23:59:59.000",
     "bidStrategy": {
       "bidStrategyType": "MANUAL_CPT",
       "bidStrategyGoal": "TAP",
       "bid": {
         "amount": "4.00",
         "currency": "USD"
       }
     },
     "targeting": {
       "locality": {
         "include": [
           "902134",
           "830123"
         ]
       },
       "daypart": {
         "include": [
           "1",
           "5",
           "10",
           "18"
         ]
       }
     },
     "automatedKeywordsOptIn": false,
     "deleted": false,
     "creationTime": "2025-01-10T09:00:00.000",
     "modificationTime": "2025-01-10T09:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Query Deleted**:

Retrieve soft-deleted ad groups for a campaign to confirm deletion or audit history.

##### Request

```json
POST /v1/adgroups/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555666
   },
   {
     "field": "deleted",
     "operator": "EQUALS",
     "value": true
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
     "id": 555666777,
     "name": "AwayFinder iOS — New Users 18-34",
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "pricingModel": "CPT",
     "status": "ENABLED",
     "systemStatus": "NOT_RUNNING",
     "deleted": true,
     "creationTime": "2025-01-10T08:00:00.000",
     "modificationTime": "2025-06-15T14:00:00.000"
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

`POST https://api.ads.apple.com/v1/adgroups/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad Group](post-adgroups.md)
  Create a new ad group within a campaign, defining targeting, bid strategy, and scheduling for a set of ads.
- [Get an Ad Group](get-adgroups-_id_.md)
  Retrieve a single ad group by its unique identifier.
- [Update an Ad Group](put-adgroups-_id_.md)
  Update an existing ad group’s name, status, bid strategy, targeting, or scheduling.
- [Delete an Ad Group](delete-adgroups-_id_.md)
  Soft-delete an ad group by its unique identifier, along with all ads and keywords associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-adgroups-query)*