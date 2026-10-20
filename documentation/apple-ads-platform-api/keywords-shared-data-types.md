# Keywords Shared Data Types

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Set the status and match type of keywords and negative keywords, and interpret a keyword’s display status.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Keywords and negative keywords share these types, so each status or match type has one definition to look up. [`KeywordStatus`](./keywordstatus.md) and [`NegativeKeywordStatus`](./negativekeywordstatus.md) control whether an entity is active or paused. [`KeywordMatchType`](./keywordmatchtype.md) controls how a keyword’s text matches searches, and [`KeywordDisplayStatus`](./keyworddisplaystatus.md) reports a keyword’s rolled-up delivery state.

## Topics

- [type KeywordStatus](./keywordstatus.md)
  Enumeration of advertiser-configurable serving states for a keyword.
- [type KeywordMatchType](./keywordmatchtype.md)
  The matching behavior used to compare a keyword against user search queries.
- [type KeywordDisplayStatus](./keyworddisplaystatus.md)
  Rolled-up delivery state for a keyword, combining advertiser settings and parent entity status.
- [type NegativeKeywordStatus](./negativekeywordstatus.md)
  Advertiser-configurable active state for a negative keyword.

## See Also

### Keywords
- [Managing Keywords and Negative Keywords](./keywords-and-negative-keywords.md)
  Create and manage keywords and negative keywords for ad groups and campaigns.
- [Keywords Endpoints](./keywords-endpoints.md)
  Create, retrieve, update, query, and delete the keywords that match your ad group’s ads to searches.
- [Negative Keywords Endpoints](./negative-keywords-endpoints.md)
  Create, retrieve, update, query, and delete negative keywords that block ads for unwanted searches.
- [Keywords Data Objects](./keywords-data-objects.md)
  Build keyword create and update requests, and read keyword responses and query results.
- [Negative Keywords Data Objects](./negative-keywords-objects.md)
  Build negative keyword create and update requests, and read responses and query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywords-shared-data-types)*