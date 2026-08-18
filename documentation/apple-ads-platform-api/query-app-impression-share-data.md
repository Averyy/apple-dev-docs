# Impression Share Query

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve impression share data showing how often your ads appear relative to total eligible impressions for a given search term and country.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint measures impression share: what fraction of available impressions your app captures for a given search term and country. To identify competitive gaps, use this data. A low impression share on a high-volume term indicates that either budget, bid, or eligibility constraints are limiting your reach.

A filter on `promotedObjectId` is required. Omitting it will result in a 400 error. The endpoint returns results synchronously as paginated JSON.

##### Output Types

Configure the output type via `options.impressionShareReportType`:

| Type | Description |
| --- | --- |
| `FIRST_SLOT` | Measures impression share for the first ad position only. |
| `ALL_SLOTS` | Measures impression share across all ad positions. |

Each row in the response carries the following fields.

| Field | Description |
| --- | --- |
| `day` | Date (`YYYY-MM-DD`). Present when granularity is `DAILY`. |
| `week` | Week start date, Sunday (`YYYY-MM-DD`). Present when granularity is `WEEKLY_SUN_SAT`. |
| `appName` | Display name of the promoted app. |
| `promotedObjectId` | Adam ID of the promoted app. |
| `countryOrRegion` | ISO 3166-1 alpha-2 country or region code. |
| `searchTerm` | The search term. Terms with fewer than 10 impressions in the period are suppressed. |
| `lowImpressionShare` | Lower bound of impression share. See Impression Share Encoding below. |
| `highImpressionShare` | Upper bound of impression share. See Impression Share Encoding below. |
| `rank` | App’s impression share rank for this search term and country. `1` = highest share. |
| `searchPopularity1to5` | Relative search volume on a 1–5 scale. `5` = most popular. |

##### Impression Share Encoding

`lowImpressionShare` and `highImpressionShare` use a tiered encoding, not a continuous range:

| Impression Share | `lowImpressionShare` | `highImpressionShare` |
| --- | --- | --- |
| 0% | `0` | `0` |
| 1% – 90% | `x` (e.g. `0.23`) | `x` (same value) |
| 91% – 100% | `0.91` | `1` |

For single-digit values (1–90%), both fields are equal. When `highImpressionShare` equals `1`, the app has >90% impression share. The encoding preserves the range at that level to avoid false precision near market saturation.

The following limits and defaults apply to this endpoint’s requests and responses.

| Constraint | Detail |
| --- | --- |
| Timezone | Fixed to `UTC`. |
| Granularity | Supports `DAILY` and `WEEKLY_SUN_SAT` only. |
| `DAILY` max range | 30 days (inclusive). |
| `WEEKLY_SUN_SAT` max range | 4 weeks (`LAST_4_WEEK`). |
| Weekly start date | When `granularity` is `WEEKLY_SUN_SAT`, `timeRange.start` must be a Sunday. The endpoint rejects requests with a non-Sunday start date. |
| Default `pageSize` | 100. |
| Maximum `pageSize` | 5000. |
| Sort fields | Maximum 2 sort fields per request. |
| High-saturation bucket | `lowImpressionShare: 0.91, highImpressionShare: 1.0` indicates >90% impression share. Marginal bid increases at this level yield diminishing returns. |
| Privacy filter | The privacy filter suppresses `searchTerm` for terms with fewer than 10 impressions in the aggregation period. |

##### Estimate Market Size

To estimate total eligible inventory for a search term, use impression share alongside confirmed impressions:

`estimated_market_impressions ≈ confirmed_impressions / lowImpressionShare`

**Example:** 10,000 confirmed impressions at `lowImpressionShare: 0.04` (4%) → ≈ 250,000 total eligible impressions. The same app at `lowImpressionShare: 0.91` (>90% bucket) has captured nearly all available inventory. Single-digit precision makes this estimate meaningful across the 1–90% range covered by `lowImpressionShare`. Only within the 91–100% bucket, where `lowImpressionShare` and `highImpressionShare` diverge to `0.91` and `1.0`, does the estimate lose that precision.

#### Payload Examples

**First Slot: Search Term**:

