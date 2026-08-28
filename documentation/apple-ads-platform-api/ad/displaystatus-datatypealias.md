# Ad.DisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Rolled-up delivery state for an ad, combining advertiser settings and system conditions into a single user-facing label.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Ad.DisplayStatus
```

#### Discussion

Because delivery depends on the full hierarchy, an ad can show `AD_GROUP_ON_HOLD` or `CAMPAIGN_ON_HOLD` even when its own settings are otherwise ready to serve.

##### Example

```json
{
  "displayStatus": "RUNNING"
}
```

See [`AdDisplayStatus`](addisplaystatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ad/displaystatus-data.typealias)*