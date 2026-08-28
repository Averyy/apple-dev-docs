# CampaignCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable run state for a campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string CampaignCreate.Status
```

#### Discussion

Include `status` in the create request to determine whether the new campaign begins competing for delivery immediately or starts paused.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`CampaignStatus`](campaignstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate/status-data.typealias)*