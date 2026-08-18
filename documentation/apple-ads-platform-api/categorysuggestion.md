# CategorySuggestion

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A category suggestion returned by the category suggestions endpoint, for either an App Store app or an Apple Maps brand.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CategorySuggestion
```

#### Discussion

`CategorySuggestion` represents a single category suggestion for targeting.

To discover high-value categories to add as targeting criteria, use category suggestions. For App Store app campaigns, results reflect app categories. For Apple Maps campaigns, results reflect the categories associated with the brand. Sort results by `popularity` to prioritize the most impactful categories.

##### Example

```json
{
  "category": "Productivity",
  "popularity": 90
}
```

## Properties

- `category` (string): The category name. For App Store apps, an app category (e.g., `Productivity`, `Games`). For Apple Maps brands, the category associated with the brand (e.g., `Restaurants`, `Retail`). Read-only.
- `popularity` (int32): Relative popularity score for this category. Read-only.

## See Also

- [object KeywordSuggestion](keywordsuggestion.md)
  A keyword suggestion returned by the keyword suggestions endpoint.
- [object PhraseSuggestion](phrasesuggestion.md)
  A phrase suggestion returned by the phrase suggestions endpoint.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/categorysuggestion)*