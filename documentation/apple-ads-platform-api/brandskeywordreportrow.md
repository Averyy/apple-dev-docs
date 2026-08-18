# BrandsKeywordReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in a Brands keyword report response.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsKeywordReportRow
```

#### Discussion

`BrandsKeywordReportRow` contains keyword metadata, performance metrics, and optional keyword insights for a single reporting row.

##### Example

```json
{
  "metadata": {
    "id": 888999100,
    "text": "coffee near me",
    "matchType": "PHRASE",
    "adAccountId": 123456789,
    "campaignId": 444555999,
    "adGroupId": 555666888,
    "status": "ENABLED",
    "deleted": false,
    "locationId": "555666777"
  },
  "totalMetrics": {
    "localSpend": {
      "amount": "845.50",
      "currency": "USD"
    },
    "impressions": 620000,
    "taps": 9800,
    "ttr": 0.0158,
    "cpt": {
      "amount": "0.09",
      "currency": "USD"
    },
    "cpm": {
      "amount": "1.36",
      "currency": "USD"
    }
  },
  "granularMetrics": [
    {
      "date": "2025-01-10",
      "localSpend": {
        "amount": "845.50",
        "currency": "USD"
      },
      "impressions": 620000,
      "taps": 9800,
      "ttr": 0.0158,
      "cpt": {
        "amount": "0.09",
        "currency": "USD"
      },
      "cpm": {
        "amount": "1.36",
        "currency": "USD"
      }
    }
  ],
  "insights": {
    "bidRecommendation": {
      "suggestedBidAmount": 2.35
    }
  }
}
```

## Properties

- `metadata` (BrandsReportingKeyword): Keyword metadata for this row. See [`BrandsReportingKeyword`](brandsreportingkeyword.md).
- `totalMetrics` (BrandsMetrics): Aggregated performance metrics over the full date range. See [`BrandsMetrics`](brandsmetrics.md).
- `granularMetrics` ([BrandsMetrics]): Metrics broken down by the requested `granularity`. Only present when `granularity` is specified. See [`BrandsMetrics`](brandsmetrics.md).
- `insights` (KeywordInsights): Keyword insights including bid recommendations. See [`KeywordInsights`](keywordinsights.md).

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
- [object BrandsReportingKeyword](brandsreportingkeyword.md)
  Keyword metadata for brands report rows, extending the base reporting keyword with brands-only internal fields.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandskeywordreportrow)*