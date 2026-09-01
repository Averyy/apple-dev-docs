# BulkKeywordCreate.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The keyword’s match type for a bulk keyword create item.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string BulkKeywordCreate.MatchType
```

#### Discussion

Available options vary by platform: App Store keywords use `EXACT` or `BROAD`, while Apple Maps keywords add `PHRASE` and category-based matching.

##### Example

```json
{
  "matchType": "EXACT"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulkkeywordcreate/matchtype-data.typealias)*