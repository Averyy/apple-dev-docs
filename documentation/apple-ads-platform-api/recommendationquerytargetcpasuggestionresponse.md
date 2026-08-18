# RecommendationQueryTargetCpaSuggestionResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Response envelope returned by the Target CPA suggestions endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationQueryTargetCpaSuggestionResponse
```

#### Discussion

`RecommendationQueryTargetCpaSuggestionResponse` is the top-level response body for `POST /suggestions/target-cpas/query`.

##### Example

```json
{
  "result": {
    "promotedObjectId": "123456789",
    "countryOrRegion": [
      "US",
      "GB"
    ],
    "suggestedTargetCPA": {
      "amount": "1.50",
      "currency": "USD"
    },
    "appCategory": "Games"
  },
  "pagination": null
}
```

## Properties

- `result` (TargetCpaSuggestion): The suggested Target CPA. See [`TargetCpaSuggestion`](targetcpasuggestion.md). Read-only.
- `pagination` (RecommendationResponsePagination): Pagination metadata. `null` for this endpoint, since it always returns a single result rather than a list. See [`ResponsePagination`](recommendationresponsepagination.md). Read-only.
- `error` (RecommendationResponseError): Error details when the request fails, in which case `result` is absent. Absent on success. See [`ResponseError`](recommendationresponseerror.md). Read-only.

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
- [object RecommendationQueryCategorySuggestionResponse](recommendationquerycategorysuggestionresponse.md)
  Response envelope returned by the category suggestions query endpoint, containing matched category suggestions.
- [object TargetCpaSuggestion](targetcpasuggestion.md)
  A suggested Target CPA for a new Maximize Conversions campaign, based on historical performance and market conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationquerytargetcpasuggestionresponse)*