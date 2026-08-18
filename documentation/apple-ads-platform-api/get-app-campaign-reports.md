# Campaigns Report

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for campaigns broken down by optional dimensions such as country, device class, or storefront.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Campaign reports return one row per campaign. Each row contains a `metadata` object with campaign identifiers, `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`.

Use `filters` to scope the report to specific campaigns by `campaignId`. Use `groupBy` to split metrics along a dimension: each dimension value produces its own row within the campaign’s result.

#### Request Body

See [`AppsReportingRequest`](appsreportingrequest.md).

##### Groupby Dimensions

`deviceClass`, `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`, `storefront`, `countryOrRegion`

Granularity constraints follow the usual date range rules, from a 7-day lookback for `HOURLY` to a 90-day-old end date for `MONTHLY`.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | Date range start must be within the last 7 days. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

Selecting a timezone of `ORTZ` or `UTC` and using the `fields` array to request specific metrics keeps campaign report responses focused.

| Constraint | Detail |
| --- | --- |
| Timezone | Use `ORTZ` (reporting timezone) or `UTC`. |
| Fields selection | Use the `fields` array to request only specific metric columns. |

#### Payload Examples

Retrieve daily campaign metrics for a specific app campaign, grouped by country. The `granularMetrics` array returns one entry per day per country combination.

##### Request

Filters by a single `campaignId` and groups results by `countryOrRegion`, using daily granularity over a 31-day window in the account’s reporting timezone.

```json
POST /v1/reports/apps/campaigns/query

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
         "id": 444555666,
         "name": "AwayFinder — US Launch",
         "adAccountId": 123456789,
         "promotedObjectType": "APPSTORE_APP",
         "promotedObjectId": "987654321",
         "promotedObject": {
           "name": "AwayFinder"
         },
         "bidStrategy": {
           "bidStrategyType": "MANUAL_CPT"
         },
         "status": "ENABLED",
         "deleted": false
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "500.00",
           "currency": "USD"
         },
         "impressions": 50000,
         "taps": 2500,
         "ttr": 0.05,
         "cpt": {
           "amount": "0.20",
           "currency": "USD"
         },
         "tapInstalls": 600,
         "totalInstalls": 720,
         "tapNewDownloads": 540,
         "tapRedownloads": 60
       },
       "granularMetrics": [
         {
           "date": "2025-01-01",
           "countryOrRegion": "US",
           "localSpend": {
             "amount": "18.40",
             "currency": "USD"
           },
           "impressions": 1850,
           "taps": 92,
           "ttr": 0.05,
           "tapInstalls": 22
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "500.00",
         "currency": "USD"
       },
       "impressions": 50000,
       "taps": 2500,
       "tapInstalls": 600
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

`POST https://api.ads.apple.com/v1/reports/apps/campaigns/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Ad Groups Report](get-app-ad-group-reports.md)
  Retrieve performance metrics for ad groups broken down by optional dimensions such as country, device class, or storefront.
- [Ads Report](get-app-ad-reports.md)
  Retrieve performance metrics for ads broken down by optional dimensions such as device class or country.
- [Keywords Report](get-app-keyword-reports.md)
  Retrieve performance metrics for keywords broken down by optional dimensions such as device class or country.
- [Search Terms Report](get-app-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches, broken down by optional dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-campaign-reports)*