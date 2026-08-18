# Create a Campaign

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Create a new advertising campaign with a promoted object, budget, targeting, and bid strategy configuration.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Every campaign identifies what it promotes through two immutable fields set at creation, `promotedObjectType` and `promotedObjectId`. You can’t change these fields after you create the campaign. To advertise a different app or brand, create a new campaign. For a full comparison of App Store and Apple Maps campaigns, including supported placements, supply sources, and creative sources, see the [`Campaigns Endpoints`](campaigns-endpoints.md) overview.

`promotedObjectType` determines which kind of object `promotedObjectId` points to:

- APPSTORE_APP: The campaign promotes an iOS app. `promotedObjectId` is the app’s `adamId`, retrieved from [`Search for Apps`](searches-for-a-list-of-apps.md). See [`Campaigns Endpoints`](campaigns-endpoints.md) for eligibility requirements before creating the campaign.
- BUSINESS_BRAND: The campaign promotes a brand and its business locations on Apple Maps. `promotedObjectId` is the brand’s unique identifier, retrieved from [`Query Brands`](query-brands.md) or `GET /v1/advertiser-resources?resourceType=BUSINESS_BRAND`. See [`Campaigns Endpoints`](campaigns-endpoints.md) for eligibility requirements before creating the campaign.

| Campaign Type | Required Fields | `promotedObjectType` | `promotedObjectId` |
| --- | --- | --- | --- |
| App Store | `adAccountId`, `billingEvent`, `bidStrategy`, `dailyBudget`, `name`, `promotedObjectId`, `promotedObjectType`, `startTime`, `endTime`, `targeting` | `APPSTORE_APP` | The app’s `adamId`. Retrieve it from [`Search for Apps`](searches-for-a-list-of-apps.md). |
| Apple Maps | `adAccountId`, `billingEvent`, `bidStrategy`, `dailyBudget`, `name`, `promotedObjectId`, `promotedObjectType`, `startTime`, `endTime`, `targeting` | `BUSINESS_BRAND` | The brand’s unique identifier. Retrieve it from [`Query Brands`](query-brands.md) or `GET /v1/advertiser-resources?resourceType=BUSINESS_BRAND`. |

Within `bidStrategy`, `bidStrategyType` and `bidStrategyGoal` are both required and must correspond per the pairings in [`BidStrategy`](bidstrategy.md) (for example, `MAX_CONVERSIONS` → `INSTALL`, `MANUAL_CPT` → `TAP`). Omitting either field, or sending a goal that doesn’t match the type, returns an error.

#### Payload Examples

**App Store Search**:

An app campaign targeting App Store Search Results. `promotedObjectType` is `APPSTORE_APP` and `promotedObjectId` is the app’s `adamId`.

> **Note**: Uses `bidStrategyType: MANUAL_CPT` with `bidStrategyGoal: TAP`.

##### Request

Creates an App Store Search campaign for an app identified by its `adamId`, targeting the `APPSTORE_SEARCH_RESULTS` placement in the US with a $100 daily budget and tap-based billing.

```json
POST /v1/campaigns

{
 "name": "AwayFinder App Campaign",
 "adAccountId": 123456789,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "status": "ENABLED",
 "billingEvent": "TAPS",
 "promotedObjectType": "APPSTORE_APP",
 "promotedObjectId": "123456789",
 "dailyBudget": {
   "value": {
     "amount": "100",
     "currency": "USD"
   }
 },
 "targeting": {
   "countryOrRegion": {
     "include": [
       "US"
     ]
   },
   "supplyPlacement": {
     "include": [
       "APPSTORE_SEARCH_RESULTS"
     ]
   }
 },
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPT",
   "bidStrategyGoal": "TAP"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 444555666,
   "name": "AwayFinder App Campaign",
   "adAccountId": 123456789,
   "promotedObjectType": "APPSTORE_APP",
   "promotedObjectId": "123456789",
   "status": "ENABLED",
   "billingEvent": "TAPS",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "dailyBudget": {
     "value": {
       "amount": "100.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "countryOrRegion": {
       "include": [
         "US"
       ]
     },
     "supplyPlacement": {
       "include": [
         "APPSTORE_SEARCH_RESULTS"
       ]
     }
   },
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP"
   },
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000",
   "deleted": false,
   "paymentModel": "PAYG",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "regulationResponses": []
 }
}
```

