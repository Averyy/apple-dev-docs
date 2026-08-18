# Query Target CPA Suggestion

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve the recommended target CPA for a new Maximize Conversions campaign on the App Store.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns the suggested target CPA for a [`Campaigns Endpoints`](campaigns-endpoints.md). The suggestion is the maximum tap-install CPI observed across the specified app’s eligible markets over the last 28 days. Only countries or regions with at least 10 installs in that window qualify.

To identify the app, use `promotedObjectId` and `promotedObjectType`. Scope results to specific markets with an optional `countryOrRegion` filter. The response returns the single highest suggested target CPA and the market that produced it, along with the `appCategory` the suggestion applies to.

#### Request Body

#### Payload Examples

**All Eligible Countries**:

Retrieve the suggested target CPA across all markets. Omitting `countryOrRegion` causes the endpoint to evaluate every country and region with at least 10 installs in the last 28 days and return the highest result.

##### Request

Identifies the app by `promotedObjectId` and `promotedObjectType`. Since you don’t supply a country filter, the endpoint evaluates all eligible markets.

```json
POST /v1/suggestions/target-cpas/query

{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": [
       "987654321"
     ]
   },
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": [
       "APPSTORE_APP"
     ]
   }
 ]
}
```

##### Response

```json
{
 "result": {
   "promotedObjectId": "987654321",
   "suggestedTargetCPA": {
     "amount": "1.20",
     "currency": "USD"
   },
   "countryOrRegion": [
     "US"
   ],
   "appCategory": "Games"
 }
}
```

**Scoped to Specific Countries**:

Restrict evaluation to specific markets by adding a `countryOrRegion` filter. The endpoint returns the highest suggested target CPA found within those countries or regions only.

##### Request

Adds a `countryOrRegion` filter restricting evaluation to the US, GB, and CA markets.

```json
POST /v1/suggestions/target-cpas/query

{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": [
       "987654321"
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
     "field": "countryOrRegion",
     "operator": "IN",
     "value": [
       "US",
       "GB",
       "CA"
     ]
   }
 ]
}
```

##### Response

```json
{
 "result": {
   "promotedObjectId": "987654321",
   "suggestedTargetCPA": {
     "amount": "0.95",
     "currency": "USD"
   },
   "countryOrRegion": [
     "GB"
   ],
   "appCategory": "Games"
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/suggestions/target-cpas/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

See [`RecommendationQueryRequest`](recommendationqueryrequest.md).

## See Also

- [Query Keyword Suggestions](query-keyword-suggestions.md)
  Query keyword suggestions based on search terms and App Store countries or regions using structured filters.
- [Query Phrase Suggestions](query-phrase-suggestions.md)
  Query phrase suggestions using either a discovery or search route based on the query type.
- [Query Category Suggestions](query-category-suggestions.md)
  Query category suggestions for apps or brands using either a discovery or search route based on the query type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-target-cpa-suggestion)*