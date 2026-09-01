# Query Campaigns

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query campaigns using filters, sorting, and pagination.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint queries campaigns using a standard `QueryRequest` body. An empty request body returns all campaigns for the ad account with default pagination.

See [`QueryFilterOperator`](queryfilteroperator.md) for the full set of supported comparison operators.

##### Filterable Fields

| Field | Type | Operators | Sortable | Description |
| --- | --- | --- | --- | --- |
| `id` | integer | `EQUALS`, `IN` | Yes | System-assigned unique identifier for the campaign. |
| `name` | string | `EQUALS`, `IN`, `LIKE`, `STARTS_WITH`, `ENDS_WITH` | Yes | Campaign name. |
| `status` | string (enum) | `EQUALS`, `IN` | Yes | Captures the advertiser’s intent for the campaign to serve. See [`CampaignStatus`](campaignstatus.md). |
| `systemStatus` | string (enum) | `EQUALS`, `IN` | Yes | System-computed operational status reflecting the campaign’s serving state. See [`CampaignSystemStatus`](campaignsystemstatus.md). |
| `systemStatusReasons` | array of strings | `CONTAINS_ANY`, `CONTAINS_ALL`, `NOT_CONTAINS_ANY`, `NOT_CONTAINS_ALL` | No | Reasons contributing to the current `systemStatus`. See [`CampaignSystemStatusReason`](campaignsystemstatusreason.md). |
| `systemStatusLimitingReasons` | array of strings | `CONTAINS_ANY`, `CONTAINS_ALL`, `NOT_CONTAINS_ANY`, `NOT_CONTAINS_ALL` | No | Reasons limiting delivery below maximum potential. See [`CampaignSystemLimitedStatusReason`](campaignsystemlimitedstatusreason.md). |
| `billingEvent` | string (enum) | `EQUALS`, `IN` | Yes | The event type that triggers a charge. See [`BillingEvent`](billingevent.md). |
| `paymentModel` | string (enum) | `EQUALS`, `IN` | Yes | The payment model for the campaign. See [`PaymentModel`](paymentmodel.md). |
| `promotedObjectType` | string (enum) | `EQUALS`, `NOT_EQUALS`, `IN`, `NOT_IN` | Yes | Whether the campaign promotes an App Store app or a brand. See [`PromotedObjectType`](promotedobjecttype.md). |
| `promotedObjectId` | string | `EQUALS`, `NOT_EQUALS`, `IN`, `NOT_IN` | Yes | The identifier of the promoted entity. |
| `startTime` | string (ISO 8601) | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` | Yes | The scheduled start date and time of the campaign. |
| `endTime` | string (ISO 8601) | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` | Yes | The scheduled end date and time of the campaign. |
| `creationTime` | string (ISO 8601) | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` | Yes | Timestamp when the campaign was created. |
| `modificationTime` | string (ISO 8601) | `EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUAL_TO`, `LESS_THAN`, `LESS_THAN_OR_EQUAL_TO` | Yes | Timestamp of the last modification to the campaign. |
| `deleted` | boolean | `EQUALS`, `IN` | Yes | Whether the campaign has been soft-deleted. |

The request body is a [`QueryRequest`](queryrequest.md) composed of [`QueryFilter`](queryfilter.md) conditions and [`QuerySort`](querysort.md) directives ([`QuerySortOrder`](querysortorder.md)), controlled by [`QueryPagination`](querypagination.md).

#### Payload Examples

**Query for a Brand**:

Query campaigns for a specific brand by pairing `promotedObjectType` and `promotedObjectId`.

##### Request

Filters campaigns to a single brand by combining an `EQUALS` match on `promotedObjectType` and `promotedObjectId`, returning results sorted by creation date descending.

```json
POST /v1/campaigns/query

