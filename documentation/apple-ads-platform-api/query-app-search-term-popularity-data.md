# Search Term Popularity Query

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve the relative search volume ranking of search terms for a given App Store genre and country or region.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns the most popular search terms for a given App Store genre and country, showing top search terms by search volume. To discover high-volume terms to target during campaign setup, use this data.

#### Request Body

See [`SearchTermPopularityQueryRequest`](searchtermpopularityqueryrequest.md). The endpoint caps `pagination.pageSize` at 5000. [`SearchTermPopularityTimeRange`](searchtermpopularitytimerange.md) documents timezone and granularity rules. `SearchTermPopularityQueryRequest`’s `sorting` field documents sort field limits.

#### Response Body

##### Mandatory Dimensions

The endpoint always includes the following dimension fields in results:

| Field | Description |
| --- | --- |
| `countryOrRegion` | The App Store country or region for the search volume data. |
| `genre` | The App Store genre category. |
| `searchTerm` | The search term text. |
| `week` or `month` | The date field corresponding to the selected granularity. |

The endpoint includes the following dimension fields only when requested.

| Field | Description |
| --- | --- |
| `rankInGenre` | The search term’s rank by volume within the genre of the given App Store country or region. |
| `searchPopularityInGenre` | Relative popularity score within the genre (1–100) of the given App Store country or region. |
| `searchPopularity1to100` | Popularity score on a 1–100 scale across all genres within the country or region. `100` = most popular overall. |
| `searchPopularity1to5` | Relative popularity on a 1–5 scale across all genres of the given App Store country or region. |

#### Payload Examples

**Weekly, US Productivity**:

Retrieve the top search terms in the US Productivity genre for a specific week.

##### Request

Fetches weekly search term popularity for the US Productivity genre over a single week, sorted by `rankInGenre` ascending to surface the highest-volume terms first.

```json
POST /v1/insights/apps/search-term-popularity/query

{
 "filters": [
   {
     "field": "countryOrRegion",
     "operator": "EQUALS",
     "value": "US"
   },
   {
     "field": "genre",
     "operator": "EQUALS",
     "value": "PRODUCTIVITY_UTILITIES"
   }
 ],
 "timeRange": {
   "start": "2025-01-05",
   "end": "2025-01-11",
   "granularity": "WEEKLY_SUN_SAT"
 },
 "sorting": [
   {
     "field": "rankInGenre",
     "order": "ASC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20
 }
}
```

##### Response

```json
{
 "result": {
   "rows": [
     {
       "week": "2025-01-05",
       "countryOrRegion": "US",
       "genre": "PRODUCTIVITY_UTILITIES",
       "searchTerm": "task manager",
       "rankInGenre": 1,
       "searchPopularityInGenre": 95,
       "searchPopularity1to100": 88,
       "searchPopularity1to5": 5
     },
     {
       "week": "2025-01-05",
       "countryOrRegion": "US",
       "genre": "PRODUCTIVITY_UTILITIES",
       "searchTerm": "to do list app",
       "rankInGenre": 2,
       "searchPopularityInGenre": 89,
       "searchPopularity1to100": 84,
       "searchPopularity1to5": 5
     },
     {
       "week": "2025-01-05",
       "countryOrRegion": "US",
       "genre": "PRODUCTIVITY_UTILITIES",
       "searchTerm": "calendar planner",
       "rankInGenre": 3,
       "searchPopularityInGenre": 76,
       "searchPopularity1to100": 72,
       "searchPopularity1to5": 4
     }
   ]
 },
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "totalCount": 3
 }
}
```

**Monthly, Multi-Country**:

Retrieve monthly search term popularity across multiple countries to identify global keyword opportunities.

##### Request

Fetches monthly search term popularity for the Travel genre across three countries (US, GB, DE) over a two-month period, sorted by `searchPopularity1to100` descending to surface globally high-volume terms.

```json
POST /v1/insights/apps/search-term-popularity/query

{
 "filters": [
   {
     "field": "countryOrRegion",
     "operator": "IN",
     "value": [
       "US",
       "GB",
       "DE"
     ]
   },
   {
     "field": "genre",
     "operator": "EQUALS",
     "value": "TRAVEL"
   }
 ],
 "timeRange": {
   "start": "2024-10-01",
   "end": "2024-11-01",
   "granularity": "MONTHLY"
 },
 "sorting": [
   {
     "field": "searchPopularity1to100",
     "order": "DESC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 50
 }
}
```

##### Response

```json
{
 "result": {
   "rows": [
     {
       "month": "2024-10",
       "countryOrRegion": "US",
       "genre": "TRAVEL",
       "searchTerm": "flight tracker",
       "rankInGenre": 1,
       "searchPopularityInGenre": 98,
       "searchPopularity1to100": 91,
       "searchPopularity1to5": 5
     },
     {
       "month": "2024-10",
       "countryOrRegion": "GB",
       "genre": "TRAVEL",
       "searchTerm": "flight tracker",
       "rankInGenre": 2,
       "searchPopularityInGenre": 92,
       "searchPopularity1to100": 87,
       "searchPopularity1to5": 5
     }
   ]
 },
 "pagination": {
   "offset": 0,
   "pageSize": 50,
   "totalCount": 2
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/insights/apps/search-term-popularity/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Impression Share Query](query-app-impression-share-data.md)
  Retrieve impression share data showing how often your ads appear relative to total eligible impressions for a given search term and country.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-app-search-term-popularity-data)*