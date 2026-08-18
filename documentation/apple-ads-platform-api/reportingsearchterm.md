# ReportingSearchTerm

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Search term metadata in a report row.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ReportingSearchTerm
```

#### Discussion

`ReportingSearchTerm` is the search term metadata object embedded in search term report rows. The `keyword` field links the search term back to the keyword that matched it, enabling attribution of observed query behavior to specific bids.

Search term reports exclusively require the ORTZ timezone. UTC is not supported. The report populates the dimension fields (`countryOrRegion`, `deviceClass`) based on the `groupBy` dimensions in the report request. The `adGroup` field provides a lightweight parent ad group summary for display and grouping purposes.

##### Example

```json
{
  "campaignId": 123456789,
  "adAccountId": 987654321,
  "searchTermText": "awayfinder travel app",
  "searchTermSource": "SEARCH",
  "keyword": {
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
  },
  "adGroupId": 234567891,
  "adGroup": {
    "name": "AwayFinder Search - Broad",
    "deleted": false
  },
  "countryOrRegion": "US",
  "deviceClass": "IPHONE"
}
```

## Properties

- `campaignId` (int64): The identifier of the campaign that owns the search term.
- `adAccountId` (int64): The identifier of the ad account that owns the search term.
- `searchTermText` (string): The actual user-entered query string.
- `searchTermSource` (string): Indicates whether the search term came from a direct user search or an auto-match source.
- `keyword` (ReportingKeyword): See [`ReportingKeyword`](reportingkeyword.md) for details.
- `adGroupId` (int64): The identifier of the ad group that owns the search term.
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
- [object ReportingKeyword](reportingkeyword.md)
  Keyword metadata in a report row.
- [object ActionMetrics](actionmetrics.md)
  Action count metrics breakdown by attribution type.
- [object CostMetrics](costmetrics.md)
  Cost metrics breakdown by attribution type.
- [object RateMetrics](ratemetrics.md)
  Rate metrics breakdown by attribution type.
- [type ReportingAdChannelType](reportingadchanneltype.md)
  The ad channel that served a report row’s metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/reportingsearchterm)*