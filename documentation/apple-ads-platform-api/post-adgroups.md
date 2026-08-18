# Create an Ad Group

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Create a new ad group within a campaign, defining targeting, bid strategy, and scheduling for a set of ads.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint creates an ad group that belongs to a single campaign via `campaignId`, which is required at creation and immutable afterward. The ad group defines its own targeting, bid strategy, and schedule, scoped within the campaign’s supply placement and budget.

`pricingModel` is also required: use `CPT` for tap-billed campaigns and `CPM` for impression-billed campaigns using the `MANUAL_CPM` bid strategy.

#### Payload Examples

**App Store Ad Group**:

An ad group for an App Store campaign targeting iPhone users aged 18–34 who have not yet downloaded the app.

##### Request

```json
POST /v1/adgroups

{
 "name": "AwayFinder iOS — New Users 18-34",
 "campaignId": 444555666,
 "pricingModel": "CPT",
 "status": "ENABLED",
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPT",
   "bidStrategyGoal": "TAP",
   "bid": {
     "amount": "2.50",
     "currency": "USD"
   }
 },
 "targeting": {
   "deviceClass": {
     "include": [
       "IPHONE"
     ]
   },
   "minAge": {
     "include": [
       "18"
     ]
   },
   "maxAge": {
     "include": [
       "34"
     ]
   },
   "appDownloader": {
     "include": [
       "123456789"
     ]
   }
 }
}
```

##### Response

```json
{
 "result": {
   "id": 555666777,
   "name": "AwayFinder iOS — New Users 18-34",
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP",
     "bid": {
       "amount": "2.50",
       "currency": "USD"
     }
   },
   "targeting": {
     "deviceClass": {
       "include": [
         "IPHONE"
       ]
     },
     "minAge": {
       "include": [
         "18"
       ]
     },
     "maxAge": {
       "include": [
         "34"
       ]
     },
     "appDownloader": {
       "include": [
         "123456789"
       ]
     }
   },
   "automatedKeywordsOptIn": false,
   "automatedKeywordsRequired": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**App Store - Maximize Conversions**:

An App Store ad group using the `MAX_CONVERSIONS` automated bid strategy, which pairs with the `INSTALL` goal to optimize bids toward app installs. `bid` is optional and acts as a ceiling rather than a fixed price.

##### Request

```json
POST /v1/adgroups

