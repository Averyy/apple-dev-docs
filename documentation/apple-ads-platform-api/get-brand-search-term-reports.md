# Search Terms Report (Brands)

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve performance metrics for the actual search terms that triggered keyword matches in Apple Maps campaigns, broken down by optional dimensions.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Apple Maps search term reports show the actual user-entered queries that matched a keyword and generated an impression on the Search Results placement. Each row contains the `searchTermText` field and the associated `keyword` object, allowing you to map observed search behavior back to specific bid keywords in your Apple Maps campaign.

Use Apple Maps search term data to:

- Discover high-intent queries (“coffee near me”, “best pizza downtown”) to promote to dedicated exact-match keywords.
- Identify irrelevant or off-brand queries to add as negative keywords.
- Understand match expansion breadth for BROAD-match keywords in Apple Maps campaigns.

Filter by `adGroupId` or `campaignId` to scope results to a specific part of your account.

> **Note**: **Note:** Apple Maps search term reports require the `ORTZ` timezone. `UTC` is not supported. The `supplyPlacement` and `locationId` dimensions are excluded from `groupBy` for the `SEARCHTERM` entity.

#### Request Body

See [`BrandsReportingRequest`](brandsreportingrequest.md).

Search term reports for Apple Maps support only the `deviceClass` groupBy dimension.

| Dimension | Description |
| --- | --- |
| `deviceClass` | Break down metrics by device type (`IPHONE`, `IPAD`). |

The following dimensions are **not** supported for the `SEARCHTERM` entity under `business-brands`:

- `supplyPlacement`
- `locationId`

Granularity constraints follow the same date range rules as other Apple Maps reports, except `HOURLY` isn’t available for search terms.

| Granularity | Constraint |
| --- | --- |
| `DAILY` | Date range start must be within the last 90 days. Date range must be greater than one day. |
| `HOURLY` | **Not supported** for the `SEARCHTERM` entity. |
| `WEEKLY` | Date range start within the last 365 days. End date must be at least 14 days in the past. |
| `MONTHLY` | End date must be at least 90 days in the past. |

To request a single day of data, omit `granularity` entirely. For a single-day request, the response returns results in `totalMetrics` only, since there is no `granularMetrics` breakdown to compute.

Search term reporting carries several restrictions beyond granularity, including a required `ORTZ` timezone and privacy-based suppression of low-volume terms.

| Constraint | Detail |
| --- | --- |
| Timezone | Only `ORTZ` is supported. `UTC` is **excluded** for search term reporting. |
| `HOURLY` granularity | Not available for search terms. |
| `EMPTY_METRICS` option | Not supported for `SEARCHTERM` in `business-brands`. |
| `supplyPlacement` groupBy | Not supported at the search term entity level. |
| `locationId` groupBy | Not supported at the search term entity level. |
| Privacy threshold | Low-volume search terms may be suppressed or aggregated to protect user privacy. |

#### Payload Examples

**Brands, Search Terms for Ad Group**:

Retrieve daily search term metrics for all keywords in a specific Apple Maps ad group. Results show the exact user queries that triggered impressions on Apple Maps.

##### Request

Filters by `adGroupId` with no `groupBy` dimension, returning daily search term metrics for all matched queries in March 2025 using the account’s reporting timezone.

```json
POST /v1/reports/business-brands/searchterms/query

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
         "searchTermText": "coffee shop near me",
         "keyword": {
           "id": 888999100,
           "text": "coffee near me",
           "matchType": "PHRASE"
         },
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "adGroupId": 555666888
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
             "amount": "11.00",
             "currency": "USD"
           },
           "impressions": 1100,
           "taps": 22,
           "actions": {
             "tap": 6
           },
           "getDirections": {
             "tap": 4
           }
         }
       ]
     },
     {
       "metadata": {
         "searchTermText": "best espresso downtown",
         "keyword": {
           "id": 888999101,
           "text": "espresso bar",
           "matchType": "PHRASE"
         },
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "adGroupId": 555666888
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
             "amount": "6.00",
             "currency": "USD"
           },
           "impressions": 600,
           "taps": 12,
           "actions": {
             "tap": 3
           },
           "getDirections": {
             "tap": 2
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
       },
       "getDirections": {
         "tap": 2520
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

**Brands, Grouped by Device Class**:

Retrieve search term metrics grouped by device class to understand whether your Apple Maps keywords attract different queries on iPhone vs iPad.

##### Request

Filters by `campaignId`, groups by `deviceClass`, and uses daily granularity to show search term performance broken down by device type over March 2025.

```json
POST /v1/reports/business-brands/searchterms/query

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
   "deviceClass"
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
         "searchTermText": "coffee shop open now",
         "keyword": {
           "id": 888999102,
           "text": "coffee open now",
           "matchType": "PHRASE"
         },
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "adGroupId": 555666888
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
           "deviceClass": "IPHONE",
           "localSpend": {
             "amount": "7.50",
             "currency": "USD"
           },
           "impressions": 750,
           "taps": 15,
           "actions": {
             "tap": 4
           },
           "getDirections": {
             "tap": 2
           }
         },
         {
           "date": "2025-03-01",
           "deviceClass": "IPAD",
           "localSpend": {
             "amount": "1.00",
             "currency": "USD"
           },
           "impressions": 100,
           "taps": 2,
           "actions": {
             "tap": 0
           },
           "getDirections": {
             "tap": 0
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

**Brands, Weekly**:

Retrieve weekly search term metrics for a campaign. Weekly granularity requires the end date to be at least 14 days in the past.

##### Request

Filters by `campaignId` with no `groupBy` dimension and uses weekly granularity over a 2-month window. The end date is more than 14 days in the past as required by weekly reporting.

```json
POST /v1/reports/business-brands/searchterms/query

{
 "pagination": {
   "offset": 0,
   "pageSize": 50
 },
 "filters": [
   {
     "field": "campaignId",
     "operator": "EQUALS",
     "value": "444555999"
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
         "searchTermText": "cafe with wifi",
         "keyword": {
           "id": 888999103,
           "text": "cafe wifi",
           "matchType": "CATEGORY"
         },
         "adAccountId": 123456789,
         "campaignId": 444555999,
         "adGroupId": 555666888
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
           "date": "2024-10-07",
           "localSpend": {
             "amount": "105.00",
             "currency": "USD"
           },
           "impressions": 10500,
           "taps": 210,
           "actions": {
             "tap": 53
           },
           "getDirections": {
             "tap": 32
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
   "pageSize": 50
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/reports/business-brands/searchterms/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Campaigns Report (Brands)](get-brand-campaign-reports.md)
  Retrieve performance metrics for Apple Maps campaigns broken down by optional dimensions such as country, device class, or storefront.
- [Ad Groups Report (Brands)](get-brand-ad-group-reports.md)
  Retrieve performance metrics for Apple Maps ad groups broken down by optional dimensions such as country, device class, or storefront.
- [Ads Report (Brands)](get-brand-ad-reports.md)
  Retrieve performance metrics for Apple Maps ads broken down by optional dimensions such as device class or country.
- [Keywords Report (Brands)](get-brand-keyword-reports.md)
  Retrieve performance metrics for Apple Maps keywords broken down by optional dimensions such as device class or country.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-brand-search-term-reports)*