{
 "filters": [
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": "BUSINESS_BRAND"
   },
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": "987654321"
   }
 ],
 "sorting": [
   {
     "field": "creationTime",
     "order": "DESC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": 111222333,
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
     "creationTime": "2025-01-15T10:30:00.000",
     "modificationTime": "2025-01-20T14:45:00.000",
     "deleted": false,
     "paymentModel": "PAYG",
     "systemStatus": "RUNNING",
     "systemStatusReasons": [],
     "systemStatusLimitingReasons": [],
     "displayStatus": "RUNNING"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Query for an App**:

Query campaigns for a specific App Store app using its `adamId` as the `promotedObjectId`.

##### Request

Filters campaigns to a specific App Store app using its `adamId` as the `promotedObjectId`, returning results sorted by most recently modified.

```json
POST /v1/campaigns/query

{
 "filters": [
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": "APPSTORE_APP"
   },
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": "123456789"
   }
 ],
 "sorting": [
   {
     "field": "modificationTime",
     "order": "DESC"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
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
     "displayStatus": "RUNNING"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Filter by Status**:

Combine `promotedObjectType`, `promotedObjectId`, and `status` to return only enabled campaigns for a specific brand.

##### Request

Adds a `status` filter alongside `promotedObjectType` and `promotedObjectId` to return only `ENABLED` campaigns for a specific brand, narrowing results without a sort order.

```json
POST /v1/campaigns/query

{
 "filters": [
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": "BUSINESS_BRAND"
   },
   {
     "field": "promotedObjectId",
     "operator": "EQUALS",
     "value": "987654321"
   },
   {
     "field": "status",
     "operator": "EQUALS",
     "value": "ENABLED"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": 111222333,
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
     "creationTime": "2025-01-15T10:30:00.000",
     "modificationTime": "2025-01-20T14:45:00.000",
     "deleted": false,
     "paymentModel": "PAYG",
     "systemStatus": "RUNNING",
     "systemStatusReasons": [],
     "systemStatusLimitingReasons": [],
     "displayStatus": "RUNNING"
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Multiple Brand IDs**:

To query campaigns across multiple brands in a single request, use the `IN` operator.

##### Request

Uses the `IN` operator on `promotedObjectId` to retrieve campaigns across three distinct brand IDs in a single request, avoiding separate per-brand queries.

```json
POST /v1/campaigns/query

{
 "filters": [
   {
     "field": "promotedObjectType",
     "operator": "EQUALS",
     "value": "BUSINESS_BRAND"
   },
   {
     "field": "promotedObjectId",
     "operator": "IN",
     "value": [
       "987654321",
       "987654322",
       "987654323"
     ]
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 50,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": 111222333,
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
     "creationTime": "2025-01-15T10:30:00.000",
     "modificationTime": "2025-01-20T14:45:00.000",
     "deleted": false,
     "paymentModel": "PAYG",
     "systemStatus": "RUNNING",
     "systemStatusReasons": [],
     "systemStatusLimitingReasons": [],
     "displayStatus": "RUNNING"
   },
   {
     "id": 222333444,
     "name": "AwayFinder Maps Campaign",
     "adAccountId": 123456789,
     "promotedObjectType": "BUSINESS_BRAND",
     "promotedObjectId": "987654322",
     "status": "ENABLED",
     "billingEvent": "TAPS",
     "startTime": "2025-08-01T00:00:00.000",
     "endTime": "2025-12-31T23:59:59.000",
     "dailyBudget": {
       "value": {
         "amount": "500.00",
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
     "creationTime": "2025-02-01T09:00:00.000",
     "modificationTime": "2025-02-15T11:00:00.000",
     "deleted": false,
     "paymentModel": "PAYG",
     "systemStatus": "RUNNING",
     "systemStatusReasons": [],
     "systemStatusLimitingReasons": [],
     "displayStatus": "RUNNING"
   },
   {
     "id": 333444555,
     "name": "AwayFinder Brand Campaign",
     "adAccountId": 123456789,
     "promotedObjectType": "BUSINESS_BRAND",
     "promotedObjectId": "987654323",
     "status": "PAUSED",
     "billingEvent": "TAPS",
     "startTime": "2025-07-01T00:00:00.000",
     "endTime": "2025-10-31T23:59:59.000",
     "dailyBudget": {
       "value": {
         "amount": "250.00",
         "currency": "USD"
       }
     },
     "targeting": {
       "supplySource": {
         "include": [
           "MAPS"
         ]
       }
     },
     "bidStrategy": {
       "bidStrategyType": "MAX_ENGAGEMENTS",
       "bidStrategyGoal": "TAP"
     },
     "creationTime": "2025-03-10T14:00:00.000",
     "modificationTime": "2025-04-01T08:30:00.000",
     "deleted": false,
     "paymentModel": "PAYG",
     "systemStatus": "NOT_RUNNING",
     "systemStatusReasons": ["PAUSED_BY_USER"],
     "systemStatusLimitingReasons": [],
     "displayStatus": "PAUSED"
   }
 ],
 "pagination": {
   "totalCount": 3,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/campaigns/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Campaign](post-campaigns.md)
  Create a new advertising campaign with a promoted object, budget, targeting, and bid strategy configuration.
- [Get a Campaign](get-campaigns-_id_.md)
  Retrieve a single campaign by its unique identifier.
- [Update a Campaign](put-campaigns-_id_.md)
  Update a campaign’s name, status, budget, targeting, or bid strategy.
- [Delete a Campaign](delete-campaigns-_id_.md)
  Soft-delete a campaign by its unique identifier, cascading to its ad groups, keywords, and ads.
- [Get Legacy App Limited Status Reason Details](get-campaigns-_id_-legacy-app-limited-status-reason-details.md)
  Return a map of country or region codes to their associated limited-status reason for legacy app campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-campaigns-query)*