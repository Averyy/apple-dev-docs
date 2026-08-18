# BrandsReportingKeyword

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Keyword metadata for brands report rows, extending the base reporting keyword with brands-only internal fields.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsReportingKeyword
```

#### Discussion

`BrandsReportingKeyword` extends the base `ReportingKeyword` object with `BRANDS`-only internal fields.

The example and `DictionaryKeys` below show only the Brands-specific additional fields (`locationId` and `matchType`). The full field set, including `id`, `text`, `bid`, `status`, and `adGroupId`, is inherited from [`ReportingKeyword`](reportingkeyword.md) and appears alongside these fields in an actual response.

##### Example

```json
{
  "locationId": "555666777",
  "matchType": "PHRASE"
}
```

## Properties

- `adAccountId` (int64)
- `adGroup` (ReportingAdGroupMin)
- `adGroupId` (int64)
- `bid` (Money)
- `campaignId` (int64)
- `countryOrRegion` (string)
- `creationTime` (date-time)
- `deleted` (boolean)
- `deviceClass` (string)
- `displayStatus` (string)
- `id` (int64)
- `locationId` (string): Location ID groupBy dimension value.
- `matchType` (string): Match type for the keyword in Maps campaigns. Possible values: `PHRASE`, `CATEGORY`.
- `modificationTime` (date-time)
- `status` (string)
- `text` (string)

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