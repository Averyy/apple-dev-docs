# NegativeKeyword.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The matching behavior used to compare this negative keyword against user search queries.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string NegativeKeyword.MatchType
```

## Possible Values

- `EXACT`: (App Store) Matches only the exact keyword term. Supported for negative keywords.
- `BROAD`: (App Store) Matches the keyword term and close variants, including plurals and misspellings. Supported for negative keywords.
- `PHRASE`: (Apple Maps) Matches the keyword and close variants within Maps search, allowing flexibility while staying focused on the search intent. Supported for negative keywords on Maps.
- `CATEGORY`: (Apple Maps keywords only) Matches user searches to a Maps business category. Use category identifiers from the Query Business Categories endpoint (for example, `dining.restaurant`, `shopping.clothing`). Does not match app categories. Not supported for negative keywords.

## Discussion

Unlike positive keywords, negative keywords can use `EXACT`, `BROAD`, or `PHRASE`, but not `CATEGORY` matching.

### Example

```json
{
  "matchType": "BROAD"
}
```

See [`KeywordMatchType`](../keywordmatchtype.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeyword/matchtype-data.typealias)*