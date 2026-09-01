# Ad.SystemStatusLimitingReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Reasons that limit an ad’s delivery capacity without fully stopping it.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Ad.SystemStatusLimitingReasons
```

#### Discussion

Unlike [`Ad.SystemStatusReasons`](ad/systemstatusreasons-data.typealias.md), these codes flag conditions, such as creative policy issues, that reduce delivery rather than stop it outright.

##### Example

```json
{
  "systemStatusLimitingReasons": ["CREATIVE_POLICY_ISSUES"]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ad/systemstatuslimitingreasons-data.typealias)*