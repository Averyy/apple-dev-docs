# NegativeKeywordCreate.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The matching behavior to use when creating this negative keyword.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string NegativeKeywordCreate.MatchType
```

## Possible Values

- `EXACT`: (App Store) Matches only the exact keyword term. Supported for negative keywords.
- `BROAD`: (App Store) Matches the keyword term and close variants, including plurals and misspellings. Supported for negative keywords.
- `PHRASE`: (Apple Maps) Matches the keyword and close variants within Maps search, allowing flexibility while staying focused on the search intent. Supported for negative keywords on Maps.
- `CATEGORY`: (Apple Maps keywords only) Matches user searches to a Maps business category. Use category identifiers from the Query Business Categories endpoint (for example, `dining.restaurant`, `shopping.clothing`). Does not match app categories. Not supported for negative keywords.

## Discussion

Set this when creating the negative keyword; `CATEGORY` matching isn’t available since it’s not supported for negative keywords.

### Example

```json
{
  "matchType": "BROAD"
}
```

See [`KeywordMatchType`](../keywordmatchtype.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordcreate/matchtype-data.typealias)*