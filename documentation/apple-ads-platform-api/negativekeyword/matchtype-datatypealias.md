# NegativeKeyword.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The matching behavior used to compare this negative keyword against user search queries.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string NegativeKeyword.MatchType
```

#### Discussion

Unlike positive keywords, negative keywords can use `EXACT`, `BROAD`, or `PHRASE`, but not `CATEGORY` matching.

##### Example

```json
{
  "matchType": "BROAD"
}
```

See [`KeywordMatchType`](keywordmatchtype.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeyword/matchtype-data.typealias)*