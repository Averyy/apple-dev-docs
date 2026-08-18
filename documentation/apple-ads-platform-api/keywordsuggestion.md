# KeywordSuggestion

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A keyword suggestion returned by the keyword suggestions endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object KeywordSuggestion
```

#### Discussion

`KeywordSuggestion` represents a single keyword text suggestion for an APPS campaign.

These suggestions are discovery tools. They surface keywords that may not already be in the ad group but are relevant to the app. Sort suggestions by `popularity` to add the highest-impact keywords first.

##### Example

```json
{
  "text": "productivity app",
  "popularity": 85
}
```

## Properties

- `text` (string): The suggested keyword text. Read-only.
- `popularity` (int32): Relative popularity score (not an absolute volume) for this keyword across App Store countries or regions. Read-only.

## See Also

- [object PhraseSuggestion](phrasesuggestion.md)
  A phrase suggestion returned by the phrase suggestions endpoint.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordsuggestion)*