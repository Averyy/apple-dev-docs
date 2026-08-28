# KeywordCreate.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The matching behavior to use when creating this keyword.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string KeywordCreate.MatchType
```

#### Discussion

Choosing `CATEGORY` restricts the keyword to Apple Maps business-category matching and rules out combining it with App Store-only options like `EXACT` or `BROAD`.

##### Example

```json
{
  "matchType": "EXACT"
}
```

See [`KeywordMatchType`](keywordmatchtype.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordcreate/matchtype-data.typealias)*