# Get an Ad

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieves a single ad by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a single ad by its ID. The response includes `systemStatus`, `displayStatus`, `systemStatusReasons`, and `systemStatusLimitingReasons`. To diagnose why an ad may not be delivering, use these fields together. See [`Ads Endpoints`](ads-endpoints.md) for the full status field semantics.

`displayStatus` resolves to one of the following values:

| Value | Description |
| --- | --- |
| `RUNNING` | The ad is actively serving impressions. |
| `PAUSED` | The advertiser paused the ad at the ad level (`status: PAUSED`). |
| `ON_HOLD` | The ad is on hold due to an ad-level condition. |
| `AD_GROUP_ON_HOLD` | The parent ad group is on hold. |
| `CAMPAIGN_ON_HOLD` | The parent campaign is on hold. |
| `LIMITED` | The ad is serving, but one or more factors restrict delivery. |
| `PROCESSING` | The system is processing the ad, or Apple is reviewing its ad creative. |
| `DELETED` | The advertiser deleted the ad. |

When `systemStatus` is `NOT_RUNNING`, check the following causes:

| Cause | Description |
| --- | --- |
| Creative pending review | Apple has not yet approved the ad creative associated with this ad. `displayStatus` is `PROCESSING`. |
| Creative rejected | Apple rejected the ad creative (`INVALID`). The ad will not serve until the advertiser associates a new ad creative via a new ad. |
| Ad paused | `status: PAUSED` on the ad itself. |
| Ad group paused | The advertiser has paused the parent ad group, or the system has put it on hold. |
| Campaign paused | The advertiser has paused the parent campaign, or the system has put it on hold. |

Keep the following constraints in mind when reading a GET response:

| Constraint | Detail |
| --- | --- |
| Deleted ads are returned | The system still returns a deleted ad with `deleted: true`. It does not remove the record from GET by ID responses. |
| Use `systemStatusReasons` for diagnostics | The `systemStatusReasons` array identifies specific causes when `systemStatus` is `NOT_RUNNING`. |
| `creativeId` and `adGroupId` are read-only | These fields are immutable. The system sets them at creation and returns them on every GET response. |
| To list all ads, use the query endpoint | `GET /v1/ads/{id}` returns a single record. To list or filter multiple ads, use `POST /v1/ads/query`. |

#### Payload Examples

**Running Ad**:

##### Request

Response for an ad that is actively serving. `systemStatus` is `RUNNING` and `displayStatus` is `RUNNING`.

```None
GET https://api.ads.apple.com/v1/ads/777888999
```

##### Response

```json
{
 "result": {
   "id": 777888999,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "adGroupId": 555666777,
   "creativeId": 666777888,
   "name": "AwayFinder - Default Product Page",
   "status": "ENABLED",
   "systemStatus": "RUNNING",
   "systemStatusReasons": [],
   "systemStatusLimitingReasons": [],
   "displayStatus": "RUNNING",
   "deleted": false,
   "creationTime": "2025-09-01T08:00:00.000",
   "modificationTime": "2025-09-01T08:00:00.000"
 }
}
```

**Ad Pending Creative Review**:

##### Request

Response for an ad whose ad creative is pending review. `systemStatus` is `NOT_RUNNING` with a reason of `AD_APPROVAL_PENDING`, and `displayStatus` is `PROCESSING`.

```None
GET https://api.ads.apple.com/v1/ads/777888998
```

##### Response

```json
{
 "result": {
   "id": 777888998,
   "adAccountId": 123456789,
   "campaignId": 444555666,
   "adGroupId": 555666777,
   "creativeId": 666777888,
   "name": "AwayFinder - Maps Creative",
   "status": "ENABLED",
   "systemStatus": "NOT_RUNNING",
   "systemStatusReasons": [
     "AD_APPROVAL_PENDING"
   ],
   "systemStatusLimitingReasons": [],
   "displayStatus": "PROCESSING",
   "deleted": false,
   "creationTime": "2025-09-01T09:00:00.000",
   "modificationTime": "2025-09-01T09:00:00.000"
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/ads/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad](post-ads.md)
  Creates a new ad that links an ad creative to an ad group for delivery.
- [Query Ads](post-ads-query.md)
  Searches and filters ads using structured query criteria including field filters, sorting, and pagination.
- [Update an Ad](put-ads-_id_.md)
  Updates the name or status of an existing ad by its unique identifier.
- [Delete an Ad](delete-ads-_id_.md)
  Soft-deletes an ad by its unique identifier, stopping delivery and removing it from active results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-ads-_id_)*