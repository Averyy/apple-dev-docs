# Campaigns Report (Brands)

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for Apple Maps campaigns broken down by optional dimensions such as country, device class, or storefront.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

These reports return one row per campaign. Each row contains a `metadata` object with campaign identifiers, `totalMetrics` aggregated over the full date range, and a `granularMetrics` array broken down by the selected `granularity`.

Use `filters` to scope results to specific campaigns by `campaignId`. Use `groupBy` to split metrics along a dimension: each dimension value produces its own row within the campaign’s result.

#### Request Body

See [`BrandsReportingRequest`](brandsreportingrequest.md).

Brand campaign reports can be grouped by device type, business location, or ad placement.

| Dimension | Description |
| --- | --- |
| `deviceClass` | Break down metrics by device type (`IPHONE`, `IPAD`). |
| `locationId` | Break down metrics per business location. |
| `supplyPlacement` | Break down metrics by ad placement. |

The following metrics are available for brand campaign reports, covering spend, engagement, and the individual Apple Maps action types.

| Metric | Description |
| --- | --- |
| `localSpend` | Total spend in the account currency. |
| `impressions` | Total number of ad impressions. |
| `taps` | Total number of taps on the ad. |
| `ttr` | Tap-through rate (`taps / impressions`). |
| `cpt` | Average cost per tap. |
| `cpm` | Cost per thousand impressions. |
| `firstActions` | First-time engagement actions taken after an ad tap. |
| `firstActionsPerTap` | First actions divided by taps. |
| `firstActionsPerImpression` | First actions divided by impressions. |
| `costPerFirstAction` | Spend divided by first actions. |
| `actions` | Total actions (directions, calls, URL taps, shares, etc.). |
| `costPerAction` | Spend divided by actions. |
| `getDirections` | Count of Get Directions taps. |
| `tapURL` | Count of URL taps. |
| `call` | Count of Call actions. |
| `share` | Count of Share actions. |
| `getTheApp` | Count of Get the App taps. |
| `galleryEngagement` | Count of gallery photo engagements. |
| `actionsPerTap` | Actions divided by taps. |
| `actionsPerImpression` | Actions divided by impressions. |

Granularity constraints follow the usual date range rules, from a 7-day lookback for `HOURLY` to a 90-day-old end date for `MONTHLY`.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | Date range start must be within the last 7 days. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

`EMPTY_METRICS` isn’t supported for `business-brands`, and only `ORTZ` or `UTC` timezones are accepted.

| Constraint | Detail |
| --- | --- |
| `EMPTY_METRICS` | Not supported for `business-brands`. |
| Timezone | Use `ORTZ` (reporting timezone) or `UTC`. |

#### Payload Examples

**Brands, Daily by Location**:

Retrieve daily campaign metrics grouped by location ID. Each entry in `granularMetrics` represents one day for one business location.

##### Request

Filters by `campaignId` for an Apple Maps campaign, groups by `locationId`, and uses daily granularity over a 31-day window in the account’s reporting timezone.

