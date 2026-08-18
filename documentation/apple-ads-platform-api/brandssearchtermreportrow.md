# BrandsSearchTermReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in a Brands search term report, pairing search-term metadata with total and granular performance metrics.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsSearchTermReportRow
```

#### Discussion

`BrandsSearchTermReportRow` is the `BRANDS` counterpart to [`AppsSearchTermReportRow`](appssearchtermreportrow.md). The `metadata` field captures the search term text and its associated keyword, ad group, and location context at report time, while `totalMetrics` contains the aggregated performance figures across the full reporting period.

Like all search term reports, `BRANDS` search term reports require the ORTZ timezone. UTC is not supported. Search term entity reports also exclude the `supplyPlacement` and `locationId` dimensions from `groupBy`.

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
    "firstActions": {
      "tap": 1450
    },
    "firstActionsPerTap": {
      "tap": 0.1480
    },
    "firstActionsPerImpression": {
      "tap": 0.0023
    },
    "costPerFirstAction": {
      "tap": {
        "amount": "0.58",
        "currency": "USD"
      }
    },
    "actions": {
      "tap": 2100
    },
    "costPerAction": {
      "tap": {
        "amount": "0.40",
        "currency": "USD"
      }
    },
    "getDirections": {
      "tap": 320
    },
    "tapURL": {
      "tap": 610
    },
    "call": {
      "tap": 145
    },
    "share": {
      "tap": 95
    },
    "getTheApp": {
      "tap": 780
    },
    "galleryEngagement": {
      "tap": 150
    },
    "actionsPerTap": {
      "tap": 0.2143
    },
    "actionsPerImpression": {
      "tap": 0.0034
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
      },
      "firstActions": {
        "tap": 1450
      },
      "firstActionsPerTap": {
        "tap": 0.1480
      },
      "firstActionsPerImpression": {
        "tap": 0.0023
      },
      "costPerFirstAction": {
        "tap": {
          "amount": "0.58",
          "currency": "USD"
        }
      },
      "actions": {
        "tap": 2100
      },
      "costPerAction": {
        "tap": {
          "amount": "0.40",
          "currency": "USD"
        }
      },
      "getDirections": {
        "tap": 320
      },
      "tapURL": {
        "tap": 610
      },
      "call": {
        "tap": 145
      },
      "share": {
        "tap": 95
      },
      "getTheApp": {
        "tap": 780
      },
      "galleryEngagement": {
        "tap": 150
      },
      "actionsPerTap": {
        "tap": 0.2143
      },
      "actionsPerImpression": {
        "tap": 0.0034
      }
    }
  ],
  "metadata": {
    "campaignId": 555666777,
    "adAccountId": 123456789,
    "searchTermText": "AwayFinder",
    "searchTermSource": "SEARCH",
    "keyword": {
      "locationId": "555666777",
      "matchType": "PHRASE"
    },
    "adGroupId": 987654321,
    "adGroup": {
      "name": "AwayFinder Brand Ad Group",
      "deleted": false
    },
    "countryOrRegion": "US",
    "deviceClass": "IPHONE"
  }
}
```

## Properties

- `totalMetrics` (BrandsMetrics): See [`BrandsMetrics`](brandsmetrics.md) for details.
- `granularMetrics` ([BrandsMetrics]): Time-series metrics broken down by the requested granularity. Present only when the request specifies a `granularity`. Otherwise, it’s omitted and all data appears in `totalMetrics`.
- `metadata` (BrandsReportingSearchTerm): See [`BrandsReportingSearchTerm`](brandsreportingsearchterm.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandssearchtermreportrow)*