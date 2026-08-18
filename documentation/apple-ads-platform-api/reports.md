# Managing Reports

**Framework**: Apple Ads Platform API

Retrieve performance data for campaigns, ad groups, ads, keywords, and search terms.

#### Overview

All report endpoints follow a shared `POST /query` pattern. You parameterize each request with `promotedObjectType`: either `apps` for App Store app campaigns or `business-brands` for Apple Maps campaigns. The request body, response objects, available groupBy dimensions, and supported options differ between the two promoted object types.

#### Choose a Reporting Endpoint

Query one of the following endpoints based on your promoted object type and the entity level you want to report on:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/reports/apps/campaigns/query` | [`Campaigns Report`](get-app-campaign-reports.md) retrieves App Store campaign performance data. |
| `POST` | `/v1/reports/apps/adgroups/query` | [`Ad Groups Report`](get-app-ad-group-reports.md) retrieves App Store ad group performance data. |
| `POST` | `/v1/reports/apps/ads/query` | [`Ads Report`](get-app-ad-reports.md) retrieves App Store ad performance data. |
| `POST` | `/v1/reports/apps/keywords/query` | [`Keywords Report`](get-app-keyword-reports.md) retrieves App Store keyword performance data. |
| `POST` | `/v1/reports/apps/searchterms/query` | [`Search Terms Report`](get-app-search-term-reports.md) retrieves App Store search term performance data. |
| `POST` | `/v1/reports/business-brands/campaigns/query` | [`Campaigns Report (Brands)`](get-brand-campaign-reports.md) retrieves Apple Maps campaign performance data. |
| `POST` | `/v1/reports/business-brands/adgroups/query` | [`Ad Groups Report (Brands)`](get-brand-ad-group-reports.md) retrieves Apple Maps ad group performance data. |
| `POST` | `/v1/reports/business-brands/ads/query` | [`Ads Report (Brands)`](get-brand-ad-reports.md) retrieves Apple Maps ad performance data. |
| `POST` | `/v1/reports/business-brands/keywords/query` | [`Keywords Report (Brands)`](get-brand-keyword-reports.md) retrieves Apple Maps keyword performance data. |
| `POST` | `/v1/reports/business-brands/searchterms/query` | [`Search Terms Report (Brands)`](get-brand-search-term-reports.md) retrieves Apple Maps search term performance data. |

##### Build the Request

Every report request uses either [`AppsReportingRequest`](appsreportingrequest.md) or [`BrandsReportingRequest`](brandsreportingrequest.md) as the request body. Both share the same top-level fields:

- The `timeRange` field defines the reporting window via [`TimeRange`](timerange.md): `start` date, `end` date, `timeZone` (`UTC` or `ORTZ`), and optional `granularity` (`HOURLY`, `DAILY`, `WEEKLY`, `MONTHLY`).
- The `filters` field is an array of [`Filter`](filter.md) conditions that narrow results by field, operator, and value.
- The `sorting` field is an array of [`Sorting`](sorting.md) objects that order rows by field and direction.
- The `pagination` field uses [`RequestPagination`](requestpagination.md), with `offset` and `pageSize` (maximum 5000, default 100).
- The `fields` field is an optional list of field names to return. Omit it to receive all fields.
- The `groupBy` field is an optional dimensional breakdown. Supported values differ between Apps and Brands, and additional restrictions apply at the keyword and search term entity levels. When you omit `groupBy`, the response returns one aggregate row per entity with no dimensional breakdown. We recommend providing at least one `groupBy` value to get meaningful segmented data in most reporting use cases.
- The `options` field sets row inclusion flags via [`AppsOptions`](appsoptions.md) or [`BrandsOptions`](brandsoptions.md).

##### Read the Response

All report responses share the same envelope: a `result` object containing a `rows` array of report rows and a `summary.grandTotal` object, plus a `pagination` object and an `error` field. Each row contains:

- The `totalMetrics` field holds aggregate metrics for the row over the full time range.
- The `granularMetrics` field breaks out metrics by the requested `granularity` period, and it appears only when you specify `granularity` in the request.
- The `metadata` field holds entity attributes (campaign name, status, targeting, and so on) plus any `groupBy` dimension values applied to the row.

When you include `GRAND_TOTAL` in `options.includeRows`, the response also includes a summary row with totals across all result rows.

##### Apply Granularity Constraints

Granularity is an optional time-series breakdown that applies to `granularMetrics`. The following constraints apply to all entities and both promoted object types unless noted:

| Granularity | Constraint |
| --- | --- |
| `HOURLY` | Date range must start within the last 7 days. Ad-level and search term-level reports don’t support it. |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there’s no `granularMetrics` breakdown to compute.

##### Compare Apps and Brands Reporting

Apps and Brands campaigns measure different coverage: app installs and engagement versus brand visibility and map interactions. Their reporting reflects this distinction. The two promoted object types use separate request and response objects and differ in the following ways:

| Feature | Apps (`apps`) | Brands (`business-brands`) |
| --- | --- | --- |
| Request object | [`AppsReportingRequest`](appsreportingrequest.md) | [`BrandsReportingRequest`](brandsreportingrequest.md) |
| Campaign/ad-group `groupBy` dimensions | `deviceClass`, `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`, `storefront`, `countryOrRegion` | `deviceClass`, `locationId`, `supplyPlacement` |
| Keyword `groupBy` dimensions | `deviceClass`, `storefront`, `countryOrRegion` | `deviceClass` |
| Search term `groupBy` dimensions | `deviceClass`, `storefront`, `countryOrRegion` | `deviceClass` |
| Ad `groupBy` dimensions | `storefront`, `countryOrRegion` | `deviceClass`, `locationId`, `supplyPlacement` |
| `EMPTY_METRICS` option | Supported | Not supported |
| Creative metadata | [`AppsReportingCreative`](appsreportingcreative.md): includes `creativeSpec` and `destination` | [`BrandsReportingCreative`](brandsreportingcreative.md): includes `id`, `creativeType`, and `systemStatus` only |
| Location-level report | Not available | Not available |
| Search term timezone | `ORTZ` only | `ORTZ` only |

##### Include Additional Rows

The `options.includeRows` field controls which additional rows appear in the response:

- The `GRAND_TOTAL` value adds a summary row with aggregate totals across all result rows. Both Apps and Brands support it.
- The `EMPTY_METRICS` value includes rows for entities that have no metric activity during the requested period. Only Apps supports it, and you can’t combine it with `groupBy`.

## See Also

- [Insights Endpoints](insights-endpoints.md)
  Query impression share and search term popularity data for your apps.
- [Recommendations Endpoints](recommendations-endpoints.md)
  Endpoints for querying, applying, and dismissing budget and Target CPA recommendations.
- [Suggestions Endpoints](suggestions-endpoints.md)
  Endpoints for querying keyword, phrase, category, and Target CPA suggestions.
- [Change History Endpoints](change-history-endpoints.md)
  Query audit summaries and retrieve change detail records for entities in an ad account.
- [App Store Reports Endpoints](apps-reports-endpoints.md)
  Endpoints for retrieving App Store campaign, ad group, ad, keyword, and search term performance data.
- [Brands Reports Endpoints](brands-reports-endpoints.md)
  Retrieve performance data for Apple Maps campaigns, ad groups, ads, keywords, and search terms.
- [Apps Data Objects](apps-reports-objects.md)
  Request, response, and metadata objects for Apps report endpoints.
- [Brands Data Objects](brands-reports-objects.md)
  Explore the request, response, and metadata objects that Brands report endpoints use.
- [Shared Objects](reports-shared-objects.md)
  Shared request and response objects used across Apps and Brands report endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/reports)*