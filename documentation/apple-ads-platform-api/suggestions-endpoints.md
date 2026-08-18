# Suggestions Endpoints

**Framework**: Apple Ads Platform API

Endpoints for querying keyword, phrase, category, and Target CPA suggestions.

**Availability**:
- apple-ads-platform-api 1.0+

#### Overview

Suggestions are read-only discovery tools for campaign setup and keyword expansion. Unlike [`Recommendations Endpoints`](recommendations-endpoints.md), they’re stateless. There’s no apply or dismiss step and no lifecycle to track.

#### Query the Suggestions Endpoints

For bid sizing when launching a new App Store [`Campaigns Endpoints`](campaigns-endpoints.md), use [`Query Target CPA Suggestion`](query-target-cpa-suggestion.md) to retrieve the recommended target CPA based on recent tap-install CPI data. That endpoint uses a `filters`-only request body.

The three keyword discovery endpoints use a `POST /query` pattern with a [`RecommendationQueryRequest`](recommendationqueryrequest.md) body. Each result includes a `popularity` score on a 0–100 scale. To prioritize the highest-impact candidates, sort by `popularity DESC`. The suggestions API exposes four endpoints, each returning a different type of suggestion:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/suggestions/keywords/query` | Returns ranked keyword strings for a given app, scoped to a promoted object and optional App Store countries or regions. See [`Query Keyword Suggestions`](query-keyword-suggestions.md). |
| `POST` | `/v1/suggestions/phrases/query` | Returns natural-language search phrases associated with an app or brand, or matched by text. Supports `SUGGESTION` and `SEARCH` routes. See [`Query Phrase Suggestions`](query-phrase-suggestions.md). |
| `POST` | `/v1/suggestions/categories/query` | Returns genre category names for apps or brands, or matched by name. Supports `SUGGESTION` and `SEARCH` routes. See [`Query Category Suggestions`](query-category-suggestions.md). |
| `POST` | `/v1/suggestions/target-cpas/query` | Retrieves the recommended target CPA for an App Store app based on recent tap-install CPI data. See [`Query Target CPA Suggestion`](query-target-cpa-suggestion.md). |

##### Request Keyword Suggestions

The `promotedObjectId` and `promotedObjectType` fields are both required. Optionally scope results to specific App Store countries or regions with `countriesOrRegions`, or seed with specific `terms` to get related suggestions. Results are [`KeywordSuggestion`](keywordsuggestion.md) objects. To activate a suggestion, create a keyword entity via [`Create a Keyword`](post-keywords.md). Here’s a sample request that scopes suggestions to a single app and two countries:

```json
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
      "field": "countriesOrRegions",
      "operator": "IN",
      "value": [
        "US",
        "GB"
      ]
    }
  ],
  "sorting": [
    {
      "field": "popularity",
      "order": "DESC"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20
  }
}
```

##### Request Phrase and Category Suggestions

Phrase and category suggestions support two distinct query routes, and you can use only one per request:

| `queryType` | Purpose | Required Filters |
| --- | --- | --- |
| `SUGGESTION` | Discover suggestions for a specific app or brand. | `promotedObjectId`, `promotedObjectType` |
| `SEARCH` | Look up popularity for known values, or search by partial string. | `phrase` or `category` with `IN` (exact lookup) or `LIKE` (partial match) |

Use `SUGGESTION` when building a keyword list from scratch. Use `SEARCH` to check whether a specific phrase or category name has meaningful traffic, or to enumerate options with a partial string.

## Topics

- [Query Keyword Suggestions](query-keyword-suggestions.md)
  Query keyword suggestions based on search terms and App Store countries or regions using structured filters.
- [Query Phrase Suggestions](query-phrase-suggestions.md)
  Query phrase suggestions using either a discovery or search route based on the query type.
- [Query Category Suggestions](query-category-suggestions.md)
  Query category suggestions for apps or brands using either a discovery or search route based on the query type.
- [Query Target CPA Suggestion](query-target-cpa-suggestion.md)
  Retrieve the recommended target CPA for a new Maximize Conversions campaign on the App Store.

## See Also

- [Recommendations Endpoints](recommendations-endpoints.md)
  Endpoints for querying, applying, and dismissing budget and Target CPA recommendations.
- [Managing Reports](reports.md)
  Retrieve performance data for campaigns, ad groups, ads, keywords, and search terms.
- [Insights Endpoints](insights-endpoints.md)
  Query impression share and search term popularity data for your apps.
- [Suggestions Data Objects](suggestions-data-objects.md)
  Response objects for keyword, phrase, category, and Target CPA suggestion endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/suggestions-endpoints)*