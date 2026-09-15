# BrandsReportingKeyword

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Keyword metadata for brands report rows, extending the base reporting keyword with brands-only internal fields.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object BrandsReportingKeyword
```

#### Discussion

The `BrandsReportingKeyword` extends the base `ReportingKeyword` object with a `brands`-only `locationId` field and a Maps-specific `matchType` override. All other fields, including `id`, `text`, `bid`, `status`, and `adGroupId`, are inherited unchanged from [`ReportingKeyword`](reportingkeyword.md) and appear alongside these fields in an actual response.

##### Example

```json
{
  "locationId": "555666777",
  "matchType": "PHRASE"
}
```

## Properties

- `id` (int64): The keyword identifier.
- `campaignId` (int64): The identifier of the campaign that owns the keyword.
- `adAccountId` (int64): The identifier of the ad account that owns the keyword.
- `deleted` (boolean): `true` if the keyword has been deleted.
- `text` (string): The keyword text.
- `status` (string): Possible values: `ENABLED`, `PAUSED`.
- `matchType` (string): Match type for the keyword in Maps campaigns. Possible values: `PHRASE`, `CATEGORY`.
- `bid` (Money): See [`Money`](money.md) for details.
- `adGroupId` (int64): The identifier of the ad group that owns the keyword.
- `modificationTime` (date-time): The time the keyword was last modified.
- `creationTime` (date-time): The time the keyword was created.
- `displayStatus` (string): The computed display status of the keyword.
- `adGroup` (ReportingAdGroupMin): See [`ReportingAdGroupMin`](reportingadgroupmin.md) for details.
- `countryOrRegion` (string): Country or region groupBy dimension value.
- `deviceClass` (string): Device class groupBy dimension value.
- `locationId` (string): Location ID groupBy dimension value.

## See Also

- [object BrandsReportingRequest](brandsreportingrequest.md)
  Request body for brands reporting queries.
- [object BrandsReportingCampaign](brandsreportingcampaign.md)
  Campaign metadata for Apple Maps report rows.
- [object BrandsReportingAdGroup](brandsreportingadgroup.md)
  Ad group metadata for brands report rows.
- [object BrandsReportingAd](brandsreportingad.md)
  Ad metadata for brands report rows.
- [object BrandsReportingCreative](brandsreportingcreative.md)
  Creative metadata for brands ads.
- [object BrandsReportingSearchTerm](brandsreportingsearchterm.md)
  Search term metadata for brands report rows, extending the base reporting search term with brands-only internal fields.
- [object BrandsCampaignReportResponse](brandscampaignreportresponse.md)
  The top-level response envelope for Apple Maps campaign-level reports.
- [object BrandsCampaignReportRow](brandscampaignreportrow.md)
  A single row in an Apple Maps campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.
- [object BrandsCampaignReportSummary](brandscampaignreportsummary.md)
  The grand-total metrics aggregated across all rows in an Apple Maps campaign report.
- [object BrandsCampaignResultContainer](brandscampaignresultcontainer.md)
  Wraps the array of Apple Maps campaign report rows along with a grand-total summary.
- [object BrandsAdGroupReportResponse](brandsadgroupreportresponse.md)
  The top-level response envelope for brands ad group reports.
- [object BrandsAdGroupReportRow](brandsadgroupreportrow.md)
  A single row in a Brands (Apple Maps) ad group report, pairing ad group metadata with total and granular performance metrics.
- [object BrandsAdGroupReportSummary](brandsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands ad group report.
- [object BrandsAdGroupResultContainer](brandsadgroupresultcontainer.md)
  Wraps the array of Brands ad group report rows along with a grand-total summary.
- [object BrandsAdReportResponse](brandsadreportresponse.md)
  The top-level response envelope for brands ad-level reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingkeyword)*