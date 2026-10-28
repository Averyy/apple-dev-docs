# AppsReportingCampaign.AdChannelType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The advertising channel type of the campaign at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AppsReportingCampaign.AdChannelType
```

## Possible Values

- `SEARCH`: Metrics from Search results ads.
- `DISPLAY`: Metrics from Search tab, Today tab, or Product Pages ads.

## Discussion

This distinguishes `SEARCH` results placements from `DISPLAY` placements such as the Search tab, Today tab, or product pages for this campaign’s rows.

### Example

```json
{
  "adChannelType": "SEARCH"
}
```

See [`ReportingAdChannelType`](../reportingadchanneltype.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingcampaign/adchanneltype-data.typealias)*