# Campaign.DisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Campaign.DisplayStatus
```

## Possible Values

- `RUNNING`: The campaign is actively delivering ads.
- `PAUSED`: The advertiser paused the campaign.
- `ON_HOLD`: Delivery is stopped due to a system or account condition.
- `LIMITED`: The campaign is serving but at reduced capacity due to a system condition.
- `PROCESSING`: The campaign was recently created or modified and is being processed.
- `DELETED`: The campaign has been soft-deleted.

#### Discussion

Because it merges both inputs into one label, a campaign set to `ENABLED` can still display as `ON_HOLD` or `LIMITED` when a system condition intervenes.

##### Example

```json
{
  "displayStatus": "RUNNING"
}
```

See [`CampaignDisplayStatus`](../campaigndisplaystatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/displaystatus-data.typealias)*