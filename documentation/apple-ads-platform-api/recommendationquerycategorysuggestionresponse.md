# RecommendationQueryCategorySuggestionResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Response envelope returned by the category suggestions query endpoint, containing matched category suggestions.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationQueryCategorySuggestionResponse
```

## Properties

- `result` ([CategorySuggestion]): The category suggestions matching the query. Array of [`CategorySuggestion`](categorysuggestion.md). Read-only.
- `pagination` (RecommendationResponsePagination): Pagination metadata for the result set. See [`ResponsePagination`](recommendationresponsepagination.md). Read-only.
- `error` (RecommendationResponseError): Error details when the request fails. Absent on success. See [`ResponseError`](recommendationresponseerror.md). Read-only.

## See Also

- [object KeywordSuggestion](keywordsuggestion.md)
  A keyword suggestion returned by the keyword suggestions endpoint.
- [object PhraseSuggestion](phrasesuggestion.md)
  A phrase suggestion returned by the phrase suggestions endpoint.
- [object CategorySuggestion](categorysuggestion.md)
  A category suggestion returned by the category suggestions endpoint, for either an App Store app or an Apple Maps brand.
- [object RecommendationQueryKeywordSuggestionResponse](recommendationquerykeywordsuggestionresponse.md)
  Response envelope returned by the keyword suggestions query endpoint, containing suggested keywords.
- [object RecommendationQueryPhraseSuggestionResponse](recommendationqueryphrasesuggestionresponse.md)
  Response envelope returned by the phrase suggestions query endpoint, containing suggested phrases.
- [object TargetCpaSuggestion](targetcpasuggestion.md)
  A suggested Target CPA for a new Maximize Conversions campaign, based on historical performance and market conditions.
- [object RecommendationQueryTargetCpaSuggestionResponse](recommendationquerytargetcpasuggestionresponse.md)
  Response envelope returned by the Target CPA suggestions endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationquerycategorysuggestionresponse)*