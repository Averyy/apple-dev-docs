# BrandsCampaignReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in an Apple Maps campaign report, containing campaign metadata, total metrics, and optional granular time-series metrics.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsCampaignReportRow
```

#### Discussion

`BrandsCampaignReportRow` is a single row in a `BRANDS` campaign report response.

For `BRANDS` reports, supported `groupBy` dimensions are `deviceClass`, `locationId`, and `supplyPlacement`. These appear as dimension values within the `metadata` object.

##### Example

```json
{
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
    },
    "getDirections": {
      "tap": 320
    },
    "call": {
      "tap": 145
    },
    "share": {
      "tap": 95
    }
  },
  "granularMetrics": [
    {
      "date": "2025-01-10",
      "localSpend": {
        "amount": "420.25",
        "currency": "USD"
      },
      "impressions": 310000,
      "taps": 4900,
      "ttr": 0.0158,
      "cpt": {
        "amount": "0.09",
        "currency": "USD"
      },
      "cpm": {
        "amount": "1.36",
        "currency": "USD"
      },
      "getDirections": {
        "tap": 160
      },
      "call": {
        "tap": 72
      },
      "share": {
        "tap": 48
      }
    }
  ],
  "metadata": {
    "id": 555666777,
    "promotedObjectType": "BUSINESS_BRAND",
    "promotedObjectId": "123456789",
    "name": "AwayFinder Apple Maps Campaign",
    "status": "ENABLED",
    "deleted": false,
    "displayStatus": "RUNNING",
    "modificationTime": "2025-01-10T08:00:00.000",
    "creationTime": "2025-01-05T08:00:00.000",
    "adAccountId": 987654321,
    "systemStatus": "RUNNING",
    "billingEvent": "IMPRESSIONS",
    "dailyBudget": {
      "value": {
        "amount": "50.00",
        "currency": "USD"
      }
    },
    "startTime": "2025-01-10T08:00:00.000",
    "endTime": "2025-12-31T08:00:00.000",
    "bidStrategy": {
      "bidStrategyType": "MANUAL_CPT",
      "bid": {
        "amount": "1.50",
        "currency": "USD"
      }
    },
    "deviceClass": "IPHONE",
    "locationId": "123456789",
    "supplyPlacement": "MAPS_SEARCH_RESULTS"
  }
}
```

## Properties

- `totalMetrics` (BrandsCampaignMetrics): Aggregated performance figures including the `BRANDS`-specific engagement metrics (directions, calls, shares, etc.). See [`BrandsCampaignMetrics`](brandscampaignmetrics.md) for details.
- `granularMetrics` ([BrandsCampaignMetrics]): Time-series breakdown, present when a `granularity` is specified in the request.
- `metadata` (BrandsReportingCampaign): Campaign identifiers, targeting projection, budget, and operational status at report time. See [`BrandsReportingCampaign`](brandsreportingcampaign.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandscampaignreportrow)*