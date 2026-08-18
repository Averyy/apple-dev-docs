# Ads Report (Brands)

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for Apple Maps ads broken down by optional dimensions such as device class or country.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Brand ad reports return one row per ad. Each row contains a `metadata` object with ad identifiers (including `campaignId` and `adGroupId`), `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`.

For Apple Maps ads, the `metadata` object includes a nested `creative` object ([`BrandsReportingCreative`](brandsreportingcreative.md)) with the creative’s `id`, `creativeType`, and `systemStatus`. There is no flat `creativeId` field. Filter by `adGroupId` or `campaignId` in the `filters` array to scope results.

#### Request Body

See [`BrandsReportingRequest`](brandsreportingrequest.md).

Brand ad reports can be grouped by device type, business location, or ad placement.

| Dimension | Description |
| --- | --- |
| `deviceClass` | Break down metrics by device type (`IPHONE`, `IPAD`). |
| `locationId` | Break down metrics per business location. |
| `supplyPlacement` | Break down metrics by ad placement. |

Ad reports follow the standard date range rules per granularity, except `HOURLY` isn’t available at the ad level.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | **Not supported** for the `AD` entity. Use `DAILY` as the finest granularity. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

`EMPTY_METRICS` isn’t supported for `business-brands` ads, `HOURLY` granularity isn’t available, and only `ORTZ` or `UTC` timezones are accepted.

| Constraint | Detail |
| --- | --- |
| `EMPTY_METRICS` | Not supported for `business-brands`. |
| `HOURLY` granularity | Not available for ads. Use `DAILY` as the finest granularity. |
| Timezone | Use `ORTZ` (reporting timezone) or `UTC`. |

#### Payload Examples

**Brands, Daily by Placement**:

Retrieve daily ad metrics for a specific ad group, grouped by supply placement.

##### Request

Filters by `adGroupId` for an Apple Maps ad group, groups by `supplyPlacement`, and uses daily granularity over a 31-day window in the account’s reporting timezone.

```json
POST /v1/reports/business-brands/ads/query

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
   "supplyPlacement"
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
         "id": 234567900,
         "name": "AwayFinder Apple Maps Ad",
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "adGroupId": 555666888,
         "creative": {
           "id": 666777888,
           "creativeType": "LOCAL_ADS_SEARCH_CREATIVE",
           "systemStatus": "VALID"
         },
         "status": "ENABLED",
         "deleted": false,
         "supplyPlacement": "MAPS_SEARCH_RESULTS"
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
             "amount": "55.00",
             "currency": "USD"
           },
           "impressions": 5500,
           "taps": 110,
           "actions": {
             "tap": 28
           },
           "getDirections": {
             "tap": 17
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

**Brands, No groupBy**:

Retrieve daily ad metrics without dimensional grouping. The `granularMetrics` array returns one entry per day with aggregate figures across all locations and placements.

##### Request

Filters by `campaignId` with no `groupBy` dimension, returning daily Apple Maps ad metrics aggregated across all locations and placements for a 7-day window.

```json
POST /v1/reports/business-brands/ads/query

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
 "timeRange": {
   "start": "2025-03-01",
   "end": "2025-03-07",
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
         "id": 234567900,
         "name": "AwayFinder Apple Maps Ad",
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "adGroupId": 555666888,
         "creative": {
           "id": 666777888,
           "creativeType": "LOCAL_ADS_SEARCH_CREATIVE",
           "systemStatus": "VALID"
         },
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
             "amount": "60.00",
             "currency": "USD"
           },
           "impressions": 6000,
           "taps": 120,
           "actions": {
             "tap": 30
           },
           "getDirections": {
             "tap": 19
           }
         },
         {
           "date": "2025-03-02",
           "localSpend": {
             "amount": "58.00",
             "currency": "USD"
           },
           "impressions": 5800,
           "taps": 116,
           "actions": {
             "tap": 29
           },
           "getDirections": {
             "tap": 18
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
       "taps": 8400,
       "actions": {
         "tap": 170
       }
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

`POST https://api.ads.apple.com/v1/reports/business-brands/ads/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Campaigns Report (Brands)](get-brand-campaign-reports.md)
  Retrieve performance metrics for Apple Maps campaigns broken down by optional dimensions such as country, device class, or storefront.
- [Ad Groups Report (Brands)](get-brand-ad-group-reports.md)
  Retrieve performance metrics for Apple Maps ad groups broken down by optional dimensions such as country, device class, or storefront.
- [Keywords Report (Brands)](get-brand-keyword-reports.md)
  Retrieve performance metrics for Apple Maps keywords broken down by optional dimensions such as device class or country.
- [Search Terms Report (Brands)](get-brand-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches in Apple Maps campaigns, broken down by optional dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-brand-ad-reports)*