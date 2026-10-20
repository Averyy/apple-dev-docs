# KeywordMatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The matching behavior used to compare a keyword against user search queries.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string KeywordMatchType
```

## Possible Values

- `EXACT`: (App Store) Matches only the exact keyword term. Supported for negative keywords.
- `BROAD`: (App Store) Matches the keyword term and close variants, including plurals and misspellings. Supported for negative keywords.
- `PHRASE`: (Apple Maps) Matches the keyword and close variants within Maps search, allowing flexibility while staying focused on the search intent. Supported for negative keywords on Maps.
- `CATEGORY`: (Apple Maps keywords only) Matches user searches to a Maps business category. Use category identifiers from the Query Business Categories endpoint (for example, `dining.restaurant`, `shopping.clothing`). Does not match app categories. Not supported for negative keywords.

#### Discussion

Keywords apply only to App Store campaigns using the Search results placement. Today tab, Search tab, and Product pages campaigns use audience targeting instead.

## See Also

- [type KeywordStatus](./keywordstatus.md)
  Enumeration of advertiser-configurable serving states for a keyword.
- [type KeywordDisplayStatus](./keyworddisplaystatus.md)
  Rolled-up delivery state for a keyword, combining advertiser settings and parent entity status.
- [type NegativeKeywordStatus](./negativekeywordstatus.md)
  Advertiser-configurable active state for a negative keyword.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordmatchtype)*