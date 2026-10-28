# CampaignCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable run state for a campaign.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string CampaignCreate.Status
```

## Possible Values

- `ENABLED`: The campaign is set to run. Delivery depends on budget availability, eligibility, and system status.
- `PAUSED`: The advertiser paused the campaign. No ads serve until the status changes to `ENABLED`.

## Discussion

Include `status` in the create request to determine whether the new campaign begins competing for delivery immediately or starts paused.

### Example

```json
{
  "status": "ENABLED"
}
```

See [`CampaignStatus`](../campaignstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate/status-data.typealias)*