# Ads Report

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for ads broken down by optional dimensions such as device class or country.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Ad reports return one row per ad. Each row contains a `metadata` object with ad identifiers (including `campaignId` and `adGroupId`), `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`.

Filter by `adGroupId` or `campaignId` in the `filters` array to scope results to a specific ad group or campaign.

#### Request Body

See [`AppsReportingRequest`](appsreportingrequest.md).

##### Groupby Dimensions

`storefront`, `countryOrRegion`

The following dimensions are **not** supported for the `AD` entity: `deviceClass`, `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`.

Ad reports follow the standard date range rules per granularity, except `HOURLY` isn’t available at the ad level.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | **Not supported** for the `AD` entity. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

Only `DAILY` granularity or coarser is available for ads, and either `ORTZ` or `UTC` timezones are accepted.

| Constraint | Detail |
| --- | --- |
| HOURLY granularity | Not available for ads. Use `DAILY` as the finest granularity. |
| Timezone | Use `ORTZ` (reporting timezone) or `UTC`. |

#### Payload Examples

**Daily by Device**:

Retrieve daily ad metrics for a specific ad group, grouped by device class.

##### Request

Filters by `adGroupId` and groups results by `deviceClass`, returning daily ad-level metrics for a 31-day window in the account’s reporting timezone.

```json
POST /v1/reports/apps/ads/query

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
   "deviceClass"
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
         "id": 234567891,
         "name": "AwayFinder Default Ad",
         "adAccountId": 123456789,
         "campaignId": 444555666,
         "adGroupId": 555666777,
         "status": "ENABLED",
         "deleted": false
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "150.00",
           "currency": "USD"
         },
         "impressions": 10000,
         "taps": 500,
         "ttr": 0.05,
         "cpt": {
           "amount": "0.30",
           "currency": "USD"
         },
         "tapInstalls": 120,
         "totalInstalls": 145
       },
       "granularMetrics": [
         {
           "date": "2025-01-01",
           "deviceClass": "IPHONE",
           "localSpend": {
             "amount": "4.80",
             "currency": "USD"
           },
           "impressions": 330,
           "taps": 16,
           "tapInstalls": 4
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "150.00",
         "currency": "USD"
       },
       "impressions": 10000,
       "taps": 500,
       "tapInstalls": 120
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

**No groupBy**:

Retrieve daily ad metrics without dimensional grouping. The `granularMetrics` array returns one entry per day with aggregate figures across all devices and countries.

##### Request

Filters by `campaignId` with no `groupBy` dimension, returning daily ad metrics aggregated across all devices and countries for a 7-day window.

```json
POST /v1/reports/apps/ads/query

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
 "timeRange": {
   "start": "2025-01-01",
   "end": "2025-01-07",
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
         "id": 234567891,
         "name": "AwayFinder Default Ad",
         "adAccountId": 123456789,
         "campaignId": 444555666,
         "adGroupId": 555666777,
         "status": "ENABLED",
         "deleted": false
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "35.00",
           "currency": "USD"
         },
         "impressions": 2300,
         "taps": 115,
         "ttr": 0.05,
         "tapInstalls": 28
       },
       "granularMetrics": [
         {
           "date": "2025-01-01",
           "localSpend": {
             "amount": "5.20",
             "currency": "USD"
           },
           "impressions": 340,
           "taps": 17,
           "tapInstalls": 4
         },
         {
           "date": "2025-01-02",
           "localSpend": {
             "amount": "4.80",
             "currency": "USD"
           },
           "impressions": 310,
           "taps": 15,
           "tapInstalls": 3
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "35.00",
         "currency": "USD"
       },
       "impressions": 2300,
       "taps": 115,
       "tapInstalls": 28
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

`POST https://api.ads.apple.com/v1/reports/apps/ads/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Campaigns Report](get-app-campaign-reports.md)
  Retrieve performance metrics for campaigns broken down by optional dimensions such as country, device class, or storefront.
- [Ad Groups Report](get-app-ad-group-reports.md)
  Retrieve performance metrics for ad groups broken down by optional dimensions such as country, device class, or storefront.
- [Keywords Report](get-app-keyword-reports.md)
  Retrieve performance metrics for keywords broken down by optional dimensions such as device class or country.
- [Search Terms Report](get-app-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches, broken down by optional dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-ad-reports)*