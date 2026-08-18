# BrandsAdGroupReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in a Brands (Apple Maps) ad group report, pairing ad group metadata with total and granular performance metrics.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsAdGroupReportRow
```

#### Discussion

`BrandsAdGroupReportRow` is the `BRANDS` counterpart to [`AppsAdGroupReportRow`](appsadgroupreportrow.md). The `metadata` field captures ad group identifiers and configuration at report time, while `totalMetrics` contains the aggregated performance figures across the full reporting period.

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
    "id": 123456789,
    "campaignId": 987654321,
    "adAccountId": 555666777,
    "name": "AwayFinder - Brands Ad Group",
    "status": "ENABLED",
    "deleted": false,
    "systemStatus": "RUNNING",
    "systemStatusReasons": ["PROCESSING"],
    "systemStatusLimitingReasons": [],
    "automatedKeywordsOptIn": false,
    "automatedKeywordsRequired": false,
    "pricingModel": "CPT",
    "displayStatus": "RUNNING",
    "modificationTime": "2025-01-10T08:00:00.000",
    "creationTime": "2025-01-05T08:00:00.000",
    "startTime": "2025-01-05T08:00:00.000",
    "endTime": "2025-06-30T08:00:00.000",
    "campaign": {},
    "bidStrategy": {
      "bidStrategyType": "MANUAL_CPT",
      "bid": {
        "amount": "2.50",
        "currency": "USD"
      }
    },
    "targeting": {
      "supplyPlacement": {
        "include": ["MAPS_SEARCH_RESULTS", "MAPS_SEARCH_HOME"]
      },
      "lifetimeStorefronts": {
        "include": ["US", "CA"]
      },
      "supplySource": {
        "include": ["MAPS"]
      },
      "promotedLocationGroup": {
        "include": ["555666777"]
      },
      "promotedLocation": {
        "include": ["123456789"]
      }
    },
    "deviceClass": "IPHONE",
    "locationId": "123456789",
    "supplyPlacement": "MAPS_SEARCH_RESULTS"
  }
}
```

## Properties

- `totalMetrics` (BrandsAdGroupMetrics): See [`BrandsAdGroupMetrics`](brandsadgroupmetrics.md) for details.
- `granularMetrics` ([BrandsAdGroupMetrics]): Time-series metrics broken down by the requested granularity (e.g., `DAILY`, `WEEKLY`). Present only when a `granularity` is specified in the request. When it isn’t, this field is absent and all data appears in `totalMetrics` instead.
- `metadata` (BrandsReportingAdGroup): See [`BrandsReportingAdGroup`](brandsreportingadgroup.md) for details.

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
- [object BrandsAdGroupReportSummary](brandsadgroupreportsummary.md)
  The grand-total metrics aggregated across all rows in a Brands ad group report.
- [object BrandsAdGroupResultContainer](brandsadgroupresultcontainer.md)
  Wraps the array of Brands ad group report rows along with a grand-total summary.
- [object BrandsAdReportResponse](brandsadreportresponse.md)
  The top-level response envelope for brands ad-level reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsadgroupreportrow)*