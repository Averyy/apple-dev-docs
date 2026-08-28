# Ad.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable serving status for an ad.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Ad.Status
```

#### Discussion

The `Status` field controls auction eligibility directly, while the system-computed [`Ad.SystemStatus`](ad/systemstatus-data.typealias.md) reflects whether the ad is actually delivering.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdStatus`](adstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ad/status-data.typealias)*