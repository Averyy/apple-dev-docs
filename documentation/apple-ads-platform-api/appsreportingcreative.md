# AppsReportingCreative

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Creative metadata for APPS ads.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsReportingCreative
```

#### Discussion

`AppsReportingCreative` is the creative metadata snapshot embedded within `AppsReportingAd` in APPS ad report rows. The `creativeType` field identifies the creative format: `DEFAULT_PRODUCT_PAGE` and `CUSTOM_PRODUCT_PAGE` both use App Store product page assets.

`systemStatus` reflects the creative’s validity at report time: `INVALID` creatives cannot serve and will not generate impressions. The `creativeSpec` provides a summary of the creative’s content configuration, and `destination` captures the click-through destination.

##### Example

```json
{
  "id": 555666777,
  "creativeType": "CUSTOM_PRODUCT_PAGE",
  "systemStatus": "VALID",
  "creativeSpec": {
    "language": "en-US"
  },
  "destination": {
    "parameters": {
      "productPageId": "555666777",
      "url": "https://apps.apple.com/us/app/awayfinder/id123456789"
    }
  }
}
```

## Topics

### Type Aliases
- [type AppsReportingCreative.CreativeType](appsreportingcreative/creativetype-data.typealias.md)
  The visual format and placement context of the creative at report time.
- [type AppsReportingCreative.SystemStatus](appsreportingcreative/systemstatus-data.typealias.md)
  System-evaluated validation state of the creative at report time.

## Properties

- `id` (int64): The creative’s unique identifier.
- `creativeType` (AppsReportingCreative.CreativeType): Possible values: `CUSTOM_PRODUCT_PAGE`, `DEFAULT_PRODUCT_PAGE`.
- `systemStatus` (AppsReportingCreative.SystemStatus): Possible values: `VALID`, `INVALID`, `PENDING`.
- `creativeSpec` (ReportingCreativeSpec): See [`ReportingCreativeSpec`](reportingcreativespec.md) for details.
- `destination` (ReportingDestination): See [`ReportingDestination`](reportingdestination.md) for details.

## See Also

- [object AppsReportingRequest](appsreportingrequest.md)
  Request body for APPS reporting queries.
- [object AppsReportingCampaign](appsreportingcampaign.md)
  Campaign metadata for APPS report rows.
- [object AppsReportingAdGroup](appsreportingadgroup.md)
  Ad group metadata for APPS report rows.
- [object AppsReportingAd](appsreportingad.md)
  Ad metadata for APPS report rows.
- [object AppsCampaignReportResponse](appscampaignreportresponse.md)
  The top-level response envelope for APPS campaign-level reports.
- [object AppsCampaignReportRow](appscampaignreportrow.md)
  A single row in an APPS campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object AppsCampaignReportSummary](appscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps campaign report.
- [object AppsCampaignResultContainer](appscampaignresultcontainer.md)
  Wraps the array of Apps campaign report rows along with a grand-total summary.
- [object AppsAdGroupReportResponse](appsadgroupreportresponse.md)
  The top-level response envelope for APPS ad group reports.
- [object AppsAdGroupReportRow](appsadgroupreportrow.md)
  A single row in an Apps ad group report, containing ad group metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdGroupReportSummary](appsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad group report.
- [object AppsAdGroupResultContainer](appsadgroupresultcontainer.md)
  Wraps the array of Apps ad group report rows along with a grand-total summary.
- [object AppsAdReportResponse](appsadreportresponse.md)
  The top-level response envelope for APPS ad-level reports.
- [object AppsAdReportRow](appsadreportrow.md)
  A single row in an Apps ad-level report, containing ad metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdReportSummary](appsadreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad-level report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingcreative)*