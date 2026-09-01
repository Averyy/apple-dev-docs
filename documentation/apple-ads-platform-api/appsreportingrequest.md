# AppsReportingRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request body for apps reporting queries.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object AppsReportingRequest
```

#### Discussion

The `AppsReportingRequest` object is the request body for all apps entity-level report endpoints (campaign, ad group, ad, keyword, search term).

##### Example

```json
{
  "pagination": {
    "offset": 0,
    "pageSize": 20
  },
  "sorting": [
    {
      "field": "localSpend",
      "order": "DESC"
    }
  ],
  "filters": [
    {
      "field": "campaignId",
      "operator": "EQUALS",
      "value": [
        "444555666"
      ]
    }
  ],
  "fields": [
    "impressions",
    "taps",
    "localSpend"
  ],
  "groupBy": [
    "countryOrRegion"
  ],
  "timeRange": {
    "start": "2025-01-01",
    "end": "2025-01-31",
    "timeZone": "ORTZ",
    "granularity": "DAILY"
  },
  "options": {
    "includeRows": ["GRAND_TOTAL"]
  }
}
```

## Properties

- `pagination` (RequestPagination): Pagination settings for the report results. See [`RequestPagination`](requestpagination.md) for details.
- `sorting` ([Sorting]): Sort entities in ascending or descending order. The default behavior is to sort by ID, ascending. See [`Sorting`](sorting.md) for details.
- `filters` ([Filter]): Filter field conditions for the report. `campaignId` is a required filter for every apps report request. See [`Filter`](filter.md) for details.
- `fields` ([string]): A list of field names to return in the response. If you omit this field, the response includes all fields.
- `groupBy` ([string]): Groups responses by selected dimensions. Supported values for apps: `deviceClass`, `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`, `storefront`, `countryOrRegion`. Note: `KEYWORD` and `SEARCHTERM` entities exclude `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`. The `AD` entity also excludes `deviceClass`, `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`, supporting only `storefront` and `countryOrRegion`.
- `timeRange` (TimeRange): The date range, timezone, and granularity for report data. Defines the start and end dates for the reporting period. See [`TimeRange`](timerange.md) for details.
- `options` (AppsOptions): Options to include additional rows in the report (for example, GRAND_TOTAL, EMPTY_METRICS). You can’t combine `EMPTY_METRICS` with `groupBy`. See [`AppsOptions`](appsoptions.md) for details.

## See Also

- [object AppsReportingCampaign](appsreportingcampaign.md)
  Campaign metadata for apps report rows.
- [object AppsReportingAdGroup](appsreportingadgroup.md)
  Ad group metadata for apps report rows.
- [object AppsReportingAd](appsreportingad.md)
  Ad metadata for apps report rows.
- [object AppsReportingCreative](appsreportingcreative.md)
  Creative metadata for apps ads.
- [object AppsCampaignReportResponse](appscampaignreportresponse.md)
  The top-level response envelope for apps campaign-level reports.
- [object AppsCampaignReportRow](appscampaignreportrow.md)
  A single row in an apps campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object AppsCampaignReportSummary](appscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps campaign report.
- [object AppsCampaignResultContainer](appscampaignresultcontainer.md)
  Wraps the array of Apps campaign report rows along with a grand-total summary.
- [object AppsAdGroupReportResponse](appsadgroupreportresponse.md)
  The top-level response envelope for apps ad group reports.
- [object AppsAdGroupReportRow](appsadgroupreportrow.md)
  A single row in an Apps ad group report, containing ad group metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdGroupReportSummary](appsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad group report.
- [object AppsAdGroupResultContainer](appsadgroupresultcontainer.md)
  Wraps the array of Apps ad group report rows along with a grand-total summary.
- [object AppsAdReportResponse](appsadreportresponse.md)
  The top-level response envelope for apps ad-level reports.
- [object AppsAdReportRow](appsadreportrow.md)
  A single row in an Apps ad-level report, containing ad metadata, total metrics, and optional granular time-series metrics.
- [object AppsAdReportSummary](appsadreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apps ad-level report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingrequest)*