```json
POST /v1/reports/business-brands/campaigns/query

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
         "id": 444555999,
         "name": "AwayFinder - Brand Q1",
         "adAccountId": 123456789,
         "promotedObjectType": "BUSINESS_BRAND",
         "promotedObjectId": "9151314442816847872",
         "promotedObject": {
           "name": "AwayFinder"
         },
         "bidStrategy": {
           "bidStrategyType": "MAX_ENGAGEMENTS"
         },
         "status": "ENABLED",
         "deleted": false,
         "locationId": "loc-001"
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
             "amount": "42.00",
             "currency": "USD"
           },
           "impressions": 4200,
           "taps": 84,
           "actions": {
             "tap": 21
           },
           "getDirections": {
             "tap": 13
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

**Brands, Monthly by Placement**:

Retrieve monthly campaign metrics grouped by supply placement to compare performance across Apple Maps and other ad placements.

##### Request

Filters by `campaignId` for an Apple Maps campaign, groups by `supplyPlacement`, and uses monthly granularity over a 3-month date range in UTC.

```json
POST /v1/reports/business-brands/campaigns/query

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
   "supplyPlacement"
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
         "id": 444555999,
         "name": "AwayFinder - Brand Q4",
         "adAccountId": 123456789,
         "promotedObjectType": "BUSINESS_BRAND",
         "promotedObjectId": "9151314442816847872",
         "promotedObject": {
           "name": "AwayFinder"
         },
         "bidStrategy": {
           "bidStrategyType": "MAX_ENGAGEMENTS"
         },
         "status": "ENABLED",
         "deleted": false,
         "supplyPlacement": "MAPS_SEARCH_RESULTS"
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "3300.00",
           "currency": "USD"
         },
         "impressions": 330000,
         "taps": 6600,
         "ttr": 0.02,
         "cpt": {
           "amount": "0.50",
           "currency": "USD"
         },
         "firstActions": {
           "tap": 130
         },
         "actions": {
           "tap": 130
         },
         "getDirections": {
           "tap": 990
         },
         "tapURL": {
           "tap": 330
         },
         "call": {
           "tap": 165
         },
         "share": {
           "tap": 165
         },
         "getTheApp": {
           "tap": 130
         },
         "galleryEngagement": {
           "tap": 130
         }
       },
       "granularMetrics": [
         {
           "date": "2024-10-01",
           "localSpend": {
             "amount": "3300.00",
             "currency": "USD"
           },
           "impressions": 330000,
           "taps": 6600,
           "actions": {
             "tap": 1650
           },
           "getDirections": {
             "tap": 990
           }
         }
       ]
     },
     {
       "metadata": {
         "id": 444555999,
         "name": "AwayFinder - Brand Q4",
         "adAccountId": 123456789,
         "promotedObjectType": "BUSINESS_BRAND",
         "promotedObjectId": "9151314442816847872",
         "promotedObject": {
           "name": "AwayFinder"
         },
         "bidStrategy": {
           "bidStrategyType": "MAX_ENGAGEMENTS"
         },
         "status": "ENABLED",
         "deleted": false,
         "supplyPlacement": "MAPS_SEARCH_HOME"
       },
       "totalMetrics": {
         "localSpend": {
           "amount": "900.00",
           "currency": "USD"
         },
         "impressions": 90000,
         "taps": 1800,
         "ttr": 0.02,
         "cpt": {
           "amount": "0.50",
           "currency": "USD"
         },
         "firstActions": {
           "tap": 36
         },
         "actions": {
           "tap": 36
         },
         "getDirections": {
           "tap": 270
         },
         "tapURL": {
           "tap": 90
         },
         "call": {
           "tap": 45
         },
         "share": {
           "tap": 45
         },
         "getTheApp": {
           "tap": 36
         },
         "galleryEngagement": {
           "tap": 36
         }
       },
       "granularMetrics": [
         {
           "date": "2024-10-01",
           "localSpend": {
             "amount": "900.00",
             "currency": "USD"
           },
           "impressions": 90000,
           "taps": 1800,
           "actions": {
             "tap": 450
           },
           "getDirections": {
             "tap": 270
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

## Endpoint

`POST https://api.ads.apple.com/v1/reports/business-brands/campaigns/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Ad Groups Report (Brands)](get-brand-ad-group-reports.md)
  Retrieve performance metrics for Apple Maps ad groups broken down by optional dimensions such as country, device class, or storefront.
- [Ads Report (Brands)](get-brand-ad-reports.md)
  Retrieve performance metrics for Apple Maps ads broken down by optional dimensions such as device class or country.
- [Keywords Report (Brands)](get-brand-keyword-reports.md)
  Retrieve performance metrics for Apple Maps keywords broken down by optional dimensions such as device class or country.
- [Search Terms Report (Brands)](get-brand-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches in Apple Maps campaigns, broken down by optional dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-brand-campaign-reports)*