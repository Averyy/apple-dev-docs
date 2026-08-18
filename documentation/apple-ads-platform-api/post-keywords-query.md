# Query Keywords

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query keywords using structured filters, sorting, and pagination.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Queries keywords using a standard `QueryRequest` body. Either `adGroupId` or `campaignId` is required. The API returns an error if neither is present.

- `adGroupId EQUALS` or `adGroupId IN` scopes the query to one or more specific ad groups, and can span ad groups across different campaigns within the same ad account. `adGroupId IN` accepts up to 1000 values. `IS_NULL`, `IS_NOT_NULL`, and `NOT_EQUALS` are not supported on `adGroupId` for keywords.
- `campaignId` scopes the query to all keywords across a campaign, and only supports `EQUALS`. There is no campaign-level keyword concept the way there is for negative keywords.
- Filtering by `id` (`EQUALS` or `IN`) is exempt from the `adGroupId`/`campaignId` requirement, since `id` already fully bounds the query.

#### Payload Examples

**Query by Ad Group**:

Query all keywords in a specific ad group, sorted by creation time descending. The response shows two keywords with different match types.

##### Request

```json
POST /v1/keywords/query

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
     "id": 888999001,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "text": "productivity app",
     "matchType": "BROAD",
     "bid": {
       "amount": "1.50",
       "currency": "USD"
     },
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-10T08:05:00.000",
     "modificationTime": "2025-01-10T08:05:00.000"
   },
   {
     "id": 888999000,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "text": "photo editor",
     "matchType": "EXACT",
     "bid": {
       "amount": "2.50",
       "currency": "USD"
     },
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-10T08:00:00.000",
     "modificationTime": "2025-01-10T08:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Query Multiple Ad Groups**:

Query keywords across several ad groups at once using `adGroupId IN`. The listed ad groups can belong to different campaigns within the same ad account.

##### Request

```json
POST /v1/keywords/query

{
 "filters": [
   {
     "field": "adGroupId",
     "operator": "IN",
     "value": [555666777, 555666888]
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
     "id": 888999001,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "text": "productivity app",
     "matchType": "BROAD",
     "bid": {
       "amount": "1.50",
       "currency": "USD"
     },
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-10T08:05:00.000",
     "modificationTime": "2025-01-10T08:05:00.000"
   },
   {
     "id": 888999010,
     "adAccountId": 123456789,
     "campaignId": 444555777,
     "adGroupId": 555666888,
     "text": "budget travel",
     "matchType": "EXACT",
     "bid": {
       "amount": "1.75",
       "currency": "USD"
     },
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-11T09:00:00.000",
     "modificationTime": "2025-01-11T09:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Filter by Match Type**:

Return only exact match keywords across an entire campaign.

##### Request

```json
POST /v1/keywords/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555666
   },
   {
     "field": "matchType",
     "operator": "EQUALS",
     "value": "EXACT"
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
     "id": 888999000,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "text": "photo editor",
     "matchType": "EXACT",
     "bid": {
       "amount": "2.50",
       "currency": "USD"
     },
     "status": "ENABLED",
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

**Query Paused Keywords**:

Retrieve all paused keywords within an ad group to review which terms are suspended.

##### Request

```json
POST /v1/keywords/query

{
 "filters": [
   {
     "field": "adGroupId",
     "operator": "EQUALS",
     "value": 555666777
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
     "id": 888999002,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "text": "image editing",
     "matchType": "BROAD",
     "bid": {
       "amount": "1.00",
       "currency": "USD"
     },
     "status": "PAUSED",
     "deleted": false,
     "creationTime": "2025-01-12T09:00:00.000",
     "modificationTime": "2025-03-01T14:00:00.000"
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

`POST https://api.ads.apple.com/v1/keywords/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Keyword](post-keywords.md)
  Create a new keyword in an ad group, setting the match type and optional bid amount.
- [Get a Keyword](get-keywords-_id_.md)
  Retrieve a single keyword by its unique identifier.
- [Update a Keyword](put-keywords-_id_.md)
  Update a keyword’s bid amount or status to optimize spend and control delivery for that term.
- [Delete a Keyword](delete-keywords-_id_.md)
  Soft-delete a keyword by ID, setting its deleted field to true and stopping bids on that term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-keywords-query)*