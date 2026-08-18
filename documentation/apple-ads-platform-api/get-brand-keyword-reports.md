# Keywords Report (Brands)

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for Apple Maps keywords broken down by optional dimensions such as device class or country.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Apple Maps keyword performance reports return one row per keyword. Each row contains a `metadata` object with keyword identifiers (including `campaignId`, `adGroupId`, `text`, and `matchType`), `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`.

Use `filters` to scope results to specific campaigns or ad groups. For Apple Maps campaigns, keywords represent search queries that trigger ad delivery on Apple Maps.

#### Request Body

See [`BrandsReportingRequest`](brandsreportingrequest.md).

##### Groupby Dimensions

Apple Maps keyword reports support a reduced set of `groupBy` dimensions. Neither `supplyPlacement` nor `locationId` is available at the keyword entity level.

| Dimension | Description |
| --- | --- |
| `deviceClass` | Break down metrics by device type (`IPHONE`, `IPAD`). |

`supplyPlacement` and `locationId` are **not** supported for the `KEYWORD` entity under `business-brands`.

Granularity constraints mirror other Apple Maps entities, with lookback windows ranging from 7 days for `HOURLY` to 90 days for `MONTHLY`.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | Date range start must be within the last 7 days. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

Keyword reports also exclude `EMPTY_METRICS` and the `supplyPlacement`/`locationId` dimensions, and should always be filtered by `adGroupId` or `campaignId`.

| Constraint | Detail |
| --- | --- |
| `EMPTY_METRICS` | Not supported for `business-brands`. |
| `supplyPlacement` groupBy | Not supported at the keyword level. |
| `locationId` groupBy | Not supported at the keyword level. |
| Filter scope | Always filter by `adGroupId` or `campaignId` to avoid retrieving all keywords across the account. |

#### Payload Examples

Retrieve daily keyword metrics for all keywords in an Apple Maps ad group.

##### Request

Filters by `adGroupId` for an Apple Maps ad group with no `groupBy` dimension, returning daily keyword metrics aggregated across all devices and locations for March 2025.

```json
POST /v1/reports/business-brands/keywords/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 20
 },
 "filters": [
   {
     "field": "adGroupId",
     "operator": "EQUALS",
     "value": "555666888"
   }
 ],
 "timeRange": {
   "start": "2025-03-01",
   "end": "2025-03-31",
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
         "id": 888999100,
         "text": "coffee near me",
         "matchType": "PHRASE",
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "adGroupId": 555666888,
         "status": "ENABLED",
         "deleted": false
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "4200.00",
           "currency": "USD"
         },
         "impressions": 420000,
         "taps": 8400,
         "ttr": 0.02,
         "cpt": {
           "amount": "0.50",
           "currency": "USD"
         },
         "firstActions": {
           "tap": 170
         },
         "actions": {
           "tap": 170
         },
         "getDirections": {
           "tap": 1260
         },
         "tapURL": {
           "tap": 420
         },
         "call": {
           "tap": 210
         },
         "share": {
           "tap": 210
         },
         "getTheApp": {
           "tap": 170
         },
         "galleryEngagement": {
           "tap": 170
         }
       },
       "granularMetrics": [
         {
           "date": "2025-03-01",
           "localSpend": {
             "amount": "20.00",
             "currency": "USD"
           },
           "impressions": 2000,
           "taps": 40,
           "actions": {
             "tap": 10
           },
           "getDirections": {
             "tap": 6
           }
         }
       ]
     },
     {
       "metadata": {
         "id": 888999101,
         "text": "best cafe downtown",
         "matchType": "CATEGORY",
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "adGroupId": 555666888,
         "status": "ENABLED",
         "deleted": false
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "4200.00",
           "currency": "USD"
         },
         "impressions": 420000,
         "taps": 8400,
         "ttr": 0.02,
         "cpt": {
           "amount": "0.50",
           "currency": "USD"
         },
         "firstActions": {
           "tap": 170
         },
         "actions": {
           "tap": 170
         },
         "getDirections": {
           "tap": 1260
         },
         "tapURL": {
           "tap": 420
         },
         "call": {
           "tap": 210
         },
         "share": {
           "tap": 210
         },
         "getTheApp": {
           "tap": 170
         },
         "galleryEngagement": {
           "tap": 170
         }
       },
       "granularMetrics": [
         {
           "date": "2025-03-01",
           "localSpend": {
             "amount": "10.00",
             "currency": "USD"
           },
           "impressions": 1000,
           "taps": 20,
           "actions": {
             "tap": 5
           },
           "getDirections": {
             "tap": 3
           }
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "8400.00",
         "currency": "USD"
       },
       "impressions": 840000,
       "taps": 16800,
       "actions": {
         "tap": 340
       }
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

## Endpoint

`POST https://api.ads.apple.com/v1/reports/business-brands/keywords/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Campaigns Report (Brands)](get-brand-campaign-reports.md)
  Retrieve performance metrics for Apple Maps campaigns broken down by optional dimensions such as country, device class, or storefront.
- [Ad Groups Report (Brands)](get-brand-ad-group-reports.md)
  Retrieve performance metrics for Apple Maps ad groups broken down by optional dimensions such as country, device class, or storefront.
- [Ads Report (Brands)](get-brand-ad-reports.md)
  Retrieve performance metrics for Apple Maps ads broken down by optional dimensions such as device class or country.
- [Search Terms Report (Brands)](get-brand-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches in Apple Maps campaigns, broken down by optional dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-brand-keyword-reports)*