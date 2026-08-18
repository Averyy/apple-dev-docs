# Search Terms Report

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for the actual search terms that triggered keyword matches, broken down by optional dimensions.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Search term reports show the actual user-entered queries that matched a keyword and generated an impression. Each row contains the `searchTermText` field and the associated `keyword` object, allowing you to map observed search behavior back to specific bid keywords.

Use search term data to:

- Discover high-performing search terms to promote to dedicated exact-match keywords.
- Identify irrelevant queries to exclude as negative keywords with [`Create a Negative Keyword`](post-negative-keywords.md).
- Understand match expansion breadth for BROAD-match keywords.

Filter by `adGroupId` or `campaignId` in the `filters` array to scope results.

#### Request Body

See [`AppsReportingRequest`](appsreportingrequest.md).

##### Groupby Dimensions

`deviceClass`, `storefront`, `countryOrRegion`

The following dimensions are **not** supported for the `SEARCHTERM` entity: `ageRange`, `gender`, `countryCode`, `adminArea`, `locality`.

Search term reports follow the usual granularity rules, except `HOURLY` isn’t available for this entity.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | **Not supported** for the `SEARCHTERM` entity. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

Search term reporting has several additional restrictions, including a required `ORTZ` timezone and privacy-based suppression of low-volume terms.

| Constraint | Detail |
| --- | --- |
| `EMPTY_METRICS` option | Not supported for `SEARCHTERM`. |
| Timezone | Only `ORTZ` is supported. `UTC` is excluded for search term reporting. |
| HOURLY granularity | Not available for search terms. |
| Privacy threshold | Low-volume search terms may be suppressed or aggregated to protect user privacy. |

#### Payload Examples

**Search Terms for Ad Group**:

Retrieve daily search term metrics for all keywords in a specific ad group. Results show the exact user queries that triggered impressions.

##### Request

Filters by `adGroupId` with no `groupBy` dimension, returning daily search term metrics for all matched queries in January 2025 using the account’s reporting timezone.

```json
POST /v1/reports/apps/searchterms/query

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
         "searchTermText": "best productivity app 2025",
         "keyword": {
           "id": 888999000,
           "text": "productivity app",
           "matchType": "BROAD"
         },
         "adAccountId": 123456789,
         "campaignId": 444555666,
         "adGroupId": 555666777
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "45.00",
           "currency": "USD"
         },
         "impressions": 3000,
         "taps": 150,
         "ttr": 0.05,
         "cpt": {
           "amount": "0.30",
           "currency": "USD"
         },
         "tapInstalls": 35,
         "totalInstalls": 42
       },
       "granularMetrics": [
         {
           "date": "2025-01-01",
           "localSpend": {
             "amount": "1.50",
             "currency": "USD"
           },
           "impressions": 100,
           "taps": 5,
           "tapInstalls": 1
         }
       ]
     },
     {
       "metadata": {
         "searchTermText": "task management tools",
         "keyword": {
           "id": 888999001,
           "text": "task manager",
           "matchType": "BROAD"
         },
         "adAccountId": 123456789,
         "campaignId": 444555666,
         "adGroupId": 555666777
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "28.50",
           "currency": "USD"
         },
         "impressions": 1900,
         "taps": 95,
         "ttr": 0.05,
         "tapInstalls": 22
       },
       "granularMetrics": [
         {
           "date": "2025-01-01",
           "localSpend": {
             "amount": "0.90",
             "currency": "USD"
           },
           "impressions": 60,
           "taps": 3,
           "tapInstalls": 1
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "73.50",
         "currency": "USD"
       },
       "impressions": 4900,
       "taps": 245,
       "tapInstalls": 57
     }
   }
 },
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Weekly**:

Retrieve weekly search term metrics for a campaign. Weekly granularity requires the end date to be at least 14 days in the past.

##### Request

Filters by `campaignId` with no `groupBy` dimension and uses weekly granularity over a 2-month window. The end date is more than 14 days in the past as required by weekly reporting.

```json
POST /v1/reports/apps/searchterms/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 50
 },
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": "444555666"
   }
 ],
 "timeRange": {
   "start": "2024-10-01",
   "end": "2024-12-01",
   "timeZone": "ORTZ",
   "granularity": "WEEKLY"
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
         "searchTermText": "organize tasks",
         "keyword": {
           "id": 888999002,
           "text": "task organizer",
           "matchType": "BROAD"
         },
         "adAccountId": 123456789,
         "campaignId": 444555666,
         "adGroupId": 555666777
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "120.00",
           "currency": "USD"
         },
         "impressions": 8000,
         "taps": 400,
         "tapInstalls": 96
       },
       "granularMetrics": [
         {
           "date": "2024-10-07",
           "localSpend": {
             "amount": "18.00",
             "currency": "USD"
           },
           "impressions": 1200,
           "taps": 60,
           "tapInstalls": 14
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "120.00",
         "currency": "USD"
       },
       "impressions": 8000,
       "taps": 400,
       "tapInstalls": 96
     }
   }
 },
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 50
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/reports/apps/searchterms/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Campaigns Report](get-app-campaign-reports.md)
  Retrieve performance metrics for campaigns broken down by optional dimensions such as country, device class, or storefront.
- [Ad Groups Report](get-app-ad-group-reports.md)
  Retrieve performance metrics for ad groups broken down by optional dimensions such as country, device class, or storefront.
- [Ads Report](get-app-ad-reports.md)
  Retrieve performance metrics for ads broken down by optional dimensions such as device class or country.
- [Keywords Report](get-app-keyword-reports.md)
  Retrieve performance metrics for keywords broken down by optional dimensions such as device class or country.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-search-term-reports)*