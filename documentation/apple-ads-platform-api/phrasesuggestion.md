# PhraseSuggestion

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A phrase suggestion returned by the phrase suggestions endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object PhraseSuggestion
```

#### Discussion

`PhraseSuggestion` represents a phrase suggestion for use as a keyword targeting input.

Phrase suggestions are similar to keyword suggestions but may reflect multi-word user queries or longer-tail search patterns. Phrase suggestions help you discover targeting opportunities beyond single-word keywords, particularly for apps with specific use cases or niche audiences.

##### Example

```json
{
  "phrase": "best productivity apps for teams",
  "popularity": 82
}
```

## Properties

- `phrase` (string): The suggested phrase text. Read-only.
- `popularity` (int32): Relative popularity score for this phrase, indicating how frequently the phrase appears in user searches. Read-only.

## See Also

- [object KeywordSuggestion](keywordsuggestion.md)
  A keyword suggestion returned by the keyword suggestions endpoint.
- [object CategorySuggestion](categorysuggestion.md)
  A category suggestion returned by the category suggestions endpoint, for either an App Store app or an Apple Maps brand.
- [object RecommendationQueryKeywordSuggestionResponse](recommendationquerykeywordsuggestionresponse.md)
  Response envelope returned by the keyword suggestions query endpoint, containing suggested keywords.
- [object RecommendationQueryPhraseSuggestionResponse](recommendationqueryphrasesuggestionresponse.md)
  Response envelope returned by the phrase suggestions query endpoint, containing suggested phrases.
- [object RecommendationQueryCategorySuggestionResponse](recommendationquerycategorysuggestionresponse.md)
  Response envelope returned by the category suggestions query endpoint, containing matched category suggestions.
- [object TargetCpaSuggestion](targetcpasuggestion.md)
  A suggested Target CPA for a new Maximize Conversions campaign, based on historical performance and market conditions.
- [object RecommendationQueryTargetCpaSuggestionResponse](recommendationquerytargetcpasuggestionresponse.md)
  Response envelope returned by the Target CPA suggestions endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/phrasesuggestion)*