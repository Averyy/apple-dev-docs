# NegativeKeywordStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable active state for a negative keyword.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string NegativeKeywordStatus
```

## Possible Values

- `ENABLED`: The negative keyword is active and will suppress ad delivery for matching search queries.
- `PAUSED`: The negative keyword is paused and will not suppress any search queries until re-enabled.

## See Also

- [type KeywordStatus](./keywordstatus.md)
  Enumeration of advertiser-configurable serving states for a keyword.
- [type KeywordMatchType](./keywordmatchtype.md)
  The matching behavior used to compare a keyword against user search queries.
- [type KeywordDisplayStatus](./keyworddisplaystatus.md)
  Rolled-up delivery state for a keyword, combining advertiser settings and parent entity status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordstatus)*