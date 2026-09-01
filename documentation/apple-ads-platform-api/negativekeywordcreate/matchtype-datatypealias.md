# NegativeKeywordCreate.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The matching behavior to use when creating this negative keyword.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string NegativeKeywordCreate.MatchType
```

#### Discussion

Set this when creating the negative keyword; `CATEGORY` matching isn’t available since it’s not supported for negative keywords.

##### Example

```json
{
  "matchType": "BROAD"
}
```

See [`KeywordMatchType`](keywordmatchtype.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordcreate/matchtype-data.typealias)*