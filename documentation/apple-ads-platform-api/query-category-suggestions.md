# Query Category Suggestions

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query category suggestions for apps or brands using either a discovery or search route based on the query type.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Each result is a [`CategorySuggestion`](categorysuggestion.md) object with a `category` name (e.g. `"Productivity"`) and a `popularity` score. Sort by `popularity DESC` and use `pagination` to page through results.

#### Request Body

#### Payload Examples

This example discovers category suggestions for a brand using the SUGGESTION route. The response is a list of category names with their relative popularity scores. The same route also works for apps, using `APPSTORE_APP` as the `promotedObjectType`.

**Suggestion for Brand**:

##### Request

```json
POST /v1/suggestions/categories/query

{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": [
       "123456"
     ]
   },
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": [
       "BUSINESS_BRAND"
     ]
   },
   {
     "field": "queryType",
     "operator": "EQUALS",
     "value": [
       "SUGGESTION"
     ]
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "category": "Productivity",
     "popularity": 90
   },
   {
     "category": "Business",
     "popularity": 78
   },
   {
     "category": "Utilities",
     "popularity": 65
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "totalCount": 3
 }
}
```

**Search by Category Name**:

##### Request

```json
POST /v1/suggestions/categories/query

{
 "filters": [
   {
     "field": "queryType",
     "operator": "EQUALS",
     "value": [
       "SEARCH"
     ]
   },
   {
     "field": "category",
     "operator": "IN",
     "value": [
       "Productivity",
       "Business"
     ]
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "category": "Productivity",
     "popularity": 90
   },
   {
     "category": "Business",
     "popularity": 78
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "totalCount": 2
 }
}
```

**Search by Partial Match**:

This example uses `LIKE` to perform a partial string match search across all available categories, rather than looking up specific named categories with `IN`.

##### Request

```json
POST /v1/suggestions/categories/query

{
 "filters": [
   {
     "field": "queryType",
     "operator": "EQUALS",
     "value": [
       "SEARCH"
     ]
   },
   {
     "field": "category",
     "operator": "LIKE",
     "value": [
       "prod"
     ]
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "category": "Productivity",
     "popularity": 90
   },
   {
     "category": "Food & Drink",
     "popularity": 42
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "totalCount": 2
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/suggestions/categories/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

See [`RecommendationQueryRequest`](recommendationqueryrequest.md). This endpoint supports two query routes selected by the `queryType` filter: `SUGGESTION` discovers categories for a specific app or brand, and `SEARCH` looks up or searches categories by name.

## See Also

- [Query Keyword Suggestions](query-keyword-suggestions.md)
  Query keyword suggestions based on search terms and App Store countries or regions using structured filters.
- [Query Phrase Suggestions](query-phrase-suggestions.md)
  Query phrase suggestions using either a discovery or search route based on the query type.
- [Query Target CPA Suggestion](query-target-cpa-suggestion.md)
  Retrieve the recommended target CPA for a new Maximize Conversions campaign on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-category-suggestions)*