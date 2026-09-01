# Campaign.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-evaluated delivery state indicating whether a campaign is currently running.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Campaign.SystemStatus
```

#### Discussion

This status reflects the campaign specifically, separate from the advertiser-set [`Campaign.Status`](campaign/status-data.typealias.md) and the system status of ad groups within it.

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`CampaignSystemStatus`](campaignsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/systemstatus-data.typealias)*