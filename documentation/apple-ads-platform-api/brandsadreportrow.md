# BrandsAdReportRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single row in a Brands (Apple Maps) ad-level report, pairing ad metadata with total and granular performance metrics.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object BrandsAdReportRow
```

#### Discussion

`BrandsAdReportRow` is the `BRANDS` counterpart to [`AppsAdReportRow`](appsadreportrow.md). It uses [`BrandsMetrics`](brandsmetrics.md), a richer metric set than the APPS metrics that includes Maps location-action fields such as `getDirections`, `call`, and `share` alongside the standard impression and tap metrics.

The `metadata` field captures ad identifiers and configuration at report time, while `totalMetrics` contains the aggregated performance figures across the full reporting period.

##### Example

```json
{
  "totalMetrics": {
    "localSpend": {
      "amount": "845.50",
      "currency": "USD"
    },
    "impressions": 210000,
    "taps": 5200,
    "ttr": 0.0247,
    "cpt": {
      "amount": "0.16",
      "currency": "USD"
    },
    "cpm": {
      "amount": "4.03",
      "currency": "USD"
    },
    "firstActions": {
      "tap": 1300
    },
    "firstActionsPerTap": {
      "tap": 0.25
    },
    "firstActionsPerImpression": {
      "tap": 0.0062
    },
    "costPerFirstAction": {
      "tap": {
        "amount": "0.65",
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
      "tap": 620
    },
    "tapURL": {
      "tap": 410
    },
    "call": {
      "tap": 180
    },
    "share": {
      "tap": 95
    },
    "getTheApp": {
      "tap": 540
    },
    "galleryEngagement": {
      "tap": 255
    },
    "actionsPerTap": {
      "tap": 0.40
    },
    "actionsPerImpression": {
      "tap": 0.01
    }
  },
  "granularMetrics": [
    {
      "date": "2025-01-10",
      "localSpend": {
        "amount": "845.50",
        "currency": "USD"
      },
      "impressions": 210000,
      "taps": 5200,
      "ttr": 0.0247,
      "cpt": {
        "amount": "0.16",
        "currency": "USD"
      },
      "cpm": {
        "amount": "4.03",
        "currency": "USD"
      },
      "firstActions": {
        "tap": 1300
      },
      "firstActionsPerTap": {
        "tap": 0.25
      },
      "firstActionsPerImpression": {
        "tap": 0.0062
      },
      "costPerFirstAction": {
        "tap": {
          "amount": "0.65",
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
        "tap": 620
      },
      "tapURL": {
        "tap": 410
      },
      "call": {
        "tap": 180
      },
      "share": {
        "tap": 95
      },
      "getTheApp": {
        "tap": 540
      },
      "galleryEngagement": {
        "tap": 255
      },
      "actionsPerTap": {
        "tap": 0.40
      },
      "actionsPerImpression": {
        "tap": 0.01
      }
    }
  ],
  "metadata": {
    "id": 555666777,
    "name": "AwayFinder - Brands Ad",
    "deleted": false,
    "status": "ENABLED",
    "systemStatus": "RUNNING",
    "systemStatusReasons": [],
    "systemStatusLimitingReasons": [],
    "adAccountId": 123456789,
    "campaignId": 987654321,
    "adGroupId": 456789123,
    "creationTime": "2025-01-10T08:00:00.000",
    "modificationTime": "2025-01-10T08:00:00.000",
    "displayStatus": "RUNNING",
    "creative": {
      "id": 321654987,
      "creativeType": "LOCAL_ADS_SEARCH_CREATIVE",
      "systemStatus": "VALID"
    },
    "deviceClass": "IPHONE",
    "locationId": "location-98765",
    "supplyPlacement": "MAPS_SEARCH_RESULTS"
  }
}
```

## Properties

- `totalMetrics` (BrandsMetrics): See [`BrandsMetrics`](brandsmetrics.md) for details.
- `granularMetrics` ([BrandsMetrics]): Time-series metrics broken down by the requested granularity (e.g., `DAILY`, `WEEKLY`). Present only when a `granularity` is specified in the request. When it isn’t, this field is absent and all data appears in `totalMetrics` instead.
- `metadata` (BrandsReportingAd): See [`BrandsReportingAd`](brandsreportingad.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsadreportrow)*