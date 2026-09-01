# Query Keywords

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query keywords using structured filters, sorting, and pagination.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint queries keywords using a standard `QueryRequest` body. Either `adGroupId` or `campaignId` is required. The API returns an error if neither is present.

- The `adGroupId EQUALS` or `adGroupId IN` filter scopes the query to one or more specific ad groups, and can span ad groups across different campaigns within the same ad account. The `adGroupId IN` filter accepts up to 1000 values. The `IS_NULL`, `IS_NOT_NULL`, and `NOT_EQUALS` operators aren’t supported on `adGroupId` for keywords.
- The `campaignId` field scopes the query to all keywords across a campaign, and only supports `EQUALS`. There is no campaign-level keyword concept the way there is for negative keywords.
- Filtering by `id` (`EQUALS` or `IN`) is exempt from the `adGroupId`/`campaignId` requirement, since `id` already fully bounds the query.

See [`QueryFilterOperator`](queryfilteroperator.md) for the full set of supported comparison operators.

##### Filterable Fields

| Field | Type | Operators | Sortable | Description |
| --- | --- | --- | --- | --- |
| `id` | integer | `EQUALS`, `IN` | Yes (default) | The unique identifier for the keyword. |
| `adGroupId` | integer | `EQUALS`, `IN` | Yes | The ad group this keyword belongs to. |
| `campaignId` | integer | `EQUALS` | Yes | The campaign ID of the parent campaign. Informational only. |
| `text` | string | `EQUALS`, `STARTS_WITH` | Yes | The original advertiser-given keyword text. |
| `matchType` | string (enum) | `EQUALS`, `IN` | Yes | Keyword match type. See [`KeywordMatchType`](keywordmatchtype.md). |
| `status` | string (enum) | `EQUALS`, `IN` | Yes | Whether the keyword is active and eligible to serve. See [`KeywordStatus`](keywordstatus.md). |
| `deleted` | boolean | `EQUALS` | Yes | Whether the keyword has been deleted. |

The request body is a [`QueryRequest`](queryrequest.md) composed of [`QueryFilter`](queryfilter.md) conditions and [`QuerySort`](querysort.md) directives ([`QuerySortOrder`](querysortorder.md)), controlled by [`QueryPagination`](querypagination.md).

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