# Query Negative Keywords

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query negative keywords using structured filters, sorting, and pagination.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Queries negative keywords using a standard `QueryRequest` body. `adGroupId` is always required. The API returns an error if it is omitted.

- `adGroupId EQUALS` or `adGroupId IN` scopes the query to one or more specific ad groups. `campaignId` is optional with these operators. `adGroupId IN` accepts up to 1000 values.
- `adGroupId IS_NULL` combined with a `campaignId EQUALS` filter returns only campaign-level negatives.
- `adGroupId IS_NOT_NULL` combined with a `campaignId EQUALS` filter returns only ad-group-level negatives across the campaign.
- `adGroupId NOT_EQUALS` combined with a `campaignId EQUALS` filter returns ad-group-level negatives, excluding the specified ad group.
- `campaignId` only supports `EQUALS`.
- Filtering by `id` (`EQUALS` or `IN`) is exempt from the `adGroupId` requirement, since `id` already fully bounds the query.

#### Payload Examples

**Query by Ad Group**:

Retrieve negative keywords for one or more specific ad groups using `adGroupId EQUALS` or `adGroupId IN`. `campaignId` is not required with this pattern.

##### Request

```json
POST /v1/negative-keywords/query

{
 "filters": [
   {
     "field": "adGroupId",
     "operator": "IN",
     "value": [555666777, 555666778]
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
     "text": "cheap downloads",
     "matchType": "EXACT",
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-10T08:05:00.000",
     "modificationTime": "2025-01-10T08:05:00.000"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Query Campaign Negatives**:

Retrieve campaign-level negative keywords for a campaign by combining a `campaignId EQUALS` filter with `adGroupId IS_NULL`.

##### Request

```json
POST /v1/negative-keywords/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555666
   },
   {
     "field": "adGroupId",
     "operator": "IS_NULL"
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
     "text": "free app",
     "matchType": "BROAD",
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-10T08:00:00.000",
     "modificationTime": "2025-01-10T08:00:00.000"
   },
   {
     "id": 777888997,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "text": "free trial",
     "matchType": "EXACT",
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-09T10:00:00.000",
     "modificationTime": "2025-01-09T10:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Query Ad Group Negatives**:

Retrieve all ad group-level negative keywords across every ad group under a campaign. The `adGroupId IS_NOT_NULL` filter excludes campaign-level negatives and returns only those scoped to an ad group.

##### Request

```json
POST /v1/negative-keywords/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555666
   },
   {
     "field": "adGroupId",
     "operator": "IS_NOT_NULL"
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
     "id": 777888998,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666777,
     "text": "cheap downloads",
     "matchType": "EXACT",
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-10T08:05:00.000",
     "modificationTime": "2025-01-10T08:05:00.000"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Exclude One Ad Group**:

Retrieve ad-group-level negative keywords for a campaign while excluding one specific ad group, using `adGroupId NOT_EQUALS` combined with a `campaignId EQUALS` filter.

##### Request

```json
POST /v1/negative-keywords/query

{
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": 444555666
   },
   {
     "field": "adGroupId",
     "operator": "NOT_EQUALS",
     "value": 555666777
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
     "id": 777888996,
     "adAccountId": 123456789,
     "campaignId": 444555666,
     "adGroupId": 555666778,
     "text": "free download",
     "matchType": "BROAD",
     "status": "ENABLED",
     "deleted": false,
     "creationTime": "2025-01-10T08:10:00.000",
     "modificationTime": "2025-01-10T08:10:00.000"
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

`POST https://api.ads.apple.com/v1/negative-keywords/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Negative Keyword](post-negative-keywords.md)
  Create a negative keyword at the campaign or ad group level to prevent ads from showing for unwanted search terms.
- [Get a Negative Keyword](get-negative-keywords-_id_.md)
  Retrieve a single negative keyword by its unique identifier.
- [Update a Negative Keyword](put-negative-keywords-_id_.md)
  Update a negative keyword’s status to enable or pause its search term exclusion.
- [Delete a Negative Keyword](delete-negative-keywords-_id_.md)
  Soft-delete a negative keyword by ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-negative-keywords-query)*