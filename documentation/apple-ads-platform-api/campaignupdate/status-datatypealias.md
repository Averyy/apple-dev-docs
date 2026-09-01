# CampaignUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable run state for a campaign.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string CampaignUpdate.Status
```

#### Discussion

Send `status: PAUSED` to stop an existing campaign from competing for delivery, or `ENABLED` to resume it.

##### Example

```json
{
  "status": "PAUSED"
}
```

See [`CampaignStatus`](campaignstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignupdate/status-data.typealias)*