# ReportingKeyword

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Keyword metadata in a report row.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ReportingKeyword
```

#### Discussion

`ReportingKeyword` is the keyword metadata object embedded in keyword report rows and within search term rows (via the `keyword` field). It captures the keyword’s text, match type, bid amount, and status at report time, along with its organizational context (`campaignId`, `adGroupId`, `adAccountId`).

The `bid` field is the keyword-level bid amount in the account currency, and `adGroup` provides a lightweight summary of the parent ad group. The report populates the dimension fields (`countryOrRegion`, `deviceClass`) when you specify those dimensions in the report request.

##### Example

```json
{
  "id": 555666777,
  "campaignId": 123456789,
  "adAccountId": 987654321,
  "deleted": false,
  "text": "awayfinder travel app",
  "status": "ACTIVE",
  "matchType": "BROAD",
  "bid": {
    "currency": "USD",
    "amount": "1.50"
  },
  "adGroupId": 234567891,
  "modificationTime": "2025-01-10T08:00:00.000",
  "creationTime": "2025-01-05T08:00:00.000",
  "displayStatus": "RUNNING",
  "adGroup": {
    "name": "AwayFinder Search - Broad",
    "deleted": false
  },
  "countryOrRegion": "US",
  "deviceClass": "IPHONE"
}
```

## Properties

- `id` (int64): The keyword identifier.
- `campaignId` (int64): The identifier of the campaign that owns the keyword.
- `adAccountId` (int64): The identifier of the ad account that owns the keyword.
- `deleted` (boolean): `true` if the keyword has been deleted.
- `text` (string): The keyword text.
- `status` (string): Possible values: `ACTIVE`, `PAUSED`, `DELETED`.
- `matchType` (string): Possible values: `BROAD`, `EXACT`.
- `bid` (Money): See [`Money`](money.md) for details.
- `adGroupId` (int64): The identifier of the ad group that owns the keyword.
- `modificationTime` (date-time): The time the keyword was last modified.
- `creationTime` (date-time): The time the keyword was created.
- `displayStatus` (string): The computed display status of the keyword.
- `adGroup` (ReportingAdGroupMin): See [`ReportingAdGroupMin`](reportingadgroupmin.md) for details.
- `countryOrRegion` (string): Country or region groupBy dimension value.
- `deviceClass` (string): Device class groupBy dimension value.

## See Also

- [object TimeRange](timerange.md)
  Date range, time zone, and granularity settings for reporting requests.
- [object Filter](filter.md)
  Filter condition for reporting requests.
- [object Sorting](sorting.md)
  Sort condition for reporting requests.
- [object RequestPagination](requestpagination.md)
  Pagination settings specific to reporting requests.
- [object ReportingMoney](reportingmoney.md)
  A monetary value wrapper used in reporting contexts, capturing bid amounts and budgets at report time.
- [object ReportingBidStrategy](reportingbidstrategy.md)
  Bid strategy configuration as reported in report rows.
- [object ReportingCampaignMin](reportingcampaignmin.md)
  Minimal campaign information included in nested report objects.
- [object ReportingAdGroupMin](reportingadgroupmin.md)
  Minimal ad group information included in nested report objects.
- [object ReportingCreativeSpec](reportingcreativespec.md)
  Creative specification embedded in report rows.
- [object ReportingDestination](reportingdestination.md)
  Creative destination embedded in report rows.
- [object ReportingSearchTerm](reportingsearchterm.md)
  Search term metadata in a report row.
- [object ActionMetrics](actionmetrics.md)
  Action count metrics breakdown by attribution type.
- [object CostMetrics](costmetrics.md)
  Cost metrics breakdown by attribution type.
- [object RateMetrics](ratemetrics.md)
  Rate metrics breakdown by attribution type.
- [type ReportingAdChannelType](reportingadchanneltype.md)
  The ad channel that served a report row’s metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/reportingkeyword)*