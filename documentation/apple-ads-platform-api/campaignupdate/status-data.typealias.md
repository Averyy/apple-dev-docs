# CampaignUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable run state for a campaign.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string CampaignUpdate.Status
```

## Possible Values

- `ENABLED`: The campaign is set to run. Delivery depends on budget availability, eligibility, and system status.
- `PAUSED`: The advertiser paused the campaign. No ads serve until the status changes to `ENABLED`.

#### Discussion

Send `status: PAUSED` to stop an existing campaign from competing for delivery, or `ENABLED` to resume it.

##### Example

```json
{
  "status": "PAUSED"
}
```

See [`CampaignStatus`](../campaignstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignupdate/status-data.typealias)*