# Campaign.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable run state for a campaign.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Campaign.Status
```

#### Discussion

This field directly controls auction eligibility for the campaign, independent of the system-computed [`Campaign.SystemStatus`](campaign/systemstatus-data.typealias.md).

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`CampaignStatus`](campaignstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/status-data.typealias)*