# Ad Groups Report

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for ad groups broken down by optional dimensions such as country, device class, or storefront.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Ad group reports return one row per ad group. Each row contains a `metadata` object with ad group identifiers (including `campaignId`), `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`.

Filter by `campaignId` or `adGroupId` in the `filters` array to scope results. Use `groupBy` to split metrics along a dimension: each dimension value produces its own row within the ad group’s result.

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

Filtering by `campaignId`, selecting a timezone of `ORTZ` or `UTC`, and narrowing the `fields` array all help keep ad group report responses manageable.

| Constraint | Detail |
| --- | --- |
| Filter by `campaignId` | Recommended to scope results and reduce response size. |
| Timezone | Use `ORTZ` (reporting timezone) or `UTC`. |
| Fields selection | Use the `fields` array to request only specific metric columns. |

#### Payload Examples

Retrieve daily ad group metrics for all ad groups in a campaign, grouped by device class.

##### Request

Filters by `campaignId` to retrieve all ad groups in a campaign, groups results by `deviceClass`, and uses daily granularity over a 31-day window in the account’s reporting timezone.

```json
POST /v1/reports/apps/adgroups/query

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
         "id": 555666777,
         "name": "AwayFinder iOS — New Users 18-34",
         "adAccountId": 123456789,
         "campaignId": 444555666,
         "status": "ENABLED",
         "pricingModel": "CPT",
         "deleted": false
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "300.00",
           "currency": "USD"
         },
         "impressions": 25000,
         "taps": 1200,
         "ttr": 0.048,
         "cpt": {
           "amount": "0.25",
           "currency": "USD"
         },
         "tapInstalls": 280,
         "totalInstalls": 340
       },
       "granularMetrics": [
         {
           "date": "2025-01-01",
           "deviceClass": "IPHONE",
           "localSpend": {
             "amount": "9.50",
             "currency": "USD"
           },
           "impressions": 820,
           "taps": 39,
           "tapInstalls": 9
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "300.00",
         "currency": "USD"
       },
       "impressions": 25000,
       "taps": 1200,
       "tapInstalls": 280
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

`POST https://api.ads.apple.com/v1/reports/apps/adgroups/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Campaigns Report](get-app-campaign-reports.md)
  Retrieve performance metrics for campaigns broken down by optional dimensions such as country, device class, or storefront.
- [Ads Report](get-app-ad-reports.md)
  Retrieve performance metrics for ads broken down by optional dimensions such as device class or country.
- [Keywords Report](get-app-keyword-reports.md)
  Retrieve performance metrics for keywords broken down by optional dimensions such as device class or country.
- [Search Terms Report](get-app-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches, broken down by optional dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-ad-group-reports)*