{
 "name": "AwayFinder iOS — Maximize Conversions",
 "campaignId": 444555666,
 "pricingModel": "CPT",
 "status": "ENABLED",
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "bidStrategy": {
   "bidStrategyType": "MAX_CONVERSIONS",
   "bidStrategyGoal": "INSTALL",
   "bid": {
     "amount": "5.00",
     "currency": "USD"
   }
 },
 "targeting": {
   "deviceClass": {
     "include": [
       "IPHONE"
     ]
   },
   "minAge": {
     "include": [
       "18"
     ]
   },
   "maxAge": {
     "include": [
       "34"
     ]
   }
 }
}
```

##### Response

```json
{
 "result": {
   "id": 555666782,
   "name": "AwayFinder iOS — Maximize Conversions",
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "bidStrategy": {
     "bidStrategyType": "MAX_CONVERSIONS",
     "bidStrategyGoal": "INSTALL",
     "bid": {
       "amount": "5.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "deviceClass": {
       "include": [
         "IPHONE"
       ]
     },
     "minAge": {
       "include": [
         "18"
       ]
     },
     "maxAge": {
       "include": [
         "34"
       ]
     }
   },
   "automatedKeywordsOptIn": false,
   "automatedKeywordsRequired": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**Apple Maps - Automated**:

An automated ad group for an Apple Maps campaign. `automatedKeywordsOptIn` is `true`, enabling Search Match to automatically identify and target relevant search queries. Separately, omitting `locationGroup` means the ad group defaults to targeting all of the brand’s locations.

##### Request

```json
POST /v1/adgroups

{
 "name": "AwayFinder — All Locations",
 "campaignId": 444555667,
 "pricingModel": "CPT",
 "automatedKeywordsOptIn": true
}
```

##### Response

```json
{
 "result": {
   "id": 555666778,
   "name": "AwayFinder — All Locations",
   "adAccountId": 123456789,
   "campaignId": 444555667,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "automatedKeywordsOptIn": true,
   "automatedKeywordsRequired": true,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**Apple Maps - Radius**:

An Apple Maps ad group using radius targeting.

##### Request

```json
POST /v1/adgroups

{
 "name": "AwayFinder Maps — Nearby Search",
 "campaignId": 444555668,
 "pricingModel": "CPT",
 "automatedKeywordsOptIn": false,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPT",
   "bidStrategyGoal": "TAP",
   "bid": {
     "amount": "5.00",
     "currency": "USD"
   }
 },
 "targeting": {
   "locationGroup": {
     "include": [
       "987654321"
     ]
   },
   "radius": {
     "include": [
       "MEDIUM"
     ]
   }
 }
}
```

##### Response

```json
{
 "result": {
   "id": 555666779,
   "name": "AwayFinder Maps — Nearby Search",
   "adAccountId": 123456789,
   "campaignId": 444555668,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP",
     "bid": {
       "amount": "5.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "locationGroup": {
       "include": [
         "987654321"
       ]
     },
     "radius": {
       "include": [
         "MEDIUM"
       ]
     }
   },
   "automatedKeywordsOptIn": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**Apple Maps - Geo**:

An Apple Maps ad group using geo location targeting (locality + daypart). Up to 1,000 geo targets total. Cannot combine with radius targeting.

##### Request

```json
POST /v1/adgroups

{
 "name": "AwayFinder Maps — SF Bay Area",
 "campaignId": 444555668,
 "pricingModel": "CPT",
 "automatedKeywordsOptIn": false,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPT",
   "bidStrategyGoal": "TAP",
   "bid": {
     "amount": "4.00",
     "currency": "USD"
   }
 },
 "targeting": {
   "locality": {
     "include": [
       "902134",
       "830123"
     ]
   },
   "daypart": {
     "include": [
       "1",
       "5",
       "10",
       "18"
     ]
   }
 }
}
```

##### Response

```json
{
 "result": {
   "id": 555666780,
   "name": "AwayFinder Maps — SF Bay Area",
   "adAccountId": 123456789,
   "campaignId": 444555668,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP",
     "bid": {
       "amount": "4.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "locality": {
       "include": [
         "902134",
         "830123"
       ]
     },
     "daypart": {
       "include": [
         "1",
         "5",
         "10",
         "18"
       ]
     }
   },
   "automatedKeywordsOptIn": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**Apple Maps - Daypart**:

An Apple Maps ad group using daypart targeting to restrict delivery to specific hours. Supported for `BUSINESS_BRAND` campaigns per the `AdGroupTargetingCreate` schema. `daypart` values are hourly slot integers 0–167 (0 = Sunday 12:00 AM, 24 = Monday 12:00 AM, and so on).

##### Request

```json
POST /v1/adgroups

{
 "name": "AwayFinder Maps — Weekday Lunch",
 "campaignId": 444555668,
 "pricingModel": "CPT",
 "automatedKeywordsOptIn": false,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPT",
   "bidStrategyGoal": "TAP",
   "bid": {
     "amount": "4.50",
     "currency": "USD"
   }
 },
 "targeting": {
   "locationGroup": {
     "include": [
       "987654321"
     ]
   },
   "daypart": {
     "include": [
       "11",
       "12",
       "35",
       "36",
       "59",
       "60",
       "83",
       "84",
       "107",
       "108"
     ]
   }
 }
}
```

##### Response

```json
{
 "result": {
   "id": 555666781,
   "name": "AwayFinder Maps — Weekday Lunch",
   "adAccountId": 123456789,
   "campaignId": 444555668,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP",
     "bid": {
       "amount": "4.50",
       "currency": "USD"
     }
   },
   "targeting": {
     "locationGroup": {
       "include": [
         "987654321"
       ]
     },
     "daypart": {
       "include": [
         "11",
         "12",
         "35",
         "36",
         "59",
         "60",
         "83",
         "84",
         "107",
         "108"
       ]
     }
   },
   "automatedKeywordsOptIn": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/adgroups`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Ad Groups](post-adgroups-query.md)
  Query ad groups using filters, sorting, and pagination.
- [Get an Ad Group](get-adgroups-_id_.md)
  Retrieve a single ad group by its unique identifier.
- [Update an Ad Group](put-adgroups-_id_.md)
  Update an existing ad group’s name, status, bid strategy, targeting, or scheduling.
- [Delete an Ad Group](delete-adgroups-_id_.md)
  Soft-delete an ad group by its unique identifier, along with all ads and keywords associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-adgroups)*