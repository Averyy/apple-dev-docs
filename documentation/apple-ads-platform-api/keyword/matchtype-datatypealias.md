# Keyword.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The matching behavior used to compare this keyword against user search queries.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Keyword.MatchType
```

#### Discussion

Available options differ by platform: App Store keywords use `EXACT` or `BROAD`, while Apple Maps keywords add `PHRASE` and category-based matching.

##### Example

```json
{
  "matchType": "EXACT"
}
```

See [`KeywordMatchType`](keywordmatchtype.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keyword/matchtype-data.typealias)*