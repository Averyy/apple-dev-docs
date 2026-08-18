# Keywords Report

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for keywords broken down by optional dimensions such as device class or country.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Keyword performance reports return one row per keyword. Each row contains a `metadata` object with keyword identifiers (including `campaignId`, `adGroupId`, `text`, and `matchType`), `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`. Rows may also include an optional `insights` object whose `bidRecommendation` field surfaces a recommended bid for the keyword.

Filter by `adGroupId` or `campaignId` in the `filters` array to scope results. Use `groupBy` to split metrics along a dimension.

#### Request Body

See [`AppsReportingRequest`](appsreportingrequest.md).

##### Groupby Dimensions

`deviceClass`, `storefront`, `countryOrRegion`

The following dimensions are **not** supported for the `KEYWORD` entity: `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`.

Granularity constraints follow the usual date range rules, from a 7-day lookback for `HOURLY` to a 90-day-old end date for `MONTHLY`.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | Date range start must be within the last 7 days. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

Always filter keyword reports by `adGroupId` or `campaignId` to avoid retrieving every keyword in the account.

| Constraint | Detail |
| --- | --- |
| Filter scope | Always filter by `adGroupId` or `campaignId` to avoid retrieving all keywords across the account. |

#### Payload Examples

**By Ad Group**:

Retrieve daily keyword metrics for all keywords in a specific ad group.

##### Request

Filters by `adGroupId` with no `groupBy` dimension, returning daily keyword metrics aggregated across all devices and countries for January 2025.

```json
POST /v1/reports/apps/keywords/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 20
 },
 "filters": [
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

Filters by `adGroupId` and groups results by `countryOrRegion`, returning daily keyword metrics split by App Store country or region for January 2025.

```json
POST /v1/reports/apps/keywords/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 20
 },
 "filters": [
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
  Retrieve performance metrics for campaigns broken down by optional dimensions such as country, device class, or storefront.
- [Ad Groups Report](get-app-ad-group-reports.md)
  Retrieve performance metrics for ad groups broken down by optional dimensions such as country, device class, or storefront.
- [Ads Report](get-app-ad-reports.md)
  Retrieve performance metrics for ads broken down by optional dimensions such as device class or country.
- [Search Terms Report](get-app-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches, broken down by optional dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-keyword-reports)*