**App Store Today Tab**:

An app campaign targeting the App Store Today tab placement. Set `supplyPlacement` to `APPSTORE_TODAY_TAB`.

> **Note**: Uses `bidStrategyType: MANUAL_CPT` with `bidStrategyGoal: TAP`.

##### Request

Creates a Today tab campaign for an app identified by its `adamId`, targeting the `APPSTORE_TODAY_TAB` placement in the US with a $200 daily budget and tap-based billing.

```json
POST /v1/campaigns

{
 "name": "AwayFinder Today Tab Campaign",
 "adAccountId": 123456789,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "status": "ENABLED",
 "billingEvent": "TAPS",
 "promotedObjectType": "APPSTORE_APP",
 "promotedObjectId": "123456789",
 "dailyBudget": {
   "value": {
     "amount": "200",
     "currency": "USD"
   }
 },
 "targeting": {
   "countryOrRegion": {
     "include": [
       "US"
     ]
   },
   "supplyPlacement": {
     "include": [
       "APPSTORE_TODAY_TAB"
     ]
   }
 },
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPT",
   "bidStrategyGoal": "TAP"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 444555672,
   "name": "AwayFinder Today Tab Campaign",
   "adAccountId": 123456789,
   "promotedObjectType": "APPSTORE_APP",
   "promotedObjectId": "123456789",
   "status": "ENABLED",
   "billingEvent": "TAPS",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "dailyBudget": {
     "value": {
       "amount": "200.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "countryOrRegion": {
       "include": [
         "US"
       ]
     },
     "supplyPlacement": {
       "include": [
         "APPSTORE_TODAY_TAB"
       ]
     }
   },
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP"
   },
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000",
   "deleted": false,
   "paymentModel": "PAYG",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "regulationResponses": []
 }
}
```

**App Store — Maximize Conversions**:

An app campaign using the automated `MAX_CONVERSIONS` bid strategy, which optimizes bids toward installs while billing per tap. See [`BidStrategy`](bidstrategy.md) for the full type/goal pairings and [`Query Target CPA Suggestion`](query-target-cpa-suggestion.md) for a data-driven starting target CPA.

> **Note**: Uses `bidStrategyType: MAX_CONVERSIONS` with `bidStrategyGoal: INSTALL`.

##### Request

Creates an App Store Search campaign for an app identified by its `adamId`, using `bidStrategyType: MAX_CONVERSIONS` with the required `INSTALL` goal. `billingEvent` remains `TAPS`, so Apple Ads still charges per tap, but it automates bidding toward installs.

```json
POST /v1/campaigns

{
 "name": "AwayFinder Maximize Conversions Campaign",
 "adAccountId": 123456789,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "status": "ENABLED",
 "billingEvent": "TAPS",
 "promotedObjectType": "APPSTORE_APP",
 "promotedObjectId": "123456789",
 "dailyBudget": {
   "value": {
     "amount": "150",
     "currency": "USD"
   }
 },
 "targeting": {
   "countryOrRegion": {
     "include": [
       "US"
     ]
   },
   "supplyPlacement": {
     "include": [
       "APPSTORE_SEARCH_RESULTS"
     ]
   }
 },
 "bidStrategy": {
   "bidStrategyType": "MAX_CONVERSIONS",
   "bidStrategyGoal": "INSTALL"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 444555673,
   "name": "AwayFinder Maximize Conversions Campaign",
   "adAccountId": 123456789,
   "promotedObjectType": "APPSTORE_APP",
   "promotedObjectId": "123456789",
   "status": "ENABLED",
   "billingEvent": "TAPS",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "dailyBudget": {
     "value": {
       "amount": "150.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "countryOrRegion": {
       "include": [
         "US"
       ]
     },
     "supplyPlacement": {
       "include": [
         "APPSTORE_SEARCH_RESULTS"
       ]
     }
   },
   "bidStrategy": {
     "bidStrategyType": "MAX_CONVERSIONS",
     "bidStrategyGoal": "INSTALL"
   },
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000",
   "deleted": false,
   "paymentModel": "PAYG",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "regulationResponses": []
 }
}
```

**Apple Maps — Maps Search results**:

An advanced Apple Maps campaign targeting the Maps Search results placement. Supports radius targeting on ad groups.

> **Note**: Uses `bidStrategyType: MAX_ENGAGEMENTS` with `bidStrategyGoal: TAP`.

