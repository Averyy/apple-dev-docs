# Keywords Report

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for keywords.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

Keyword performance reports return one row per keyword. Each row contains a `metadata` object with keyword identifiers (including `campaignId`, `adGroupId`, `text`, and `matchType`), `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`. Rows may also include an optional `insights` object whose `bidRecommendation` field surfaces a recommended bid for the keyword.

Filter by the required `campaignId` in the `filters` array, optionally narrowed further by `adGroupId`. Use `groupBy` to split metrics along a dimension.

See [`Filter`](filter.md) for the full set of supported comparison operators.

#### Request Body

See [`AppsReportingRequest`](appsreportingrequest.md).

##### Groupby Dimensions

`deviceClass`, `countryOrRegion`

The following dimensions are **not** supported for the `KEYWORD` entity: `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`.

Date range requirements vary by granularity: `HOURLY` and `DAILY` are capped at 7-day and 90-day spans respectively, while `WEEKLY` and `MONTHLY` require spans of at least 14 and 90 days respectively.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range must span 90 days or less. |
| `HOURLY` | Date range must span 7 days or less, and the start date must be within the last 365 days. |
| `WEEKLY` | Date range must span at least 14 days. |
| `MONTHLY` | Date range must span at least 90 days. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

Always filter keyword reports by the required `campaignId`, optionally narrowed further by `adGroupId`.

| Constraint | Detail |
| --- | --- |
| Filter by `campaignId` | Required to scope results and avoid retrieving all keywords across the account. |

#### Payload Examples

**By Ad Group**:

Retrieve daily keyword metrics for all keywords in a specific ad group.

##### Request

Filters by `campaignId`, narrowed to a specific ad group with `adGroupId`, with no `groupBy` dimension, returning daily keyword metrics aggregated across all devices and countries for January 2025.

```json
POST /v1/reports/apps/keywords/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 20
 },
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": "444555666"
   },
   {
     "field": "adGroupId",
     "operator": "EQUALS",
     "value": "555666777"
   }
 ],
 "timeRange": {
   "start": "2025-01-01",
   "end": "2025-01-31",
   "timeZone": "ORTZ",
   "granularity": "DAILY"
 }
}
```

##### Response

```json
{
 "result": {
   "rows": [
     {
       "metadata": {
         "id": 888999000,
         "text": "productivity app",
         "matchType": "BROAD",
         "adAccountId": 123456789,
         "campaignId": 444555666,
         "adGroupId": 555666777,
         "status": "ENABLED",
         "deleted": false
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "75.00",
           "currency": "USD"
         },
         "impressions": 5000,
         "taps": 250,
         "ttr": 0.05,
         "cpt": {
           "amount": "0.30",
           "currency": "USD"
         },
         "tapInstalls": 60,
         "totalInstalls": 72
       },
       "granularMetrics": [
         {
           "date": "2025-01-01",
           "localSpend": {
             "amount": "2.40",
             "currency": "USD"
           },
           "impressions": 160,
           "taps": 8,
           "tapInstalls": 2
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "75.00",
         "currency": "USD"
       },
       "impressions": 5000,
       "taps": 250,
       "tapInstalls": 60
     }
   }
 },
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Grouped by Country**:

Retrieve keyword metrics grouped by country to see which App Store countries or regions are driving installs for each keyword.

##### Request

Filters by `campaignId`, narrowed to a specific ad group with `adGroupId`, and groups results by `countryOrRegion`, returning daily keyword metrics split by App Store country or region for January 2025.

```json
POST /v1/reports/apps/keywords/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 20
 },
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": "444555666"
   },
   {
     "field": "adGroupId",
     "operator": "EQUALS",
     "value": "555666777"
   }
 ],
 "groupBy": [
   "countryOrRegion"
 ],
 "timeRange": {
   "start": "2025-01-01",
   "end": "2025-01-31",
   "timeZone": "ORTZ",
   "granularity": "DAILY"
 }
}
```

##### Response

```json
{
 "result": {
   "rows": [
     {
       "metadata": {
         "id": 888999001,
         "text": "task manager",
         "matchType": "EXACT",
         "adAccountId": 123456789,
         "campaignId": 444555666,
         "adGroupId": 555666777,
         "status": "ENABLED",
         "deleted": false
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "48.00",
           "currency": "USD"
         },
         "impressions": 3200,
         "taps": 160,
         "ttr": 0.05,
         "tapInstalls": 38
       },
       "granularMetrics": [
         {
           "date": "2025-01-01",
           "countryOrRegion": "US",
           "localSpend": {
             "amount": "1.80",
             "currency": "USD"
           },
           "impressions": 120,
           "taps": 6,
           "tapInstalls": 1
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "48.00",
         "currency": "USD"
       },
       "impressions": 3200,
       "taps": 160,
       "tapInstalls": 38
     }
   }
 },
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/reports/apps/keywords/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Campaigns Report](get-app-campaign-reports.md)
  Retrieve performance metrics for campaigns.
- [Ad Groups Report](get-app-ad-group-reports.md)
  Retrieve performance metrics for ad groups.
- [Ads Report](get-app-ad-reports.md)
  Retrieve performance metrics for ads.
- [Search Terms Report](get-app-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-keyword-reports)*