# AppsTargetingProjection

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Targeting projection for APPS campaigns.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppsTargetingProjection
```

#### Discussion

`AppsTargetingProjection` describes the targeting scope for an APPS campaign entity as captured in a report row. Each field is an `IncludeExclude` wrapper whose `include` array lists the active targeting values at the time of the report.

##### Example

```json
{
  "supplyPlacement": {
    "include": ["APPSTORE_SEARCH_RESULTS", "APPSTORE_SEARCH_TAB"]
  },
  "lifetimeStorefronts": {
    "include": ["US", "CA", "GB"]
  },
  "countryOrRegion": {
    "include": ["US", "CA"]
  }
}
```

## Properties

- `supplyPlacement` (IncludeExclude): The ad placement slots included in delivery. Values: `APPSTORE_SEARCH_RESULTS`, `APPSTORE_SEARCH_TAB`, `APPSTORE_TODAY_TAB`, `APPSTORE_PRODUCT_PAGES`. See [`IncludeExclude`](includeexclude.md) for details.
- `lifetimeStorefronts` (IncludeExclude): App Store countries or regions targeted over the campaign’s lifetime, which may differ from the currently active `countryOrRegion` targeting. See [`IncludeExclude`](includeexclude.md) for details.
- `countryOrRegion` (IncludeExclude): ISO 3166-1 alpha-2 country codes currently targeted by the campaign. See [`IncludeExclude`](includeexclude.md) for details.

## See Also

- [object AppsReportingRequest](appsreportingrequest.md)
  Request body for APPS reporting queries.
- [object AppsReportingCampaign](appsreportingcampaign.md)
  Campaign metadata for APPS report rows.
- [object AppsReportingAdGroup](appsreportingadgroup.md)
  Ad group metadata for APPS report rows.
- [object AppsReportingAd](appsreportingad.md)
  Ad metadata for APPS report rows.
- [object AppsReportingCreative](appsreportingcreative.md)
  Creative metadata for APPS ads.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appstargetingprojection)*