##### Request

Creates an advanced Apple Maps campaign explicitly targeting the `MAPS_SEARCH_RESULTS` placement, which enables radius targeting at the ad group level.

```json
POST /v1/campaigns

{
 "name": "AwayFinder Apple Maps Campaign",
 "adAccountId": 123456789,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "status": "ENABLED",
 "billingEvent": "TAPS",
 "promotedObjectType": "BUSINESS_BRAND",
 "promotedObjectId": "987654321",
 "dailyBudget": {
   "value": {
     "amount": "900.00",
     "currency": "USD"
   }
 },
 "targeting": {
   "supplySource": {
     "include": [
       "MAPS"
     ]
   },
   "supplyPlacement": {
     "include": [
       "MAPS_SEARCH_RESULTS"
     ]
   }
 },
 "bidStrategy": {
   "bidStrategyType": "MAX_ENGAGEMENTS",
   "bidStrategyGoal": "TAP"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 444555668,
   "name": "AwayFinder Apple Maps Campaign",
   "adAccountId": 123456789,
   "promotedObjectType": "BUSINESS_BRAND",
   "promotedObjectId": "987654321",
   "status": "ENABLED",
   "billingEvent": "TAPS",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "dailyBudget": {
     "value": {
       "amount": "900.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "supplySource": {
       "include": [
         "MAPS"
       ]
     },
     "supplyPlacement": {
       "include": [
         "MAPS_SEARCH_RESULTS"
       ]
     }
   },
   "bidStrategy": {
     "bidStrategyType": "MAX_ENGAGEMENTS",
     "bidStrategyGoal": "TAP"
   },
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000",
   "deleted": false,
   "paymentModel": "PAYG",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "regulationResponses": []
 }
}
```

**Apple Maps — Maps Search home**:

An advanced Apple Maps campaign targeting the Maps Search home placement. This placement doesn’t support radius targeting.

> **Note**: Uses `bidStrategyType: MAX_ENGAGEMENTS` with `bidStrategyGoal: TAP`.

##### Request

Creates an advanced Apple Maps campaign targeting the `MAPS_SEARCH_HOME` placement. This placement doesn’t support radius targeting, so don’t configure it at the ad group level.

```json
POST /v1/campaigns

{
 "name": "AwayFinder Apple Maps Search Home Campaign",
 "adAccountId": 123456789,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "status": "ENABLED",
 "billingEvent": "TAPS",
 "promotedObjectType": "BUSINESS_BRAND",
 "promotedObjectId": "987654321",
 "dailyBudget": {
   "value": {
     "amount": "900.00",
     "currency": "USD"
   }
 },
 "targeting": {
   "supplySource": {
     "include": [
       "MAPS"
     ]
   },
   "supplyPlacement": {
     "include": [
       "MAPS_SEARCH_HOME"
     ]
   }
 },
 "bidStrategy": {
   "bidStrategyType": "MAX_ENGAGEMENTS",
   "bidStrategyGoal": "TAP"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 444555669,
   "name": "AwayFinder Apple Maps Search Home Campaign",
   "adAccountId": 123456789,
   "promotedObjectType": "BUSINESS_BRAND",
   "promotedObjectId": "987654321",
   "status": "ENABLED",
   "billingEvent": "TAPS",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "dailyBudget": {
     "value": {
       "amount": "900.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "supplySource": {
       "include": [
         "MAPS"
       ]
     },
     "supplyPlacement": {
       "include": [
         "MAPS_SEARCH_HOME"
       ]
     }
   },
   "bidStrategy": {
     "bidStrategyType": "MAX_ENGAGEMENTS",
     "bidStrategyGoal": "TAP"
   },
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000",
   "deleted": false,
   "paymentModel": "PAYG",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "regulationResponses": []
 }
}
```

**Apple Maps — Manual CPT**:

An Apple Maps campaign using manual cost-per-tap bidding. Requires an explicit supply placement. You set the tap bid amount at the ad group level.

> **Note**: Uses `bidStrategyType: MANUAL_CPT` with `bidStrategyGoal: TAP`.

##### Request

Creates an Apple Maps campaign with manual cost-per-tap bidding, explicitly setting `bidStrategyType` to `MANUAL_CPT` and targeting `MAPS_SEARCH_RESULTS`. You configure the tap bid amount at the ad group level.

