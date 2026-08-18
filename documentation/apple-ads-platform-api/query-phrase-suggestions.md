# Query Phrase Suggestions

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query phrase suggestions using either a discovery or search route based on the query type.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Each result is a [`PhraseSuggestion`](phrasesuggestion.md) object. Sort by `popularity DESC` and use `pagination` to page through results.

#### Request Body

#### Payload Examples

This example discovers relevant search phrases for an app using the SUGGESTION route. The response is a list of phrases with their relative popularity scores, useful for expanding keyword targeting. The same route also works for Apple Maps brands, using `BUSINESS_BRAND` as the `promotedObjectType`.

**Discover Phrases for an App**:

##### Request

```json
POST /v1/suggestions/phrases/query

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
       "APPSTORE_APP"
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
     "phrase": "best productivity apps",
     "popularity": 82
   },
   {
     "phrase": "task management tools",
     "popularity": 75
   },
   {
     "phrase": "organize my day app",
     "popularity": 61
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "totalCount": 3
 }
}
```

**Discover Phrases for Maps**:

##### Request

```json
POST /v1/suggestions/phrases/query

{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": [
       "9151314442816847872"
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
     "phrase": "coffee shop near me",
     "popularity": 88
   },
   {
     "phrase": "family friendly restaurant",
     "popularity": 70
   },
   {
     "phrase": "best brunch spot",
     "popularity": 64
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "totalCount": 3
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/suggestions/phrases/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

See [`RecommendationQueryRequest`](recommendationqueryrequest.md). This endpoint supports two query routes selected by the `queryType` filter: `SUGGESTION` discovers phrases for an app or Apple Maps brand, and `SEARCH` looks up or searches specific phrases.

## See Also

- [Query Keyword Suggestions](query-keyword-suggestions.md)
  Query keyword suggestions based on search terms and App Store countries or regions using structured filters.
- [Query Category Suggestions](query-category-suggestions.md)
  Query category suggestions for apps or brands using either a discovery or search route based on the query type.
- [Query Target CPA Suggestion](query-target-cpa-suggestion.md)
  Retrieve the recommended target CPA for a new Maximize Conversions campaign on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-phrase-suggestions)*