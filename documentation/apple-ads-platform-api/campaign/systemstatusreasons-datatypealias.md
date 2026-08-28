# Campaign.SystemStatusReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

A reason code explaining why a campaign isn’t currently running.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Campaign.SystemStatusReasons
```

#### Discussion

These reasons span budget, billing, app eligibility, and Sapin Law conditions, so resolving `NOT_RUNNING` often means checking more than just the campaign’s own settings.

##### Example

```json
{
  "systemStatusReasons": ["PROCESSING"]
}
```

See [`CampaignSystemStatusReason`](campaignsystemstatusreason.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/systemstatusreasons-data.typealias)*