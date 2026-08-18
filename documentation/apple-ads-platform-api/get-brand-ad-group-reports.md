# Ad Groups Report (Brands)

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for Apple Maps ad groups broken down by optional dimensions such as country, device class, or storefront.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Brand ad group reports return one row per ad group. Each row contains a `metadata` object with ad group identifiers (including `campaignId`), `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`.

Filter by `campaignId` or `adGroupId` in the `filters` array to scope results. Use `groupBy` to split metrics along a dimension: each dimension value produces its own row within the ad group’s result.

#### Request Body

See [`BrandsReportingRequest`](brandsreportingrequest.md).

The `groupBy` array supports three dimensions for ad groups: device class, business location, and ad placement.

| Dimension | Description |
| --- | --- |
| `deviceClass` | Break down metrics by device type (`IPHONE`, `IPAD`). |
| `locationId` | Break down metrics per business location. |
| `supplyPlacement` | Break down metrics by ad placement. |

Each granularity value comes with its own date range restrictions, from a 7-day lookback for `HOURLY` to a 90-day-old end date for `MONTHLY`.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | Date range start must be within the last 7 days. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

Beyond granularity, note that `EMPTY_METRICS` isn’t supported for `business-brands`, filtering by `campaignId` keeps responses manageable, and only `ORTZ` or `UTC` timezones are accepted.

| Constraint | Detail |
| --- | --- |
| `EMPTY_METRICS` | Not supported for `business-brands`. |
| Filter scope | Always filter by `campaignId` to reduce response size. |
| Timezone | Use `ORTZ` (reporting timezone) or `UTC`. |

#### Payload Examples

**Brands, By Location**:

Retrieve daily ad group metrics for all ad groups in a campaign, grouped by location ID.

##### Request

Filters by `campaignId` to retrieve all brand ad groups in a campaign, groups by `locationId`, and uses daily granularity over a 31-day window in the account’s reporting timezone.

```json
POST /v1/reports/business-brands/adgroups/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 20
 },
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": "444555999"
   }
 ],
 "groupBy": [
   "locationId"
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
         "id": 555666888,
         "name": "AwayFinder — SF Metro Locations",
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "status": "ENABLED",
         "deleted": false,
         "locationId": "loc-002"
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
             "amount": "24.00",
             "currency": "USD"
           },
           "impressions": 2400,
           "taps": 48,
           "actions": {
             "tap": 12
           },
           "getDirections": {
             "tap": 7
           }
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "4200.00",
         "currency": "USD"
       },
       "impressions": 420000,
       "taps": 8400
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

**Brands, By Device**:

Retrieve monthly ad group metrics grouped by device class to understand performance differences between iPhone and iPad users.

##### Request

Filters by `adGroupId` for a specific brand ad group, groups by `deviceClass`, and uses monthly granularity over a 3-month date range in UTC.

```json
POST /v1/reports/business-brands/adgroups/query

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
 "groupBy": [
   "deviceClass"
 ],
 "timeRange": {
   "start": "2024-10-01",
   "end": "2024-12-31",
   "timeZone": "UTC",
   "granularity": "MONTHLY"
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
         "id": 555666888,
         "name": "AwayFinder — SF Metro Locations",
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "status": "ENABLED",
         "deleted": false,
         "deviceClass": "IPHONE"
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "1680.00",
           "currency": "USD"
         },
         "impressions": 168000,
         "taps": 3360,
         "ttr": 0.02,
         "cpt": {
           "amount": "0.50",
           "currency": "USD"
         },
         "firstActions": {
           "tap": 68
         },
         "actions": {
           "tap": 68
         },
         "getDirections": {
           "tap": 504
         },
         "tapURL": {
           "tap": 168
         },
         "call": {
           "tap": 84
         },
         "share": {
           "tap": 84
         },
         "getTheApp": {
           "tap": 68
         },
         "galleryEngagement": {
           "tap": 68
         }
       },
       "granularMetrics": [
         {
           "date": "2024-10-01",
           "localSpend": {
             "amount": "1680.00",
             "currency": "USD"
           },
           "impressions": 168000,
           "taps": 3360,
           "actions": {
             "tap": 840
           },
           "getDirections": {
             "tap": 504
           }
         }
       ]
     },
     {
       "metadata": {
         "id": 555666888,
         "name": "AwayFinder — SF Metro Locations",
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "status": "ENABLED",
         "deleted": false,
         "deviceClass": "IPAD"
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "120.00",
           "currency": "USD"
         },
         "impressions": 12000,
         "taps": 240,
         "ttr": 0.02,
         "cpt": {
           "amount": "0.50",
           "currency": "USD"
         },
         "firstActions": {
           "tap": 5
         },
         "actions": {
           "tap": 5
         },
         "getDirections": {
           "tap": 36
         },
         "tapURL": {
           "tap": 12
         },
         "call": {
           "tap": 6
         },
         "share": {
           "tap": 6
         },
         "getTheApp": {
           "tap": 5
         },
         "galleryEngagement": {
           "tap": 5
         }
       },
       "granularMetrics": [
         {
           "date": "2024-10-01",
           "localSpend": {
             "amount": "120.00",
             "currency": "USD"
           },
           "impressions": 12000,
           "taps": 240,
           "actions": {
             "tap": 60
           },
           "getDirections": {
             "tap": 36
           }
         }
       ]
     }
   ],
   "summary": {
     "grandTotal": {
       "localSpend": {
         "amount": "1800.00",
         "currency": "USD"
       },
       "impressions": 180000,
       "taps": 3600
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

`POST https://api.ads.apple.com/v1/reports/business-brands/adgroups/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Campaigns Report (Brands)](get-brand-campaign-reports.md)
  Retrieve performance metrics for Apple Maps campaigns broken down by optional dimensions such as country, device class, or storefront.
- [Ads Report (Brands)](get-brand-ad-reports.md)
  Retrieve performance metrics for Apple Maps ads broken down by optional dimensions such as device class or country.
- [Keywords Report (Brands)](get-brand-keyword-reports.md)
  Retrieve performance metrics for Apple Maps keywords broken down by optional dimensions such as device class or country.
- [Search Terms Report (Brands)](get-brand-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches in Apple Maps campaigns, broken down by optional dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-brand-ad-group-reports)*