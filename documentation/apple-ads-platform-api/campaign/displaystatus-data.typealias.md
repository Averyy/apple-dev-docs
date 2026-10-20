# Campaign.DisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string Campaign.DisplayStatus
```

#### Discussion

Because it merges both inputs into one label, a campaign set to `ENABLED` can still display as `ON_HOLD` or `LIMITED` when a system condition intervenes.

##### Example

```json
{
  "displayStatus": "RUNNING"
}
```

See [`CampaignDisplayStatus`](campaigndisplaystatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/displaystatus-data.typealias)*