Retrieve daily first-slot impression share for an app, filtered to a specific country and search term.

##### Request

Queries daily first-slot impression share for a specific app in the US over a seven-day window, scoping results to the first ad position only.

```json
POST /v1/insights/apps/impression-share/query

{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": "123456789"
   },
   {
     "field": "countryOrRegion",
     "operator": "EQUALS",
     "value": "US"
   }
 ],
 "options": {
   "impressionShareReportType": "FIRST_SLOT"
 },
 "timeRange": {
   "start": "2025-01-01",
   "end": "2025-01-07",
   "granularity": "DAILY"
 },
 "pagination": {
   "offset": 0,
   "pageSize": 20
 }
}
```

##### Response

```json
{
 "result": {
   "rows": [
     {
       "day": "2025-01-01",
       "appName": "AwayFinder",
       "promotedObjectId": "123456789",
       "countryOrRegion": "US",
       "searchTerm": "travel planner app",
       "lowImpressionShare": 0.18,
       "highImpressionShare": 0.18,
       "rank": 2,
       "searchPopularity1to5": 4
     },
     {
       "day": "2025-01-01",
       "appName": "AwayFinder",
       "promotedObjectId": "123456789",
       "countryOrRegion": "US",
       "searchTerm": "trip organizer",
       "lowImpressionShare": 0.35,
       "highImpressionShare": 0.35,
       "rank": 1,
       "searchPopularity1to5": 3
     }
   ]
 },
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**All Slots: Weekly**:

Retrieve weekly all-slots impression share to understand overall reach across all ad positions.

##### Request

Queries weekly all-slots impression share for an app over a four-week window (the maximum for `WEEKLY_SUN_SAT` granularity), sorted by `highImpressionShare` descending to highlight the search terms with the strongest reach.

```json
POST /v1/insights/apps/impression-share/query

{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": "123456789"
   }
 ],
 "options": {
   "impressionShareReportType": "ALL_SLOTS"
 },
 "timeRange": {
   "start": "2024-10-06",
   "end": "2024-10-27",
   "granularity": "WEEKLY_SUN_SAT"
 },
 "sorting": [
   {
     "field": "highImpressionShare",
     "order": "DESC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 50
 }
}
```

##### Response

```json
{
 "result": {
   "rows": [
     {
       "week": "2024-10-06",
       "appName": "AwayFinder",
       "promotedObjectId": "123456789",
       "countryOrRegion": "US",
       "searchTerm": "vacation planning",
       "lowImpressionShare": 0.42,
       "highImpressionShare": 0.42,
       "rank": 1,
       "searchPopularity1to5": 5
     }
   ]
 },
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 50
 }
}
```

**High Saturation: Branded Term**:

Retrieve first-slot impression share for a branded search term. When `lowImpressionShare` and `highImpressionShare` are `0.91` and `1.0`, the app holds >90% of available impressions (the 91–100% bucket). Bid increases at this level yield negligible gains.

##### Request

Queries daily first-slot impression share for a branded term where the app already dominates the auction.

```json
POST /v1/insights/apps/impression-share/query

{
 "filters": [
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": "123456789"
   },
   {
     "field": "countryOrRegion",
     "operator": "EQUALS",
     "value": "US"
   }
 ],
 "options": {
   "impressionShareReportType": "FIRST_SLOT"
 },
 "timeRange": {
   "start": "2025-01-01",
   "end": "2025-01-07",
   "granularity": "DAILY"
 },
 "pagination": {
   "offset": 0,
   "pageSize": 20
 }
}
```

##### Response

```json
{
 "result": {
   "rows": [
     {
       "day": "2025-01-01",
       "appName": "AwayFinder",
       "promotedObjectId": "123456789",
       "countryOrRegion": "US",
       "searchTerm": "awayfinder",
       "lowImpressionShare": 0.91,
       "highImpressionShare": 1.0,
       "rank": 1,
       "searchPopularity1to5": 2
     }
   ]
 },
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/insights/apps/impression-share/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Search Term Popularity Query](query-app-search-term-popularity-data.md)
  Retrieve the relative search volume ranking of search terms for a given App Store genre and country or region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-app-impression-share-data)*