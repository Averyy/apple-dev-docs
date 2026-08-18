# TargetCpaSuggestion

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A suggested Target CPA for a new Maximize Conversions campaign, based on historical performance and market conditions.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object TargetCpaSuggestion
```

#### Discussion

`TargetCpaSuggestion` represents the recommended cost-per-acquisition goal returned by the Target CPA suggestions endpoint. Use this value as the starting Target CPA when creating a new [`Campaigns Endpoints`](campaigns-endpoints.md) campaign.

##### Example

```json
{
  "suggestedTargetCPA": {
    "amount": "3.75",
    "currency": "USD"
  },
  "countryOrRegion": [
    "US",
    "GB"
  ],
  "promotedObjectId": "555666777",
  "appCategory": "Games"
}
```

## Properties

- `suggestedTargetCPA` (RecommendationMoney): The suggested Target CPA. Calculated as the maximum tap-install CPI across the evaluated countries or regions that have at least 10 installs in the last 28 days, scoped to the app’s category. See [`Money`](recommendationmoney.md). Read-only.
- `countryOrRegion` ([string]): The country or region codes that this suggestion applies to. Read-only.
- `promotedObjectId` (string): The ID of the promoted object (app or brand) this suggestion was calculated for. Read-only.
- `appCategory` (string): The App Store category used to scope the suggestion’s performance data. Read-only.

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
- [object RecommendationQueryTargetCpaSuggestionResponse](recommendationquerytargetcpasuggestionresponse.md)
  Response envelope returned by the Target CPA suggestions endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/targetcpasuggestion)*