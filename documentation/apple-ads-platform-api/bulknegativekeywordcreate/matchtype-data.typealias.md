# BulkNegativeKeywordCreate.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The negative keyword’s match type for a bulk negative-keyword create item.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BulkNegativeKeywordCreate.MatchType
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulknegativekeywordcreate/matchtype-data.typealias)*