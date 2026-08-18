# Ad

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Ad entity that links an ad creative to an ad group for serving.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Ad
```

#### Discussion

An `Ad` links a `Creative` to an `AdGroup` and is the atomic serving unit, the object that appears to users. To serve a different ad creative on an ad group, create a new ad rather than modifying an existing one.

`status` is the advertiser-controlled on/off switch. `ENABLED` allows the ad to participate in auctions while `PAUSED` suspends it.

When `systemStatus` is `NOT_RUNNING`, inspect `systemStatusReasons` for the cause. Common causes include ad creative review pending (`AD_APPROVAL_PENDING`), a rejected ad creative (`AD_APPROVAL_CREATIVE_DOC_REJECTED`), or an incompatible product page (`PRODUCT_PAGE_INCOMPATIBLE`).

Fields marked **Filterable** in the dictionary keys work as filter criteria in query endpoint requests. See [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md) for details on constructing queries.

##### Example

```json
{
  "id": 777888999,
  "name": "AwayFinder - Default Product Page",
  "status": "ENABLED",
  "adAccountId": 123456789,
  "campaignId": 444555666,
  "adGroupId": 555666777,
  "creativeId": 666777888,
  "systemStatus": "RUNNING",
  "systemStatusReasons": [],
  "systemStatusLimitingReasons": [],
  "creationTime": "2025-09-01T08:00:00.000",
  "modificationTime": "2025-09-01T08:00:00.000",
  "displayStatus": "RUNNING",
  "deleted": false
}
```

## Topics

### Type Aliases
- [type Ad.DisplayStatus](ad/displaystatus-data.typealias.md)
  Rolled-up delivery state for an ad, combining advertiser settings and system conditions into a single user-facing label.
- [type Ad.Status](ad/status-data.typealias.md)
  Advertiser-configurable serving status for an ad.
- [type Ad.SystemStatus](ad/systemstatus-data.typealias.md)
  System-computed delivery status of an ad.
- [type Ad.SystemStatusLimitingReasons](ad/systemstatuslimitingreasons-data.typealias.md)
  Reasons that limit an ad’s delivery capacity without fully stopping it.
- [type Ad.SystemStatusReasons](ad/systemstatusreasons-data.typealias.md)
  Reasons that can cause an ad’s system status to be `NOT_RUNNING`.

## Properties

- `id` (int64): The unique identifier of the ad. Read-only. Filterable: EQUALS, IN.
- `name` (string): Advertiser-given name of the ad. Mutable.
- `status` (Ad.Status): Advertiser-configurable status. Use to pause or enable the ad. See [`AdStatus`](adstatus.md). Mutable. Filterable: EQUALS, IN.
- `adAccountId` (int64): The identifier of the ad account this ad belongs to. Immutable after creation.
- `campaignId` (int64): The identifier of the campaign this ad belongs to. Immutable after creation. Filterable: EQUALS.
- `adGroupId` (int64): The identifier of the ad group this ad belongs to. Immutable after creation. Filterable: EQUALS.
- `creativeId` (int64): The unique identifier of the ad creative this ad was created from. Immutable after creation. Filterable: EQUALS.
- `systemStatus` (Ad.SystemStatus): System-computed serving status of the ad. See [`AdSystemStatus`](adsystemstatus.md). Read-only.
- `systemStatusReasons` ([Ad.SystemStatusReasons]): Reasons for the current system status. Populated when the ad is not serving. Possible values: `AD_APPROVAL_CREATIVE_DOC_EXPIRED`, `AD_APPROVAL_CREATIVE_DOC_NOT_SUBMITTED`, `AD_APPROVAL_CREATIVE_DOC_PENDING`, `AD_APPROVAL_CREATIVE_DOC_REJECTED`, `AD_APPROVAL_PENDING`, `AD_APPROVAL_REJECTED`, `CREATIVE_INVALID`, `CREATIVE_LOCALE_INCOMPATIBLE`, `CREATIVE_PENDING`, `CREATIVE_SET_INVALID`, `CREATIVE_SET_UNSUPPORTED`, `DELETED_BY_USER`, `PAUSED_BY_SYSTEM`, `PAUSED_BY_USER`, `PROCESSING`, `PRODUCT_PAGE_DELETED`, `PRODUCT_PAGE_HIDDEN`, `PRODUCT_PAGE_INCOMPATIBLE`, `PRODUCT_PAGE_INSUFFICIENT_ASSETS`, `PRODUCT_PAGE_UNAVAILABLE`. Read-only.
- `systemStatusLimitingReasons` ([Ad.SystemStatusLimitingReasons]): System status limited reasons for the ad. Possible values: `CREATIVE_POLICY_ISSUES`. Read-only.
- `creationTime` (date-time): Timestamp when the ad was created. Read-only.
- `modificationTime` (date-time): Timestamp of the last modification to the ad. Read-only.
- `displayStatus` (Ad.DisplayStatus): Rolled-up delivery state combining ad, ad group, and campaign conditions. Possible values: `RUNNING`, `PAUSED`, `ON_HOLD`, `AD_GROUP_ON_HOLD`, `CAMPAIGN_ON_HOLD`, `LIMITED`, `PROCESSING`, `DELETED`. Read-only.
- `deleted` (boolean): Indicates whether the ad is deleted. Read-only. Filterable: EQUALS.

## See Also

- [object AdCreate](adcreate.md)
  The request body for creating a new Ad object.
- [object AdUpdate](adupdate.md)
  The request body for updating an existing Ad object.
- [object AdResponse](adresponse.md)
  The response object for an Ad operation.
- [object AdQueryResponse](adqueryresponse.md)
  The response object for an Ad query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ad)*