# BulkNegativeKeywordCreate.MatchType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The negative keyword’s match type for a bulk negative-keyword create item.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BulkNegativeKeywordCreate.MatchType
```

#### Discussion

Unlike positive keywords, negative keywords can use `EXACT`, `BROAD`, or `PHRASE`, but not `CATEGORY` matching.

##### Example

```json
{
  "matchType": "BROAD"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulknegativekeywordcreate/matchtype-data.typealias)*