```json
POST /v1/campaigns

{
 "name": "AwayFinder Apple Maps Manual CPT Campaign",
 "adAccountId": 123456789,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "status": "ENABLED",
 "billingEvent": "TAPS",
 "promotedObjectType": "BUSINESS_BRAND",
 "promotedObjectId": "987654321",
 "dailyBudget": {
   "value": {
     "amount": "1000.00",
     "currency": "USD"
   }
 },
 "targeting": {
   "supplySource": {
     "include": [
       "MAPS"
     ]
   },
   "supplyPlacement": {
     "include": [
       "MAPS_SEARCH_RESULTS"
     ]
   }
 },
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPT",
   "bidStrategyGoal": "TAP"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 444555670,
   "name": "AwayFinder Apple Maps Manual CPT Campaign",
   "adAccountId": 123456789,
   "promotedObjectType": "BUSINESS_BRAND",
   "promotedObjectId": "987654321",
   "status": "ENABLED",
   "billingEvent": "TAPS",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "dailyBudget": {
     "value": {
       "amount": "1000.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "supplySource": {
       "include": [
         "MAPS"
       ]
     },
     "supplyPlacement": {
       "include": [
         "MAPS_SEARCH_RESULTS"
       ]
     }
   },
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP"
   },
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000",
   "deleted": false,
   "paymentModel": "PAYG",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "regulationResponses": []
 }
}
```

**Apple Maps — Manual CPM**:

An Apple Maps campaign using manual cost-per-thousand-impressions bidding. `billingEvent` must be `IMPRESSIONS`.

> **Note**: Uses `bidStrategyType: MANUAL_CPM` with `bidStrategyGoal: IMPRESSION`.

##### Request

Creates an Apple Maps campaign with manual cost-per-thousand-impressions bidding, setting `billingEvent` to `IMPRESSIONS` and `bidStrategyGoal` to `IMPRESSION` as required by `MANUAL_CPM`.

```json
POST /v1/campaigns

{
 "name": "AwayFinder Apple Maps Manual CPM Campaign",
 "adAccountId": 123456789,
 "startTime": "2025-09-01T00:00:00.000",
 "endTime": "2025-12-31T23:59:59.000",
 "status": "ENABLED",
 "billingEvent": "IMPRESSIONS",
 "promotedObjectType": "BUSINESS_BRAND",
 "promotedObjectId": "987654321",
 "dailyBudget": {
   "value": {
     "amount": "1000.00",
     "currency": "USD"
   }
 },
 "targeting": {
   "supplySource": {
     "include": [
       "MAPS"
     ]
   },
   "supplyPlacement": {
     "include": [
       "MAPS_SEARCH_RESULTS"
     ]
   }
 },
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPM",
   "bidStrategyGoal": "IMPRESSION"
 }
}
```

##### Response

```json
{
 "result": {
   "id": 444555671,
   "name": "AwayFinder Apple Maps Manual CPM Campaign",
   "adAccountId": 123456789,
   "promotedObjectType": "BUSINESS_BRAND",
   "promotedObjectId": "987654321",
   "status": "ENABLED",
   "billingEvent": "IMPRESSIONS",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
   "dailyBudget": {
     "value": {
       "amount": "1000.00",
       "currency": "USD"
     }
   },
   "targeting": {
     "supplySource": {
       "include": [
         "MAPS"
       ]
     },
     "supplyPlacement": {
       "include": [
         "MAPS_SEARCH_RESULTS"
       ]
     }
   },
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPM",
     "bidStrategyGoal": "IMPRESSION"
   },
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000",
   "deleted": false,
   "paymentModel": "PAYG",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "regulationResponses": []
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/campaigns`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Campaigns](post-campaigns-query.md)
  Query campaigns using filters, sorting, and pagination.
- [Get a Campaign](get-campaigns-_id_.md)
  Retrieve a single campaign by its unique identifier.
- [Update a Campaign](put-campaigns-_id_.md)
  Update a campaign’s name, status, budget, targeting, or bid strategy.
- [Delete a Campaign](delete-campaigns-_id_.md)
  Soft-delete a campaign by its unique identifier, cascading to its ad groups, keywords, and ads.
- [Get Legacy App Limited Status Reason Details](get-campaigns-_id_-legacy-app-limited-status-reason-details.md)
  Return a map of country or region codes to their associated limited-status reason for legacy app campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-campaigns)*