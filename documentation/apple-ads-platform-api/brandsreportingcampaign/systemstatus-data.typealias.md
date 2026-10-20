# BrandsReportingCampaign.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

System-evaluated delivery state of the campaign at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingCampaign.SystemStatus
```

## Possible Values

- `RUNNING`: The campaign is actively delivering ads.
- `NOT_RUNNING`: The campaign isn’t currently delivering. Check `systemStatusReasons` for the cause.

#### Discussion

This reflects delivery conditions evaluated at the moment the report was generated, separate from the advertiser-set [`BrandsReportingCampaign.Status`](./status-data.typealias.md) reported alongside it.

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`CampaignSystemStatus`](../campaignsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcampaign/systemstatus-data.typealias)*