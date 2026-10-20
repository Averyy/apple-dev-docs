# Suggestions Data Objects

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Read the keyword, phrase, category, and Target CPA suggestions that the suggestions endpoints return.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Each suggestion endpoint returns its own result object: [`KeywordSuggestion`](./keywordsuggestion.md), [`PhraseSuggestion`](./phrasesuggestion.md), [`CategorySuggestion`](./categorysuggestion.md), or [`TargetCpaSuggestion`](./targetcpasuggestion.md), each inside a matching query response. Suggestion requests reuse the query and filter objects in [Recommendations Query and Filter Objects](./recommendations-query-filter-objects.md).

For the calls that return these objects, see [Suggestions Endpoints](./suggestions-endpoints.md).

## Topics

- [object KeywordSuggestion](./keywordsuggestion.md)
  A keyword suggestion returned by the keyword suggestions endpoint.
- [object PhraseSuggestion](./phrasesuggestion.md)
  A phrase suggestion returned by the phrase suggestions endpoint.
- [object CategorySuggestion](./categorysuggestion.md)
  A category suggestion returned by the category suggestions endpoint, for either an App Store app or an Apple Maps brand.
- [object RecommendationQueryKeywordSuggestionResponse](./recommendationquerykeywordsuggestionresponse.md)
  Response envelope returned by the keyword suggestions query endpoint, containing suggested keywords.
- [object RecommendationQueryPhraseSuggestionResponse](./recommendationqueryphrasesuggestionresponse.md)
  Response envelope returned by the phrase suggestions query endpoint, containing suggested phrases.
- [object RecommendationQueryCategorySuggestionResponse](./recommendationquerycategorysuggestionresponse.md)
  Response envelope returned by the category suggestions query endpoint, containing matched category suggestions.
- [object TargetCpaSuggestion](./targetcpasuggestion.md)
  A suggested Target CPA for a new Maximize Conversions campaign, based on historical performance and market conditions.
- [object RecommendationQueryTargetCpaSuggestionResponse](./recommendationquerytargetcpasuggestionresponse.md)
  Response envelope returned by the Target CPA suggestions endpoint.

## See Also

### Suggestions
- [Suggestions Endpoints](./suggestions-endpoints.md)
  Discover keyword, phrase, category, and Target CPA suggestions to expand keywords and size bids.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/suggestions-data-objects)*