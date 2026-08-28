# Keyword.DisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Rolled-up delivery state for a keyword, combining advertiser settings and parent entity status.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Keyword.DisplayStatus
```

#### Discussion

Because it rolls up the full hierarchy, a keyword can show `AD_GROUP_ON_HOLD` or `CAMPAIGN_ON_HOLD` even when its own status is otherwise fine.

##### Example

```json
{
  "displayStatus": "RUNNING"
}
```

See [`KeywordDisplayStatus`](keyworddisplaystatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keyword/displaystatus-data.typealias)*