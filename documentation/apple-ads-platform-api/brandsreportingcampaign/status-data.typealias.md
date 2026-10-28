# BrandsReportingCampaign.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving status of the campaign at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingCampaign.Status
```

## Possible Values

- `ENABLED`: The campaign is set to run. Delivery depends on budget availability, eligibility, and system status.
- `PAUSED`: The campaign is paused by the advertiser. No ads will serve until the status is changed to `ENABLED`.

## Discussion

This captures the advertiser-set status as of the report’s generation, separate from the system-evaluated [`BrandsReportingCampaign.SystemStatus`](./systemstatus-data.typealias.md) alongside it.

### Example

```json
{
  "status": "ENABLED"
}
```

See [`CampaignStatus`](../campaignstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcampaign/status-data.typealias)*