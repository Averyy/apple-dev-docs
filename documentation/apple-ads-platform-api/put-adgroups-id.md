# Update an Ad Group

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Update an existing ad group’s name, status, bid strategy, targeting, or scheduling.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint updates an existing ad group. Only include the fields you want to modify. See the Determine Which Fields You Can Update section below to confirm which fields you can change.

For ad groups under an auto-bidding campaign, see [`AdGroupUpdate.BidStrategy`](adgroupupdate/bidstrategy-data.dictionary.md) for how to echo the campaign’s bid strategy so the API doesn’t reject a `GET`-then-`PUT` round trip.

##### Determine Which Fields You Can Update

To change any field marked Yes below, use this endpoint. Fields marked No are either only settable at creation via [`Create an Ad Group`](post-adgroups.md) or are system-computed. Sending them in an update request has no effect. See the Notes column for which applies to a given field. `cpaCap` is marked Deprecated: the API still accepts it on update for backward compatibility, but new integrations should use `bidStrategy` instead.

| Field | Mutable | Notes |
| --- | --- | --- |
| `name` | Yes | Ad group display name. |
| `status` | Yes | `ENABLED` or `PAUSED`. |
| `startTime` | Yes | Ad group schedule start time. |
| `endTime` | Yes | Ad group schedule end time. |
| `automatedKeywordsOptIn` | Yes | Toggle Search Match automated keyword targeting. |
| `automatedKeywordsRequired` | **No** | Set at creation. Whether automated keyword generation is required for this ad group. Immutable afterward. |
| `bidStrategy` | Yes | You can update `bidStrategyType`, `bidStrategyGoal`, and `bid`. You must send `bidStrategyType` and `bidStrategyGoal` together, matched per the pairings in [`BidStrategy`](bidstrategy.md). See [`BidStrategyUpdate`](bidstrategyupdate.md). |
| `targeting` | Yes | Supports partial updates. The request modifies only the targeting dimensions it includes. Omitted dimensions remain unchanged. |
| `cpaCap` | Deprecated | Still accepted on update for backward compatibility, but deprecated in favor of `bidStrategy` with `MAX_CONVERSIONS`. |
| `campaignId` | **No** | Set at creation. Identifies the parent campaign. Immutable afterward. |
| `pricingModel` | **No** | Set at creation. Must match the parent campaign’s `billingEvent`. Immutable afterward. |
| `adAccountId` | No | Inherited from the campaign. You cannot reassign it. Read-only. |
| `id` | No | System-assigned identifier. Read-only. |
| `systemStatus` | No | System-computed delivery eligibility. Read-only. |
| `systemStatusReasons` | No | System-applied reasons contributing to `systemStatus`. Read-only. |
| `systemStatusLimitingReasons` | No | System-applied reasons limiting delivery below maximum potential. Read-only. |
| `displayStatus` | No | Computed, rolled-up delivery state combining `status` and `systemStatus`. Read-only. |
| `creationTime` | No | Set when the ad group is created. Read-only. |
| `modificationTime` | No | Updated automatically on every change. Read-only. |
| `deleted` | No | Managed via [`Delete an Ad Group`](delete-adgroups-_id_.md), not via update. Read-only. |

#### Payload Examples

**Pause Ad Group**:

Pause an ad group by setting `status` to `PAUSED`. Send only the fields you want to change.

##### Request

```json
PUT /v1/adgroups/555666777

{
 "status": "PAUSED"
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
   "status": "PAUSED",
   "systemStatus": "NOT_RUNNING",
   "displayStatus": "PAUSED",
   "startTime": "2025-09-01T00:00:00.000",
   "endTime": "2025-12-31T23:59:59.000",
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
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-06-01T10:00:00.000"
 }
}
```

**Update Bid**:

Increase the tap bid for an Apple Maps ad group. Send only the `bidStrategy` field.

##### Request

```json
PUT /v1/adgroups/555666779

{
 "bidStrategy": {
   "bidStrategyType": "MANUAL_CPT",
   "bidStrategyGoal": "TAP",
   "bid": {
     "amount": "7.50",
     "currency": "USD"
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
   "bidStrategy": {
     "bidStrategyType": "MANUAL_CPT",
     "bidStrategyGoal": "TAP",
     "bid": {
       "amount": "7.50",
       "currency": "USD"
     }
   },
   "targeting": {
     "radius": {
       "include": [
         "MEDIUM"
       ]
     }
   },
   "automatedKeywordsOptIn": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-06-01T11:00:00.000"
 }
}
```

**Echo Auto-Bidding Strategy**:

For an ad group under an auto-bidding campaign (`MAX_CONVERSIONS` or `MAX_ENGAGEMENTS`), a `GET`-then-`PUT` round trip is safe: echo the same `bidStrategyType` and `bidStrategyGoal` as the campaign with `bid` set to `0`. The API rejects a non-zero bid or a type/goal that doesn’t match the campaign’s.

##### Request

```json
PUT /v1/adgroups/555666781

{
 "bidStrategy": {
   "bidStrategyType": "MAX_CONVERSIONS",
   "bidStrategyGoal": "INSTALL",
   "bid": {
     "amount": "0.00",
     "currency": "USD"
   }
 },
 "status": "ENABLED"
}
```

##### Response

```json
{
 "result": {
   "id": 555666781,
   "name": "AwayFinder iOS — Lookalike Audiences",
   "adAccountId": 123456789,
   "campaignId": 444555669,
   "pricingModel": "CPT",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "displayStatus": "RUNNING",
   "bidStrategy": {
     "bidStrategyType": "MAX_CONVERSIONS",
     "bidStrategyGoal": "INSTALL",
     "bid": {
       "amount": "0.00",
       "currency": "USD"
     }
   },
   "automatedKeywordsOptIn": false,
   "deleted": false,
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-06-01T13:00:00.000"
 }
}
```

**Update Targeting**:

Update specific targeting dimensions. The request modifies only the dimensions it includes. Omitted dimensions remain unchanged. Each dimension’s `include` array fully replaces the existing values for that dimension. Daypart slot values range from 0–167 (slot 0 = Sunday 12:00 AM, slot 24 = Monday 12:00 AM).

##### Request

```json
PUT /v1/adgroups/555666780

{
 "targeting": {
   "locality": {
     "include": [
       "902134",
       "830123",
       "812456"
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
   "targeting": {
     "locality": {
       "include": [
         "902134",
         "830123",
         "812456"
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
   "modificationTime": "2025-06-01T12:00:00.000"
 }
}
```

## Endpoint

`PUT https://api.ads.apple.com/v1/adgroups/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad Group](post-adgroups.md)
  Create a new ad group within a campaign, defining targeting, bid strategy, and scheduling for a set of ads.
- [Query Ad Groups](post-adgroups-query.md)
  Query ad groups using filters, sorting, and pagination.
- [Get an Ad Group](get-adgroups-_id_.md)
  Retrieve a single ad group by its unique identifier.
- [Delete an Ad Group](delete-adgroups-_id_.md)
  Soft-delete an ad group by its unique identifier, along with all ads and keywords associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/put-adgroups-_id_)*