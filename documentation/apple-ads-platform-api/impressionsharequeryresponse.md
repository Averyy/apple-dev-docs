# ImpressionShareQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The impression share query endpoint returns this response wrapper.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ImpressionShareQueryResponse
```

#### Response Structure

##### Top Level Fields

The `ImpressionShareResultContainer` wrapping `result` exposes a single field.

| Field | Type | Description |
| --- | --- | --- |
| `rows` | array | Array of `ImpressionShareRow` objects, one per date + search term + country combination. |

Each `ImpressionShareRow` in `rows` carries the following fields.

| Field | Type | Description |
| --- | --- | --- |
| `day` | string | Date (`YYYY-MM-DD`). Present when granularity is `DAILY`. |
| `week` | string | Week start date, Sunday (`YYYY-MM-DD`). Present when granularity is `WEEKLY_SUN_SAT`. |
| `appName` | string | Display name of the promoted app. |
| `promotedObjectId` | string | Adam ID of the promoted app. |
| `countryOrRegion` | string | ISO 3166-1 alpha-2 country or region code (e.g., `US`, `GB`). |
| `searchTerm` | string | The search term. Suppressed for terms with fewer than 10 impressions in the aggregation period. |
| `lowImpressionShare` | number | Lower bound of impression share. See encoding table below. |
| `highImpressionShare` | number | Upper bound of impression share. See encoding table below. |
| `rank` | integer | App’s impression share rank for this search term and country. `1` = highest share. |
| `searchPopularity1to5` | integer | Relative search volume on a 1–5 scale. `5` = most popular. |

##### Impression Share Encoding

`lowImpressionShare` and `highImpressionShare` use a tiered encoding. They are not always a range:

| Impression Share | `lowImpressionShare` | `highImpressionShare` |
| --- | --- | --- |
| 0% | `0` | `0` |
| 1% – 90% | `x` (e.g. `0.23`) | `x` (same value) |
| 91% – 100% | `0.91` | `1` |

For 1–90%, both fields carry the same single-digit value. The 91–100% bucket retains a range because accuracy of the estimated metric declines near full market saturation, and reporting a precise value there would overstate confidence.

**Parsing tip:** `lowImpressionShare == highImpressionShare` and value < 0.91 → precise single-digit percentage. `highImpressionShare == 1` → app has >90% impression share.

The `pagination` object included in the response reports the following.

| Field | Type | Description |
| --- | --- | --- |
| `totalCount` | integer | Total number of rows matching the query. |
| `offset` | integer | Current page offset. |
| `pageSize` | integer | Number of rows returned in this response. |

## Properties

- `result` (ImpressionShareResultContainer): See [`ImpressionShareResultContainer`](impressionshareresultcontainer.md).
- `pagination` (ResponsePagination): See [`ResponsePagination`](responsepagination.md).
- `error` (Error): See [`Error`](error.md). Present only on failure.

## See Also

- [object ImpressionShareQueryRequest](impressionsharequeryrequest.md)
  Request body for the impression share query endpoint.
- [object ImpressionShareRow](impressionsharerow.md)
  A single impression share data row.
- [object ImpressionShareTimeRange](impressionsharetimerange.md)
  Time range for impression share queries.
- [object ImpressionShareOptions](impressionshareoptions.md)
  Report options for impression share queries.
- [object SearchTermPopularityQueryRequest](searchtermpopularityqueryrequest.md)
  Request body for the search term popularity query endpoint.
- [object SearchTermPopularityQueryResponse](searchtermpopularityqueryresponse.md)
  A response wrapper for search term popularity query results.
- [object SearchTermPopularityRow](searchtermpopularityrow.md)
  A single search term popularity data row.
- [object SearchTermPopularityTimeRange](searchtermpopularitytimerange.md)
  Time range for search term popularity queries.
- [object ImpressionShareResultContainer](impressionshareresultcontainer.md)
  Container holding the array of impression share rows a query returns.
- [object SearchTermPopularityResultContainer](searchtermpopularityresultcontainer.md)
  Container holding the array of search term popularity rows a query returns.
- [object KeywordInsights](keywordinsights.md)
  Insights for keyword reporting rows.
- [object ReportingKeywordBidRecommendation](reportingkeywordbidrecommendation.md)
  Keyword bid recommendation details, including a suggested bid amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/impressionsharequeryresponse)*