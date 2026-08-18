# Query Keyword Suggestions

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query keyword suggestions based on search terms and App Store countries or regions using structured filters.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Each [`KeywordSuggestion`](keywordsuggestion.md) result contains `text` (the suggested keyword string) and `popularity` (a relative score). Sort by `popularity DESC` and use `pagination` to page through results.

#### Request Body

#### Payload Examples

This example queries keyword suggestions for an app scoped to the US and GB App Store countries or regions, seeded by specific search terms. The response returns suggested keyword strings with their relative popularity scores.

##### Request

```json
POST /v1/suggestions/keywords/query

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
     "field": "terms",
     "operator": "IN",
     "value": [
       "productivity",
       "task management"
     ]
   },
   {
     "field": "countriesOrRegions",
     "operator": "IN",
     "value": [
       "US",
       "GB"
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
     "text": "productivity app",
     "popularity": 85
   },
   {
     "text": "task manager",
     "popularity": 72
   },
   {
     "text": "to do list",
     "popularity": 68
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

`POST https://api.ads.apple.com/v1/suggestions/keywords/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

See [`RecommendationQueryRequest`](recommendationqueryrequest.md).

## See Also

- [Query Phrase Suggestions](query-phrase-suggestions.md)
  Query phrase suggestions using either a discovery or search route based on the query type.
- [Query Category Suggestions](query-category-suggestions.md)
  Query category suggestions for apps or brands using either a discovery or search route based on the query type.
- [Query Target CPA Suggestion](query-target-cpa-suggestion.md)
  Retrieve the recommended target CPA for a new Maximize Conversions campaign on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-keyword-suggestions)*